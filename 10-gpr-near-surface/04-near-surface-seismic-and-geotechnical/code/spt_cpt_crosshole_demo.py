#!/usr/bin/env python3
"""Geotechnical testing: SPT and CPT index corrections, and S-wave velocity from
cross-hole and down-hole surveys.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spt_cpt_crosshole_demo.py

All models and data in this module are SYNTHETIC.  The blow counts, cone
resistances, densities, layer velocities and pick errors are chosen teaching
values, not measurements from any site.  Physical constants and adopted
conventions (the 60% reference energy ratio, the 100 kPa reference stress, the
standard cone net-area ratio) are labelled as such.

Contents
--------
1. SPT: energy-ratio and overburden corrections on a synthetic profile.
2. CPT: net cone resistance, friction ratio and the soil-behaviour-type index.
3. Cross-hole: exact first-arrival times in a layered model, and the interval
   velocities recovered by the straight-ray formula, with a pick-error analysis.
4. Down-hole: interval velocities from arrival-time differences; what cancels and
   what does not.
5. Derived stiffness: Gmax = rho Vs^2, and the index-versus-stiffness comparison.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_ACC = 9.80665            # m/s^2, standard gravity (exact by definition)
PA_KPA = 100.0             # reference stress for overburden normalisation, kPa
ER_REF = 60.0              # reference energy ratio of the SPT, % (convention)
CONE_A = 0.80              # standard cone net area ratio (convention)
RHO_KG_M3 = 1900.0         # SYNTHETIC bulk density of the sandy profile

# SYNTHETIC SPT profile: depth (m), measured blow count N, hammer energy ratio (%)
SPT = ((1.5, 5.0, 72.0), (3.0, 8.0, 72.0), (4.5, 13.0, 72.0),
       (6.0, 17.0, 72.0), (7.5, 21.0, 72.0), (9.0, 26.0, 72.0))
Z_WATER = 2.0              # SYNTHETIC water-table depth, m
GAMMA_DRY = 18.0           # kN/m^3 above the water table (SYNTHETIC)
GAMMA_SAT = 20.0           # kN/m^3 below the water table (SYNTHETIC)

# SYNTHETIC CPT: depth (m), cone resistance qc (MPa), sleeve friction (kPa), u2 (kPa)
CPT = ((1.5, 3.20, 28.0, 15.0), (3.0, 5.10, 36.0, 32.0), (4.5, 8.40, 44.0, 45.0),
       (6.0, 11.20, 52.0, 60.0), (9.0, 15.60, 70.0, 90.0),
       (12.0, 1.80, 90.0, 140.0))

# SYNTHETIC shear-wave velocity model: (top m, bottom m, Vs m/s)
VS_LAYERS = ((0.0, 2.0, 180.0), (2.0, 6.0, 260.0), (6.0, 10.0, 420.0),
             (10.0, 15.0, 600.0))
L_BOREHOLE = 4.0           # SYNTHETIC borehole separation for the cross-hole test
Z_SOURCE = 1.0             # source depth in the cross-hole test, m


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def total_stress_kpa(z_m):
    """Total vertical stress at depth z, kPa, from the SYNTHETIC unit weights."""
    if z_m <= Z_WATER:
        return GAMMA_DRY * z_m
    return GAMMA_DRY * Z_WATER + GAMMA_SAT * (z_m - Z_WATER)


def effective_stress_kpa(z_m):
    """Vertical effective stress, kPa (pore pressure = hydrostatic below the table)."""
    u = 0.0 if z_m <= Z_WATER else 9.81 * (z_m - Z_WATER)
    return total_stress_kpa(z_m) - u


def vs_of_depth(z_m):
    for top, bot, vs in VS_LAYERS:
        if top <= z_m < bot:
            return vs
    return VS_LAYERS[-1][2]


def first_arrival_crosshole(z_s, z_r, x_m):
    """Exact first-arrival time across a layered medium, by ray-parameter scan.

    The ray leaves the source at depth z_s and reaches a receiver at depth z_r in
    a borehole x_m away.  The horizontal slowness p is scanned and the geometry
    constraint sum(h_i tan(theta_i)) = x_m solved by interpolation.  Valid for a
    down-going leg, i.e. z_r >= z_s.  Returns time in milliseconds.
    """
    if abs(z_r - z_s) < 1e-12:
        return x_m / vs_of_depth(z_s) * 1e3
    p = np.linspace(1e-9, 0.999999 / min(vs_of_depth(z) for z in
                                          np.linspace(z_s, z_r, 200)),
                    200000)
    x = np.zeros_like(p)
    t = np.zeros_like(p)
    for top, bot, vs in VS_LAYERS:
        lo, hi = max(top, min(z_s, z_r)), min(bot, max(z_s, z_r))
        if hi <= lo:
            continue
        h = hi - lo
        root = np.sqrt(np.clip(1.0 - (p * vs) ** 2, 1e-12, None))
        x += h * p * vs / root
        t += h / (vs * root)
    return float(np.interp(x_m, x, t)) * 1e3      # s -> ms


def main():
    section("1. SPT: energy ratio and overburden correction")
    print(f"SYNTHETIC profile, water table at {Z_WATER:.1f} m, unit weights "
          f"{GAMMA_DRY:.0f} and {GAMMA_SAT:.0f} kN/m^3")
    print("  conventions used: N60 = N (ER/60); CN = sqrt(100/sigma'_v) with")
    print("  sigma'_v in kPa; (N1)60 = N60 CN")
    print("  z(m)   sigma_v  sigma'_v    N    N60    CN    (N1)60")
    for z, n_meas, er in SPT:
        sv = total_stress_kpa(z)
        sv_eff = effective_stress_kpa(z)
        n60 = n_meas * er / ER_REF
        cn = np.sqrt(PA_KPA / sv_eff)
        print(f"  {z:5.1f}  {sv:8.1f}  {sv_eff:8.1f}  {n_meas:5.0f}  {n60:5.1f}  "
              f"{cn:5.2f}  {n60 * cn:7.1f}")
    print("  Note the two corrections act in opposite directions: the energy ratio")
    print("  raises every count by 1.20, the overburden correction lowers the")
    print("  deeper ones.  Reporting an uncorrected N is reporting neither.")

    section("2. CPT: net resistance, friction ratio and soil behaviour type")
    print("  qt = qc + (1-a) u2 with a = 0.80 (convention); Rf = fs/qt x 100%")
    print("  Q = (qt - sigma_v)/sigma'_v; F = fs/(qt - sigma_v) x 100%")
    print("  Ic = sqrt((3.47 - log10 Q)^2 + (1.22 + log10 F)^2)")
    print("  z(m)   qc(MPa)   qt(MPa)  Rf(%)     Q      F     Ic    behaviour type")
    zones = ((1.31, "gravelly sand"), (2.05, "sand"), (2.60, "silty sand"),
             (2.95, "sandy silt"), (3.60, "clayey silt"))
    for z, qc_mpa, fs_kpa, u2_kpa in CPT:
        sv = total_stress_kpa(z)
        sv_eff = effective_stress_kpa(z)
        qt = qc_mpa * 1e3 + (1.0 - CONE_A) * u2_kpa          # kPa
        rf = fs_kpa / qt * 100.0
        q = (qt - sv) / sv_eff
        f = fs_kpa / (qt - sv) * 100.0
        ic = np.sqrt((3.47 - np.log10(q)) ** 2 + (1.22 + np.log10(f)) ** 2)
        name = "clay"
        for lim, nm in zones:
            if ic < lim:
                name = nm
                break
        print(f"  {z:5.1f}  {qc_mpa:8.2f}  {qt / 1e3:8.3f}  {rf:6.2f}  {q:6.1f}  "
              f"{f:5.2f}  {ic:5.2f}   {name}")
    print("  The index is a classification, not a stiffness: Ic and Vs30 are")
    print("  different measurements of the same soil and neither is a substitute")
    print("  for the other (lesson 02).")

    section("3. Cross-hole: two geometries, two different answers")
    print(f"SYNTHETIC model: {VS_LAYERS}")
    print(f"borehole separation {L_BOREHOLE:.1f} m")
    print("\n  (a) same-depth source and receiver, horizontal path: v = L / t")
    print("  z(m)   t(ms)   v = L/t (m/s)   true Vs (m/s)")
    for z in (1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0):
        t_h = first_arrival_crosshole(z, z, L_BOREHOLE)
        print(f"  {z:5.1f}  {t_h:6.3f}   {L_BOREHOLE / (t_h * 1e-3):13.1f}   "
              f"{vs_of_depth(z - 1e-9):13.1f}")
    print("  This configuration measures the layer velocity directly, because the")
    print("  ray is horizontal inside one layer.  It needs a source and a receiver")
    print("  at the SAME depth, which requires a source that can be lowered, or a")
    print("  string of sources and receivers in both holes.")
    print("\n  (b) fixed source at the surface, receivers deepening in the second")
    print("  hole, and the straight-ray interval formula v = (r2-r1)/(t2-t1):")
    print("  z_r(m)   range(m)   exact t(ms)   dt(ms)   v_int straight(m/s)   true")
    zs = np.arange(1.0, 14.01, 1.0)
    times = np.array([first_arrival_crosshole(Z_SOURCE, z, L_BOREHOLE) for z in zs])
    rng_geo = np.sqrt(L_BOREHOLE ** 2 + (zs - Z_SOURCE) ** 2)
    for i in range(1, zs.size):
        v_int = (rng_geo[i] - rng_geo[i - 1]) / ((times[i] - times[i - 1]) * 1e-3)
        z_mid = 0.5 * (zs[i] + zs[i - 1])
        print(f"  {zs[i]:6.1f}  {rng_geo[i]:8.3f}  {times[i]:11.3f}  "
              f"{times[i] - times[i - 1]:7.3f}  {v_int:19.1f}  "
              f"{vs_of_depth(z_mid - 1e-9):6.1f}")
    print("  The negative value at 2-3 m is not an arithmetic slip: the ray to the")
    print("  deeper receiver dives into the faster second layer and arrives EARLIER")
    print("  than a straight-line path would, so (r2-r1)/(t2-t1) returns an")
    print("  unphysical velocity.  A refraction-corrected (Snell) inversion or a")
    print("  layered model is required; the straight-ray formula is only valid when")
    print("  the path crosses no velocity increase, which is exactly what a")
    print("  geotechnical site investigation cannot assume.")

    section("4. Down-hole: interval velocities, and what cancels")
    print("  A constant trigger-time offset cancels exactly in a difference of")
    print("  arrival times; a random trigger jitter does not.")
    z_rec = np.arange(1.0, 13.01, 2.0)
    t_true = np.array([first_arrival_crosshole(Z_SOURCE, z, L_BOREHOLE) for z in z_rec])
    rng_rec = np.sqrt(L_BOREHOLE ** 2 + (z_rec - Z_SOURCE) ** 2)
    print("  z_r(m)   t_true(ms)   v_int exact   v_int with +1 ms offset   "
          "v_int with 1 ms jitter")
    for shift, jitter in ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0)):
        t_a = t_true + shift + jitter * RNG.standard_normal(t_true.size)
        v_a = (rng_rec[1:] - rng_rec[:-1]) / ((t_a[1:] - t_a[:-1]) * 1e-3)
        print(f"  offset {shift:.1f} ms, jitter {jitter:.1f} ms: "
              + "  ".join(f"{v:7.1f}" for v in v_a))
    print("  The +1 ms constant offset reproduces the exact interval velocities to")
    print("  the printed precision: a constant trigger delay cancels in a")
    print("  difference.  The jitter line scatters by tens of per cent, and the")
    print("  scatter is largest where the interval travel time is smallest -- i.e.")
    print("  in the fastest, deepest intervals and wherever the receiver spacing is")
    print("  short.  That is an arithmetic property, not a field-craft problem: the")
    print("  uncertainty of an interval velocity is delta(t)/delta(t), so it grows")
    print("  as the interval gets faster.")

    section("5. Derived stiffness, and index versus stiffness")
    print("  Gmax = rho Vs^2 with rho = "
          f"{RHO_KG_M3:.0f} kg/m^3 (SYNTHETIC)")
    print("  top(m)  bottom(m)   Vs(m/s)   Gmax(MPa)   E = 2G(1+nu) with nu=0.3 (MPa)")
    for top, bot, vs in VS_LAYERS:
        gmax = RHO_KG_M3 * vs ** 2 / 1e6
        print(f"  {top:6.1f}  {bot:8.1f}   {vs:7.1f}   {gmax:9.1f}   "
              f"{2 * gmax * 1.3:25.1f}")
    print("\n  Ratio (N1)60/Vs for two depths of the two profiles of this demo:")
    for z, n, er in SPT[2:4]:
        sv_eff = effective_stress_kpa(z)
        n1 = n * er / ER_REF * np.sqrt(PA_KPA / sv_eff)
        vs = vs_of_depth(z)
        print(f"    z = {z:.1f} m: (N1)60 = {n1:.1f}, Vs = {vs:.0f} m/s, "
              f"ratio = {n1 / vs:.4f} s/m")
    print("  A ratio is not a correlation.  Penetration resistance and small-strain")
    print("  stiffness respond to different properties (density and stress state")
    print("  versus shear modulus), and any transfer function between them is an")
    print("  empirical fit with scatter that must be quoted with the fit.")


if __name__ == "__main__":
    main()
