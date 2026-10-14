#!/usr/bin/env python3
"""GPR antennas: dipole length, radiation pattern, ground coupling, polarisation
and the offset-imposed near-surface blind zone.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_antennas_demo.py

Everything here is SYNTHETIC.  The antenna is the idealised infinitesimal
(Hertzian) dipole, the standard far-field model of a linearly polarised antenna;
the permittivities are chosen teaching values.  No instrument model, no measured
radiation pattern and no field site is involved.

Contents
--------
1. Half-wave dipole length in air and in the coupled medium, for four nominal
   frequencies and three permittivities.
2. The dipole power pattern sin^2(theta): 3 dB beam width, and the fraction of
   radiated power inside a cone, verified against numerical quadrature.
3. Refraction at the ground interface: critical angle, and the footprint radius
   a ray of the maximum in-ground angle reaches at depth.
4. Polarisation: the cos(psi) coupling of a linear dipole to a linear target,
   and the 3 dB and null orientations.
5. The offset-imposed blind zone: air wave, ground wave and the shallowest
   separable reflection.
6. The travel-time penalty of antenna separation for a shallow target.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def dipole_power_fraction(theta_rad):
    """Fraction of an infinitesimal dipole's radiated power inside a cone of
    half-angle theta about the dipole axis, from the closed form

        F(theta) = (3/4) [cos^3(theta)/3 - cos(theta) + 2/3],

    normalised so that F(pi/2) = 1/2 (half the power in each hemisphere).
    """
    return 0.75 * (np.cos(theta_rad) ** 3 / 3.0 - np.cos(theta_rad) + 2.0 / 3.0)


def main():
    section("1. Half-wave dipole length: in air and in the coupled medium")
    print("   A half-wave dipole resonates where its physical length is half the")
    print("   wavelength IN THE MEDIUM it is coupled to (two limits, between which")
    print("   a real ground-coupled antenna sits):")
    print("   f (MHz)   lambda_air (m)   L_air/2 (m)   L/2 in eps=9 (m)   "
          "L/2 in eps=16 (m)")
    for f_mhz in (100, 250, 500, 900):
        f = f_mhz * 1e6
        la = C_M_NS * 1e9 / f
        print(f"   {f_mhz:7.0f}   {la:14.3f}   {la/2:11.3f}   "
              f"{(C_M_NS/np.sqrt(9.0))*1e9/f/2:17.3f}   "
              f"{(C_M_NS/np.sqrt(16.0))*1e9/f/2:16.3f}")
    print("   The same physical antenna therefore resonates at a LOWER frequency")
    print("   when it is coupled to wet ground than when it radiates into air, by")
    print("   the factor sqrt(eps_r) if the idealisation is taken literally:")
    print("   L = 0.5 lambda = 0.5 v/f, so f = v/(2L) = c/(2L sqrt(eps_r)).")
    for eps_r in (1.0, 4.0, 9.0, 16.0, 25.0):
        f_res = C_M_NS * 1e9 / (2.0 * 0.15 * np.sqrt(eps_r))
        print(f"     a 0.150 m dipole: eps_r = {eps_r:5.1f} -> "
              f"f = {f_res/1e6:7.1f} MHz")

    section("2. Dipole power pattern: beam width and power fraction")
    print("   Power pattern P(theta) = sin^2(theta), theta from the dipole axis.")
    half_power = np.arcsin(np.sqrt(0.5))
    print(f"   sin^2(theta) = 0.5 at theta = {np.degrees(half_power):.3f} deg, so")
    print(f"   the 3 dB beam width is "
          f"{np.degrees(np.pi - 2*half_power):.3f} deg in the plane of the axis,")
    print("   and the pattern is a torus: omnidirectional about the axis.")
    print("   theta (deg)   fraction of power inside the cone (closed form)   "
          "numeric")
    th = np.linspace(0.0, np.pi, 2000001)
    pdf = np.sin(th) ** 3
    cum = np.cumsum(pdf) * (th[1] - th[0])
    tot = cum[-1]
    for deg in (15.0, 30.0, 45.0, 60.0, 90.0):
        t = np.radians(deg)
        i = int(round(deg / 180.0 * 2000000))
        print(f"   {deg:11.0f}   {dipole_power_fraction(t):33.5f}   "
              f"{cum[i]/tot:7.5f}")
    print(f"   half the power (0.50000) is inside theta = 90 deg by symmetry:")
    print(f"   numeric {cum[1000001]/tot:.5f} at theta = 90 deg.  Half-angle 45 deg")
    print(f"   contains only {dipole_power_fraction(np.radians(45.0))*100:.2f}% of")
    print("   the power: a dipole concentrates very little energy in any cone, and")
    print("   that -- not the antenna length -- is why the ground-coupled footprint")
    print("   is wide (Section 3).")

    section("3. Refraction at the ground surface: critical angle and footprint")
    print("   Snell: sin(theta_air) = sqrt(eps_r) sin(theta_ground), so a ray")
    print("   travelling at theta_air = 90 deg enters the ground at the CRITICAL")
    print("   angle theta_c = asin(1/sqrt(eps_r)) from the vertical:")
    print("   eps_r    theta_c (deg)   footprint radius at 1 m   at 2 m   at 3 m")
    for eps_r in (4.0, 9.0, 16.0, 25.0):
        tc = np.degrees(np.arcsin(1.0 / np.sqrt(eps_r)))
        r = 1.0 / np.sqrt(eps_r - 1.0)
        print(f"   {eps_r:6.1f}   {tc:13.3f}   {r*1.0:21.3f} m   {r*2:6.3f} m   "
              f"{r*3:6.3f} m")
    print("   The footprint radius is d tan(theta_c) = d/sqrt(eps_r - 1): energy")
    print("   entering at the steepest allowed angle reaches the widest lateral")
    print("   offset.  Rays inside the ground steeper than theta_c are totally")
    print("   internally reflected at the surface, which is why a buried layer")
    print("   acts as a waveguide and why deep targets are still illuminated.")
    print("   MAXIMUM lateral offset reached by such a ray at depth d:")
    for eps_r in (9.0, 16.0):
        for d in (0.5, 1.0, 2.0):
            print(f"     eps_r = {eps_r:5.1f}, d = {d:.1f} m -> "
                  f"r = {d/np.sqrt(eps_r-1.0):.3f} m")

    section("4. Polarisation: dipole coupling to a linear target")
    print("   A linear dipole couples to the component of the target response")
    print("   along its axis: amplitude factor |cos(psi)|.  Energy factors as")
    print("   cos^2(psi).")
    print("   psi (deg)   amplitude factor   power factor   relative dB")
    for deg in (0, 15, 30, 45, 60, 75, 90):
        c = np.cos(np.radians(deg))
        if abs(c) < 1e-9:
            print(f"   {deg:9.0f}   {abs(c):16.4f}   {c**2:12.4f}   "
                  f"{'-inf (null)':>11s}")
        else:
            print(f"   {deg:9.0f}   {abs(c):16.4f}   {c**2:12.4f}   "
                  f"{20*np.log10(abs(c)):11.2f}")
    print("   psi = 45 deg is the 3 dB point, psi = 90 deg is a null.  Two")
    print("   antenna systems at right angles (crossed dipoles) are therefore")
    print("   near-blind to a target whose axis lies along the other one, and a")
    print("   survey that needs a target's strike must repeat it with both")
    print("   orientations.")

    section("5. The offset-imposed blind zone")
    print("   With antennas separated by x, the first arrival at the receiver is")
    print("   the AIR wave (t = x/c) and the second is the GROUND wave")
    print("   (t = x/v_ground).  A reflection from depth d at two-way time 2d/v")
    print("   is separable only if it arrives after the ground wave:")
    print("   x (m)   t_air (ns)   t_ground (ns)   shallowest separable d (m)")
    v_g = 0.09993          # SYNTHETIC ground-coupled value, eps_r = 9
    for x in (0.10, 0.20, 0.30, 0.50, 1.00):
        d_min = x / 2.0
        print(f"   {x:5.2f}   {x/C_M_NS:11.3f}   {x/v_g:15.3f}   {d_min:25.3f}")
    print("   For a ground-coupled antenna (v_ground = v of the target medium)")
    print("   the blind depth is exactly d_min = x/2, independent of frequency:")
    print("   zero-offset geometry is blind to the top x/2 of the section, and")
    print("   a large fixed offset enlarges that window.  Reducing x -- not")
    print("   increasing frequency -- is what recovers the near-surface.")

    section("6. Travel-time penalty of antenna separation for a shallow target")
    print("   t(x) = sqrt(4 d^2 + x^2)/v is the two-way time; the zero-offset time")
    print("   is 2d/v.  The extra time is not noise: ignoring it biases depth.")
    print("   d (m)   v (m/ns)   x (m)   t(x) (ns)   t(0) (ns)   extra (ns)   "
          "depth bias (cm)")
    for d, v in ((0.30, 0.09993), (0.50, 0.09993), (1.00, 0.09993)):
        for x in (0.10, 0.20, 0.30):
            tx = np.sqrt(4.0 * d ** 2 + x ** 2) / v
            t0 = 2.0 * d / v
            print(f"   {d:5.2f}   {v:8.5f}   {x:5.2f}   {tx:10.3f}   {t0:10.3f}   "
                  f"{(tx-t0):10.3f}   {(tx-t0)*v/2*100:14.2f}")
    print("   For d >> x the penalty vanishes (t(x) - t(0) ~ x^2/(4 d v)), but at")
    print("   d of the order of the separation it is several percent of the time")
    print("   and it must be corrected, not ignored.")

    section("7. Verification of the pattern integrals")
    print("   Independent check of the closed form F(theta) against a fine")
    print("   numerical quadrature of sin^3(theta) d(theta), and of the normalisation")
    print("   F(pi/2) = 1/2 (equal power in the two hemispheres):")
    for deg in (30.0, 60.0, 90.0, 120.0):
        t = np.radians(deg)
        closed = dipole_power_fraction(t)
        num = cum[int(round(deg / 180.0 * 2000000))] / tot
        print(f"     theta = {deg:5.1f} deg: closed form {closed:.6f}, "
              f"numeric {num:.6f}, difference {abs(closed-num):.2e}")
    print("   The two hemispheres carry equal power, as the geometry requires.")
    print("\n   Every number above comes from the idealised SYNTHETIC antenna model")
    print("   of this script; no measured radiation pattern is quoted.")


if __name__ == "__main__":
    main()
