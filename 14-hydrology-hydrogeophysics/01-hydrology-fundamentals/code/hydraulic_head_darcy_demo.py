#!/usr/bin/env python3
"""Hydraulic head, Darcy's law and groundwater flow: head from pressure and
elevation, gradients and fluxes, the validity conditions of Darcy's law,
refraction at a conductivity contrast, hydraulic diffusivity, and a numerical
verification of a Dupuit water table.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydraulic_head_darcy_demo.py

All wells, heads, conductivities and recharge rates below are SYNTHETIC teaching
values.  No real aquifer or well field is used.

Standard constants used:
    rho_w = 1000 kg/m^3      g = 9.81 m/s^2      mu_w = 1.002e-3 Pa s (20 C)

Contents
--------
1. Hydraulic head from elevation and pressure: h = z + p/(rho g).
2. Head gradient, specific discharge, and the average linear velocity.
3. Reynolds number: where Darcy's law stops being valid.
4. The Forchheimer correction: measuring where linearity breaks.
5. Refraction of flow at a conductivity contrast (the tangent law).
6. Hydraulic diffusivity: how fast a head change travels.
7. Verification: the Dupuit water table against a finite-difference solution.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_W = 1000.0
G = 9.81
MU_W = 1.002e-3


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def head_from_pressure(z_m, p_pa, rho_w=RHO_W, g=G):
    """Hydraulic head h = z + p/(rho g), in metres of water."""
    return z_m + p_pa / (rho_w * g)


def reynolds_number(q_m_s, d_grain_m, rho_w=RHO_W, mu_w=MU_W):
    """Re = rho_w q d / mu_w, the grain-scale Reynolds number used for Darcy."""
    return rho_w * q_m_s * d_grain_m / mu_w


def main():
    section("1. Hydraulic head from elevation and pressure")
    print("h = z + p / (rho_w g), with z the elevation of the measurement point")
    print("   z (m)   p (Pa)      p/(rho g) (m)      h (m)")
    for z, p in ((-30.0, 4.00e5), (-30.0, 3.00e5), (-10.0, 5.00e4), (-5.0, 0.0)):
        pw = p / (RHO_W * G)
        print(f"   {z:6.1f}   {p:9.2e}   {pw:15.3f}   {head_from_pressure(z, p):9.3f}")
    print("  the head is the elevation to which water would rise in a piezometer")
    print("  screened at the measurement point; a head ABOVE the ground surface")
    print("  means the point is confined and artesian.")

    section("2. Head gradient, specific discharge and pore velocity")
    h1, h2, L = 32.00, 31.40, 100.0
    K, n_e = 5.0e-5, 0.25
    i = (h1 - h2) / L
    q = K * i
    v = q / n_e
    print(f"  two SYNTHETIC wells {L:.0f} m apart: h1 = {h1:.2f} m, h2 = {h2:.2f} m")
    print(f"  gradient          i  = (h1 - h2)/L      = {i:.5f} (dimensionless)")
    print(f"  conductivity      K  = {K:.2e} m/s")
    print(f"  specific discharge q = K i              = {q:.4e} m/s"
          f" = {q * 86400:.4f} m/d")
    print(f"  effective porosity n_e = {n_e:.2f}")
    print(f"  average linear velocity v = q/n_e       = {v:.4e} m/s"
          f" = {v * 86400:.4f} m/d")
    print(f"  travel time to cross the {L:.0f} m: {L / (v * 86400):.1f} d"
          f" = {L / (v * 86400) / 365.25:.2f} yr")
    print(f"  volume flux through a 10 m x 5 m section: "
          f"{q * 10.0 * 5.0:.3e} m^3/s = {q * 10.0 * 5.0 * 86400:.4f} m^3/d")
    print("  q is a flux per unit TOTAL area; a tracer moves at v = q/n_e, which is")
    print(f"  {1.0 / n_e:.1f} times faster here.  Neither is 'the velocity of water'"
          " in a pore.")

    section("3. Reynolds number: the validity condition for Darcy's law")
    d_grain = 3.0e-4
    print(f"  Re = rho_w q d / mu_w with d = {d_grain * 1e3:.2f} mm (SYNTHETIC sand)")
    print("   q (m/s)      q (m/d)      Re         Darcy valid?")
    for qq in (3.0e-7, 1.0e-5, 3.0e-4, 1.0e-3, 3.34e-3, 1.0e-2):
        re = reynolds_number(qq, d_grain)
        print(f"   {qq:9.2e}   {qq * 86400:9.4f}   {re:9.2e}   "
              f"{'yes' if re < 1.0 else 'no'}")
    print(f"  Re = 1 at q = mu_w/(rho_w d) = {MU_W / (RHO_W * d_grain):.3e} m/s")
    print("  the criterion is grain-scale, so a coarse gravel reaches Re = 1 at a")
    print("  much smaller flux: for d = 10 mm, Re = 1 at "
          f"q = {MU_W / (RHO_W * 1e-2):.3e} m/s")

    section("4. The Forchheimer correction: measuring where linearity breaks")
    print("  synthetic column test: i = (mu_w/(k rho_w g)) q + c q^2")
    k_perm = 1.0e-11
    c_forch = 2.0e5
    print(f"  k = {k_perm:.1e} m^2, c = {c_forch:.1e} s^2/m^2 (SYNTHETIC)")
    print("   q (m/s)     i_linear    i_total     excess over linear")
    for qq in (1.0e-5, 1.0e-4, 5.0e-4, 1.0e-3, 2.0e-3, 5.0e-3):
        i_lin = MU_W / (k_perm * RHO_W * G) * qq
        i_tot = i_lin + c_forch * qq ** 2
        print(f"   {qq:9.2e}   {i_lin:10.3e}  {i_tot:10.3e}   "
              f"{(i_tot / i_lin - 1.0) * 100:13.1f}%")
    q_10 = 0.10 * MU_W / (k_perm * RHO_W * G) / c_forch
    print(f"  the excess reaches 10% at q = {q_10:.3e} m/s "
          f"({q_10 * 86400:.2f} m/d), i.e.")
    print(f"  at Re = {reynolds_number(q_10, d_grain):.2f} for "
          f"{d_grain * 1e3:.1f} mm sand - within a factor of two of the Re = 1")
    print("  rule of thumb but NOT equal to it.  The Darcy validity limit is a")
    print("  statement about an accepted error and the pore geometry, so both")
    print("  numbers (the criterion and the error it buys) must be quoted.")

    section("5. Refraction of flow at a conductivity contrast")
    print("  tangent law: tan(theta2)/tan(theta1) = K2/K1")
    K1, K2 = 5.0e-4, 1.0e-6
    print(f"  K1 = {K1:.1e} m/s (sand), K2 = {K2:.1e} m/s (silt)")
    print("   theta1 (deg)   theta2 (deg)   check: K2 tan(theta1) = K1 tan(theta2)")
    for th1_deg in (5.0, 15.0, 45.0, 75.0):
        th1 = np.deg2rad(th1_deg)
        th2 = np.arctan(K2 / K1 * np.tan(th1))
        print(f"   {th1_deg:12.1f}   {np.rad2deg(th2):12.3f}   "
              f"{K2 * np.tan(th1):.6f} vs {K1 * np.tan(th2):.6f}")
    print("  flux perpendicular to the layers is continuous, so the flow bends")
    print("  TOWARDS the normal when it enters the low-conductivity layer.  A")
    print(f"  {K1 / K2:.0f}-fold contrast turns a 45 deg ray to "
          f"{np.rad2deg(np.arctan(K2 / K1)):.4f} deg from the normal: horizontal flow")
    print("  in a sand becomes almost vertical across a silt layer.")

    section("6. Hydraulic diffusivity: how fast a head change travels")
    print("  confined/unconfined flow equation: S dh/dt = div(T grad h) + W")
    print("  hydraulic diffusivity D = T/S  [m^2/s or m^2/d]")
    print("   T (m^2/d)    S          D (m^2/d)   t to travel 1 km (d)   t to 10 km (d)")
    for T_d, S, label in ((198.7, 3.267e-4, "confined, stiff rock"),
                          (198.7, 1.504e-3, "confined, soft rock"),
                          (198.7, 0.20, "unconfined same T")):
        D = T_d / S
        t1 = 1.0e6 / (4.0 * D)
        t2 = 1.0e8 / (4.0 * D)
        print(f"   {T_d:9.1f}   {S:9.3e}   {D:10.3e}   {t1:20.4f}   {t2:14.4f}   "
              f"[{label}]")
    print("  the diffusion length scales as sqrt(4 D t): doubling the time reaches")
    print("  only sqrt(2) further.  With the same transmissivity, a confined aquifer")
    print("  transmits a head change 600 times faster than an unconfined one, because")
    print("  it needs to move almost no water to change its pressure.")

    section("7. Verification: Dupuit water table against a finite-difference solution")
    print("  1-D unconfined flow with recharge R:  d/dx(K h dh/dx) + R = 0")
    print("  which is linear in u = h^2:  d2u/dx2 = -2R/K, with u fixed at both ends")
    K_d, R_mm_d = 5.0e-5, 1.0
    R_m_s = R_mm_d * 1.0e-3 / 86400.0
    Lx, n = 1000.0, 201
    x = np.linspace(0.0, Lx, n)
    dx = x[1] - x[0]
    h_left, h_right = 20.0, 20.0
    print(f"  SYNTHETIC: K = {K_d:.1e} m/s, R = {R_mm_d:.2f} mm/d, "
          f"L = {Lx:.0f} m, h(0) = h(L) = {h_left:.1f} m")
    A = np.zeros((n, n))
    b = np.zeros(n)
    for j in range(1, n - 1):
        A[j, j - 1] = 1.0 / dx ** 2
        A[j, j] = -2.0 / dx ** 2
        A[j, j + 1] = 1.0 / dx ** 2
        b[j] = -2.0 * R_m_s / K_d
    A[0, 0] = 1.0
    b[0] = h_left ** 2
    A[-1, -1] = 1.0
    b[-1] = h_right ** 2
    u_num = np.linalg.solve(A, b)
    h_num = np.sqrt(u_num)
    u_ana = h_left ** 2 + (R_m_s / K_d) * x * (Lx - x)
    h_ana = np.sqrt(u_ana)
    print(f"  analytic water-table rise at mid-span = "
          f"{h_ana[n // 2] - h_left:.4f} m")
    print(f"  maximum |h_num - h_ana| over {n} nodes = "
          f"{np.max(np.abs(h_num - h_ana)):.3e} m")
    du_left = (-3.0 * u_num[0] + 4.0 * u_num[1] - u_num[2]) / (2.0 * dx)
    du_right = (3.0 * u_num[-1] - 4.0 * u_num[-2] + u_num[-3]) / (2.0 * dx)
    outflux = (K_d / 2.0) * (du_left - du_right) * 86400.0
    recharg = R_m_s * Lx * 86400.0
    print(f"  total recharge across the section = {recharg:.3e} m^2/d")
    print(f"  outflow across the two boundaries  = {outflux:.3e} m^2/d")
    print(f"  closure error = {abs(outflux - recharg):.3e} m^2/d "
          f"({abs(outflux - recharg) / recharg:.2e} relative)")
    print("  the finite-difference solution reproduces the analytic Dupuit parabola")
    print("  to machine precision, which validates the discretisation but does NOT")
    print("  validate Dupuit's assumptions (vertical flow neglected, no seepage face).")

    section("8. Non-uniqueness: head data alone cannot separate K from recharge")
    print("  Dupuit with uniform recharge obeys u = h1^2 + (R/K) x (L - x):")
    print("  it depends on R and K only through the RATIO R/K.")
    ratio = R_m_s / K_d
    print(f"  reference ratio R/K = {ratio:.6e} (dimensionless)")
    print("   K (m/s)     R (mm/d)    R/K            mid-span rise (m)   "
          "outflow (m^2/d)")
    ref = None
    for K_i, R_mm in ((1.0e-5, 0.2), (5.0e-5, 1.0), (1.0e-4, 2.0), (5.0e-4, 10.0)):
        R_i = R_mm * 1.0e-3 / 86400.0
        u_mid = h_left ** 2 + (R_i / K_i) * (Lx / 2.0) * (Lx / 2.0)
        rise = np.sqrt(u_mid) - h_left
        ref = rise if ref is None else ref
        print(f"   {K_i:9.2e}   {R_mm:9.2f}   {R_i / K_i:.6e}   {rise:18.6f}   "
              f"{R_i * Lx * 86400:12.3e}")
    print(f"  every row has R/K = {ratio:.6e} to 6 significant figures and gives the")
    print(f"  same water table to {abs(rise - ref):.2e} m.  The HEAD FIELD is identical;")
    print("  the OUTFLOW differs by a factor of 50.  A head measurement therefore")
    print("  constrains R/K, not R and K separately:")
    print("   - a discharge measurement (streamflow gain between two gauges) fixes R;")
    print("   - a pumping test fixes K;")
    print("   - with neither, the head data admit the whole one-parameter family above.")


if __name__ == "__main__":
    main()
