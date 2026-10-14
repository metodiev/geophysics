#!/usr/bin/env python3
"""Mantle composition: from mineral modes to rock velocities, and from measured
velocities back to the family of compositions that could produce them.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_composition_demo.py

Everything is SYNTHETIC.  The mineral elastic properties, densities and mixing
parameters below are chosen teaching values, picked so that the aggregates land in a
plausible upper-mantle range.  They are not measurements and no published value is
quoted.  "Peridotite", "harzburgite" and "lherzolite" are used as rock names only.

Contents
--------
1. Mineral modes, end-member properties and the aggregate density.
2. Voigt, Reuss, Hill and the Hashin-Shtrikman bounds, with the ordering check that
   validates the implementation.
3. Velocities, vp/vs and Poisson's ratio of the aggregate.
4. Sensitivity to olivine content and to Mg#.
5. The inverse problem: which compositions fit a measured (rho, vp, vs)?
6. Thermal versus compositional anomalies: why density is the tie-breaker.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC mineral end members -------------------------------------------
# (name, density g/cm^3, bulk modulus GPa, shear modulus GPa)
MINERALS = (
    ("olivine",     3.22, 129.0, 82.0),
    ("orthopyroxene", 3.21, 105.0, 77.0),
    ("clinopyroxene", 3.28, 113.0, 67.0),
    ("garnet",      3.58, 175.0, 94.0),
)
# SYNTHETIC Fe-substitution slopes: per unit decrease of Mg# (i.e. per mole
# fraction of Fe replacing Mg), relative changes in density and moduli.
# Slopes per unit of d = (0.90 - Mg#), i.e. per unit of Fe substituting for Mg.
DRHO_DMG = +0.032      # density rises by 3.2 %
DK_DMG = -0.045        # bulk modulus falls by 4.5 %
DG_DMG = -0.065        # shear modulus falls by 6.5 %


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def end_member(i, mg_number=0.90):
    """(rho, K, G) of mineral i at a given Mg# (relative to a 0.90 reference)."""
    _, rho0, k0, g0 = MINERALS[i]
    d = 0.90 - mg_number
    return (rho0 * (1.0 + DRHO_DMG * d),
            k0 * (1.0 + DK_DMG * d),
            g0 * (1.0 + DG_DMG * d))


def voigt_reuss_hill(fractions, values):
    """Voigt (upper), Reuss (lower) and their mean for any positive property."""
    f = np.asarray(fractions, dtype=float)
    v = np.asarray(values, dtype=float)
    voigt = float(np.sum(f * v))
    reuss = 1.0 / float(np.sum(f / v))
    return voigt, reuss, 0.5 * (voigt + reuss)


def hs_two_phase(k1, g1, f2, k2, g2):
    """Hashin-Shtrikman bound for phase 2 of fraction f2 in host (k1, g1).

    Using a stiffer inclusion (k2 > k1) gives the LOWER bound; using a softer
    inclusion gives the UPPER bound.  This is the standard pair of formulas.
    """
    k = k1 + f2 / (1.0 / (k2 - k1) + (1.0 - f2) / (k1 + 4.0 * g1 / 3.0))
    g = g1 + f2 / (1.0 / (g2 - g1)
                   + 2.0 * (1.0 - f2) * (k1 + 2.0 * g1)
                   / (5.0 * g1 * (k1 + 4.0 * g1 / 3.0)))
    return k, g


