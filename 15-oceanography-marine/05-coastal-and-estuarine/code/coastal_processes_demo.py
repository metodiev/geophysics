#!/usr/bin/env python3
"""Coastal processes: wave dispersion and shoaling, the longshore energy flux and
sediment transport, the Bruun response to sea-level rise, and shoreline change
from a transport gradient.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_processes_demo.py

Everything here is SYNTHETIC.  The wave climate, the coastal profile and the
sediment budget are teaching models with the stated model constants.  No real
beach, coast, delta or survey is referenced, and no number is quoted from a
published measurement.

Contents
--------
1. Linear wave dispersion: solving omega^2 = g k tanh(kh), and the deep- and
   shallow-water limits.
2. Shoaling and breaking: energy-flux conservation, the breaking depth, and how
   the wave height at breaking depends on the deep-water height.
3. The longshore energy flux, derived from shallow-water theory, and the
   CERC-type transport rate.
4. The Bruun response to sea-level rise and the sediment budget it implies.
5. Shoreline change from a longshore transport gradient.
6. Worked examples used in the lesson.
"""

import numpy as np
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

G = 9.80665           # m/s^2, standard gravity
RHO = 1030.0          # kg/m^3, seawater
RHO_S = 2650.0        # kg/m^3, quartz sediment
POROSITY = 0.40       # model value
GAMMA_B = 0.78        # breaking index H/h, a standard empirical constant
SEC_PER_YR = 3.15576e7


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def solve_k(T_s, h):
    """Solve the linear dispersion relation for the wavenumber k (rad/m)."""
    omega = 2.0 * np.pi / T_s
    f = lambda k: G * k * np.tanh(k * h) - omega ** 2
    k_lo = 1e-6 / max(h, 1.0)
    k_hi = 1e4
    return brentq(f, k_lo, k_hi)


def wave_kinematics(T_s, h):
    """Return (k, c, cg, L, kh) for a wave of period T in depth h."""
    k = solve_k(T_s, h)
    omega = 2.0 * np.pi / T_s
    c = omega / k
    kh = k * h
    n = 0.5 * (1.0 + 2.0 * kh / np.sinh(2.0 * kh))
    return k, c, n * c, 2.0 * np.pi / k, kh


