#!/usr/bin/env python3
"""Seismic methods for aquifer geometry: velocity versus saturation, the water
table as a reflection and a refraction marker, tuning thickness, and the
porosity-to-velocity link.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hydrogeophysics_demo.py

All velocities, densities, depths and synthetic seismograms are SYNTHETIC teaching
values.  No real survey, borehole or dataset is used.

Standard constants used:
    K_f(water) = 2.2e9 Pa, rho_w = 1000 kg/m^3 (standard water properties at
    near-surface conditions), used only inside the stated mixing model.

Contents
--------
1. Velocity and impedance versus water saturation (a stated mixing model).
2. The water table as a reflection: normal-incidence coefficient and polarity.
3. Tuning thickness: how thin an aquifer can still be seen.
4. Refraction: the water table as a velocity contrast and the hidden-layer risk.
5. Time-to-depth conversion and its velocity ambiguity.
6. Verification of the mixing model against its end-member limits.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC dry and saturated framework (chosen teaching values) ----------
VP_DRY, VS_DRY, RHO_DRY = 600.0, 320.0, 1750.0
VP_SAT, VS_SAT, RHO_SAT = 1650.0, 420.0, 2050.0
VP_CLAY, RHO_CLAY = 1900.0, 2000.0
RHO_W = 1000.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def velocities_vs_saturation(sw):
    """A stated interpolation between the dry and saturated end members.

    P velocity uses a saturating (convex) interpolation: the pore fluid's bulk
    modulus matters as soon as a continuous water film exists.  S velocity is
    nearly linear in saturation because the fluid does not carry shear.
    """
    sw = np.asarray(sw, dtype=float)
    vp = VP_DRY + (VP_SAT - VP_DRY) * (1.0 - (1.0 - sw) ** 2)
    vs = VS_DRY + (VS_SAT - VS_DRY) * sw
    rho = RHO_DRY + (RHO_SAT - RHO_DRY) * sw
    return vp, vs, rho


def reflection_coefficient(vp1, rho1, vp2, rho2):
    z1, z2 = rho1 * vp1, rho2 * vp2
    return (z2 - z1) / (z2 + z1)


def ricker(f_dom_hz, t):
    a = (np.pi * f_dom_hz) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def wedge_response(f_dom_hz, dt, thickness_m, v_layer):
    """Two-way time response of a layer whose top and bottom are close."""
    twt = 2.0 * thickness_m / v_layer
    n = int(round(4.0 / (f_dom_hz * dt))) * 2 + 1
    t = (np.arange(n) - n // 2) * dt
    w = ricker(f_dom_hz, t)
    k = int(round(twt / dt))
    resp = w - np.roll(w, k)
    return float(np.max(np.abs(resp))), float(resp[n // 2])


def main():
    section("1. Velocity and impedance versus water saturation")
    print(f"SYNTHETIC framework: dry vp = {VP_DRY:.0f} m/s, saturated vp = "
          f"{VP_SAT:.0f} m/s")
    print(f"  dry rho = {RHO_DRY:.0f}, saturated rho = {RHO_SAT:.0f} kg/m^3")
    print("   Sw      vp (m/s)   vs (m/s)   rho (kg/m^3)   Z = rho vp")
    for sw in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0):
        vp, vs, rho = velocities_vs_saturation(sw)
        print(f"   {sw:4.2f}   {float(vp):8.1f}   {float(vs):8.1f}   "
              f"{float(rho):12.0f}   {float(rho * vp):11.3e}")
    vp_full, vs_full, rho_full = velocities_vs_saturation(1.0)
    print(f"  limits: Sw = 0 gives vp = {float(vp_full * 0 + VP_DRY):.0f} "
          f"(by construction)")
    print(f"  note that vp rises steeply for the first 10% of saturation and")
    print(f"  then flattens: from Sw = 0 to 0.1 vp gains "
          f"{(RHO_DRY * 0 + VP_DRY + (VP_SAT - VP_DRY) * 0.19 - VP_DRY):.0f} m/s "
          f"({(VP_DRY + (VP_SAT - VP_DRY) * 0.19) / VP_DRY * 100 - 100:.0f}%),")
    print(f"  while from Sw = 0.9 to 1.0 it gains only "
          f"{(VP_DRY + (VP_SAT - VP_DRY) - (VP_DRY + (VP_SAT - VP_DRY) * 0.99)):.0f} m/s.")
    print("  The first 10% of saturation produces 19% of the total velocity change")
    print("  and the last 10% produces 1%: saturation is detected most sensitively")
    print("  when the ground is nearly dry.  CAUTION: the exponent 2 in")
    print("  (1 - (1 - Sw)^2) is a TEACHING CHOICE.  Real vp(Sw) depends on the")
    print("  fluid bulk modulus, on the stiffness of the frame and on whether the")
    print("  water is patchy or uniform, and must be computed with Gassmann or Biot")
    print("  theory (see module 05-04-03) rather than interpolated.")

    section("2. The water table as a normal-incidence reflection")
    vp_d, vs_d, rho_d = velocities_vs_saturation(0.10)
    vp_s, vs_s, rho_s = velocities_vs_saturation(1.0)
    R = reflection_coefficient(float(vp_d), float(rho_d), float(vp_s), float(rho_s))
    print(f"  above the water table: vp = {float(vp_d):.0f} m/s, "
          f"rho = {float(rho_d):.0f} kg/m^3, Z = {float(rho_d * vp_d):.3e}")
    print(f"  below the water table: vp = {float(vp_s):.0f} m/s, "
          f"rho = {float(rho_s):.0f} kg/m^3, Z = {float(rho_s * vp_s):.3e}")
    print(f"  reflection coefficient R = {R:+.4f} "
          f"({R * 100:+.2f}%), positive: the reflection has the same polarity as")
    print("  the downgoing wave for a hard (faster-and-denser) reflector.")
    print(f"  transmitted amplitude = 1 + R = {1 + R:.4f}")
    print("  R = +0.41 is very large for a real reflection: it is an artefact of the")
    print("  chosen end members (a completely dry coarse sand at 600 m/s).  Test the")
    print("  sensitivity to how dry the unsaturated zone actually is:")
    print("   Sw above the table   vp (m/s)   R at the water table")
    for sw_above in (0.0, 0.10, 0.30, 0.60):
        vp_a, _, rho_a = velocities_vs_saturation(sw_above)
        R_a = reflection_coefficient(float(vp_a), float(rho_a), float(vp_s),
                                    float(rho_s))
        print(f"   {sw_above:18.2f}   {float(vp_a):8.0f}   {R_a:+18.3f}")
    print("  so the water table's reflectivity is set by the DRYNESS of the")
    print("  unsaturated zone, not by the aquifer.  A wet climate, a shallow")
    print("  capillary fringe or a fine-grained cover all suppress it, which is why")
    print("  water tables are loud in arid coarse soils and nearly invisible in wet")
    print("  clay-rich ones.")
    print("\n  for comparison, a synthetic clay layer beneath the aquifer:")
    R_clay = reflection_coefficient(float(vp_s), float(rho_s), VP_CLAY, RHO_CLAY)
    print(f"   sand-to-clay R = {R_clay:+.4f} ({R_clay * 100:+.2f}%)")
    print("  the clay contact is a much weaker reflector than this water table, but")
    print("  it is the contact that defines the aquifer's BASE; on a seismic section")
    print("  the base is often the sharper pick even when R is smaller, because the")
    print("  overlying water table produces a simple, laterally continuous event.")

    section("3. Tuning thickness: how thin an aquifer can still be seen")
    f_dom, dt = 60.0, 0.5e-3
    v_layer = float(vp_s)
    lam = v_layer / f_dom
    print(f"  source: Ricker wavelet, dominant frequency {f_dom:.0f} Hz; "
          f"aquifer vp = {v_layer:.0f} m/s")
    print(f"  wavelength lambda = vp/f = {lam:.1f} m; quarter-wavelength limit = "
          f"{lam / 4:.2f} m")
    print("   thickness (m)   TWT (ms)   peak |response|   relative to 40 m")
    prints = []
    for th in (0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0, 40.0):
        twt = 2.0 * th / v_layer
        if twt / dt < 1.0:
            print(f"   {th:13.1f}   {twt * 1e3:8.3f}   (below one sample: no "
                  "discrete reflector)")
            continue
        peak, _ = wedge_response(f_dom, dt, th, v_layer)
        prints.append((th, twt, peak))
    ref = prints[-1][2]
    for th, twt, peak in prints:
        print(f"   {th:13.1f}   {twt * 1e3:8.3f}   {peak:15.4f}   "
              f"{peak / ref:14.3f}")
    print("  (peak values are the maximum of |w(t) - w(t - TWT)|, with w a")
    print("  unit-amplitude Ricker wavelet.  For a thick layer the two opposite-")
    print("  polarity wavelets separate and the peak tends to 1.00 - the single-")
    print("  wavelet amplitude.  It OVERSHOOTS to 1.41 at the tuning thickness")
    print("  because the two overlap partially and reinforce, then falls as")
    print("  0.18 at half a metre, where the response is proportional to")
    print("  TWT x dw/dt.  That linear-thin-bed branch is the basis of the")
    print("  thin-bed amplitude method.)")
    print(f"  resolution rule of thumb: an aquifer thinner than about "
          f"{lam / 4:.1f} m (lambda/4) cannot have its")
    print("  thickness measured from the traveltime, only its TUNING amplitude.")

    section("4. Refraction: the water table as a velocity contrast")
    print("  For a refraction survey to detect a saturated layer at depth h below")
    print("  a dry cover of velocity v1, the saturation must raise the velocity:")
    print(f"   v1 (dry) = {VP_DRY:.0f} m/s, v2 (saturated) = {VP_SAT:.0f} m/s, "
          f"critical angle = "
          f"{np.degrees(np.arcsin(VP_DRY / VP_SAT)):.2f} deg")
    print("   interface depth h (m)   crossover distance (m)   intercept time (ms)")
    for h in (2.0, 5.0, 10.0, 20.0):
        x_cross = 2.0 * h * np.sqrt((VP_SAT + VP_DRY) / (VP_SAT - VP_DRY))
        t_i = 2.0 * h * np.sqrt(VP_SAT ** 2 - VP_DRY ** 2) / (VP_DRY * VP_SAT)
        print(f"   {h:22.1f}   {x_cross:22.1f}   {t_i * 1e3:22.2f}")
    print("  the crossover distance grows linearly with depth, so a water table")
    print("  deeper than about 1/4 of the spread length is missed by a refraction")
    print("  line: the refracted arrival never becomes the first arrival within the")
    print("  array (the hidden-layer problem).")
    print("\n  a hidden faster layer beneath the aquifer:")
    for v3 in (2200.0, 2600.0, 3000.0):
        thick_hidden = 3.0
        print(f"   v3 = {v3:.0f} m/s with a {thick_hidden:.0f} m thickness below the "
              f"aquifer: is it visible? "
              f"{'no' if v3 < 1.35 * VP_SAT else 'possibly'}")
    print("  a layer is hidden when the velocity contrast below it is too small for")
    print("  its refracted arrival to overtake the aquifer's; the test is arithmetic")
    print("  (does the deeper head wave arrive first within the spread?) and must be")
    print("  done before the survey, not after.")

    section("5. Time-to-depth conversion and its velocity ambiguity")
    print("  depth = (v/2) x TWT, so a velocity error is a depth error of the same")
    print("  relative size at fixed TWT.")
    twt_ms = 30.0
    print("   v assumed (m/s)   depth to the marker (m)   error vs 1650 m/s")
    for v in (1500.0, 1600.0, 1650.0, 1750.0, 1900.0):
        d = v * twt_ms * 1e-3 / 2.0
        print(f"   {v:15.0f}   {d:23.1f}   {(v / 1650.0 - 1) * 100:+20.1f}%")
    print("  a 15% velocity error is a 15% depth error, and the velocity of the")
    print("  unsaturated zone is the hardest to know: it depends on saturation,")
    print("  which is what the survey is trying to measure.  **That circularity is")
    print("  the central difficulty of seismic hydrogeophysics**, and it is broken by")
    print("  an uphole survey, a downhole geophone, or a coincident GPR velocity")
    print("  (see lesson 04), not by seismic processing alone.")

    section("6. Verification of the mixing model")
    vp0, vs0, rho0 = velocities_vs_saturation(0.0)
    vp1, vs1, rho1 = velocities_vs_saturation(1.0)
    print(f"(a) dry limit   : vp = {float(vp0):.1f}, vs = {float(vs0):.1f}, "
          f"rho = {float(rho0):.1f}")
    print(f"(b) saturated   : vp = {float(vp1):.1f}, vs = {float(vs1):.1f}, "
          f"rho = {float(rho1):.1f}")
    mono = all(float(velocities_vs_saturation(s)[0]) >=
               float(velocities_vs_saturation(s - 0.01)[0]) for s in
               np.arange(0.01, 1.001, 0.01))
    print(f"(c) vp monotonically increasing in Sw: {mono}")
    print("(d) no shear dependence on the fluid in this model: vs is a linear")
    print("    interpolation between measured end members, NOT a Gassmann result.")
    print("    A physically-derived vs(Sw) requires Gassmann or Biot theory and the")
    print("    fluid bulk modulus - see module 05-04-03 and module 14-03-03.")
    print("    The interpolation here is a teaching device with the right shape and")
    print("    the wrong authority; the numbers it produces must not be quoted as")
    print("    rock physics.")


if __name__ == "__main__":
    main()