def hs_brackets(fractions, ks, gs, i_inclusion=0):
    """An inner bracket for one phase treated as an inclusion in the rest.

    The exact multi-phase Hashin-Shtrikman bounds require the incremental
    construction treated in 05-04-02.  Here the remaining phases are collapsed
    into a single matrix whose moduli are taken at their Reuss limit (for the
    lower bracket) and their Voigt limit (for the upper bracket), and the exact
    two-phase HS formula is applied.  Because the true multi-phase bounds lie
    outside this pair, the result is an INNER bracket: useful, self-consistent,
    and not a rigorous bound.  The ordering test below checks the two-phase
    formulas themselves.
    """
    f = np.asarray(fractions, dtype=float)
    rest = np.array([j for j in range(len(f)) if j != i_inclusion])
    f_rest = f[rest].sum()
    m = rest[f[rest] > 0]
    k_r = 1.0 / float(np.sum(f[m] / ks[m]) / f_rest)
    g_r = 1.0 / float(np.sum(f[m] / gs[m]) / f_rest)
    k_v = float(np.sum(f[m] * ks[m]) / f_rest)
    g_v = float(np.sum(f[m] * gs[m]) / f_rest)
    if ks[i_inclusion] >= k_r:
        lo = hs_two_phase(k_r, g_r, f[i_inclusion], ks[i_inclusion], gs[i_inclusion])
    else:
        lo = hs_two_phase(ks[i_inclusion], gs[i_inclusion], f_rest, k_r, g_r)
    if ks[i_inclusion] >= k_v:
        hi = hs_two_phase(k_v, g_v, f[i_inclusion], ks[i_inclusion], gs[i_inclusion])
    else:
        hi = hs_two_phase(ks[i_inclusion], gs[i_inclusion], f_rest, k_v, g_v)
    if lo[0] > hi[0]:
        lo, hi = hi, lo
    return lo, hi


def aggregate_velocities(fractions, mg_number=0.90, method="hill"):
    """Density and velocities of an aggregate by a chosen averaging scheme."""
    f = np.asarray(fractions, dtype=float)
    props = [end_member(i, mg_number) for i in range(len(MINERALS))]
    rho = float(np.sum(f * [p[0] for p in props]))
    ks = np.array([p[1] for p in props])
    gs = np.array([p[2] for p in props])
    if method == "voigt":
        k = float(np.sum(f * ks))
        g = float(np.sum(f * gs))
    elif method == "reuss":
        k = 1.0 / float(np.sum(f / ks))
        g = 1.0 / float(np.sum(f / gs))
    elif method == "hill":
        k = 0.5 * (float(np.sum(f * ks)) + 1.0 / float(np.sum(f / ks)))
        g = 0.5 * (float(np.sum(f * gs)) + 1.0 / float(np.sum(f / gs)))
    else:
        lo, hi = hs_brackets(f, ks, gs, i_inclusion=0)
        k, g = (0.5 * (lo[0] + hi[0]), 0.5 * (lo[1] + hi[1]))
    vp = np.sqrt((k + 4.0 * g / 3.0) / rho)     # GPa and g/cm^3 -> km/s
    vs = np.sqrt(g / rho)
    return rho, k, g, vp, vs


