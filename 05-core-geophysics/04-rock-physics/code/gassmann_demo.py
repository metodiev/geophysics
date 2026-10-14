"""Gassmann fluid substitution: what it does, and exactly where it fails.

Gassmann's equation predicts the saturated bulk modulus of a rock from the
dry-frame modulus, the mineral modulus, the fluid modulus and the porosity:

    K_sat = K_dry + (1 - K_dry/K_min)^2
                   / ( phi/K_fl + (1-phi)/K_min - K_dry/K_min^2 )

and it predicts that the SHEAR modulus is unchanged by the pore fluid.

This script:

  1. implements Gassmann and checks its three exact limits;
  2. performs a fluid substitution (fluid A -> fluid B) and reports the
     velocity changes;
  3. shows the DERIVED consequence that Vs may change only through density,
     Vs_sat/Vs_dry = sqrt(rho_dry/rho_sat), and uses that as a falsifiable test;
  4. shows the classic misuse of Gassmann (treating the saturated modulus as
     if it were the dry modulus) and quantifies how badly it fails.

Every modulus, density and porosity below is a STATED SYNTHETIC INPUT.  These
are not measured rock properties: real values vary by orders of magnitude and
must come from measurement or a cited compilation.

Run:  python3 gassmann_demo.py
"""

from __future__ import annotations

import numpy as np

GPA = 1.0e9


def gassmann(k_dry, g_dry, k_min, k_fl, phi):
    """Saturated bulk modulus, and the unchanged shear modulus."""
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min**2
    return k_dry + num / den, g_dry


