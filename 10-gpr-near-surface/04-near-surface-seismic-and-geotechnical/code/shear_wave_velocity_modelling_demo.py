#!/usr/bin/env python3
"""Shear-wave velocity modelling and site classification: profile construction,
stiffness, modulus reduction, settlement and liquefaction screening.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shear_wave_velocity_modelling_demo.py

All models and data in this module are SYNTHETIC.  The velocity profiles, the
densities, the footing and the shaking parameters are chosen teaching values, not
measurements from any site.  Published relations that are used as relations (the
NCEER/Youd simplified liquefaction procedure, the Andrus-Stokoe Vs-based cyclic
resistance, the Hardin-Drnevich modulus-reduction form) are attributed in the
lesson; the numbers they produce here come from SYNTHETIC inputs.

Contents
--------
1. Three independent Vs profiles for one site, and the Vs30 each implies.
2. Site class from the code boundaries, and whether the class survives the data.
3. Stiffness: Gmax = rho Vs^2, E = 2G(1+nu), and the operative modulus at a
   working strain.
4. Settlement of a rigid footing with the small-strain and the operative modulus.
5. Liquefaction screening: CSR, CRR, factor of safety, and a Monte Carlo.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_ACC = 9.80665                 # m/s^2, standard gravity (exact by definition)
PA_KPA = 100.0
RHO_KG_M3 = 1850.0              # SYNTHETIC bulk density
NU = 0.30                       # SYNTHETIC Poisson's ratio
TAU_MAX_KPA = 60.0              # SYNTHETIC shear strength for the G/Gmax curve
Z_REF = 30.0                    # Vs30 reference depth, m

# NEHRP/IBC site classes by Vs30 (m/s): real code boundaries
NEHRP = ((1500.0, "A"), (760.0, "B"), (360.0, "C"), (180.0, "D"), (0.0, "E"))

# SYNTHETIC profiles: (top m, bottom m, Vs m/s)
BOREHOLE = ((0.0, 2.0, 175.0), (2.0, 4.0, 245.0), (4.0, 8.0, 320.0),
            (8.0, 12.0, 430.0), (12.0, 20.0, 520.0), (20.0, 30.0, 600.0))
SURFACE_WAVE = ((0.0, 3.0, 165.0), (3.0, 6.0, 210.0), (6.0, 15.0, 300.0),
                (15.0, 30.0, 470.0))
MODEL_COARSE = ((0.0, 5.0, 180.0), (5.0, 12.0, 265.0), (12.0, 30.0, 450.0))


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def vs30(profile, z_max=Z_REF):
    """Vs30 = 30 / sum(h_i / Vs_i), the travel-time average to 30 m."""
    total = 0.0
    for top, bot, vs in profile:
        lo, hi = top, min(bot, z_max)
        if hi <= lo:
            continue
        total += (hi - lo) / vs
    return z_max / total


def site_class(vs30_val):
    for lim, name in NEHRP:
        if vs30_val > lim:
            return name
    return "F"


def total_stress(z_m):
    return 18.0 * z_m if z_m <= 2.0 else 18.0 * 2.0 + 20.0 * (z_m - 2.0)


def eff_stress(z_m):
    u = 0.0 if z_m <= 2.0 else 9.81 * (z_m - 2.0)
    return total_stress(z_m) - u


def main():
    section("1. Three profiles for one site, and the Vs30 each implies")
    print(f"  z(m)      borehole    surface-wave   coarse model   (Vs, m/s)")
    zs = np.arange(1.0, 30.01, 1.0)

    def vs_at(profile, z):
        for top, bot, vs in profile:
            if top <= z < bot:
                return vs
        return profile[-1][2]
    for z in zs[::2]:
        print(f"  {z:5.0f}   {vs_at(BOREHOLE, z):10.0f}   {vs_at(SURFACE_WAVE, z):12.0f}   "
              f"{vs_at(MODEL_COARSE, z):12.0f}")
    for name, prof in (("borehole (interval)", BOREHOLE),
                       ("surface wave (dispersion)", SURFACE_WAVE),
                       ("coarse refraction-like", MODEL_COARSE)):
        v30 = vs30(prof)
        print(f"  {name:26s} Vs30 = {v30:6.1f} m/s -> site class {site_class(v30)}")
    v_all = [vs30(p) for p in (BOREHOLE, SURFACE_WAVE, MODEL_COARSE)]
    print(f"  spread of Vs30 across the three models: {min(v_all):.1f} to "
          f"{max(v_all):.1f} m/s ({max(v_all) / min(v_all) - 1:.1%})")
    print("  The three models see the same ground.  The difference is what each")
    print("  method weights: a travel-time average weights the SLOW layers, and a")
    print("  dispersion curve weights the layers its wavelengths sample.  A single")
    print("  Vs30 must therefore be reported as an interval, not a value.")

    section("2. Site class against the code boundaries")
    print("  NEHRP/IBC boundaries used (m/s): A > 1500, B 760-1500, C 360-760,")
    print("  D 180-360, E < 180 (code values, not measurements).")
    for name, prof in (("borehole", BOREHOLE), ("surface wave", SURFACE_WAVE),
                       ("coarse", MODEL_COARSE)):
        v30 = vs30(prof)
        margin = min(abs(v30 - lim) for lim, _ in NEHRP)
        print(f"  {name:14s} Vs30 = {v30:6.1f} m/s, class {site_class(v30)}, "
              f"distance to the nearest boundary {margin:6.1f} m/s")
    print("  A profile within a few m/s of a boundary has a class that is decided")
    print("  by the measurement uncertainty rather than by the ground.")

    section("3. Stiffness: small-strain and operative")
    print("  Gmax = rho Vs^2; E = 2G(1+nu);  G/Gmax = 1/(1 + gamma/gamma_r),")
    print("  gamma_r = tau_max/Gmax (Hardin-Drnevich form)")
    print("  Vs(m/s)   Gmax(MPa)   E(MPa)   gamma_r      G/Gmax at 1e-3   G(MPa)")
    for vs in (175.0, 245.0, 320.0, 430.0, 520.0, 600.0):
        gmax_mpa = RHO_KG_M3 * vs ** 2 / 1e6
        e_mpa = 2.0 * gmax_mpa * (1.0 + NU)
        gamma_r = (TAU_MAX_KPA * 1e-3) / gmax_mpa
        ratio = 1.0 / (1.0 + 1e-3 / gamma_r)
        print(f"  {vs:7.0f}   {gmax_mpa:9.1f}   {e_mpa:7.1f}   {gamma_r:9.2e}   "
              f"{ratio:15.3f}   {ratio * gmax_mpa:7.1f}")
    print("  A working strain of 1e-3 is not exotic: it is the order reached under")
    print("  a footing at working load, and it removes most of the small-strain")
    print("  modulus.")

    section("4. Settlement with the two moduli")
    q_kpa, b_m = 150.0, 2.0
    a_m = b_m / np.sqrt(np.pi)
    print(f"  rigid footing, equivalent-area radius a = B/sqrt(pi) = {a_m:.4f} m")
    print("  delta = (pi/2) q a (1-nu^2)/E   [rigid circular punch, elastic")
    print("  half-space; the ratio to a flexible load's centre settlement is 0.785]")
    for vs in (245.0, 320.0):
        gmax_mpa = RHO_KG_M3 * vs ** 2 / 1e6
        e_small = 2.0 * gmax_mpa * (1.0 + NU) * 1e3          # kPa
        gamma_r = (TAU_MAX_KPA * 1e-3) / gmax_mpa
        ratio = 1.0 / (1.0 + 1e-3 / gamma_r)
        e_op = e_small * ratio
        d_small = np.pi / 2 * (q_kpa / e_small) * a_m * (1.0 - NU ** 2) * 1e3
        d_op = np.pi / 2 * (q_kpa / e_op) * a_m * (1.0 - NU ** 2) * 1e3
        print(f"  Vs = {vs:.0f} m/s: E_small = {e_small / 1e3:7.1f} MPa -> "
              f"delta = {d_small:5.2f} mm;  E_op = {e_op / 1e3:6.1f} MPa -> "
              f"delta = {d_op:5.2f} mm (x{d_op / d_small:.2f})")
    print("  Reporting Gmax as the design modulus under-predicts settlement by a")
    print("  factor of three or more.  The strain level is part of the input.")

    section("5. Liquefaction screening")
    print("  CSR = 0.65 (sigma_v/sigma'_v)(a_max/g) r_d,")
    print("  r_d = 1 - 0.00765 z for z <= 9.15 m (simplified form)")
    print("  CRR7.5 from (N1)60cs  [NCEER simplified procedure]; MSF = 10^2.24/M^2.56")
    print("  Vs-based CRR from Vs1 = Vs (100/sigma'_v)^0.25  [Andrus-Stokoe form]")
    amax_g, mag = 0.30, 7.0
    msf = 10.0 ** 2.24 / mag ** 2.56
    print(f"  SYNTHETIC shaking: a_max = {amax_g:.2f} g, M = {mag:.1f}, "
          f"MSF = {msf:.3f}")
    print("  z(m)  sigma_v sigma'_v  CSR   (N1)60cs  CRR_N   FS_N   Vs1   CRR_V   FS_V")
    data = ((2.0, 8.0), (4.0, 12.0), (6.0, 16.0), (8.0, 20.0), (10.0, 24.0))
    for z, n1 in data:
        sv, sve = total_stress(z), eff_stress(z)
        rd = 1.0 - 0.00765 * z
        csr = 0.65 * (sv / sve) * amax_g * rd
        crr_n = (1.0 / (34.0 - n1) + n1 / 135.0 + 50.0 / (10.0 * n1 + 45.0) ** 2
                 - 1.0 / 200.0)
        fs_n = (crr_n / msf) / csr
        vs = vs_at(BOREHOLE, z)
        vs1 = vs * (PA_KPA / sve) ** 0.25
        crr_v = 0.022 * (vs1 / 100.0) ** 2 + 2.8 * (1.0 / (215.0 - vs1)
                                                    - 1.0 / 215.0)
        fs_v = (crr_v / msf) / csr
        print(f"  {z:4.1f}  {sv:7.1f} {sve:8.1f}  {csr:.3f}   {n1:8.1f}  "
              f"{crr_n:5.3f}  {fs_n:5.2f}  {vs1:5.1f}  {crr_v:7.4f}  {fs_v:5.2f}")
    print("  Two independent routes to the same question, and they are not")
    print("  calibrated against each other; a factor-of-safety near 1 from one")
    print("  route and not the other is information, not a contradiction.")

    section("6. Monte Carlo: what the uncertainty does to the answer")
    n = 20000
    sigma_vs = 0.08                     # 8% Vs uncertainty (SYNTHETIC)
    v30_b = vs30(BOREHOLE)
    v30_s = vs30(SURFACE_WAVE)
    draws = v30_b + RNG.normal(0.0, v30_b * sigma_vs, n)
    print(f"  borehole Vs30 = {v30_b:.1f} m/s with 8% uncertainty:")
    print(f"    class C fraction: "
          f"{np.mean((draws > 360.0) & (draws <= 760.0)):.3f}, class D fraction: "
          f"{np.mean((draws > 180.0) & (draws <= 360.0)):.3f}")
    print(f"  The surface-wave profile's Vs30 = {v30_s:.1f} m/s differs from the")
    print(f"  borehole value by {(v30_b - v30_s) / v30_b * 100:.1f}%, which is "
          f"far larger than the 8%")
    print("  measurement uncertainty of either.  The difference is therefore NOT")
    print("  random error: it is what the two methods weight, and it moves the code")
    print("  class from C to D.  A report quoting one number would hide a")
    print("  decision-relevant difference behind a plausible-looking precision.")
    z_c, amax_draw = 4.0, 0.30 * (1.0 + 0.25 * RNG.standard_normal(n))
    sv, sve = total_stress(z_c), eff_stress(z_c)
    rd = 1.0 - 0.00765 * z_c
    csr = 0.65 * (sv / sve) * amax_draw * rd
    vs_draw = vs_at(BOREHOLE, z_c) * (1.0 + sigma_vs * RNG.standard_normal(n))
    vs1 = vs_draw * (PA_KPA / sve) ** 0.25
    crr = 0.022 * (vs1 / 100.0) ** 2 + 2.8 * (1.0 / (215.0 - vs1) - 1.0 / 215.0)
    fs = (crr / msf) / csr
    print(f"  at z = {z_c:.1f} m the Vs-based factor of safety is "
          f"{fs.mean():.2f} +/- {fs.std():.2f}; P(FS < 1) = {np.mean(fs < 1):.3f}")
    print("  The deterministic value for the same inputs (Section 5) is 0.88,")
    print("  against a mean of %.2f here: the difference is the non-linearity of" % fs.mean())
    print("  the CRR(Vs1) relation, which pulls the mean up (a convex function of")
    print("  its input).  A factor of safety quoted to two decimals without the")
    print("  spread behind it is a decision with no error bar attached.")


if __name__ == "__main__":
    main()
