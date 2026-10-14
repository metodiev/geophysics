#!/usr/bin/env python3
"""Rifting and break-up: uniform (McKenzie) stretching, the water-loaded
subsidence it predicts, and the exponential that post-rift cooling approximates.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rift_and_breakup_demo.py

Everything is SYNTHETIC.  The lithosphere, its geotherm, the densities and the
stretching factors are chosen teaching values, not measurements of any real
margin.  No published subsidence curve is used or quoted.

Contents
--------
1. Geometry of uniform stretching: crust and lithosphere thinned by beta.
2. The heat equation after instantaneous stretching, solved on a grid.
3. Water-loaded subsidence from isostasy, integrated over the cooling column.
4. The t = 0 limit checked against the closed-form crustal-thinning term.
5. The post-rift curve fitted with S(t) = S0 + Sth (1 - exp(-t/tau)).
6. Sensitivity to beta, and the strain rate needed to rift in a given time.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
A_KM = 125.0            # initial lithosphere thickness
TC0_KM = 35.0           # initial crustal thickness
TM_C = 1300.0           # mantle potential temperature, deg C
ALPHA = 3.0e-5          # thermal expansion coefficient, 1/K
RHO_M = 3330.0          # mantle density at T = Tm, kg/m^3
RHO_C = 2800.0          # crust density, kg/m^3
RHO_W = 1030.0          # sea water density, kg/m^3
KAPPA_M2_S = 1.0e-6     # thermal diffusivity, m^2/s (SYNTHETIC, uniform)
G = 9.81                # m/s^2, standard gravity (exact standard constant)

DZ_KM = 0.5             # grid spacing in depth (puts tc0 and A/beta on nodes)
DT_MYR = 0.0025         # time step in Myr
T_END_MYR = 200.0       # total model time


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def kappa_km2_myr():
    """Convert the diffusivity to km^2/Myr and print the conversion."""
    seconds_per_myr = 365.25 * 24.0 * 3600.0 * 1.0e6
    value = KAPPA_M2_S * seconds_per_myr / 1.0e6
    print(f"  kappa = {KAPPA_M2_S:.1e} m^2/s  ->  "
          f"{KAPPA_M2_S:.1e} x {seconds_per_myr:.4e} s/Myr / 1e6 m^2/km^2")
    print(f"        = {value:.3f} km^2/Myr")
    return value


def equilibrium_geotherm(z_km):
    return TM_C * z_km / A_KM


def initial_geotherm(z_km, beta):
    """Geotherm immediately after uniform stretching: hot below A/beta."""
    thinned = A_KM / beta
    return TM_C * np.minimum(z_km, thinned) / thinned


def heat_solution(z_km, T0, beta, kappa, t_end_myr, record_myr):
    """Explicit finite-difference solution of T_t = kappa T_zz.

    Surface held at 0 C, base of the model held at Tm.  Returns a dict of times.
    """
    n = z_km.size
    r = kappa * DT_MYR / DZ_KM ** 2
    assert r <= 0.5, f"explicit scheme unstable: r = {r}"
    T = T0.copy()
    out = {}
    steps = int(round(t_end_myr / DT_MYR))
    wanted = {int(round(t / DT_MYR)): t for t in record_myr}
    for step in range(steps + 1):
        if step in wanted:
            out[wanted[step]] = T.copy()
        if step == steps:
            break
        T[1:n - 1] += r * (T[2:] - 2.0 * T[1:n - 1] + T[0:n - 2])
        T[0] = 0.0
        T[n - 1] = TM_C
    return out


def column_deficit(z_km, T, beta, tc_km):
    """Mass excess per unit area referenced to pure asthenosphere, kg/m^2.

    Phi = integral (rho(z) - rho_m) dz, with rho within the crust = rho_c and
    rho in the mantle = rho_m (1 + alpha (Tm - T)) so that cold mantle is dense.
    """
    rho = np.where(z_km <= tc_km, RHO_C,
                   RHO_M * (1.0 + ALPHA * (TM_C - T)))
    return np.trapezoid(rho - RHO_M, z_km) * 1.0e3


def subsidence_km(z_km, T, beta):
    """Water-loaded subsidence relative to the pre-rift equilibrium column."""
    tc = TC0_KM / beta
    phi_struct = column_deficit(z_km, T, beta, tc)
    phi_ref = column_deficit(z_km, equilibrium_geotherm(z_km), 1.0, TC0_KM)
    return (phi_struct - phi_ref) / (RHO_M - RHO_W) / 1.0e3


def fit_exponential(t_myr, s_km):
    """Least-squares fit of S0 + Sth (1 - exp(-t/tau))."""
    def model(t, s0, sth, tau):
        return s0 + sth * (1.0 - np.exp(-t / tau))

    from scipy.optimize import curve_fit
    p0 = (s_km[0], s_km[-1] - s_km[0], 50.0)
    popt, _ = curve_fit(model, t_myr, s_km, p0=p0, maxfev=20000)
    residual = model(t_myr, *popt) - s_km
    return popt, residual


def s0_closed(beta):
    """Exact water-loaded subsidence at t = 0 for uniform stretching.

    Phi_stretched(0) = Phi_reference / beta exactly, because pure shear thins
    every layer by the same factor, so S(0) = (1 - 1/beta)(A - B) with
    A = (rho_m - rho_c) tc0 / (rho_m - rho_w)                 (crust)
    B = rho_m alpha Tm (a - tc0)^2 / (2a) / (rho_m - rho_w)   (cold mantle)
    """
    a_term = (RHO_M - RHO_C) * TC0_KM / (RHO_M - RHO_W)
    b_term = (RHO_M * ALPHA * TM_C * (A_KM - TC0_KM) ** 2
              / (2.0 * A_KM) / (RHO_M - RHO_W))
    return (1.0 - 1.0 / beta) * (a_term - b_term), a_term, b_term


def s_inf_closed(beta):
    """Exact water-loaded subsidence after infinite cooling time."""
    tc = TC0_KM / beta
    crust = (RHO_M - RHO_C) * TC0_KM * (1.0 - 1.0 / beta) / (RHO_M - RHO_W)
    mantle = (RHO_M * ALPHA * TM_C * ((A_KM - tc) ** 2 - (A_KM - TC0_KM) ** 2)
              / (2.0 * A_KM) / (RHO_M - RHO_W))
    return crust + mantle


def main():
    z = np.arange(0.0, A_KM + DZ_KM / 2.0, DZ_KM)
    kappa = kappa_km2_myr()

    section("1. Geometry of uniform stretching")
    print(f"  SYNTHETIC lithosphere: a = {A_KM:.0f} km, crust tc0 = {TC0_KM:.0f} km, "
          f"Tm = {TM_C:.0f} C")
    print(f"  densities: rho_m = {RHO_M:.0f}, rho_c = {RHO_C:.0f}, "
          f"rho_w = {RHO_W:.0f} kg/m^3")
    print(f"  thermal expansion alpha = {ALPHA:.1e} 1/K")
    print("  uniform (pure shear) stretching by beta thins every layer by beta:")
    print("    beta    crust (km)   lithosphere (km)   extension (%)   strain")
    for beta in (1.0, 1.25, 1.5, 2.0, 3.0, 5.0):
        strain = np.log(beta)
        print(f"    {beta:4.2f}   {TC0_KM / beta:10.2f}   {A_KM / beta:16.2f}   "
              f"{100.0 * (beta - 1.0):14.1f}   {strain:6.3f}")
    print("  (extension % is (beta-1)*100, which is the finite extension;")
    print("   strain is ln(beta) for the natural-strain convention)")

    section("2. Post-rift cooling of the beta = 2 column")
    beta = 2.0
    T0 = initial_geotherm(z, beta)
    record = (0.0, 5.0, 10.0, 25.0, 50.0, 100.0, 200.0)
    sols = heat_solution(z, T0, beta, kappa, T_END_MYR, record)
    print(f"  grid: {z.size} nodes, dz = {DZ_KM:.1f} km, dt = {DT_MYR:.4f} Myr, "
          f"r = kappa dt/dz^2 = {kappa * DT_MYR / DZ_KM ** 2:.3f} (stable)")
    print("  temperature at selected depths and times (deg C):")
    print("    t (Myr)   " + "".join(f"z={d:4.0f}km " for d in (10, 30, 60, 100)))
    for t in record:
        T = sols[t]
        idx = [int(d / DZ_KM) for d in (10, 30, 60, 100)]
        print(f"    {t:6.1f}   " + "".join(f"{T[i]:9.1f}" for i in idx))
    print("  The kink at the base of the thinned lithosphere diffuses away; by")
    print("  200 Myr the geotherm has returned close to the pre-rift profile.")

    section("3. Water-loaded subsidence from isostasy")
    times = np.array(sorted(sols.keys()))
    s_km = np.array([subsidence_km(z, sols[t], beta) for t in times])
    print("  S(t) = (Phi_stretched - Phi_reference) / (rho_m - rho_w), with")
    print("  Phi = integral (rho(z) - rho_m) dz over the column, kg/m^2.")
    print("    t (Myr)    S (km)     S (m)     subsidence rate (mm/yr)")
    for i, t in enumerate(times):
        rate = (s_km[i] - s_km[i - 1]) / (times[i] - times[i - 1]) * 1e3 \
            if i > 0 else float("nan")
        print(f"    {t:6.1f}   {s_km[i]:7.3f}   {s_km[i] * 1e3:8.0f}   "
              f"{rate:26.4f}")
    print(f"  total post-rift subsidence to {T_END_MYR:.0f} Myr = "
          f"{s_km[-1] - s_km[0]:.3f} km")

    section("4. The t = 0 limit against an exact closed form")
    s0_model = s_km[0]
    s0_an, a_term, b_term = s0_closed(beta)
    print("  Pure shear thins the crust AND the mantle lithosphere by the same")
    print("  factor beta, so the whole pre-rift density deficit is simply divided:")
    print("    Phi_stretched(0) = Phi_reference / beta        (exact for pure shear)")
    print("  With Phi = integral (rho - rho_m) dz and S = (Phi_struct - Phi_ref)/")
    print("  (rho_m - rho_w), this gives S(0) = (1 - 1/beta)(A - B):")
    print(f"    crustal term A = (rho_m-rho_c)tc0/(rho_m-rho_w)              "
          f"= {a_term:6.3f} km")
    print(f"    cold-mantle term B = rho_m alpha Tm (a-tc0)^2/(2a)/(rho_m-rho_w) "
          f"= {b_term:6.3f} km")
    print(f"    A - B = {a_term - b_term:.3f} km, and (1 - 1/{beta:.2f}) = "
          f"{1.0 - 1.0 / beta:.3f}")
    print(f"    S(0) closed form = {s0_an:.3f} km;  model = {s0_model:.3f} km;  "
          f"difference = {abs(s0_an - s0_model) * 1e3:.1f} m")
    print("  Physical reading: A is the subsidence the thinned crust alone would")
    print("  produce; B is the contribution of the cold pre-rift mantle lithosphere,")
    print("  which the freshly stretched column does not (yet) have.")

    section("5. Fitting the post-rift curve with a single exponential")
    tau_analytic = A_KM ** 2 / (np.pi ** 2 * kappa)
    popt, residual = fit_exponential(times, s_km)
    s0_fit, sth_fit, tau_fit = popt
    s_inf_an = s_inf_closed(beta)
    print(f"  fit: S(t) = {s0_fit:.3f} + {sth_fit:.3f} (1 - exp(-t/{tau_fit:.2f})) km")
    print(f"  analytic first-mode decay constant a^2/(pi^2 kappa) = "
          f"{tau_analytic:.2f} Myr; fitted = {tau_fit:.2f} Myr "
          f"({100.0 * (tau_fit / tau_analytic - 1.0):+.1f}%)")
    print(f"  total thermal subsidence: closed form S(inf) - S(0) = "
          f"{s_inf_an - s0_an:.3f} km")
    print(f"  amplitude required to reach the measured S(200 Myr): "
          f"(S_meas - S0_fit)/(1 - exp(-200/tau)) = "
          f"{(s_km[-1] - s0_fit) / (1.0 - np.exp(-200.0 / tau_fit)):.3f} km "
          f"(vs {sth_fit:.3f} km fitted)")
    print(f"  rms residual of the exponential fit over 0-200 Myr = "
          f"{np.sqrt(np.mean(residual ** 2)) * 1e3:.2f} m "
          f"(max {np.max(np.abs(residual)) * 1e3:.1f} m)")
    print("  A single exponential is a good but not exact description: the initial")
    print("  condition is a piecewise-linear geotherm, not the first eigenmode, so")
    print("  higher modes are present and bias the fitted decay constant.")
    late = times >= 25.0
    fit_late, _ = fit_exponential(times[late], s_km[late])
    print(f"  refitting after 25 Myr (higher modes gone): tau = {fit_late[2]:.2f} Myr "
          f"versus analytic {tau_analytic:.2f} Myr "
          f"({100.0 * (fit_late[2] / tau_analytic - 1.0):+.1f}%)")

    section("6. Sensitivity to beta, from the closed forms")
    print("    beta   S(0) km   S(inf) km   thermal subs. km   final crust km")
    for b in (1.0, 1.25, 1.5, 2.0, 3.0, 5.0, 10.0):
        s0, _, _ = s0_closed(b)
        sinf = s_inf_closed(b)
        print(f"    {b:5.2f}   {s0:7.3f}   {sinf:9.3f}   {sinf - s0:15.3f}   "
              f"{TC0_KM / b:13.2f}")
    print("  Both terms saturate: the crustal term grows as (1 - 1/beta) and the")
    print("  thermal term as the change in heat content of the thinned lithosphere,")
    print("  so the total subsidence is a strongly nonlinear function of beta.")

    print("\n  strain rate for a given rift duration (natural strain ln(beta)):")
    print("    beta   duration (Myr)   strain rate (1/Myr)   (nanostrain/yr)")
    for b, duration in ((1.5, 30.0), (2.0, 20.0), (2.0, 5.0), (3.0, 10.0)):
        sr = np.log(b) / duration
        print(f"    {b:4.2f}   {duration:14.1f}   {sr:18.4f}   {sr * 1e3:14.1f}")
    print("  (1/Myr times 1e3 gives nanostrain/yr: 1e-6/Myr = 1e-6/1e6 yr =")
    print("   1e-12/yr = 1 nanostrain/yr)")
    print("  A 20 Myr rift that reaches beta = 2 needs tens of nanostrain per year;")
    print("  a 5 Myr rift needs an order of magnitude more.  The same final geometry")
    print("  therefore corresponds to very different strain-rate histories, which is")
    print("  why subsidence alone cannot date a rift.")


if __name__ == "__main__":
    main()