def velocities(k, g, rho):
    """P- and S-wave speeds from moduli and density."""
    vp = np.sqrt((k + 4.0 * g / 3.0) / rho)
    vs = np.sqrt(g / rho)
    return vp, vs


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    # --- SYNTHETIC inputs (stated choices) ------------------------------
    K_min, G_min = 37.0 * GPA, 44.0 * GPA      # mineral
    phi_c = 0.40                                # critical porosity (stated)
    phi = 0.20
    rho_min = 2650.0                            # kg/m^3
    fluid_A = {"name": "fluid A (stiff)", "K": 2.2 * GPA, "rho": 1000.0}
    fluid_B = {"name": "fluid B (soft)", "K": 0.05 * GPA, "rho": 200.0}

    def dry_frame(p):
        """STATED SYNTHETIC frame law: linear to zero at the critical porosity.

        K_dry = K_min (1 - phi/phi_c), the same for the shear modulus.  This is
        a deliberate, simple choice so that porosity and frame stiffness are
        not independent in the examples below.  Real frame laws are empirical
        (Module lesson 04) and carry their own assumptions.
        """
        return K_min * (1.0 - p / phi_c), G_min * (1.0 - p / phi_c)

    K_dry, G_dry = dry_frame(phi)
    print("SYNTHETIC inputs (chosen, not measured):")
    print(f"  mineral   K = {K_min/GPA:.1f} GPa, G = {G_min/GPA:.1f} GPa, "
          f"rho = {rho_min:.0f} kg/m^3")
    print(f"  dry frame law: K_dry = K_min(1 - phi/phi_c), phi_c = {phi_c:.2f}")
    print(f"  dry frame at phi = {phi:.2f}: K = {K_dry/GPA:.2f} GPa, "
          f"G = {G_dry/GPA:.2f} GPa")
    for f in (fluid_A, fluid_B):
        print(f"  {f['name']}: K = {f['K']/GPA:.3f} GPa, "
              f"rho = {f['rho']:.0f} kg/m^3")

    # ==================================================================
    section("1. Three exact limits that any correct implementation must obey")
    k_sat, g_sat = gassmann(K_dry, G_dry, K_min, fluid_A["K"], phi)
    print("  (a) K_fl = K_min  : the pore fluid IS the mineral, so the rock is")
    print("      chemically homogeneous and K_sat must equal K_min exactly,")
    print("      whatever the porosity.")
    ks_eq, _ = gassmann(K_dry, G_dry, K_min, K_min, phi)
    print(f"        K_fl = K_min = {K_min/GPA:.6f} GPa -> "
          f"K_sat = {ks_eq/GPA:.9f} GPa (rel. diff "
          f"{abs(ks_eq-K_min)/K_min:.3e})")
    print("  (a') K_fl -> infinity : an incompressible fluid makes the rock")
    print("      bear load through the pore fluid, so K_sat lands ABOVE K_min.")
    print("      (Bulk modulus is not bounded by the stiffer constituent.)")
    for fK in (1e3, 1e6, 1e9):
        ks_inf, _ = gassmann(K_dry, G_dry, K_min, fK * GPA, phi)
        print(f"        K_fl = {fK:.0e} GPa -> K_sat = {ks_inf/GPA:.6f} GPa")
    print("  (b) K_fl -> 0       : a vacuum-filled frame is the dry frame.")
    ks0, _ = gassmann(K_dry, G_dry, K_min, 1e-6 * GPA, phi)
    print(f"        K_fl = 1e-6 GPa -> K_sat = {ks0/GPA:.6f} GPa "
          f"(K_dry = {K_dry/GPA:.6f})")
    print("  (c) shear modulus is returned unchanged by construction:")
    print(f"        G_sat = {g_sat/GPA:.6f} GPa = G_dry = {G_dry/GPA:.6f} GPa")

    # ==================================================================
    section("2. Fluid substitution: same frame, different pore fluid")
    rho_dry = (1 - phi) * rho_min
    rows = []
    for f in (fluid_A, fluid_B):
        k, g = gassmann(K_dry, G_dry, K_min, f["K"], phi)
        rho = (1 - phi) * rho_min + phi * f["rho"]
        vp, vs = velocities(k, g, rho)
        rows.append((f["name"], k, g, rho, vp, vs))
        print(f"  {f['name']:<18} K_sat = {k/GPA:7.4f} GPa   "
              f"rho = {rho:7.1f} kg/m^3")
        print(f"  {'':18} Vp    = {vp:7.1f} m/s     Vs  = {vs:7.1f} m/s")
    (nA, kA, gA, rA, vpA, vsA), (nB, kB, gB, rB, vpB, vsB) = rows
    print(f"  substitution {nA} -> {nB}:")
    print(f"    dK_sat/K = {100*(kB-kA)/kA:+.3f} %")
    print(f"    dVp/Vp   = {100*(vpB-vpA)/vpA:+.3f} %")
    print(f"    dVs/Vs   = {100*(vsB-vsA)/vsA:+.3f} %")
    print("  Shear velocity changes even though G is unchanged, because the")
    print("  DENSITY changed.  Vp changes from both.")

    # ==================================================================
    section("3. The Vs prediction is falsifiable: density effect alone")
    # Gassmann => G unchanged => Vs_sat/Vs_dry = sqrt(rho_dry/rho_sat).
    for f in (fluid_A, fluid_B):
        rho = (1 - phi) * rho_min + phi * f["rho"]
        ratio = np.sqrt(rho_dry / rho)
        k_f, g_f = gassmann(K_dry, G_dry, K_min, f["K"], phi)
        vp_f, vs_f = velocities(k_f, g_f, rho)
        print(f"  {f['name']:<18} predicted Vs_sat/Vs_dry = {ratio:.6f}"
              f"   (Vp/Vs = {vp_f/vs_f:.4f})")
    print("  So Gassmann makes a sharp, testable claim: any Vs change must be")
    print("  fully explained by the density change.  If a laboratory or")
    print("  borehole measurement shows additional Vs softening, Gassmann's")
    print("  assumptions -- homogeneous mineral, isotropic frame, low")
    print("  frequency, fluid pressure equilibrated -- are violated.  Soft")
    print("  clays and patchy saturation are the usual culprits.  The failure")
    print("  is informative; it points at the mechanism.")

    # ==================================================================
    section("4. Classic misuse: substituting on the saturated modulus")
    k_bad, g_bad = gassmann(kA, gA, K_min, fluid_B["K"], phi)
    rho_bad = (1 - phi) * rho_min + phi * fluid_B["rho"]
    vp_bad, vs_bad = velocities(k_bad, g_bad, rho_bad)
    print(f"  correct  : K_sat = {kB/GPA:.4f} GPa, Vp = {vpB:.1f} m/s")
    print(f"  mistaken : K_sat = {k_bad/GPA:.4f} GPa, Vp = {vp_bad:.1f} m/s")
    print(f"  error in K_sat = {100*(k_bad-kB)/kB:+.2f} %  ; "
          f"error in Vp = {100*(vp_bad-vpB)/vpB:+.2f} %")
    print("  Gassmann's first argument is the DRY-FRAME modulus.  Passing the")
    print("  saturated modulus instead inflates the predicted softening, and")
    print("  the error grows with porosity and with the fluid contrast.")

    # ==================================================================
    section("5. Where Gassmann's fluid effect is large and where it is not")
    print("  The dry frame is recomputed at each porosity from the stated law,")
    print("  so this compares physically distinct rocks, not one frame.")
    print("   phi    K_dry(GPa)   dVp/Vp (A->B)   dVs/Vs (A->B)")
    for p in (0.02, 0.05, 0.10, 0.20, 0.30, 0.35):
        kd, gd = dry_frame(p)
        k1, g1 = gassmann(kd, gd, K_min, fluid_A["K"], p)
        k2, g2 = gassmann(kd, gd, K_min, fluid_B["K"], p)
        r1 = (1 - p) * rho_min + p * fluid_A["rho"]
        r2 = (1 - p) * rho_min + p * fluid_B["rho"]
        vp1, vs1 = velocities(k1, g1, r1)
        vp2, vs2 = velocities(k2, g2, r2)
        print(f"  {p:5.2f}   {kd/GPA:9.2f}   {100*(vp2-vp1)/vp1:+13.3f} %   "
              f"{100*(vs2-vs1)/vs1:+12.3f} %")
    print("  At low porosity the frame is nearly the mineral and the fluid can")
    print("  barely move the rock; the effect grows steeply with porosity.")
    print("  This is why 4-D seismic monitoring works well in soft, "
          "high-porosity")
    print("  sands and poorly in stiff, low-porosity carbonates.")

    print("\nSUMMARY: Gassmann is exact within its assumptions and silent")
    print("outside them.  Use its limits to test an implementation, use its")
    print("Vs prediction to test the rock, and always state K_fl and the")
    print("frame modulus you substituted from.")


if __name__ == "__main__":
    main()