def main():
    section("1. Mineral modes and end-member properties")
    print("  SYNTHETIC end members at Mg# = 0.90 (chosen values):")
    print("    mineral           rho (g/cm^3)   K (GPa)   G (GPa)")
    for name, rho, k, g in MINERALS:
        print(f"    {name:16s}  {rho:12.2f}  {k:8.1f}  {g:8.1f}")
    modes = np.array([0.57, 0.17, 0.12, 0.14])       # SYNTHETIC lherzolite mode
    print(f"\n  SYNTHETIC mode: olivine {modes[0] * 100:.0f} %, opx "
          f"{modes[1] * 100:.0f} %, cpx {modes[2] * 100:.0f} %, garnet "
          f"{modes[2] * 100 + modes[3] * 100 - modes[2] * 100:.0f} %")
    print(f"  (the sum is {modes.sum():.2f})")

    section("2. Averaging schemes and their bounds at the mode of section 1")
    props = [end_member(i) for i in range(len(MINERALS))]
    ks = np.array([p[1] for p in props])
    gs = np.array([p[2] for p in props])
    k_v, k_r, k_h = voigt_reuss_hill(modes, ks)
    g_v, g_r, g_h = voigt_reuss_hill(modes, gs)
    (k_lo, g_lo), (k_hi, g_hi) = hs_brackets(modes, ks, gs, i_inclusion=0)
    print("    scheme                     K (GPa)        G (GPa)")
    print(f"    Voigt (uniform strain)   {k_v:10.2f}   {g_v:10.2f}")
    print(f"    Reuss (uniform stress)   {k_r:10.2f}   {g_r:10.2f}")
    print(f"    Hill (mean of the two)   {k_h:10.2f}   {g_h:10.2f}")
    print(f"    inner bracket, low side  {k_lo:10.2f}   {g_lo:10.2f}")
    print(f"    inner bracket, high side {k_hi:10.2f}   {g_hi:10.2f}")
    ok_k = k_r <= k_lo <= k_h <= k_hi <= k_v
    ok_g = g_r <= g_lo <= g_h <= g_hi <= g_v
    print(f"  ordering check K: Reuss <= bracket <= Hill <= bracket <= Voigt : "
          f"{ok_k}")
    print(f"  ordering check G: Reuss <= bracket <= Hill <= bracket <= Voigt : "
          f"{ok_g}")
    print("  the Hashin-Shtrikman brackets lie INSIDE the Voigt-Reuss range,")
    print("  which is why the ordering is Reuss <= HS- <= Hill <= HS+ <= Voigt.")
    print("  the ordering check is the implementation test: a wrong recursion or a")
    print("  sign error breaks it immediately.  Note that Voigt and Reuss are")
    print("  strict bounds only in the sense that no microstructure can exceed")
    print("  them, and the Hill average is a convenient middle value, NOT a bound;")
    print("  the physical answer lies between the Hashin-Shtrikman brackets, which")
    print("  are tighter than Voigt and Reuss.")
    print("  The pair printed here is an INNER bracket built by collapsing the other")
    print("  three phases into a matrix at its Reuss and Voigt limits and applying")
    print("  the exact two-phase formula; the rigorous multi-phase brackets are wider")
    print("  and need the incremental construction of 05-04-02.")

    section("3. Velocities of the aggregate")
    print("    scheme    rho (g/cm^3)   vp (km/s)   vs (km/s)   vp/vs   Poisson")
    for method in ("voigt", "hill", "reuss", "hs"):
        rho, k, g, vp, vs = aggregate_velocities(modes, method=method)
        nu = (vp ** 2 - 2 * vs ** 2) / (2.0 * (vp ** 2 - vs ** 2))
        print(f"    {method:8s}  {rho:12.3f}  {vp:10.3f}  {vs:10.3f}  "
              f"{vp / vs:6.3f}  {nu:7.4f}")
    print("  the spread between the Voigt and Reuss brackets is the mixing-model")
    print("  uncertainty: a mineral physicist cannot do better than this without")
    print("  knowing the microstructure.")

    section("4. Sensitivity to olivine content and to Mg#")
    print("  olivine fraction varied, other three phases in their original ratio:")
    print("    f_ol   rho (g/cm^3)   vp (km/s)   vs (km/s)   vs change (%)")
    v_ref = None
    base_rest = modes[1:] / modes[1:].sum()
    for f_ol in (0.40, 0.50, 0.57, 0.65, 0.75, 0.85):
        f = np.concatenate(([f_ol], base_rest * (1.0 - f_ol)))
        rho, k, g, vp, vs = aggregate_velocities(f)
        if v_ref is None:
            v_ref = vs
        print(f"  {f_ol:6.2f}   {rho:12.3f}  {vp:10.3f}  {vs:10.3f}   "
              f"{100 * (vs - v_ref) / v_ref:+10.3f}")
    print("  Mg# varied at the original mode (Fe substituting for Mg):")
    print("    Mg#    rho (g/cm^3)   vp (km/s)   vs (km/s)   vs change (%)")
    v_ref = None
    for mg in (0.95, 0.92, 0.90, 0.86, 0.82, 0.78):
        rho, k, g, vp, vs = aggregate_velocities(modes, mg_number=mg)
        if v_ref is None:
            v_ref = vs
        print(f"  {mg:6.2f}   {rho:12.3f}  {vp:10.3f}  {vs:10.3f}   "
              f"{100 * (vs - v_ref) / v_ref:+10.3f}")
    print("  both knobs move vs, and both also move the density - but with OPPOSITE")
    print("  signs relative to the velocity change.  That is the lever section 6 uses.")

    section("5. The inverse problem: which compositions fit a measured rock?")
    true_ol, true_mg = 0.60, 0.89
    rho_t, k_t, g_t, vp_t, vs_t = aggregate_velocities(
        np.concatenate(([true_ol], base_rest * (1.0 - true_ol))), mg_number=true_mg)
    print(f"  SYNTHETIC 'measured' rock: f_ol = {true_ol:.2f}, Mg# = {true_mg:.2f}")
    print(f"    rho = {rho_t:.4f} g/cm^3, vp = {vp_t:.4f}, vs = {vs_t:.4f} km/s")
    tol = 0.005
    tol_rho = 0.002
    print(f"  now search all compositions and keep those within "
          f"+/-{tol * 100:.1f} % on the velocities and "
          f"+/-{tol_rho * 100:.1f} % on the density")
    ol_grid = np.linspace(0.35, 0.85, 101)
    mg_grid = np.linspace(0.76, 0.96, 61)
    rows = []
    for ol in ol_grid:
        for mg in mg_grid:
            f = np.concatenate(([ol], base_rest * (1.0 - ol)))
            rho, k, g, vp, vs = aggregate_velocities(f, mg_number=mg)
            fit_v = (abs(vp - vp_t) / vp_t <= tol) and (abs(vs - vs_t) / vs_t <= tol)
            fit_r = abs(rho - rho_t) / rho_t <= tol_rho
            rows.append((ol, mg, rho, vp, vs, fit_v, fit_r))
    arr = np.array(rows)
    for name, mask in (("velocities only (vp, vs)", arr[:, 5] == 1),
                       ("velocities and density", (arr[:, 5] == 1) & (arr[:, 6] == 1))):
        sel = arr[mask]
        if sel.size == 0:
            print(f"    {name:26s}: no composition fits")
            continue
        print(f"    {name:26s}: {int(mask.sum()):5d} compositions")
        print(f"      f_ol range {sel[:, 0].min():.2f}-{sel[:, 0].max():.2f}, "
              f"Mg# range {sel[:, 1].min():.2f}-{sel[:, 1].max():.2f}")
        print(f"      rho range {sel[:, 2].min():.3f}-{sel[:, 2].max():.3f} g/cm^3")
    print("  the velocity-only region is a long ridge (the depth-velocity trade-off")
    print("  in compositional clothing); adding a density good to 0.2 % cuts the")
    print("  admissible set to about a third of its size and, more importantly,")
    print("  removes the ends of the ridge.  A density constraint is therefore worth")
    print("  more here than a slightly better velocity.")

    section("6. Thermal against compositional anomalies")
    dlnv_dT = -1.2e-5                    # K^-1, chosen sensitivity of ln(vs) to T
    alpha = 2.5e-5                       # K^-1, thermal expansion (chosen)
    print(f"  sensitivities used: d(ln vs)/dT = {dlnv_dT:.2e} K^-1, "
          f"alpha = {alpha:.2e} K^-1")
    print("    anomaly                        dln vs (%)   dln rho (%)   sign")
    for dT in (100.0, 300.0):
        print(f"  {str(int(dT)) + ' K hotter':30s}"
              f"  {100 * dlnv_dT * dT:+11.3f}   {100 * (-alpha * dT):+11.3f}"
              f"   anti-correlated")
    f_base = np.concatenate(([true_ol], base_rest * (1.0 - true_ol)))
    rho0, k0_, g0_, vp0, vs0 = aggregate_velocities(f_base, mg_number=true_mg)
    for d_ol in (0.05,):
        f = np.concatenate(([true_ol + d_ol], base_rest * (1.0 - true_ol - d_ol)))
        rho2, k2, g2, vp2, vs2 = aggregate_velocities(f, mg_number=true_mg)
        print(f"  {'olivine mode +5 %':30s}"
              f"  {100 * (vs2 - vs0) / vs0:+11.3f}   "
              f"{100 * (rho2 - rho0) / rho0:+11.3f}   correlated")
    for d_mg in (-0.03,):
        rho3, k3, g3, vp3, vs3 = aggregate_velocities(
            f_base, mg_number=true_mg + d_mg)
        print(f"  {'Mg# -0.03 (more Fe)':30s}"
              f"  {100 * (vs3 - vs0) / vs0:+11.3f}   "
              f"{100 * (rho3 - rho0) / rho0:+11.3f}   anti-correlated")
    print("  read the signs, not the sizes.  A hot anomaly lowers vs AND lowers")
    print("  density; an Fe-rich (more fertile, more dense) anomaly lowers vs and")
    print("  RAISES density.  A density anomaly therefore decides between them, and")
    print("  that is the quantitative reason normal modes and geodetic constraints")
    print("  (lesson 01-01) matter to a mineralogical argument.  A velocity anomaly")
    print("  alone cannot: two of the three rows above have the same sign of dln vs.")


if __name__ == "__main__":
    main()
