#!/usr/bin/env python3
"""GPR for soil moisture and the water table: velocity and depth, reflection
polarity, moveout velocity analysis, water-content inversion bias, and
attenuation-limited penetration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_for_soil_moisture_demo.py

All soils, water contents, conductivities and synthetic records are SYNTHETIC
teaching values.  No real radar system, site or dataset is used.

Standard constants used:
    c = 0.299792458 m/ns (exact), mu_0 = 4 pi x 10^-7 H/m (exact),
    eps_water = 81, eps_mineral = 4.5, eps_air = 1 (stated end members).

Contents
--------
1. Velocity and two-way time versus water content (CRIM).
2. Reflection coefficients: the surface and the water table, and polarity.
3. Moveout (CMP) velocity analysis: measuring the velocity from the data.
4. Water-content inversion and the bias from an uncalibrated mixing model.
5. Attenuation and penetration versus conductivity, clay and frequency.
6. Verification of CRIM against its end-member limits and of the reflection
   coefficient against the impedance form.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_LIGHT = 0.299792458     # m/ns
MU0 = 4.0e-7 * np.pi
EPS_W, EPS_S, EPS_A = 81.0, 4.5, 1.0
PHI = 0.40                # SYNTHETIC porosity


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def crim(theta, phi=PHI, es=EPS_S, ew=EPS_W, ea=EPS_A):
    """CRIM: sqrt(eps) is linear in water content theta."""
    root = (1.0 - phi) * np.sqrt(es) + theta * np.sqrt(ew) + (phi - theta) * np.sqrt(ea)
    return root ** 2


def theta_from_crim(eps, phi=PHI, es=EPS_S, ew=EPS_W, ea=EPS_A):
    root = np.sqrt(eps)
    return (root - (1.0 - phi) * np.sqrt(es) - phi) / (np.sqrt(ew) - 1.0)


def velocity_m_per_ns(eps):
    return C_LIGHT / np.sqrt(eps)


def reflection_coefficient(eps1, eps2):
    n1, n2 = np.sqrt(eps1), np.sqrt(eps2)
    return (n1 - n2) / (n1 + n2)


def main():
    section("1. Velocity and two-way time versus water content")
    print(f"SYNTHETIC soil: phi = {PHI:.2f}, eps_s = {EPS_S}, eps_w = {EPS_W}, "
          f"eps_a = {EPS_A}")
    print("   theta   eps_eff   v (m/ns)   v (m/us)   TWT over 1 m (ns)   depth for "
          "10 ns (m)")
    for th in (0.02, 0.05, 0.10, 0.20, 0.30, 0.40):
        e = float(crim(th))
        v = velocity_m_per_ns(e)
        print(f"   {th:5.2f}   {e:7.3f}   {v:8.4f}   {v * 1e3:8.2f}   "
              f"{2.0 / v:17.2f}   {v * 10.0 / 2:16.2f}")
    print("  the velocity falls by a factor of "
          f"{velocity_m_per_ns(crim(0.02)) / velocity_m_per_ns(crim(0.40)):.2f} "
          "between nearly dry and")
    print("  saturated, so a single conversion velocity cannot handle a whole")
    print("  profile: the depth scale changes by more than a factor of two across")
    print("  the water table.")

    section("2. Reflection coefficients and polarity")
    e_dry = float(crim(0.05))
    e_wet = float(crim(PHI))
    print(f"  dry soil (theta = 0.05): eps = {e_dry:.3f}, v = "
          f"{velocity_m_per_ns(e_dry):.4f} m/ns")
    print(f"  saturated  (theta = {PHI:.2f}): eps = {e_wet:.3f}, v = "
          f"{velocity_m_per_ns(e_wet):.4f} m/ns")
    R_air_ground = reflection_coefficient(1.0, e_dry)
    R_table = reflection_coefficient(e_dry, e_wet)
    print(f"  air-to-ground reflection coefficient = {R_air_ground:+.4f} "
          f"({R_air_ground * 100:+.1f}%)")
    print(f"  dry-to-saturated (the water table)   = {R_table:+.4f} "
          f"({R_table * 100:+.1f}%)")
    print("  The water-table reflection has NEGATIVE polarity: the wave enters a")
    print("  higher-permittivity medium, so the reflected pulse is inverted.  That")
    print("  polarity reversal is the most reliable GPR water-table diagnostic, and")
    print("  it distinguishes the water table from a reflector caused by a change in")
    print("  texture at constant water content (which can have either sign).")
    print("\n  strength versus water-content contrast:")
    print("   theta above   theta below   R at the table")
    for th_a, th_b in ((0.02, 0.40), (0.05, 0.40), (0.10, 0.40), (0.20, 0.40),
                       (0.05, 0.20)):
        print(f"   {th_a:11.2f}   {th_b:11.2f}   "
              f"{reflection_coefficient(float(crim(th_a)), float(crim(th_b))):+.4f}")
    print("  a wet cover, or a small saturation step, halves or removes the")
    print("  reflection: as with seismics, the water table's visibility is a")
    print("  statement about the zone above it.")

    section("3. Moveout velocity analysis: measuring v instead of assuming it")
    print("  A common-midpoint gather over a flat reflector at depth d, with antenna")
    print("  separation x, satisfies  t^2 = t0^2 + x^2 / v^2  (normal moveout), so a")
    print("  least-squares fit of t^2 against x^2 gives the velocity from the SPREAD.")
    d_true = 2.0
    xs = np.array([0.2, 0.5, 1.0, 1.5, 2.0])
    for e_soil, label in ((float(crim(0.05)), "dry sand"),
                          (float(crim(0.30)), "moist sand")):
        v_true = velocity_m_per_ns(e_soil)
        t0 = 2.0 * d_true / v_true
        t_meas = np.sqrt(t0 ** 2 + (xs / v_true) ** 2) \
            + 0.2 * RNG.standard_normal(xs.size)   # 0.2 ns picking noise
        slope, intercept = np.polyfit(xs ** 2, t_meas ** 2, 1)
        v_nmo = 1.0 / np.sqrt(slope)
        d_fit = np.sqrt(intercept) * v_nmo / 2.0
        print(f"\n  {label}: eps = {e_soil:.2f}, true v = {v_true:.4f} m/ns, "
              f"true d = {d_true:.2f} m")
        print("   x (m)   t (ns)   t^2 (ns^2)   [0.2 ns picking noise added]")
        for x, t in zip(xs, t_meas):
            print(f"   {x:5.1f}   {t:7.3f}   {t ** 2:10.2f}")
        print(f"  fitted slope = {slope:.4f} ns^2/m^2 -> v_NMO = {v_nmo:.4f} m/ns "
              f"(error {(v_nmo / v_true - 1) * 100:+.2f}%)")
        print(f"  fitted intercept -> d = {d_fit:.4f} m "
              f"(error {(d_fit / d_true - 1) * 100:+.2f}%)")
        d_wrong = 1.5 * v_true * t0 / 2.0
        print(f"  using 1.5x the true velocity would give d = {d_wrong:.2f} m, "
              f"an error of {(d_wrong / d_true - 1) * 100:+.0f}%")
    print("\n  The velocity is recovered from the CURVATURE of the moveout and the")
    print("  depth from the fitted zero-offset time: the two are separated by the")
    print("  fit, which is why a multi-offset (CMP or wide-angle) GPR gather is")
    print("  worth the extra effort over a single fixed-offset profile.  The")
    print("  practical limit is that the moveout needed to resolve v requires")
    print("  separations comparable with the target depth, where the plane-layer")
    print("  assumption and the antenna's directivity both begin to fail.")

    section("4. Water-content inversion and calibration bias")
    print("  SYNTHETIC truth: this soil contains clay-bound water that CRIM does not")
    print("  count, so the true water content exceeds the CRIM prediction by 0.04.")
    print("   true theta   eps_meas   theta(CRIM)   bias     relative bias")
    for th_true in (0.06, 0.10, 0.15, 0.20, 0.30):
        eps_meas = float(crim(th_true - 0.04))
        th_inv = float(theta_from_crim(eps_meas))
        print(f"   {th_true:10.2f}   {eps_meas:8.3f}   {th_inv:11.4f}   "
              f"{th_inv - th_true:+7.4f}   {(th_inv / th_true - 1) * 100:+12.1f}%")
    print("  The bias is a constant -0.04 in absolute terms but a 67% relative error")
    print("  at theta = 0.06: **a clay-bearing soil needs a site calibration**, and")
    print("  the relative error is worst exactly where the water content is small.")
    print("  A gravimetric calibration at three to five points across the range")
    print("  removes it; assuming an end-member model does not.")

    section("5. Attenuation and penetration")
    EPS0 = 8.8541878128e-12
    print("  Exact attenuation: alpha = omega sqrt(mu eps/2) x sqrt( sqrt(1 + "
          "(sigma/omega eps)^2) - 1 )")
    print("  In the LOW-LOSS limit (sigma << omega eps) this reduces to")
    print("  alpha = (sigma/2) sqrt(mu/eps), which is INDEPENDENT of frequency.")
    print("  In the HIGH-LOSS limit (sigma >> omega eps) it becomes")
    print("  alpha = sqrt(omega mu sigma / 2), which grows as sqrt(f).")
    print("\n   f (MHz)   sigma (S/m)   eps    loss tangent   alpha (dB/m)   "
          "60 dB depth (m)   regime")
    for f_mhz in (100.0, 250.0):
        for sigma in (0.005, 0.02, 0.05, 0.2):
            for e in (float(crim(0.05)), float(crim(0.30))):
                omega = 2.0 * np.pi * f_mhz * 1e6
                eps_abs = e * EPS0
                lt = sigma / (omega * eps_abs)
                alpha = omega * np.sqrt(MU0 * eps_abs / 2.0) * \
                    np.sqrt(np.sqrt(1.0 + lt ** 2) - 1.0)
                alpha_db = alpha * 8.686
                regime = "low loss" if lt < 0.1 else (
                    "transition" if lt < 1.0 else "HIGH loss")
                print(f"   {f_mhz:7.0f}   {sigma:11.3f}   {e:5.2f}   "
                      f"{lt:12.4f}   {alpha_db:12.3f}   {60.0 / alpha_db:15.1f}   "
                      f"{regime}")
    print("\n  low-loss check (the two formulas must agree when sigma << omega eps):")
    for sigma in (0.001, 0.005):
        for f_mhz in (100.0, 250.0):
            omega = 2.0 * np.pi * f_mhz * 1e6
            eps_abs = float(crim(0.05)) * EPS0
            lt = sigma / (omega * eps_abs)
            exact = omega * np.sqrt(MU0 * eps_abs / 2.0) * \
                np.sqrt(np.sqrt(1.0 + lt ** 2) - 1.0)
            approx = 0.5 * sigma * np.sqrt(MU0 / eps_abs)
            print(f"   sigma = {sigma:.3f}, f = {f_mhz:.0f} MHz: exact = "
                  f"{exact:.6e}, low-loss = {approx:.6e} Np/m, "
                  f"ratio = {exact / approx:.6f}")
    e_dry_ = float(crim(0.05))
    e_wet_ = float(crim(0.30))
    def alpha_db(sigma, eps_r, f_mhz):
        omega = 2.0 * np.pi * f_mhz * 1e6
        eps_abs = eps_r * EPS0
        lt = sigma / (omega * eps_abs)
        return 8.686 * omega * np.sqrt(MU0 * eps_abs / 2.0) * \
            np.sqrt(np.sqrt(1.0 + lt ** 2) - 1.0)
    a_dry = alpha_db(0.005, e_dry_, 250.0)
    a_wet = alpha_db(0.05, e_wet_, 250.0)
    print(f"  Concretely, at 250 MHz: 60 dB of loss is reached at "
          f"{60.0 / a_dry:.1f} m in a clean dry sand")
    print(f"  (sigma = 0.005 S/m) and at {60.0 / a_wet:.1f} m in a clay-rich soil "
          f"(sigma = 0.05 S/m,")
    print(f"  theta = 0.30): a factor of {(60.0 / a_dry) / (60.0 / a_wet):.1f} in "
          "useful depth from a factor of 10 in")
    print("  conductivity.  **Clay content and salinity, not depth, are what limit")
    print("  GPR**, and a survey that suddenly loses penetration nearly always has a")
    print("  conductivity problem rather than a moisture problem.")
    print("\n  A further consequence of the exact formula: because alpha is")
    print("  frequency-INDEPENDENT in the low-loss regime, lowering the frequency")
    print("  does not improve penetration there at all - it only worsens")
    print("  resolution.  Frequency below about 100 MHz helps only where the loss")
    print("  tangent is large enough to matter, which is exactly the clay-rich ground")
    print("  where the low-loss assumptions of section 1 have already failed.")

    section("6. Verification")
    th_zero = float(theta_from_crim(crim(0.0)))
    th_phi = float(theta_from_crim(crim(PHI)))
    print(f"(a) CRIM end members: theta(eps(theta=0)) = {th_zero:+.3e} "
          f"(should be 0)")
    print(f"    theta(eps(theta=phi)) = {th_phi:.6f} (should equal phi = {PHI:.2f})")
    e1, e2 = 4.0, 16.0
    R_dielectric = reflection_coefficient(e1, e2)
    Z1, Z2 = np.sqrt(MU0 / (e1 * 8.8541878128e-12)), np.sqrt(
        MU0 / (e2 * 8.8541878128e-12))
    R_impedance = (Z2 - Z1) / (Z2 + Z1)
    print(f"(b) reflection coefficient: dielectric form = {R_dielectric:+.6f}, "
          f"impedance form = {R_impedance:+.6f}")
    print(f"    difference = {abs(R_dielectric - R_impedance):.2e}: the two agree")
    print("    because Z = sqrt(mu/eps) in the low-loss regime, so the permittivity")
    print("    and impedance forms are algebraically identical there.")
    print("(c) moveout check: at x = 0 the normal-moveout formula must reduce to t0")
    t0 = 2.0 * 1.0 / velocity_m_per_ns(float(crim(0.20)))
    print(f"    t(x=0) = {np.sqrt(t0 ** 2 + 0.0 ** 2):.6f} ns against t0 = "
          f"{t0:.6f} ns")
    print("    which it does identically, as a linear-in-x^2 formula requires.")


if __name__ == "__main__":
    main()
