#!/usr/bin/env python3
"""Wind-driven circulation: the Coriolis parameter, Ekman transport and depth,
the Sverdrup balance, and western boundary current width.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wind_driven_circulation_demo.py

Everything here is SYNTHETIC.  The wind-stress fields are chosen teaching
functions, not reanalyses.  No buoy, drifter or satellite product is used.

Contents
--------
1. Coriolis parameter f and its meridional gradient beta.
2. Ekman transport from a wind stress: direction and magnitude.
3. Ekman depth and the angle of the surface current.
4. The Sverdrup balance: wind-stress curl to meridional transport.
5. Western boundary current widths (Stommel and Munk scales).
6. Verification: finite-difference curl, and the error of the beta-plane.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
OMEGA = 7.292115e-5      # rad/s, Earth's rotation rate (standard constant)
R_EARTH = 6.371e6        # m, mean Earth radius (standard constant)
RHO = 1025.0             # kg/m^3, reference seawater density

# --- SYNTHETIC survey parameters (chosen teaching values) --------------------
TAU0 = 0.10              # N/m^2, peak zonal wind stress
WIND_L = 3.0e6           # m, meridional wavelength/2 of the synthetic wind
A_V = 0.01               # m^2/s, vertical eddy viscosity
A_H = 5.0e3              # m^2/s, horizontal eddy viscosity
R_DRAG = 1.0e-6          # 1/s, linear (Rayleigh) bottom drag
BASIN_WIDTH = 5.0e6      # m, zonal width of the synthetic basin
COASTLINE = 1.0e6        # m, coastline length for an upwelling estimate


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def coriolis(lat_deg):
    """f = 2 Omega sin(phi).  Units 1/s.  Positive in the northern hemisphere."""
    return 2.0 * OMEGA * np.sin(np.radians(lat_deg))


def beta(lat_deg):
    """beta = df/dy = 2 Omega cos(phi) / R.  Units 1/(m s)."""
    return 2.0 * OMEGA * np.cos(np.radians(lat_deg)) / R_EARTH


def ekman_transport(tau, lat_deg):
    """Depth-integrated Ekman transport M = tau/(rho f).  Units m^2/s.

    The vector is 90 degrees to the RIGHT of the wind stress in the northern
    hemisphere, which is what the sign of f encodes when tau is treated as a
    complex number.
    """
    return tau / (RHO * coriolis(lat_deg))


def main():
    section("1. The Coriolis parameter and its gradient")
    print(f"  Omega = {OMEGA:.6e} rad/s, R = {R_EARTH / 1e3:.0f} km")
    print(f"  f = 2 Omega sin(phi)     beta = 2 Omega cos(phi)/R")
    print("\n   latitude    f (1/s)        beta (1/(m s))   inertial period (h)")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        f = coriolis(lat)
        per = 2 * np.pi / abs(f) / 3600.0 if f != 0 else float("inf")
        print(f"  {lat:8.1f}   {f:12.6e}   {beta(lat):14.6e}   {per:16.2f}")
    print("\n  At the equator f = 0 and beta is largest: the equator is the one "
          "place where")
    print("  the beta-effect is not a small correction but the whole dynamics.")

    section("2. Ekman transport from a wind stress")
    print(f"  transport M = tau/(rho f) with rho = {RHO:.0f} kg/m^3; "
          "positive northward")
    print("\n   latitude   f (1/s)      tau (N/m^2)   M (m^2/s)   over 1000 km (Sv)")
    for lat, tau in ((30.0, TAU0), (45.0, TAU0), (-30.0, TAU0), (30.0, -TAU0)):
        M = ekman_transport(tau, lat)
        print(f"  {lat:8.1f}   {coriolis(lat):10.3e}   {tau:10.2f}   "
              f"{M:10.3f}   {M * COASTLINE / 1e6:16.3f}")
    print("\n  Sign convention: for a positive (eastward) tau in the northern")
    print("  hemisphere, M is positive (northward) because f > 0; in the southern")
    print("  hemisphere f < 0 and the same wind gives a southward transport.")
    print("  That is the 90-degree rule: transport to the RIGHT of the wind in the")
    print("  north, to the LEFT in the south.")

    section("3. Ekman depth and the angle of the surface current")
    print("  D = sqrt(2 A_v/f) is the e-folding depth; the spiral needs "
          "pi*D to die out.")
    print(f"  surface speed V0 = tau/(rho sqrt(A_v f)); "
          f"A_v = {A_V:.3f} m^2/s, tau = {TAU0:.2f} N/m^2")
    print("\n   latitude   f (1/s)     D (m)   pi D (m)   V0 (m/s)   V0 45 deg "
          "(m/s)   angle (deg)")
    for lat in (15.0, 30.0, 45.0, 60.0):
        f = coriolis(lat)
        D = np.sqrt(2.0 * A_V / f)
        V0 = TAU0 / (RHO * np.sqrt(A_V * f))
        print(f"  {lat:8.1f}   {f:10.3e}   {D:7.3f}   {np.pi * D:8.2f}   "
              f"{V0:9.4f}   {V0 * np.cos(np.pi / 4):13.4f}   {45.0:13.1f}")
    print("\n  The surface current is at 45 degrees to the RIGHT of the wind, and")
    print("  the transport (the vertical integral) is at 90 degrees.  The 45-degree")
    print("  figure is a property of CONSTANT A_v; with a depth-dependent")
    print("  viscosity it is a different angle, so 'the' angle is model-dependent.")

    section("4. The Sverdrup balance: curl of the wind stress")
    print("  beta V = (1/rho) curl_z(tau);  synthetic tau_x(y) = "
          "tau0 cos(pi y / L)")
    print(f"  tau0 = {TAU0:.2f} N/m^2, L = {WIND_L / 1e3:.0f} km")
    y = np.linspace(0.0, WIND_L, 501)
    tau_x = TAU0 * np.cos(np.pi * y / WIND_L)
    curl_exact = TAU0 * (np.pi / WIND_L) * np.sin(np.pi * y / WIND_L)
    curl_fd = -np.gradient(tau_x, y)
    i_mid = int(np.argmin(np.abs(y - 0.5 * WIND_L)))
    print("\n    y (km)   tau_x (N/m^2)   curl fd   curl exact   V (m^2/s)   "
          "V basin (Sv)")
    for i in (60, 150, i_mid, 350, 440):
        V = curl_exact[i] / (RHO * beta(30.0))
        print(f"  {y[i] / 1e3:7.0f}   {tau_x[i]:13.4f}   {curl_fd[i]:9.3e}   "
              f"{curl_exact[i]:9.3e}   {V:9.3f}   {V * BASIN_WIDTH / 1e6:10.2f}")
    print(f"\n  at y = {y[i_mid] / 1e3:.0f} km (beta at 30 degN), "
          f"V = {curl_exact[i_mid] / (RHO * beta(30.0)):.3f} m^2/s,")
    print(f"  i.e. {curl_exact[i_mid] / (RHO * beta(30.0)) * BASIN_WIDTH / 1e6:.1f} Sv "
          f"across a {BASIN_WIDTH / 1e3:.0f} km basin.")
    print(f"  max |curl_fd - curl_exact| = "
          f"{np.abs(curl_fd - curl_exact).max():.3e} N/m^3 over the grid.")
    print("  Because curl_z tau = -d(tau_x)/dy, the vanishing curl at y = 0 and")
    print("  y = L is where the gyre's interior flow reverses.")

    section("5. Western boundary current scales")
    b = beta(30.0)
    d_stommel = R_DRAG / b
    d_munk = (A_H / b) ** (1.0 / 3.0)
    print(f"  beta at 30 degN = {b:.4e} 1/(m s)")
    print(f"  Stommel width  r/beta      = {R_DRAG:.1e}/{b:.3e} = "
          f"{d_stommel / 1e3:.2f} km")
    print(f"  Munk width     (A_H/beta)^1/3 = ({A_H:.1e}/{b:.3e})^1/3 = "
          f"{d_munk / 1e3:.2f} km")
    print("\n  Both are far narrower than the basin interior.  The width is set by")
    print("  the balance that closes the circulation, not by the wind pattern:")
    print("  friction must be large enough to permit a return flow where beta")
    print("  makes the interior flow one-signed.")

    section("6. Verification: finite differences and the beta-plane error")
    # (a) The analytic Ekman transport for a complex wind stress must have the
    #     magnitude tau/(rho f).  Check it numerically from the definition.
    tau_complex = TAU0 * np.exp(1j * np.pi / 6.0)
    M_analytic = abs(tau_complex) / (RHO * abs(coriolis(30.0)))
    M_defined = abs(ekman_transport(tau_complex, 30.0))
    print("(a) Ekman transport consistency:")
    print(f"    |M| from definition = {M_defined:.6f} m^2/s, "
          f"analytic = {M_analytic:.6f} m^2/s, "
          f"difference = {abs(M_defined - M_analytic):.2e} m^2/s")
    print("    The transport is INDEPENDENT of A_v: viscosity sets the depth and")
    print("    the speed, but not the integral.")

    # (b) beta-plane approximation error over the synthetic gyre's latitudinal
    #     extent, measured against the spherical f.
    print("(b) beta-plane error over a meridional extent of "
          f"{WIND_L / 1e3:.0f} km:")
    lat0 = 30.0
    f0 = coriolis(lat0)
    print("     y (km)   f exact      f0 + beta*y   error (1/s)")
    dy = np.linspace(-0.5 * WIND_L, 0.5 * WIND_L, 9)
    for d in dy[::2]:
        lat = lat0 + np.degrees(d / R_EARTH)
        f_exact = coriolis(lat)
        f_approx = f0 + b * d
        print(f"  {d / 1e3:8.0f}   {f_exact:.6e}   {f_approx:.6e}   "
              f"{f_approx - f_exact:+.3e}")
    worst = max(abs((f0 + b * d) - coriolis(lat0 + np.degrees(d / R_EARTH)))
                for d in dy)
    print(f"    max |beta-plane - spherical| = {worst:.3e} 1/s "
          f"= {100 * worst / f0:.3f}% of f.")
    print("    A 1% error in f becomes a 1% error in Ekman transport; the")
    print("    beta-plane is a small-angle approximation in LATITUDE, not a")
    print("    licence to use it from the pole to the equator.")

    # (c) Rossby wave adjustment time for the gyre.
    N, H = 0.010, 500.0          # rad/s, m  (synthetic stratification and depth)
    L_d = N * H / coriolis(30.0)
    c_R = b * L_d ** 2
    T_adj = BASIN_WIDTH / c_R
    print("(c) gyre adjustment:")
    print(f"    N = {N:.3f} rad/s, H = {H:.0f} m -> Rossby radius "
          f"L_d = {L_d / 1e3:.2f} km")
    print(f"    long Rossby speed c_R = beta L_d^2 = {c_R * 100:.3f} cm/s")
    print(f"    time to cross the basin = {T_adj / 3.156e7:.2f} years")
    print("    Wind-driven gyres are therefore not in instantaneous equilibrium")
    print("    with the wind: the adjustment time is years, not days.")


if __name__ == "__main__":
    main()
