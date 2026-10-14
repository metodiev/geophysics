#!/usr/bin/env python3
"""River profiles and tectonic inference: the stream-power steady state, the
steepness index and concavity, the chi transform, the exact degeneracy of the
erodibility with the uplift rate, the sensitivity to the assumed exponents, and
a transient knickpoint.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python river_profile_tectonics_demo.py

Everything is SYNTHETIC: the drainage network is a chosen area-distance relation,
not a mapped river, and the erosion parameters are teaching values.

Contents
--------
1. Steady stream-power profile and the measured concavity.
2. The chi transform and the recovery of the steepness index.
3. The exact degeneracy: only the ratio U/K is measurable in steady state.
4. The bias from an assumed-wrong concavity or exponent.
5. A transient knickpoint and what a steady-state inference then reports.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# grid: x runs downstream from the divide (x = 0) to the outlet (x = L)
L_M = 1.0e5            # 100 km
N_NODE = 401
X = np.linspace(0.0, L_M, N_NODE)
A_MIN, A_MAX = 1.0e5, 1.0e6      # m^2
HACK_EXP = 1.7                   # chosen exponent of the area-distance relation
A = A_MIN + (A_MAX - A_MIN) * (X / L_M) ** HACK_EXP

M_EXP = 0.5            # chosen area exponent
N_EXP = 1.0            # chosen slope exponent
K_TRUE = 1.0e-5        # 1/yr for n = 1, m = 0.5
U_TRUE = 1.0e-4        # m/yr (0.1 mm/yr)


def steady_profile(U, K, m=M_EXP, n=N_EXP):
    """Integrate dz/dx = (U/K)^(1/n) A^(-m/n) downstream to z(L) = 0."""
    s = (U / K) ** (1.0 / n) * A ** (-m / n)
    z = np.zeros_like(X)
    for i in range(N_NODE - 2, -1, -1):
        z[i] = z[i + 1] + 0.5 * (s[i] + s[i + 1]) * (X[i + 1] - X[i])
    return z, s


def chi_transform(m_over_n):
    """chi(x) = integral of (A0/A)^(m/n) dx upstream, with A0 = max(A)."""
    f = (A_MAX / A) ** m_over_n
    chi = np.zeros_like(X)
    for i in range(1, N_NODE):
        chi[i] = chi[i - 1] + 0.5 * (f[i] + f[i - 1]) * (X[i] - X[i - 1])
    return chi


def demonstration_1():
    section("1. Steady stream-power profile and the measured concavity")
    print("  Stream-power incision: dz/dt = U - K A^m S^n with S = -dz/dx.")
    print("  In steady state U = K A^m S^n, so")
    print("     S = k_s A^(-theta),  theta = m/n,  k_s = (U/K)^(1/n).")
    print("  The constants are usually quoted as theta (a ratio of exponents, so")
    print("  it is reasonably well constrained) and k_s (a ratio of two poorly")
    print("  known quantities, so it is not).\n")
    print(f"  synthetic network: A from {A_MIN:.1e} to {A_MAX:.1e} m^2 over "
          f"L = {L_M / 1e3:.0f} km,")
    print(f"  A(x) = A_min + (A_max - A_min)(x/L)^{HACK_EXP:.1f}; "
          f"m = {M_EXP:.1f}, n = {N_EXP:.1f}")
    print(f"  U = {U_TRUE * 1e3:.2f} mm/yr, K = {K_TRUE:.1e} (units of "
          f"m^(1-2m)/yr = 1/yr here)\n")
    z, s = steady_profile(U_TRUE, K_TRUE)
    print("    x (km)   A (km^2)   slope (m/km)   elevation (m)")
    for i in (0, 100, 200, 300, 400):
        print(f"    {X[i] / 1e3:7.1f}   {A[i] / 1e6:9.3f}   "
              f"{s[i] * 1e3:13.2f}   {z[i]:13.1f}")
    p = np.polyfit(np.log(A), np.log(s), 1)
    print(f"\n  fitted slope-area relation: S = {np.exp(p[1]):.6e} A^{p[0]:.6f}")
    print(f"    measured theta = {-p[0]:.6f}   input m/n = {M_EXP / N_EXP:.6f}")
    print(f"    measured k_s   = {np.exp(p[1]):.6e}   input (U/K)^(1/n) = "
          f"{U_TRUE / K_TRUE:.6e}")
    print("  (units of k_s: m^(2m/n) per yr^(1/n); the numbers here are in")
    print("   metres and years, and the slope of the profile depends on both.)")


def demonstration_2():
    section("2. The chi transform")
    print("  With theta = m/n, define chi(x) = integral of (A0/A(x'))^theta dx'.")
    print("  Then dz/dchi = -k_s / A0^theta exactly, so a steady profile is a")
    print("  straight line in the (chi, z) plane; the normalisation A0 is a choice,")
    print("  and the steepness index is read off the slope together with it.\n")
    z, s = steady_profile(U_TRUE, K_TRUE)
    chi = chi_transform(M_EXP / N_EXP)
    p = np.polyfit(chi, z, 1)
    resid = z - np.polyval(p, chi)
    ss_tot = np.sum((z - z.mean()) ** 2)
    r2 = 1.0 - np.sum(resid ** 2) / ss_tot
    print(f"    chi spans 0 to {chi[-1] / 1e3:.2f} km")
    k_s_rec = -p[0] * A_MAX ** (M_EXP / N_EXP)
    print(f"    fitted slope dz/dchi = {p[0]:.6e}")
    print(f"    k_s recovered as -slope * A0^theta = {k_s_rec:.6e}")
    print(f"    input k_s = (U/K)^(1/n) = {U_TRUE / K_TRUE:.6e}")
    print(f"    relative difference = "
          f"{abs(k_s_rec - U_TRUE / K_TRUE) / (U_TRUE / K_TRUE):.3e}")
    print(f"    R^2 of the straight-line fit = {r2:.10f}")
    print(f"    largest residual of the fit  = {np.max(np.abs(resid)):.3e} m")
    print("\n  the chi plot is exactly linear here because the profile was built")
    print("  from the steady state it is tested against; on real data the")
    print("  curvature that remains is the signal, and its interpretation is where")
    print("  the assumptions enter.")
    print("\n  a wrong concavity destroys the linearity.  Using theta_try instead:")
    print("    theta_try   k_s recovered   R^2")
    for th in (0.25, 0.4, M_EXP / N_EXP, 0.6, 0.8):
        chi_try = chi_transform(th)
        pt = np.polyfit(chi_try, z, 1)
        rt = z - np.polyval(pt, chi_try)
        r2t = 1.0 - np.sum(rt ** 2) / ss_tot
        print(f"    {th:9.2f}   {-pt[0] * A_MAX ** th:12.5e}   {r2t:.6f}")
    print("  the fitted slope changes by a factor of several and the fit quality")
    print("  degrades: a chi plot constrains theta and k_s jointly, not k_s alone.")


def demonstration_3():
    section("3. The exact degeneracy: only the ratio U/K is measurable")
    print("  In steady state the profile depends on U and K only through")
    print("  k_s = (U/K)^(1/n).  Three parameter pairs with the same ratio:\n")
    z_ref, _ = steady_profile(U_TRUE, K_TRUE)
    print("    U (mm/yr)   K (1/yr)     k_s (m)      max |z - z_ref| (m)")
    for fac in (0.01, 0.1, 1.0, 10.0, 100.0):
        z_i, _ = steady_profile(U_TRUE * fac, K_TRUE * fac)
        print(f"    {U_TRUE * fac * 1e3:9.3f}   {K_TRUE * fac:.3e}   "
              f"{(U_TRUE * fac) / (K_TRUE * fac):10.4e}   "
              f"{np.max(np.abs(z_i - z_ref)):18.3e}")
    print("\n  the profiles are identical to round-off across four orders of")
    print("  magnitude in both parameters.  This is not a limitation of the data")
    print("  or of the fit: no steady-state river profile can separate the")
    print("  uplift rate from the erodibility, and a paper that quotes an uplift")
    print("  rate from a steepness index has assumed a K to do it.")
    print("\n  the assumption is not harmless: for the same k_s, a factor of ten")
    print("  in K is a factor of ten in the uplift rate.")
    z10, _ = steady_profile(U_TRUE * 10.0, K_TRUE)
    print(f"    k_s for U x10 with K fixed: {(U_TRUE * 10.0) / K_TRUE:.4e}")
    print(f"    its maximum elevation above the reference profile: "
          f"{np.max(z10 - z_ref):.1f} m")
    print("  The way out is not a better profile but an independent measurement")
    print("  of one of the two: a dated terrace, a cosmogenic erosion rate, a")
    print("  sediment budget or a thermochronological exhumation rate.")


def demonstration_4():
    section("4. The bias from an assumed-wrong exponent")
    print("  Two exponent assumptions enter: the concavity theta = m/n (used in")
    print("  the chi transform) and the slope exponent n (used to convert k_s to")
    print("  an uplift rate).\n")
    z, _ = steady_profile(U_TRUE, K_TRUE)
    print("  (a) wrong theta in the chi transform, then k_s read off the slope:")
    print("      theta_try   k_s recovered   k_s true    bias in U (K fixed)")
    k_s_true = U_TRUE / K_TRUE
    for th in (0.4, 0.45, 0.5, 0.55, 0.6):
        chi_try = chi_transform(th)
        p = np.polyfit(chi_try, z, 1)
        k_rec = -p[0] * A_MAX ** th
        print(f"      {th:9.2f}   {k_rec:13.6e}   {k_s_true:.4e}   "
              f"{(k_rec / k_s_true - 1.0) * 100:+16.2f}%")
    print("\n  (b) wrong n in the conversion U = K k_s^n, with k_s correct:")
    print("      n_try   U recovered (mm/yr)   bias")
    k_s_meas = k_s_true
    for n_try in (0.8, 0.9, 1.0, 1.1, 1.2):
        u_rec = K_TRUE * k_s_meas ** n_try
        print(f"      {n_try:5.1f}   {u_rec * 1e3:21.4f}   "
              f"{(u_rec / U_TRUE - 1.0) * 100:+7.2f}%")
    print("\n  the concavity error is the more damaging of the two in this test,")
    print("  because it distorts the abscissa of the chi plot and biases the")
    print("  slope systematically; the exponent error scales the answer.  Neither")
    print("  is detectable from the profile alone, since the profile is what the")
    print("  fit was made from.")


def demonstration_5():
    section("5. A transient knickpoint")
    print("  With n = 1, U = K A^m S becomes, in the chi coordinate,")
    print("     dz/dt = U - K A0^m dz/dchi,")
    print("  a linear advection of the profile with speed c = K A0^m.  Doubling U")
    print("  at t = 0 propagates a knickpoint upstream at exactly that speed.\n")
    c = K_TRUE * A_MAX ** M_EXP
    print(f"  c = K A0^m = {c:.4e} m/yr = {c * 1e3:.3f} mm/yr = "
          f"{c * 1e6 / 1e3:.1f} km/Myr")
    chi = chi_transform(M_EXP / N_EXP)
    nth = chi.size
    dchi = np.diff(chi)                  # the chi grid is not uniform in x
    dt = 0.4 * float(np.min(dchi)) / c
    z0, _ = steady_profile(U_TRUE, K_TRUE)
    z = z0.copy()
    U_new = 2.0 * U_TRUE
    t_end = 9.0e6
    n_step = int(t_end / dt)
    print(f"  grid {nth} points in chi, spacing from {np.min(dchi):.1f} to "
          f"{np.max(dchi):.1f} m,")
    print(f"  dt = {dt / 1e6:.4f} Myr,")
    print(f"  {n_step} steps to {t_end / 1e6:.0f} Myr ->")
    print(f"  the knickpoint travel time from the outlet to the divide is")
    print(f"  chi_total/c = {chi[-1] / c / 1e6:.1f} Myr\n")
    track = []
    for step in range(n_step):
        # information travels upstream (towards smaller chi), so the advection
        # uses the downstream difference; the outlet elevation is pinned at 0
        dz = (z[1:] - z[:-1]) / dchi              # forward difference in chi
        z[:-1] = z[:-1] + dt * (U_new + c * dz)
        z[-1] = 0.0
        if step % max(1, n_step // 5) == 0:
            track.append((step * dt / 1e6, z[0], z[nth // 2], z[nth - 2]))
    print("    t (Myr)   z at divide (m)   z at chi/2 (m)   z near outlet (m)")
    for t, a1, a2, a3 in track:
        print(f"    {t:7.1f}   {a1:16.1f}   {a2:15.1f}   {a3:17.1f}")
    z_final = z
    print("\n  the inference a steady-state analysis would make on the final")
    print("  profile, reach by reach from the divide (reach 1) to the outlet")
    print("  (reach 5):")
    print("    reach   apparent U (mm/yr)   % of the true 0.20 mm/yr")
    edges = np.linspace(0, nth - 1, 6).astype(int)
    for r in range(5):
        sl = slice(edges[r], edges[r + 1] + 1)
        p = np.polyfit(chi[sl], z_final[sl], 1)
        u_app = K_TRUE * (-p[0] * A_MAX ** (M_EXP / N_EXP)) ** N_EXP
        print(f"    {r + 1:5d}   {u_app * 1e3:19.4f}   "
              f"{u_app / U_new * 100:21.1f}%")
    print("\n  The reaches close to the outlet have already adjusted to the new")
    print("  rate; the reaches near the divide still carry the old one, and the")
    print("  transition between them is the knickpoint, whose position moves")
    print("  upstream at the speed c computed above.  A steepness index quoted")
    print("  without saying which reach it came from is therefore not a")
    print("  measurement of any single uplift rate, and the knickpoint's position")
    print("  is itself the most useful observable in the profile.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    demonstration_5()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
