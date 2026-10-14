#!/usr/bin/env python3
"""GPR velocity estimation and depth conversion: air-wave time zero, diffraction
hyperbola fitting, offset geometry and the multi-layer (Dix) correction.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_velocity_and_depth_demo.py

Everything here is SYNTHETIC.  The two- and three-layer models are chosen
teaching models; no field site, no instrument and no measurement is involved.

Contents
--------
1. Depth conversion d = v t / 2, and the depth error from a velocity error.
2. The air wave and the ground wave as time-zero references; the depth error
   produced by a time-zero error.
3. Diffraction hyperbola over a point target: t(x) = sqrt(4 d^2 + x^2)/v, and
   the velocity recovered by least-squares fitting of t^2 against x^2.
4. GPR CMP moveout t^2 = t0^2 + x^2/v_nmo^2, and the residual moveout left by a
   constant-velocity correction in a two-layer medium.
5. Dix inversion of interval velocity, and the error amplification it carries.
6. Verification of the fitted velocity against the forward-modelled times.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458

# SYNTHETIC two-layer model (chosen teaching values, not measured)
V1_M_NS = 0.060          # layer 1 speed  (eps_r = 24.96)
V2_M_NS = 0.090          # layer 2 speed  (eps_r = 11.09)
H1_M = 1.20              # thickness of layer 1
D_TARGET_M = 2.40        # depth to a point target in layer 2


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def two_way_time_hyperbola(d_m, x_m, v_m_ns):
    """Two-way travel time in ns for antennas separated by x (GPR CMP geometry).

    Path length = 2*sqrt(d^2 + (x/2)^2) = sqrt(4 d^2 + x^2), so
    t = sqrt(4 d^2 + x^2)/v.  Note the 4, not the 2 of reflection seismology:
    in GPR both antennas move apart from the midpoint.
    """
    return np.sqrt(4.0 * d_m ** 2 + x_m ** 2) / v_m_ns


def two_layer_time(h1_m, v1_m_ns, d_m, v2_m_ns, x_m, iters=90):
    """Exact two-way time (ns) for a specular reflection from a horizontal
    interface at depth d in layer 2, with antennas at +/- x/2.

    The refraction point at the interface lies a signed horizontal distance a
    from the midpoint (it is on the source side of it, so a < 0); Fermat's
    principle fixes a, and the total path is

        t = 2*hypot(a + x/2, h1)/v1 + 2*hypot(a, d - h1)/v2,

    minimised here by golden-section search so that the comparison with the
    hyperbolic approximation is exact, not assumed.
    """
    phi = (np.sqrt(5.0) - 1.0) / 2.0

    def total(a):
        return (2.0 * np.hypot(a + x_m / 2.0, h1_m) / v1_m_ns
                + 2.0 * np.hypot(a, d_m - h1_m) / v2_m_ns)

    lo, hi = -(d_m + x_m), x_m / 2.0 + d_m
    for _ in range(iters):
        c = hi - phi * (hi - lo)
        e = lo + phi * (hi - lo)
        if total(c) < total(e):
            hi = e
        else:
            lo = c
    return total(0.5 * (lo + hi))


def main():
    section("1. Depth conversion d = v t / 2 (t is two-way time)")
    print("   v (m/ns)   eps_r     t = 20 ns   t = 50 ns   t = 100 ns   t = 200 ns")
    for v in (0.0335, 0.060, 0.075, 0.0999, 0.1499):
        eps_r = (C_M_NS / v) ** 2
        ds = [v * t_ns / 2.0 for t_ns in (20.0, 50.0, 100.0, 200.0)]
        print(f"   {v:8.5f}   {eps_r:6.2f}   " +
              "".join(f"{d:11.3f} m" for d in ds))
    print("   Depths in m.  A single time maps to a FAMILY of depths indexed by v.")
    t_pick = 80.0
    print(f"\n   for one pick t = {t_pick:.0f} ns:")
    for fac in (0.9, 0.95, 1.0, 1.05, 1.1):
        v = 0.075 * fac
        print(f"     v = {0.075*fac:.5f} m/ns ({fac*100:5.1f}% of nominal) -> "
              f"d = {v*t_pick/2:6.4f} m  ({(fac-1)*100:+5.1f}% vs nominal)")
    print("   d is exactly linear in v at fixed t: the fractional depth error")
    print("   equals the fractional velocity error, with no cancellation.")

    section("2. Air wave, ground wave and time zero")
    print("   antenna separation x (m)   t_air = x/c (ns)   t_ground = x/v1 (ns) "
          " (v1 = 0.060 m/ns)")
    for x in (0.10, 0.20, 0.30, 0.50, 1.00):
        print(f"   {x:22.2f}   {x/C_M_NS:16.3f}   {x/V1_M_NS:20.3f}")
    print("   The air wave is the fastest event on the record and is used to set")
    print("   t = 0.  The ground wave (direct wave through the top layer) is")
    print("   slower by the factor c/v1 = "
          f"{C_M_NS/V1_M_NS:.2f} and is the one that can be inverted for v1.")
    print("\n   time-zero error -> depth error: dd = (v/2) dt0")
    for dt0 in (0.2, 0.5, 1.0, 2.0):
        for v in (0.06, 0.09):
            print(f"     dt0 = {dt0:4.2f} ns, v = {v:.3f} m/ns -> "
                  f"dd = {v*dt0/2*100:6.2f} cm")
    print("   At 0.2 ns sampling and v = 0.06 m/ns one sample of time-zero error")
    print("   is 6 mm of depth: small, but it is a SYSTEMATIC shift, not noise.")

    section("3. Diffraction hyperbola: velocity from curvature (SYNTHETIC)")
    v_true, d_true = V2_M_NS, D_TARGET_M
    xs = np.arange(0.0, 4.01, 0.20)                     # +/-2 m aperture
    t_clean = two_way_time_hyperbola(d_true, xs, v_true)
    print(f"   true v = {v_true:.4f} m/ns, true depth = {d_true:.2f} m")
    print("   x (m)   t (ns)   t^2 (ns^2)   x^2 (m^2)")
    for x, tt in list(zip(xs, t_clean))[::4]:
        print(f"   {x:5.2f}   {tt:6.3f}   {tt**2:10.3f}   {x**2:9.3f}")
    # fit t^2 = t0^2 + x^2/v^2
    A = np.vstack([np.ones_like(xs), xs ** 2]).T
    coef, *_ = np.linalg.lstsq(A, t_clean ** 2, rcond=None)
    t0_sq, slope = coef
    v_fit = 1.0 / np.sqrt(slope)
    d_fit = v_fit * np.sqrt(t0_sq) / 2.0
    print(f"   least-squares fit of t^2 vs x^2: intercept {t0_sq:.4f} ns^2, "
          f"slope {slope:.6f} ns^2/m^2")
    print(f"   recovered v = {v_fit:.5f} m/ns (true {v_true:.5f}, error "
          f"{(v_fit/v_true-1)*100:+.4f}%)")
    print(f"   recovered apex depth d = {d_fit:.5f} m (true {d_true:.5f}, error "
          f"{(d_fit/d_true-1)*100:+.4f}%)")
    print("   The fit is exact here because the data are exact; the information")
    print("   used is the CURVATURE of the hyperbola in the x direction.")
    print("\n   with picking noise of 0.2 ns (one sample):")
    for trial_scale in (0.2,):
        for rep in range(3):
            t_noise = t_clean + trial_scale * RNG.standard_normal(xs.size)
            c2, *_ = np.linalg.lstsq(A, t_noise ** 2, rcond=None)
            v_n = 1.0 / np.sqrt(c2[1])
            print(f"     realisation {rep+1}: v = {v_n:.5f} m/ns  "
                  f"({(v_n/v_true-1)*100:+6.3f}%), d = "
                  f"{v_n*np.sqrt(c2[0])/2:.4f} m")
    print("   A 0.2 ns pick error moves v by a few tenths of a per cent: the")
    print("   curvature is a robust estimator when the aperture is wide.")

    section("4. CMP moveout and the residual left by one constant velocity")
    print("   GPR CMP geometry: t^2 = t0^2 + x^2 / v_nmo^2 "
          "(seismic uses 4 x^2; here both antennas move)")
    t0_1 = 2.0 * H1_M / V1_M_NS
    print(f"   event 1 (base of layer 1): t0 = {t0_1:.3f} ns")
    x_off = np.arange(0.0, 4.01, 0.25)
    t1 = two_way_time_hyperbola(H1_M, x_off, V1_M_NS)
    print("   x (m)   event-1 t (ns)   x^2 (m^2)")
    for x, tt in list(zip(x_off, t1))[::4]:
        print(f"   {x:5.2f}   {tt:13.3f}   {x**2:9.3f}")
    v_nmo_1 = x_off[-1] / np.sqrt(t1[-1] ** 2 - t1[0] ** 2)
    print(f"   v_nmo fitted for event 1 = {v_nmo_1:.5f} m/ns "
          f"(true layer speed {V1_M_NS:.5f}): a single layer is exactly hyperbolic")

    print("\n   event 2: a horizontal reflector at 2.40 m, below the interface at")
    print(f"   {H1_M:.2f} m.  The ray refracts at the interface, so Fermat's")
    print("   principle is minimised numerically over the refraction offset a:")
    print("     t = 2 hypot(a + x/2, h1)/v1 + 2 hypot(a, D - h1)/v2")
    x_off2 = np.arange(0.0, 4.01, 0.40)
    t2_exact = np.array([two_layer_time(H1_M, V1_M_NS, D_TARGET_M, V2_M_NS, x)
                         for x in x_off2])
    t0_2 = t2_exact[0]
    print(f"   exact two-way time at x = 0: {t0_2:.3f} ns "
          f"(= 2 h1/v1 + 2 (D - h1)/v2 = {2*H1_M/V1_M_NS + 2*(D_TARGET_M-H1_M)/V2_M_NS:.3f})")
    A2m = np.vstack([np.ones_like(x_off2), x_off2 ** 2]).T
    c2, *_ = np.linalg.lstsq(A2m, t2_exact ** 2, rcond=None)
    v_fit2 = 1.0 / np.sqrt(c2[1])
    t1_ns = 2.0 * H1_M / V1_M_NS
    v_dix = np.sqrt((V1_M_NS ** 2 * t1_ns + V2_M_NS ** 2 * (t0_2 - t1_ns)) / t0_2)
    print(f"   v_nmo by least squares over 0-{x_off2[-1]:.1f} m: "
          f"{v_fit2:.5f} m/ns")
    print(f"   Dix prediction from v1, v2 and the times: {v_dix:.5f} m/ns")
    resid = t2_exact - np.sqrt(t0_2 ** 2 + x_off2 ** 2 / v_dix ** 2)
    print(f"   residual moveout after NMO with the Dix velocity: max "
          f"{np.max(np.abs(resid)):.3f} ns = "
          f"{np.max(np.abs(resid))*V2_M_NS/2*100:.2f} cm at the far offset")
    print("   The two-layer moveout is only approximately hyperbolic: a single")
    print("   v_nmo leaves a small residual at the far offsets, and the fit value")
    print(f"   ({v_fit2:.5f}) differs from the Dix value ({v_dix:.5f}) by "
          f"{(v_fit2/v_dix-1)*100:+.2f}%.")

    section("5. Dix inversion and its error amplification")
    t0_a, v_a = 40.0, 0.060        # first reflector, ns and m/ns
    t0_b, v_b = 120.0, 0.075       # second reflector
    print(f"   picks: (t0 = {t0_a:.1f} ns, v_nmo = {v_a:.4f} m/ns) and "
          f"(t0 = {t0_b:.1f} ns, v_nmo = {v_b:.4f} m/ns)")
    v_int = np.sqrt((v_b ** 2 * t0_b - v_a ** 2 * t0_a) / (t0_b - t0_a))
    print(f"   interval velocity v2 = {v_int:.5f} m/ns")
    print("   perturbing each pick separately by +5%:")
    for label, tt_b, vv_b, tt_a, vv_a in (
            ("v_nmo(b) +5%", t0_b, v_b * 1.05, t0_a, v_a),
            ("v_nmo(a) +5%", t0_b, v_b, t0_a, v_a * 1.05),
            ("t0(b) +5%", t0_b * 1.05, v_b, t0_a, v_a),
            ("t0(a) +5%", t0_b, v_b, t0_a * 1.05, v_a)):
        vn = np.sqrt((vv_b ** 2 * tt_b - vv_a ** 2 * tt_a) / (tt_b - tt_a))
        print(f"     {label:14s} -> v2 = {vn:.5f} m/ns  "
              f"({(vn/v_int-1)*100:+7.3f}%)")
    print("   The shallow pick enters with the LARGER weight: t0(a) errors are")
    print("   amplified more than t0(b) errors, and v_nmo(a) errors for a thin")
    print("   top layer are amplified strongly.")

    section("6. Verification against the forward model")
    print(f"   the synthetic event-2 time at x = 0 is t0 = {t0_2:.3f} ns for a")
    print(f"   reflector at {D_TARGET_M:.2f} m, below an interface at "
          f"{H1_M:.2f} m")
    d_wrong = V1_M_NS * t0_2 / 2.0
    d_right = (2.0 * H1_M + V2_M_NS * (t0_2 - 2.0 * H1_M / V1_M_NS)) / 2.0
    print(f"   single (top-layer) velocity {V1_M_NS:.4f} m/ns -> d = "
          f"{d_wrong:.4f} m, error {d_wrong - D_TARGET_M:+.4f} m "
          f"({(d_wrong/D_TARGET_M-1)*100:+.2f}%)")
    print(f"   two-layer conversion with v2 = {V2_M_NS:.4f} m/ns -> d = "
          f"{d_right:.4f} m, error {d_right - D_TARGET_M:+.4f} m "
          f"({(d_right/D_TARGET_M-1)*100:+.2f}%)")
    print("   Verification rule: a velocity used for depth conversion must be")
    print("   tested by predicting a time that was not used to derive it.  The")
    print("   Fermat ray time at finite offset was computed exactly above; the")
    print("   free-intercept fit of t^2 against x^2 reproduces the reflector")
    print(f"   depth as {v_fit2*np.sqrt(c2[0])/2:.4f} m, i.e. "
          f"{abs(v_fit2*np.sqrt(c2[0])/2 - D_TARGET_M)*100:.2f} cm from the")
    print(f"   value used to build the data ({D_TARGET_M:.2f} m).")


if __name__ == "__main__":
    main()
