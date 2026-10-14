#!/usr/bin/env python3
"""Marine subduction zones: critical taper of a Coulomb wedge, flexural bending
of the incoming plate at the trench, and the accretion budget of a prism.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_zones_marine_demo.py

Everything here is SYNTHETIC.  The wedge, the plate and the prism are teaching
models with the stated model constants: no real trench, prism, subduction zone or
cruise is used, and no number is quoted from a published measurement.

Contents
--------
1. Critical taper: derivation check by numerical force balance, alpha vs lambda.
2. Flexural bending: D, flexural parameter, deflection, outer-rise bulge,
   verified against a Fourier solution of the beam equation.
3. Bending stress and the effective elastic thickness implied by a yield cap.
4. Accretion budget: sediment flux, prism width, pore-water expulsion.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 9.81              # m/s^2
RHO_R = 2700.0        # kg/m^3   wedge rock density (model)
RHO_W = 1030.0        # kg/m^3   seawater (model)
RHO_M = 3300.0        # kg/m^3   mantle (model)
E_YOUNG = 70.0e9      # Pa       elastic modulus of the plate (model)
NU = 0.25             # dimensionless Poisson ratio (model)
SEC_PER_MYR = 3.15576e13


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def k_stress(phi_deg):
    """Ratio of horizontal to vertical effective stress at Coulomb failure."""
    phi = np.radians(phi_deg)
    return (1.0 + np.sin(phi)) / (1.0 - np.sin(phi))


def wedge_forces(alpha, beta, mu_b, lam, K, L=100e3, rho=RHO_R):
    """Numerically integrated horizontal force balance on a finite-angle wedge.

    Returns (back push, basal shear, base-normal horizontal component) in N/m.
    """
    x = np.linspace(0.0, L, 20001)
    H = x * (np.tan(alpha) + np.tan(beta))
    integral_H = np.trapezoid(H, x)          # m^2
    P_back = K * (1.0 - lam) * rho * G * H[-1] ** 2 / 2.0
    tau_b = mu_b * (1.0 - lam) * rho * G * integral_H / np.cos(beta)
    W = rho * G * integral_H
    return P_back, tau_b, W * np.tan(beta)


def critical_alpha(beta, mu_b, lam, K):
    """Small-angle critical taper: theta = (mu_b (1-lam_b) + beta) / (K (1-lam))."""
    return (mu_b * (1.0 - lam) + beta) / (K * (1.0 - lam)) - beta


def flexural_rigidity(Te, E=E_YOUNG, nu=NU):
    """D = E Te^3 / (12 (1 - nu^2)) in N m."""
    return E * Te ** 3 / (12.0 * (1.0 - nu ** 2))


def main():
    section("1. Critical taper of a Coulomb wedge")
    phi, mu_b, lam, beta_deg = 30.0, 0.55, 0.40, 3.0
    beta = np.radians(beta_deg)
    K = k_stress(phi)
    alpha = critical_alpha(beta, mu_b, lam, K)
    theta = alpha + beta
    print("  model constants: internal friction angle phi = "
          f"{phi:.0f} deg -> mu = tan(phi) = {np.tan(np.radians(phi)):.3f}")
    print(f"  K = (1+sin phi)/(1-sin phi) = {K:.4f} (compressional stress state)")
    print(f"  basal friction mu_b = {mu_b:.2f}; pore-pressure ratio lambda = "
          f"{lam:.2f}; decollement dip beta = {beta_deg:.1f} deg")
    print(f"  critical taper theta = alpha + beta = "
          f"({mu_b:.2f} x (1-{lam:.2f}) + {beta:.5f}) / ({K:.2f} x (1-{lam:.2f}))")
    print(f"    theta = {theta:.5f} rad = {np.degrees(theta):.2f} deg")
    print(f"    alpha = theta - beta = {np.degrees(alpha):.2f} deg")
    P, T, N = wedge_forces(alpha, beta, mu_b, lam, K)
    print(f"\n  numerical force balance at that alpha (per metre of trench):")
    print(f"    back push          {P:.4e} N/m")
    print(f"    basal shear        {T:.4e} N/m")
    print(f"    base-normal horiz. {N:.4e} N/m")
    print(f"    residual (push - resistances) = {P - T - N:+.4e} N/m "
          f"({(P - T - N) / P * 100:+.2f}% of the push)")
    alpha_flat = (mu_b * (1.0 - lam) + beta) / (K * (1.0 - lam))
    P_f, T_f, N_f = wedge_forces(alpha_flat, beta, mu_b, lam, K)
    print(f"    forgetting to subtract beta gives alpha = "
          f"{np.degrees(alpha_flat):.2f} deg, residual "
          f"{P_f - T_f - N_f:+.3e} N/m "
          f"({(P_f - T_f - N_f) / P_f * 100:+.1f}% of the push), so the residual")
    print("    is a usable test of the algebra.")

    print("\n  pore-pressure sensitivity (beta = 3 deg, mu_b = 0.55, phi = 30 deg):")
    print("    lambda   alpha (deg)   theta (deg)   dalpha/dlambda (deg)")
    prev_lam = prev_a = None
    for lam_i in (0.0, 0.2, 0.4, 0.6, 0.8, 0.9):
        a_i = np.degrees(critical_alpha(beta, mu_b, lam_i, K))
        slope = "--" if prev_a is None else \
            f"{(a_i - prev_a) / (lam_i - prev_lam):+8.2f}"
        print(f"    {lam_i:6.2f}   {a_i:11.2f}   "
              f"{a_i + np.degrees(beta):12.2f}   {slope:>18s}")
        prev_lam, prev_a = lam_i, a_i
    print("  the wedge slope is controlled by the pore pressure, which is why a")
    print("  gas-hydrate or overpressured decollement changes prism geometry.")

    section("2. Flexural bending of the incoming plate at the trench")
    Te = 30e3
    D = flexural_rigidity(Te)
    k_found = (RHO_M - RHO_W) * G
    lam_f = (k_found / (4.0 * D)) ** 0.25
    alpha_f = 1.0 / lam_f
    P_load = 3.0e12
    W0 = P_load / (8.0 * D * lam_f ** 3)
    print(f"  Te = {Te / 1e3:.0f} km, E = {E_YOUNG:.1e} Pa, nu = {NU:.2f}")
    print(f"  D = E Te^3 / (12 (1-nu^2)) = {D:.4e} N m")
    print(f"  foundation modulus (rho_m - rho_w) g = {k_found:.1f} N/m^3")
    print(f"  flexural parameter alpha = (4D/k)^(1/4) = {alpha_f / 1e3:.2f} km, "
          f"lambda = 1/alpha = {lam_f:.4e} 1/m")
    print(f"  line load P = {P_load:.1e} N/m -> peak deflection "
          f"w0 = P/(8 D lambda^3) = {W0:.1f} m")
    bulge_x = np.pi * alpha_f
    print(f"  outer-rise bulge: w = -w0 exp(-pi) = {-W0 * np.exp(-np.pi):.1f} m "
          f"at x = pi alpha = {bulge_x / 1e3:.1f} km")
    print(f"  zero crossing of w at x = 3pi/4 alpha = "
          f"{3 * np.pi / 4 * alpha_f / 1e3:.1f} km")
    print(f"  bending moment at the load, M0 = P/(4 lambda) = "
          f"{P_load / (4 * lam_f):.4e} N (per unit width)")

    # independent check: Fourier solution of D w'''' + k w = q(x), periodic
    print("\n  independent check: Fourier solution of D w'''' + k w = q on a")
    print("  periodic domain (a different route to the same ODE):")
    L, n_nodes = 4000e3, 8192
    x = np.linspace(-L / 2, L / 2, n_nodes, endpoint=False)
    dx = x[1] - x[0]
    sigma_q = 1.5e3
    q = P_load * np.exp(-(x ** 2) / (2 * sigma_q ** 2)) / \
        (np.sqrt(2 * np.pi) * sigma_q)      # integrates to P_load
    kf = 2.0 * np.pi * np.fft.fftfreq(n_nodes, d=dx)
    w_hat = np.fft.fft(q) / (k_found + D * kf ** 4)
    w_fd = np.real(np.fft.ifft(w_hat))
    i0 = int(np.argmin(np.abs(x)))
    i_min = int(np.argmin(w_fd))
    print(f"    domain {L / 1e3:.0f} km, {n_nodes} nodes, dx = {dx:.1f} m")
    print(f"    Fourier |w(0)|    = {abs(w_fd[i0]):.1f} m (analytic {W0:.1f} m, "
          f"difference {(abs(w_fd[i0]) - W0) / W0 * 100:+.2f}%)")
    print(f"    Fourier extremum  = {abs(w_fd[i_min]):.1f} m at x = "
          f"{x[i_min] / 1e3:.1f} km (analytic bulge "
          f"{W0 * np.exp(-np.pi):.1f} m at {bulge_x / 1e3:.1f} km; the sign is")
    print("    opposite to the deflection, as the bulge must be)")
    print("    the small differences are the finite width of the numerical load")
    print("    and the periodic wrap; the shape and amplitude agree.")

    section("3. Bending stress and the effective elastic thickness")
    M0 = P_load / (4 * lam_f)
    sigma_max = 6.0 * M0 / Te ** 2
    print(f"  fibre stress at the plate surface, sigma = 6 M0 / Te^2:")
    print(f"    M0 = {M0:.4e} N, Te = {Te / 1e3:.0f} km -> sigma = "
          f"{sigma_max / 1e6:.0f} MPa")
    sigma_yield = 500e6
    # at fixed deflection w0, alpha ~ Te^-1/2; solve for the Te that gives the cap
    Te_cap = Te * (sigma_max / sigma_yield) ** 2
    print(f"  if the plate yields at {sigma_yield / 1e6:.0f} MPa, the elastic")
    print(f"  thickness that keeps the same peak deflection is")
    print(f"    Te = {Te / 1e3:.0f} km x ({sigma_max / 1e6:.0f}/{sigma_yield / 1e6:.0f})^2 "
          f"= {Te_cap / 1e3:.1f} km")
    D_c = flexural_rigidity(Te_cap)
    lam_c = (k_found / (4.0 * D_c)) ** 0.25
    P_c = W0 * 8.0 * D_c * lam_c ** 3
    M_c = P_c / (4 * lam_c)
    print(f"    check at that thickness: D = {D_c:.3e} N m, alpha = "
          f"{1 / lam_c / 1e3:.1f} km,")
    print(f"    load adjusted to the same {W0:.0f} m deflection: P = "
          f"{P_c:.3e} N/m, sigma = {6 * M_c / Te_cap ** 2 / 1e6:.0f} MPa")
    print("  the bent plate therefore behaves as a thinner elastic plate than its")
    print("  thermal thickness: permanent deformation near the trench is why.")

    section("4. Accretion budget of the prism")
    h_sed, v_conv, f_acc, t_myr = 400.0, 0.050, 0.50, 10.0
    flux = h_sed * v_conv                      # m^2/yr per metre of trench
    print(f"  incoming sediment thickness {h_sed:.0f} m, convergence rate "
          f"{v_conv * 1e3:.0f} mm/yr")
    print(f"  volume flux = {flux:.1f} m^2/yr per metre of trench "
          f"= {flux * 1e6 / 1e6:.1f} km^3 per Myr per km of trench")
    for f in (0.0, 0.5, 1.0):
        A = f * flux * t_myr * 1e6
        tan_th = np.tan(theta)
        w = np.sqrt(2.0 * A / tan_th)
        print(f"  accreted fraction {f:.1f}: cross-section after {t_myr:.0f} Myr "
              f"= {A / 1e6:.2f} km^2, width at a {np.degrees(theta):.1f} deg taper "
              f"= {w / 1e3:.1f} km")
    print("  (a fraction above 1 is subduction erosion: the prism shrinks and the")
    print("   forearc subsides.)")
    phi0, phi_lam = 0.60, 1000.0
    H_sec = 1000.0
    water = phi0 * phi_lam * (1.0 - np.exp(-H_sec / phi_lam))
    A_v = f_acc * flux * t_myr * 1e6
    vol_water = water * A_v
    print(f"\n  pore water: porosity phi0 = {phi0:.2f} at the surface, "
          f"compaction length {phi_lam:.0f} m,")
    print(f"  section thickness {H_sec:.0f} m -> water released "
          f"{water:.0f} m^3 per m^2 of section")
    print(f"  over the accreted area {A_v / 1e6:.2f} km^2: "
          f"{vol_water:.3e} m^3 per metre of trench")
    rate_m3 = vol_water / (t_myr * 1e6)          # m^3/yr per metre of trench
    print(f"  averaged over {t_myr:.0f} Myr: {rate_m3:.1f} m^3/yr per metre of "
          f"trench = {rate_m3 * 1e3:.0f} L/yr = {rate_m3 * 1e3 / 31.5576e6:.3f} "
          f"L/s")
    print("  every number here is a model value; the partition of the flux between")
    print("  accreted, subducted and underplated is the least certain quantity.")

    section("5. Worked examples used in the lesson")
    print(f"(a) critical taper: theta = {np.degrees(theta):.2f} deg, alpha = "
          f"{np.degrees(alpha):.2f} deg, residual of the balance = "
          f"{(P - T - N) / P * 100:+.2f}%")
    print(f"(b) flexure: D = {D:.4e} N m, alpha = {alpha_f / 1e3:.2f} km, "
          f"w0 = {W0:.1f} m, bulge {W0 * np.exp(-np.pi):.1f} m at "
          f"{bulge_x / 1e3:.0f} km")
    print(f"(c) bending stress {sigma_max / 1e6:.0f} MPa at Te = 30 km; "
          f"Te = {Te_cap / 1e3:.1f} km for a 500 MPa cap at the same deflection")
    print(f"(d) prism: accreted area {A_v / 1e6:.2f} km^2 in {t_myr:.0f} Myr, "
          f"width {np.sqrt(2 * A_v / np.tan(theta)) / 1e3:.1f} km")
    print(f"(e) pore-water release = {water:.0f} m^3/m^2 of section, "
          f"{vol_water:.3e} m^3 per metre of trench")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
