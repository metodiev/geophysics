#!/usr/bin/env python3
"""Crustal structure: what refraction, vertical reflection, converted phases and
isostasy can each say about a crust, and what they cannot.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python crustal_structure_demo.py

Everything is SYNTHETIC.  The continental and oceanic crustal models below are
chosen teaching models, not measured structures, and no station, survey or
published number is used.  Velocities, densities and thicknesses are all inputs
we chose so that the arithmetic of each method can be checked.

Contents
--------
1. A two-layer refraction: travel-time curve, critical and crossover distances.
2. Inverting noisy picks for thickness and velocities, with the scatter.
3. A systematic velocity error and the depth bias it produces.
4. Poisson's ratio from vp/vs and its sensitivity.
5. A SYNTHETIC continental and a SYNTHETIC oceanic column: vertical times and
   what a vertical-incidence depth conversion does with a wrong velocity.
6. Airy isostasy: root, ocean-basin crust, and the isostatic thickness scale.
7. Gravity equivalence: different (density, size, depth) bodies with identical
   anomalies, i.e. the fundamental non-uniqueness.
8. The same Moho seen four ways: the four depth answers for one structure.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --- SYNTHETIC two-layer refraction model (chosen, not measured) -------------
V1_C, V2_C, H_C = 6.00, 8.00, 30.0       # km/s, km/s, km


def head_wave_time(x_km, v1, v2, h_km):
    """First-arrival time of the head wave from a layer of thickness h."""
    return x_km / v2 + 2.0 * h_km * np.sqrt(1.0 / v1 ** 2 - 1.0 / v2 ** 2)


def direct_time(x_km, v1):
    return x_km / v1


def crossover_distance(v1, v2, h_km):
    """Offset at which the head wave overtakes the direct wave."""
    t_i = 2.0 * h_km * np.sqrt(1.0 / v1 ** 2 - 1.0 / v2 ** 2)
    return t_i / (1.0 / v1 - 1.0 / v2)


def critical_distance(v1, v2, h_km):
    """Smallest offset at which the head wave exists: 2 h tan(i_c)."""
    return 2.0 * h_km * v1 / np.sqrt(v2 ** 2 - v1 ** 2)


def h_from_intercept(t_i, v1, v2):
    """Thickness from the intercept time of the head-wave branch."""
    return t_i * v1 * v2 / (2.0 * np.sqrt(v2 ** 2 - v1 ** 2))


def main():
    section("1. A two-layer refraction: the travel-time curve")
    print(f"SYNTHETIC model: layer 1 v1 = {V1_C:.2f} km/s, half space "
          f"v2 = {V2_C:.2f} km/s, thickness H = {H_C:.1f} km")
    x_crit = critical_distance(V1_C, V2_C, H_C)
    x_cross = crossover_distance(V1_C, V2_C, H_C)
    t_i = head_wave_time(0.0, V1_C, V2_C, H_C)
    print(f"  critical distance (head wave first exists)  = {x_crit:7.2f} km")
    print(f"  crossover distance (head wave becomes first) = {x_cross:7.2f} km")
    print(f"  head-wave intercept time t_i                = {t_i:7.3f} s")
    print("\n  x (km)   T_direct (s)   T_head (s)   first arrival")
    for x in (10, 40, 68, 100, 150, 159, 200, 250):
        td = direct_time(x, V1_C)
        th = head_wave_time(x, V1_C, V2_C, H_C)
        first = "direct" if min(td, th) == td else "head"
        print(f"  {x:6.1f}   {td:11.4f}   {th:10.4f}   {first}")
    print(f"  thickness from the intercept: H = t_i v1 v2 / "
          f"(2 sqrt(v2^2 - v1^2)) = {h_from_intercept(t_i, V1_C, V2_C):.3f} km")

    section("2. Inverting noisy picks (300 synthetic surveys)")
    offsets = np.arange(10.0, 410.0, 10.0)
    sigma = 0.020                     # s, a typical hand-picking error
    n_trials = 300
    h_est = np.empty(n_trials)
    v1_est = np.empty(n_trials)
    v2_est = np.empty(n_trials)
    near = offsets <= x_crit          # direct branch is first arrival here
    far = offsets >= 1.2 * x_cross    # head branch is first arrival here
    for k in range(n_trials):
        tt = np.minimum(direct_time(offsets, V1_C),
                        head_wave_time(offsets, V1_C, V2_C, H_C))
        tt = tt + RNG.normal(0.0, sigma, offsets.size)
        v1_est[k] = np.polyfit(offsets[near], tt[near], 1)[0] ** (-1)
        slope, intercept = np.polyfit(offsets[far], tt[far], 1)
        v2_est[k] = 1.0 / slope
        h_est[k] = h_from_intercept(intercept, v1_est[k], v2_est[k])
    print(f"  noise sigma = {sigma * 1000:.0f} ms on every pick, "
          f"{offsets.size} offsets, {n_trials} repeat surveys")
    print(f"  direct branch fitted for {int(near.sum())} offsets "
          f"<= {x_crit:.1f} km; head branch for {int(far.sum())} offsets "
          f">= {1.2 * x_cross:.1f} km")
    print(f"  v1: true {V1_C:.3f} km/s, mean estimate {v1_est.mean():.4f} "
          f"+/- {v1_est.std():.4f} km/s")
    print(f"  v2: true {V2_C:.3f} km/s, mean estimate {v2_est.mean():.4f} "
          f"+/- {v2_est.std():.4f} km/s")
    print(f"  H : true {H_C:.3f} km, mean estimate {h_est.mean():.3f} "
          f"+/- {h_est.std():.3f} km")
    print(f"  the depth errors are correlated with the velocity errors: "
          f"corr(H, v1) = {np.corrcoef(h_est, v1_est)[0, 1]:+.3f}")
    print(f"  a 1 sigma pick error therefore becomes about "
          f"{100 * h_est.std() / H_C:.1f} % of depth here.")
    print(f"  the recovered velocities are much better determined than the depth:")
    print(f"  the head-wave branch measures v2 from a slope, an average over many")
    print(f"  picks, while H comes from a single intercept.")

    section("3. A systematic velocity error is worse than random noise")
    print("  the analyst adopts v1 too high by 5 % (keeps the same picks):")
    for bias in (-0.05, 0.0, 0.05):
        v1_bad = V1_C * (1.0 + bias)
        h_bad = h_from_intercept(t_i, v1_bad, V2_C)
        print(f"    v1 error {bias * 100:+5.1f} %  ->  H = {h_bad:6.2f} km "
              f"({h_bad - H_C:+6.2f} km, {100 * (h_bad - H_C) / H_C:+5.1f} %)")
    print("  the head-wave time itself is barely affected: the layer is simply")
    print("  interpreted as thicker or thinner, which is the depth-velocity")
    print("  trade-off in its simplest form.")

    section("4. Poisson's ratio from vp/vs")
    print("  nu = (k^2 - 2) / (2 (k^2 - 1)) with k = vp/vs")
    print("    k      nu       dnu/dk (per unit k)")
    for k in (1.60, 1.70, 1.75, 1.80, 1.90):
        nu = (k ** 2 - 2.0) / (2.0 * (k ** 2 - 1.0))
        dnu = 2.0 * k * (2.0 * (k ** 2 - 1.0)) - (k ** 2 - 2.0) * 4.0 * k
        dnu /= (2.0 * (k ** 2 - 1.0)) ** 2
        print(f"  {k:5.2f}   {nu:6.4f}   {dnu:9.4f}")
    k0 = 1.75
    nu0 = (k0 ** 2 - 2.0) / (2.0 * (k0 ** 2 - 1.0))
    dnu_dk = (2.0 * k0 * 2.0 * (k0 ** 2 - 1.0) - (k0 ** 2 - 2.0) * 4.0 * k0)
    dnu_dk /= (2.0 * (k0 ** 2 - 1.0)) ** 2
    print(f"  at k = {k0:.2f} (nu = {nu0:.4f}) a 1 % error in k moves nu by "
          f"about {abs(0.01 * k0 * dnu_dk):.4f}")
    print("  the mapping is smooth and monotonic, so a measured k converts")
    print("  directly to a compositional hint -- provided vp and vs sample the")
    print("  same volume, which is an assumption, not a fact.")

    section("5. A SYNTHETIC continental and a SYNTHETIC oceanic column")
    continental = [("sediment", 2.0, 3.00), ("upper crust", 15.0, 6.00),
                   ("lower crust", 18.0, 6.80)]
    oceanic = [("water", 4.0, 1.50), ("sediment", 1.0, 2.00),
               ("basalt layer 1", 1.5, 4.50), ("gabbro layer 2", 3.5, 6.20)]
    for name, col, v_sub in (("continental", continental, 8.10),
                             ("oceanic", oceanic, 8.10)):
        tot_h = sum(h for _, h, _ in col)
        tot_t = sum(h / v for _, h, v in col)
        print(f"  {name}: total column {tot_h:.1f} km, vertical travel time "
              f"{tot_t:.3f} s")
        for label, h, v in col:
            print(f"      {label:16s} {h:5.1f} km  vp = {v:4.2f} km/s  "
                  f"t = {h / v:6.3f} s")
        print(f"      mantle half-space vp = {v_sub:.2f} km/s")
        print(f"      column-averaged vp (harmonic mean) = "
              f"{tot_h / tot_t:.4f} km/s")
        for v_try in (tot_h / tot_t, 6.00):
            z = v_try * tot_t
            print(f"      depth conversion with v = {v_try:6.4f} km/s gives "
                  f"{z:7.2f} km ({z - tot_h:+6.2f} km from the true {tot_h:.1f} km)")

    section("6. Airy isostasy")
    rho_c, rho_m, rho_w = 2.90, 3.30, 1.03    # g/cm^3, chosen values
    print(f"  densities: crust {rho_c:.2f}, mantle {rho_m:.2f}, water {rho_w:.2f}"
          " g/cm^3")
    print("  a topographic load of height h displaces a root of")
    print("    r = h rho_c / (rho_m - rho_c),   total thickness = T0 + h + r")
    print("    h (km)    root r (km)    total thickness with T0 = 30 km (km)")
    for h in (0.0, 1.0, 2.0, 4.0, 6.0):
        r = h * rho_c / (rho_m - rho_c)
        print(f"  {h:7.1f}   {r:11.2f}   {30.0 + h + r:11.2f}")
    print(f"  scale factor: 1 km of topography needs "
          f"{rho_c / (rho_m - rho_c):.2f} km of root")
    print("\n  beneath an ocean basin of depth d the crust is thinner by")
    print("    delta_T = d (rho_m - rho_w) / (rho_m - rho_c)")
    for d in (2.0, 4.0, 5.0):
        delta = d * (rho_m - rho_w) / (rho_m - rho_c)
        print(f"    ocean depth {d:.1f} km -> crust thinner by {delta:6.2f} km "
              f"(from 30 km: {30.0 - delta:6.2f} km)")
    print("  the arithmetic is exact; the physics is the assumption that the")
    print("  compensation is local and complete, which is an idealisation.")

    section("7. Gravity equivalence: identical anomalies, different bodies")
    G = 6.674e-11        # SI, exact defining constant
    target_mgal = 10.0   # mGal, the anomaly to match
    target_si = target_mgal * 1e-5
    print(f"  a deep buried sphere gives g = (4/3) pi G rho a^3 / d^2;")
    print(f"  matching a {target_mgal:.1f} mGal anomaly is a one-parameter family:")
    print("    depth d (km)   radius a (km)   density contrast (g/cm^3)")
    for d_km in (2, 5, 10, 20, 40):
        d_m = d_km * 1e3
        a_m = 0.5 * d_m                     # choose a = d/2 to close the system
        rho = target_si * d_m ** 2 / ((4.0 / 3.0) * np.pi * G * a_m ** 3)
        print(f"  {d_km:12.0f}   {a_m / 1e3:13.1f}   {rho / 1e3:12.3f}")
    print("  every row produces the same anomaly: gravity sees rho * a^3 / d^2,")
    print("  one combination of three unknowns, so a gravity profile alone cannot")
    print("  return an unambiguous body.  Only a second observable can.")

    section("8. The same Moho, four methods, four answers")
    print("  SYNTHETIC truth: Moho at 30.0 km, vp = 6.00, vs = 3.50 km/s")
    vp, vs = 6.00, 3.50
    k = vp / vs
    p_tel = 0.060
    q_p = np.sqrt(1.0 / vp ** 2 - p_tel ** 2)
    q_s = np.sqrt(1.0 / vs ** 2 - p_tel ** 2)
    dt_ps = H_C * (q_s - q_p)
    print(f"  conversion delay for this structure: dt_Ps = {dt_ps:.3f} s "
          f"at p = {p_tel:.3f} s/km")
    for k_try in (1.65, 1.70, 1.714, 1.75, 1.80):
        vs_try = vp / k_try
        H_try = dt_ps / (np.sqrt(1.0 / vs_try ** 2 - p_tel ** 2) - q_p)
        print(f"    assumed k = {k_try:.3f} -> H = {H_try:6.2f} km "
              f"({H_try - H_C:+5.2f} km)")
    print("  summary of the four answers for the same structure:")
    print(f"    refraction (correct v1, v2)      H = {H_C:6.2f} km")
    print(f"    refraction with v1 5 % too high  H = "
          f"{h_from_intercept(t_i, V1_C * 1.05, V2_C):6.2f} km")
    print(f"    receiver function with k = 1.714 H = "
          f"{dt_ps / (np.sqrt(1.0 / (vp / 1.714) ** 2 - p_tel ** 2) - q_p):6.2f} km")
    print(f"    vertical reflection with a 10 % fast velocity  H = "
          f"{tot_avg():6.2f} km")
    print("  each answer is conditional on a velocity assumption, and the four")
    print("  assumptions are different.  The disagreement is not an error; it is")
    print("  the information the methods need before they can agree.")


def tot_avg():
    """Depth of the synthetic continental Moho from a vertical two-way time with
    a velocity that is 10 % too high."""
    col = [("sediment", 2.0, 3.00), ("upper crust", 15.0, 6.00),
           ("lower crust", 18.0, 6.80)]
    tot_h = sum(h for _, h, _ in col)
    tot_t = sum(h / v for _, h, v in col)
    v_mean = tot_h / tot_t
    return 1.1 * v_mean * tot_t


if __name__ == "__main__":
    main()