def main():
    section("1. Linear wave dispersion and its limits")
    print("  dispersion relation: omega^2 = g k tanh(k h), omega = 2 pi / T")
    for T in (6.0, 10.0, 14.0):
        kg = 2.0 * np.pi / T
        print(f"\n  T = {T:.0f} s; deep-water (kh >> 1) limits:")
        print(f"    L0 = g T^2 / (2 pi) = {G * T ** 2 / (2 * np.pi):8.2f} m, "
              f"c0 = g T / (2 pi) = {G * T / (2 * np.pi):6.2f} m/s")
        print("    depth (m)      k (1/m)      c (m/s)   cg (m/s)   c/c0    c/sqrt(gh)")
        for h in (2.0, 5.0, 10.0, 25.0, 50.0, 200.0):
            k, c, cg, L, kh = wave_kinematics(T, h)
            print(f"    {h:9.1f}   {k:10.4f}   {c:9.3f}   {cg:8.3f}   "
                  f"{c / (G * T / (2 * np.pi)):6.3f}   {c / np.sqrt(G * h):9.3f}")
    print("\n  the phase speed approaches the shallow-water limit c = sqrt(gh)")
    print("  from BELOW as kh -> 0 (c = sqrt(gh)(1 - (kh)^2/6 + ...)), and the")
    print("  group velocity falls to c: in shallow water the wave is non-dispersive.")

    section("2. Shoaling and breaking")
    T, H0, slope = 10.0, 2.5, 0.02
    print(f"  deep-water wave: T = {T:.0f} s, H0 = {H0:.1f} m, beach slope "
          f"{slope:.3f} (1:{1 / slope:.0f})")
    cg0 = wave_kinematics(T, 1000.0)[2]
    print(f"  deep-water group velocity cg0 = {cg0:.3f} m/s")
    print("\n  depth (m)   h/L     H (m)   H/h     breaking?")
    h_b = None
    for h in (20.0, 10.0, 6.0, 4.0, 3.0, 2.5, 2.0, 1.5, 1.0):
        k, c, cg, L, kh = wave_kinematics(T, h)
        H = H0 * np.sqrt(cg0 / cg)
        flag = "yes" if H >= GAMMA_B * h else ""
        if h_b is None and H >= GAMMA_B * h:
            h_b = h
        print(f"  {h:9.1f}   {h / L:5.3f}   {H:6.2f}   {H / h:6.2f}   {flag}")
    # solve precisely for the breaking depth
    def fbreak(h):
        k, c, cg, L, kh = wave_kinematics(T, h)
        return H0 * np.sqrt(cg0 / cg) - GAMMA_B * h
    h_br = brentq(fbreak, 0.05, 50.0)
    k, c, cg, L, kh = wave_kinematics(T, h_br)
    H_br = GAMMA_B * h_br
    print(f"\n  breaking depth h_b = {h_br:.3f} m, breaking height H_b = "
          f"{H_br:.3f} m")
    print(f"  shoaling amplification H_b/H0 = {H_br / H0:.3f}, breaker index "
          f"H_b/h_b = {H_br / h_br:.3f}")
    print(f"  the breaking depth is reached at a shoreward distance of about "
          f"{h_br / slope:.0f} m from the still-water line")
    print("\n  sensitivity of the breaking depth to the deep-water height:")
    print("   H0 (m)   h_b (m)   H_b (m)")
    for H0_i in (0.5, 1.0, 2.0, 4.0):
        fb = lambda h: H0_i * np.sqrt(cg0 / wave_kinematics(T, h)[2]) - \
            GAMMA_B * h
        hb = brentq(fb, 0.05, 60.0)
        print(f"   {H0_i:6.1f}   {hb:7.3f}   {GAMMA_B * hb:7.3f}")

    section("3. Longshore energy flux and sediment transport")
    print("  derived from shallow-water theory:")
    print("    E = rho g H^2 / 8,  cg = sqrt(g h) = sqrt(g H / gamma),")
    print("    P = E cg = rho g^(3/2) H^(5/2) / (8 sqrt(gamma))   [W/m of crest]")
    print("    P_ls = P sin(alpha_b) cos(alpha_b) = (P/2) sin(2 alpha_b)")
    H_b, alpha_b = 1.2, np.radians(6.0)
    P = RHO * G ** 1.5 * H_b ** 2.5 / (8.0 * np.sqrt(GAMMA_B))
    P_ls = 0.5 * P * np.sin(2 * alpha_b)
    print(f"\n  H_b = {H_b:.1f} m, breaking angle alpha_b = "
          f"{np.degrees(alpha_b):.1f} deg")
    print(f"    P    = {P:.1f} W/m")
    print(f"    P_ls = {P_ls:.1f} W/m")
    K_cerc = 0.39
    denom = RHO * G * (RHO_S / RHO - 1.0) * (1.0 - POROSITY)
    Q = K_cerc * P_ls / denom
    print(f"  CERC-type transport Q = K P_ls / [rho g (s-1)(1-p)] with "
          f"K = {K_cerc:.2f}")
    print(f"    rho g (s-1)(1-p) = {denom:.1f} J/m^3 (the energy to move unit")
    print(f"    volume of sediment)")
    print(f"    Q = {Q:.4f} m^3/s = {Q * SEC_PER_YR / 1e6:.3f} x 10^6 m^3/yr")
    print("\n  sensitivity to the wave height and angle:")
    print("   H_b (m)   alpha_b (deg)   Q (10^6 m^3/yr)")
    for H_i in (0.8, 1.2, 1.6):
        for a_i in (2.0, 6.0, 12.0):
            ar = np.radians(a_i)
            Pi = RHO * G ** 1.5 * H_i ** 2.5 / (8.0 * np.sqrt(GAMMA_B))
            Qi = K_cerc * 0.5 * Pi * np.sin(2 * ar) / denom
            print(f"   {H_i:6.1f}   {a_i:13.1f}   {Qi * SEC_PER_YR / 1e6:16.3f}")
    print(f"  Q scales as H_b^(5/2) sin(2 alpha_b): the 33% height increase from")
    print(f"  1.2 to 1.6 m multiplies the transport by "
          f"{(1.6 / 1.2) ** 2.5:.2f}.")

    section("4. The Bruun response and the sediment budget")
    print("  Bruun rule: a sea-level rise S translates the profile landward and")
    print("  upward, so the shoreline retreats by R = S / tan(beta) with tan(beta)")
    print("  the slope of the active profile.  The profile also deepens to the")
    print("  closure depth h_c, so the volume moved is S x W with W = h_c/tan(beta).")
    S = 0.003          # m/yr sea-level rise
    print(f"\n  sea-level rise S = {S * 1e3:.1f} mm/yr")
    print("   slope tan(beta)   h_c (m)   W (m)   retreat R (m/yr)   volume (m^3/yr/m)")
    for tanb in (0.02, 0.01, 0.005):
        for h_c in (10.0, 20.0):
            W = h_c / tanb
            R = S / tanb
            print(f"   {tanb:15.3f}   {h_c:7.0f}   {W:6.0f}   {R:17.4f}   "
                  f"{S * W:18.3f}")
    print("  the retreat is set by the slope alone, and the volume by the closure")
    print("  depth: a gentle profile retreats fast and needs a large sediment")
    print("  supply to keep up.")
    tanb, h_c = 0.01, 15.0
    R = S / tanb
    vol = S * h_c / tanb
    print(f"\n  model profile: tan(beta) = {tanb:.3f}, h_c = {h_c:.0f} m")
    print(f"    retreat R = S/tan(beta) = {R:.4f} m/yr = {R * 100:.2f} cm/yr")
    print(f"    sediment required = S x h_c/tan(beta) = {vol:.3f} m^3/(yr m of shore)")
    print(f"  for a 10 km shoreline that is {vol * 10e3 / 1e6:.3f} x 10^6 m^3/yr,")
    print(f"  against the longshore transport of "
          f"{Q * SEC_PER_YR / 1e6:.2f} x 10^6 m^3/yr computed in section 3.")
    print(f"  the total longshore transport is "
          f"{Q * SEC_PER_YR / (vol * 10e3):.0f} times the Bruun requirement, so")
    print("  it is the GRADIENT of that transport, not its magnitude, that")
    print("  competes with sea-level rise: a few per cent of convergence or")
    print("  divergence in the drift over 10 km is the same size as the Bruun")
    print("  term.")

    section("5. Shoreline change from a transport gradient")
    print("  continuity: dy/dt = -(1/h_c) dQ/dx, with y the shoreline position")
    print("  and Q the longshore transport (positive to the right).  A gradient of")
    print("  dQ/dx = 1 m^3/yr per metre of shoreline is the same as 1000 m^3/yr per")
    print("  kilometre, which is the scale at which a drift gradient is measurable.")
    print("   dQ/dx (m^3/yr per m)   (= per km)   dy/dt (m/yr)   dy/dt (cm/yr)   trend")
    for dQdx in (-5.0, -1.0, 0.0, 1.0, 5.0):
        dydt = -dQdx / h_c
        trend = "accretion" if dydt > 0 else ("erosion" if dydt < 0 else "stable")
        print(f"   {dQdx:21.1f}   {dQdx * 1000:11.0f}   {dydt:12.4f}   "
              f"{dydt * 100:13.2f}   {trend}")
    print(f"  a gradient of 1 m^3/yr per metre (1000 m^3/yr per km) gives")
    print(f"  {abs(1.0 / h_c) * 100:.2f} cm/yr, which is "
          f"{abs(1.0 / h_c) / R * 100:.0f}% of the {R * 100:.1f} cm/yr Bruun")
    print(f"  retreat for the {S * 1e3:.1f} mm/yr rise: the two terms are the same")
    print("  order, which is why shoreline-change studies must measure the drift")
    print("  gradient and the sea-level trend together.")

    section("6. Worked examples used in the lesson")
    k, c, cg, L, kh = wave_kinematics(10.0, 10.0)
    print(f"(a) T = 10 s at h = 10 m: L = {L:.2f} m, c = {c:.3f} m/s, "
          f"cg = {cg:.3f} m/s, kh = {kh:.3f}")
    print(f"    shallow-water check sqrt(gh) = {np.sqrt(G * 10.0):.3f} m/s "
          f"(c is {100 - c / np.sqrt(G * 10.0) * 100:.1f}% below it)")
    print(f"    deep-water check gT/2pi = {G * 10.0 / (2 * np.pi):.3f} m/s")
    print(f"(b) breaking: h_b = {h_br:.3f} m, H_b = {H_br:.3f} m for "
          f"H0 = {H0:.1f} m, T = {T:.0f} s")
    print(f"(c) longshore transport for H_b = {H_b:.1f} m at "
          f"{np.degrees(alpha_b):.1f} deg = {Q * SEC_PER_YR / 1e6:.3f} x 10^6 "
          f"m^3/yr")
    print(f"(d) Bruun retreat for {S * 1e3:.1f} mm/yr on a 1:{1 / tanb:.0f} slope "
          f"= {R * 100:.2f} cm/yr, requiring {vol:.3f} m^3/(yr m)")
    print(f"(e) shoreline change for dQ/dx = 1 m^3/yr per m "
          f"(= 1000 m^3/yr per km) = {-1.0 / h_c * 100:.2f} cm/yr, against the "
          f"Bruun retreat of {R * 100:.2f} cm/yr")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
