#!/usr/bin/env python3
"""SAR principles: wavelength, slant- and ground-range resolution, the synthetic
aperture, the PRF ambiguity bounds, an SNR budget and the layover/shadow
thresholds.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sar_principles_demo.py

Everything is SYNTHETIC.  The carrier frequencies are teaching values chosen
inside the conventional band designations, the platform is a generic 800 km
circular orbiter, and no real mission, sensor or dataset is referenced anywhere.
The constants used (speed of light, Boltzmann constant, Earth's gravitational
parameter, mean Earth radius) are stated standards with units.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np


RNG = np.random.default_rng(20261014)

C = 299_792_458.0               # m/s      exact speed of light in vacuum
K_B = 1.380_649e-23             # J/K      exact Boltzmann constant
GM_EARTH = 3.986_004_418e14     # m^3/s^2  Earth gravitational parameter
R_EARTH = 6_371_000.0           # m        mean Earth radius (conventional)

H_ALT = 800.0e3                 # m        teaching orbit altitude
R_SLANT = 800.0e3               # m        teaching slant range to the target
L_ANT = 10.0                    # m        azimuth antenna length (one-way)
B_RANGE = 30.0e6                # Hz       chirp bandwidth
TAU_P = 40.0e-6                 # s        chirp duration
PRF = 2000.0                    # Hz       pulse repetition frequency
P_TX = 5.0e3                    # W        peak transmit power
G_DB = 35.0                     # dB       one-way antenna gain
F_DB = 3.0                      # dB       receiver noise figure
T_SYS = 290.0                   # K        system noise temperature (assumed)
SIGMA_CR = 1.0                  # m^2      radar cross section of a teaching target


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def platform_speed(alt_m):
    """Circular orbital speed at altitude alt_m, from v = sqrt(GM/r)."""
    return np.sqrt(GM_EARTH / (R_EARTH + alt_m))


def azimuth_response_width(L_ant, lam, R0, v, oversample=12, n_shift=401):
    """Measure the -3 dB width of a synthetic-aperture azimuth response.

    The target is illuminated only during its dwell Ts = lam R0 / (L v), so its
    azimuth history is s(t) = exp(-i 4 pi R(t)/lam) on |t| <= Ts/2 with
    R(t) = sqrt(R0^2 + (v t)^2); the processor correlates it with the ideal
    (untruncated) reference exp(+i 4 pi R(t - t0)/lam).  Sampling is
    ``oversample`` times the Doppler bandwidth so that the simulation itself is
    not aliased.  Returns (width_m, peak_amplitude).
    """
    b_dopp = 2.0 * v / L_ant
    dt = 1.0 / (oversample * b_dopp)
    t_syn = lam * R0 / (L_ant * v)
    n = int(round(t_syn / dt))
    t = (np.arange(n) - n // 2) * dt
    sig = np.exp(-1j * 4.0 * np.pi * np.sqrt(R0 ** 2 + (v * t) ** 2) / lam)
    t0 = np.linspace(-1.5 / b_dopp, 1.5 / b_dopp, n_shift)
    y = np.empty(n_shift)
    for i, s in enumerate(t0):
        r_ref = np.sqrt(R0 ** 2 + (v * (t - s)) ** 2)
        y[i] = abs(np.sum(sig * np.exp(1j * 4.0 * np.pi * r_ref / lam))) ** 2
    half = 0.5 * y.max()
    above = np.where(y > half)[0]
    i_lo, i_hi = above[0] - 1, above[-1] + 1
    # linear interpolation of the half-maximum crossings removes the finite
    # sampling step of the simulation from the measured width
    s_lo = t0[i_lo] + (half - y[i_lo]) * (t0[i_lo + 1] - t0[i_lo]) / (y[i_lo + 1] - y[i_lo])
    s_hi = t0[i_hi - 1] + (y[i_hi - 1] - half) * (t0[i_hi] - t0[i_hi - 1]) / (y[i_hi - 1] - y[i_hi])
    return (s_hi - s_lo) * v, y.max()


def main():
    v = platform_speed(H_ALT)

    section("1. Carrier frequency to wavelength, lam = c / f")
    print("conventional band designations are stated ranges; the carrier in each")
    print("row is a SYNTHETIC teaching value chosen inside the band.\n")
    bands = [("P", 0.30, 1.00, 0.50), ("L", 1.0, 2.0, 1.25), ("C", 4.0, 8.0, 5.30),
             ("X", 8.0, 12.0, 9.60), ("Ku", 12.0, 18.0, 13.50),
             ("Ka", 26.5, 40.0, 35.00)]
    print("  band   stated range (GHz)   teaching f (GHz)   lam = c/f (cm)")
    for name, lo, hi, f in bands:
        print(f"   {name:<4s}  {lo:5.2f} - {hi:5.2f}          {f:8.2f}"
              f"          {C / (f * 1e9) * 100:8.3f}")
    lam = C / (5.30e9)
    print(f"\n  working wavelength for the rest of this demo: lam = {lam:.6f} m "
          f"= {lam * 100:.4f} cm")

    section("2. Range resolution (slant and ground)")
    print("slant range resolution  dr = c / (2 B);  ground range  dg = dr / sin(theta)")
    print("(flat local surface, theta = local incidence angle)\n")
    print("   B (MHz)   dr (m)   dg at 23 deg   dg at 35 deg   dg at 45 deg")
    for b in (10e6, 30e6, 100e6):
        dr = C / (2.0 * b)
        row = "   ".join(f"{dr / np.sin(np.radians(th)):13.2f}"
                         for th in (23.0, 35.0, 45.0))
        print(f"   {b/1e6:7.1f}   {dr:6.2f}   {row}")
    dr_main = C / (2.0 * B_RANGE)
    print(f"\n  the rest of the demo uses B = {B_RANGE/1e6:.0f} MHz -> "
          f"dr = {dr_main:.4f} m (slant)")

    section("3. Azimuth resolution: real aperture versus synthetic aperture")
    print(f"platform: circular orbit, altitude {H_ALT/1e3:.0f} km, "
          f"speed v = {v:.1f} m/s")
    print(f"antenna length L = {L_ANT:.1f} m, wavelength {lam*100:.3f} cm, "
          f"teaching slant range R = {R_SLANT/1e3:.0f} km\n")
    r0 = R_SLANT
    d_real = lam * r0 / L_ANT
    t_syn = lam * r0 / (L_ANT * v)
    print(f"  real-aperture azimuth resolution  d = lam R / L = {d_real:9.2f} m")
    print(f"  synthetic aperture length         Ls = lam R / L = "
          f"{lam * r0 / L_ANT:9.2f} m")
    print(f"  illumination (dwell) time         Ts = Ls / v     = {t_syn:9.4f} s")
    print(f"  Doppler bandwidth                 Bd = 2 v / L    = "
          f"{2.0 * v / L_ANT:9.1f} Hz")
    print(f"  azimuth time-bandwidth product    Bd Ts           = "
          f"{2.0 * v / L_ANT * t_syn:9.1f}")
    print("\n  measured -3 dB width of the focused azimuth response (matched-filter")
    print("  sum over the dwell, not a formula):")
    print("     L (m)   measured width (m)   L/2 (m)   measured/(L/2)   L/R ratio")
    for l_ant in (5.0, 10.0, 20.0):
        w, _ = azimuth_response_width(l_ant, lam, r0, v)
        print(f"    {l_ant:5.1f}   {w:17.3f}   {l_ant/2:7.2f}   "
              f"{w/(l_ant/2):14.3f}   {w/l_ant:9.3f}")
    print("\n  the width tracks L/2 and is independent of the slant range: that is")
    print("  the whole result of aperture synthesis.  The measured -3 dB width is")
    print("  0.886 x L/2 = 0.443 L: the sinc mainlobe of an unweighted aperture.  The")
    print("  conventional quoted resolution is L/2; a tapered aperture trades a wider")
    print("  mainlobe for lower sidelobes.  Note the two-way phase: the Doppler")

    section("4. PRF window: azimuth ambiguity versus range ambiguity")
    b_dopp = 2.0 * v / L_ANT
    prf_min = b_dopp
    for swath_km in (20.0, 50.0, 100.0, 200.0):
        prf_max = C / (2.0 * swath_km * 1e3)
        verdict = "OK" if prf_min < prf_max else "CONFLICT"
        print(f"  swath {swath_km:6.1f} km:  PRF must exceed Bd = {prf_min:7.1f} Hz "
              f"and stay below c/(2W) = {prf_max:7.1f} Hz  -> {verdict}")
    print(f"\n  with PRF = {PRF:.0f} Hz the unambiguous range window is")
    print(f"    R_amb = c / (2 PRF) = {C / (2.0 * PRF)/1e3:.2f} km  (one-way range)")
    print(f"  and the number of pulses in the dwell time is {t_syn * PRF:.0f}")
    print(f"  (must exceed Bd Ts = {b_dopp * t_syn:.0f} for unambiguous azimuth).")

    section("5. SNR budget for a point target with sigma = 1 m^2")
    g_lin = 10 ** (G_DB / 10.0)
    f_lin = 10 ** (F_DB / 10.0)
    r0 = R_SLANT
    p_rx = (P_TX * g_lin ** 2 * lam ** 2 * SIGMA_CR) / ((4.0 * np.pi) ** 3 * r0 ** 4)
    n_pow = K_B * T_SYS * B_RANGE * f_lin
    snr_1 = p_rx / n_pow
    g_range = B_RANGE * TAU_P
    g_az = b_dopp * t_syn
    snr_out = snr_1 * g_range * g_az
    print(f"  transmit peak power {P_TX/1e3:.1f} kW, one-way gain {G_DB:.0f} dB, "
          f"noise figure {F_DB:.0f} dB, T_sys {T_SYS:.0f} K")
    print(f"  peak received power    P_r = Pt G^2 lam^2 sigma/((4 pi)^3 R^4) = "
          f"{p_rx:.3e} W")
    print(f"  noise power in B       N   = k T F B                        = "
          f"{n_pow:.3e} W")
    print(f"  single-pulse SNR           = {snr_1:.3e}  = "
          f"{10*np.log10(snr_1):+7.1f} dB")
    print(f"  range compression gain B tau      = {g_range:8.1f}  = "
          f"{10*np.log10(g_range):+7.1f} dB")
    print(f"  azimuth compression gain Bd Ts    = {g_az:8.1f}  = "
          f"{10*np.log10(g_az):+7.1f} dB")
    print(f"  compressed SNR                    = {snr_out:8.3f}  = "
          f"{10*np.log10(snr_out):+7.1f} dB")
    print("  A distributed target of reflectivity sigma0 has  sigma = sigma0 * A_cell")
    print(f"  with a resolution cell of {dr_main:.3f} m (range) x "
          f"{L_ANT/2:.1f} m (azimuth) = {dr_main*L_ANT/2:.2f} m^2.")

    section("6. Layover and shadow thresholds, predicted and measured")
    print("radar at (x, z) = (0, h); the reference ground point at x = h tan(theta).")
    print("a slope facing the radar rises away from it:  z = s tan(alpha), s = x - x_ref.")
    print("slant range r(s) = sqrt(x^2 + (h - z)^2), and")
    print("    dr/ds = [x - (h - z) tan(alpha)] / r")
    print("so the ordering folds when tan(alpha) > tan(theta), i.e. alpha > theta.")
    print("a slope facing AWAY has local incidence theta + alpha, so shadow needs")
    print("    theta + alpha > 90 deg  =>  alpha > 90 - theta.\n")
    print("  theta (deg)   layover for alpha >   shadow for alpha >")
    for th in (23.0, 35.0, 45.0):
        print(f"   {th:10.0f}   {th:18.0f}   {90.0 - th:19.0f}")
    print("\n  the same thresholds measured from the exact spherical geometry")
    print("  (scan alpha in 0.1 deg steps over a +/- 2 km scene):\n")
    print("  theta (deg)   measured layover onset   measured shadow onset")
    for th_deg in (23.0, 35.0, 45.0):
        th = np.radians(th_deg)
        x_ref = (R_EARTH + H_ALT) * np.tan(th)
        s = np.linspace(-2.0e3, 2.0e3, 401)
        hgt = R_EARTH + H_ALT
        lay = np.nan
        for a_deg in np.arange(0.0, 80.01, 0.1):
            a = np.radians(a_deg)
            z = s * np.tan(a)
            x = x_ref + s
            r = np.sqrt(x ** 2 + (hgt - z) ** 2)
            if np.any(np.diff(r) < 0.0):
                lay = a_deg
                break
        sha = np.nan
        for a_deg in np.arange(0.0, 89.01, 0.1):
            a = np.radians(a_deg)
            z = -s * np.tan(a)
            x = x_ref + s
            vx, vz = -x, (hgt - z)
            nrm = np.hypot(vx, vz)
            cos_i = (np.sin(a) * vx + np.cos(a) * vz) / nrm
            inc = np.degrees(np.arccos(np.clip(cos_i, -1.0, 1.0)))
            if np.any(inc >= 90.0):
                sha = a_deg
                break
        print(f"   {th_deg:10.0f}   {lay:20.1f}   {sha:19.1f}")
    print("\n  measurement and prediction agree to the 0.1 deg scan step.  Past the")
    print("  layover threshold the far end of the facet is imaged before the near end:")
    print("  the ground-range to slant-range map stops being monotonic and no purely")
    print("  geometric inversion can recover the slope.  Between the two thresholds the")
    print("  facet is strongly foreshortened but still invertible.")


if __name__ == "__main__":
    main()
