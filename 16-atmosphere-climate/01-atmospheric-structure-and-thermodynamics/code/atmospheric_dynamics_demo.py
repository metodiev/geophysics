#!/usr/bin/env python3
"""Atmospheric dynamics basics: the Coriolis parameter, Rossby number,
geostrophic balance, the inertial oscillation, and the thermal wind.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_dynamics_demo.py

All models are SYNTHETIC teaching models.  The rotation rate of the Earth, the
gas constant and gravity are standard constants, listed below; the pressure
gradient, the temperature gradient and the static stability are chosen inputs,
printed below.  No quantity here is a measurement made by this module.

Contents
--------
1. The Coriolis parameter f = 2 Omega sin(phi) and its timescales.
2. The inertial oscillation, integrated and measured against 2*pi/f.
3. Rossby number and the geostrophic wind for a stated pressure gradient.
4. The gradient-wind correction as a measure of the geostrophic error.
5. A self-consistent synthetic atmosphere with a constant meridional
   temperature gradient.
6. The thermal wind: the shear from the analytic geostrophic wind, from the
   thermal-wind integral, and from a numerical differentiation of the
   geopotential field.
7. The Rossby radius of deformation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.2921150e-5    # rad s^-1, Earth rotation rate (standard constant)
R_D = 287.041           # J kg^-1 K^-1, dry-air gas constant (lesson 01)
G0 = 9.80665            # m s^-2, standard gravity
T0 = 288.15             # K, surface temperature of the model
GAMMA = 6.5e-3          # K m^-1, model tropospheric lapse rate
P_SURF = 100000.0       # Pa, model surface pressure
T_GRAD_Y = -1.0e-5      # K m^-1, meridional temperature gradient (colder northward)
RHO_SURF = 1.225        # kg m^-3, surface density of the model (lesson 01)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def coriolis(lat_deg):
    """Coriolis parameter f = 2 Omega sin(phi), s^-1."""
    return 2.0 * OMEGA * np.sin(np.radians(lat_deg))


def T_profile(p):
    """Model tropospheric temperature (K) as a function of pressure (Pa)."""
    return T0 * (p / P_SURF) ** (R_D * GAMMA / G0)


def geopotential_y_gradient(p):
    """dPhi/dy (m s^-2) for T(y,p) = T_profile(p) + T_GRAD_Y y, exactly."""
    return R_D * T_GRAD_Y * np.log(P_SURF / p)


def u_geostrophic(p, lat_deg):
    """Geostrophic zonal wind (m/s) from the synthetic field, exactly."""
    return -geopotential_y_gradient(p) / coriolis(lat_deg)


def height_of_pressure(p):
    """Geometric height (m) of pressure level p in the model atmosphere."""
    # dz = -(R_d T/g) dln p, integrated from the surface
    n = 4000
    pgrid = np.linspace(P_SURF, p, n + 1)
    integrand = R_D * T_profile(pgrid) / (G0 * pgrid)
    return -np.trapezoid(integrand, pgrid)


def main():
    section("1. The Coriolis parameter and its timescales")
    print(f"  Omega = {OMEGA:.7e} rad/s;  f = 2 Omega sin(phi)")
    print("  latitude   f (1e-4 s^-1)   1/f (h)   2 pi/f (h)")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        f = coriolis(lat)
        if f == 0.0:
            print(f"  {lat:8.1f}   {0.0:13.4f}        -          -")
        else:
            print(f"  {lat:8.1f}   {f * 1e4:13.4f}   {1 / f / 3600:8.3f}   "
                  f"{2 * np.pi / f / 3600:9.3f}")
    print("  1/f is the time in which the Coriolis force turns a wind by ~1 radian;")
    print("  2 pi/f is the inertial period, the time for a full circle.  At 45 deg")
    print("  the inertial period is about 17 hours: the atmosphere cannot adjust to")
    print("  balance in less than a few hours, and that is why weather systems are")
    print("  larger than a few hundred kilometres (Section 7).")

    section("2. The inertial oscillation, integrated and measured")
    f = coriolis(45.0)
    dt = 1.0
    t_end = 4.0 * 2.0 * np.pi / f
    n = int(t_end / dt)
    u = np.empty(n + 1)
    v = np.empty(n + 1)
    u[0], v[0] = 10.0, 0.0
    for i in range(n):
        def rhs(uu, vv):
            return f * vv, -f * uu
        k1 = rhs(u[i], v[i])
        k2 = rhs(u[i] + dt / 2 * k1[0], v[i] + dt / 2 * k1[1])
        k3 = rhs(u[i] + dt / 2 * k2[0], v[i] + dt / 2 * k2[1])
        k4 = rhs(u[i] + dt * k3[0], v[i] + dt * k3[1])
        u[i + 1] = u[i] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v[i + 1] = v[i] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    t = np.arange(n + 1) * dt
    zero_cross = np.where((u[:-1] < 0.0) & (u[1:] >= 0.0))[0]
    measured = (t[zero_cross[-1]] - t[zero_cross[0]]) / (zero_cross.size - 1)
    print(f"  du/dt = f v,  dv/dt = -f u,  started at (u,v) = (10, 0) m/s")
    print(f"    speed at every step (should be constant): "
          f"{np.sqrt(u ** 2 + v ** 2).min():.6f} to "
          f"{np.sqrt(u ** 2 + v ** 2).max():.6f} m/s")
    print(f"    measured period from zero crossings = {measured:.2f} s "
          f"({measured / 3600:.4f} h)")
    print(f"    predicted 2 pi/f                    = {2 * np.pi / f:.2f} s "
          f"({2 * np.pi / f / 3600:.4f} h)")
    print(f"    difference = {measured - 2 * np.pi / f:+.3f} s "
          f"({(measured - 2 * np.pi / f) / (2 * np.pi / f) * 100:+.4f}%)")
    print("  A pure inertial oscillation is a circle in the hodograph, clockwise in")
    print("  the northern hemisphere.  Nothing in it is a 'force' along the motion;")
    print("  the Coriolis acceleration is always perpendicular to the velocity.")

    section("3. Rossby number and the geostrophic wind")
    print("  Ro = U/(f L) measures the size of the acceleration term against the")
    print("  Coriolis term in the horizontal momentum equation.")
    print("  U (m/s)   L (km)    f (1e-4 /s)   Ro        regime")
    for U, L, lat in ((10.0, 1000.0, 45.0), (10.0, 300.0, 45.0), (10.0, 100.0, 45.0),
                      (10.0, 1000.0, 10.0), (30.0, 2000.0, 45.0), (1.0, 100.0, 45.0)):
        f = coriolis(lat)
        ro = U / (f * L * 1e3)
        regime = ("geostrophic" if ro < 0.1 else
                  "quasi-geostrophic" if ro < 0.5 else "ageostrophic")
        print(f"  {U:7.1f}   {L:8.1f}   {f * 1e4:12.4f}   {ro:8.4f}   {regime}")
    print("\n  Geostrophic wind from a stated pressure gradient, 45 deg latitude:")
    print("  dp/dy (hPa/100 km)   u_g (m/s)   direction")
    for dpdy in (-2.0, -1.0, 0.0, 1.0, 2.0):
        grad = dpdy * 100.0 / 1.0e5      # Pa per metre
        ug = -grad / (RHO_SURF * coriolis(45.0))
        direction = "westerly (+u)" if ug > 0 else ("easterly (-u)" if ug < 0 else "-")
        print(f"  {dpdy:19.1f}   {ug:9.3f}   {direction}")
    print("\n  Note the sign: pressure FALLING northward gives a WESTERLY.  The")
    print("  geostrophic wind blows along the isobars, not down the gradient, and")
    print("  in the northern hemisphere it has low pressure on its left.")

    section("4. Geostrophic balance as a small-Rossby-number limit")
    print("  The ratio of the acceleration to the Coriolis term is O(Ro), so the")
    print("  fractional error of the geostrophic approximation should scale with Ro.")
    print("  Test on a circular vortex in gradient-wind balance, u^2/R + f u = f u_g:")
    print("   Ro        u_g (m/s)   u_exact (m/s)   (u_exact-u_g)/u_g   that ratio/Ro")
    for ro in (0.01, 0.03, 0.1, 0.3):
        f = coriolis(45.0)
        ug = 10.0
        R = ug / (f * ro)                # radius chosen so that Ro = u_g/(f R)
        a, b, c = 1.0 / R, f, -f * ug
        u_exact = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        frac = (u_exact - ug) / ug
        print(f"  {ro:6.3f}   {ug:10.3f}   {u_exact:14.4f}   {frac:18.6f}   "
              f"{frac / ro:11.4f}")
    print("  The correction is negative (tight lows are sub-geostrophic) and its")
    print("  magnitude is about 1.0% at Ro = 0.01, 2.8% at 0.03, 8.4% at 0.1 and")
    print("  19.5% at 0.3 - so O(Ro) is a real estimate, not merely an order of")
    print("  magnitude, and the coefficient is close to 1 for small Ro.")

    section("5. A self-consistent synthetic atmosphere with a T gradient")
    print(f"  T(y,p) = T_profile(p) + (dT/dy) y,  dT/dy = {T_GRAD_Y * 1e5:+.1f} K "
          f"per 100 km")
    print("  T_profile(p) = T0 (p/p_surf)^(R_d Gamma/g), Gamma = "
          f"{GAMMA * 1e3:.1f} K/km")
    print("   p (hPa)    z (km)    T (K)    dPhi/dy (m/s^2)   u_g (m/s) at 45N")
    levels = (1000.0, 850.0, 700.0, 500.0, 300.0, 200.0)
    zs = {}
    for pl in levels:
        p = pl * 100.0
        z = height_of_pressure(p)
        zs[pl] = z
        print(f"  {pl:8.0f}   {z / 1e3:7.3f}   {T_profile(p):7.3f}   "
              f"{geopotential_y_gradient(p):15.6f}   {u_geostrophic(p, 45.0):12.3f}")
    print("  Because dT/dy is constant, dPhi/dy = R_d (dT/dy) ln(p_surf/p) exactly,")
    print("  so the geostrophic wind is exactly proportional to ln(p_surf/p).")

    section("6. The thermal wind: two independent routes to the same shear")
    f = coriolis(45.0)
    print("  Route A: u_g(p_top) - u_g(p_bot) from the analytic geostrophic wind.")
    print("  Route B: -integral (g/(f T)) dT/dy dz, using the hydrostatic heights.")
    print("\n   p (hPa)   u_g (m/s)   shear A (m/s)   shear B (m/s)   difference")
    u_bot = u_geostrophic(1000.0 * 100.0, 45.0)
    for pl in (850.0, 700.0, 500.0, 300.0, 200.0):
        p = pl * 100.0
        shear_a = u_geostrophic(p, 45.0) - u_bot
        # Route B: integrate -(g/(f T)) dT/dy dz between the two levels
        z_lo, z_hi = zs[1000.0], zs[pl]
        n = 20000
        zgrid = np.linspace(z_lo, z_hi, n + 1)
        # invert the height-pressure relation on the same grid via the hydrostatic
        # profile: p(z) from the model temperature profile
        pgrid = P_SURF * (1.0 - GAMMA * zgrid / T0) ** (G0 / (R_D * GAMMA))
        integrand = -(G0 / (f * T_profile(pgrid))) * T_GRAD_Y
        shear_b = np.trapezoid(integrand, zgrid)
        print(f"  {pl:8.0f}   {u_geostrophic(p, 45.0):9.3f}   {shear_a:13.3f}   "
              f"{shear_b:13.3f}   {shear_a - shear_b:11.4f}")
    print("\n  The two routes agree to quadrature.  This is a CONSISTENCY check, not")
    print("  an independent measurement: (g/T) dz = -R_d d ln p is an identity from")
    print("  hydrostatic balance, so the integral collapses onto R_d ln(p_surf/p)")
    print("  exactly.  What it does establish is that the synthetic atmosphere is")
    print("  internally consistent and that the relation is a consequence of")
    print("  geostrophic plus hydrostatic balance, not an extra law.")
    print("\n  An INDEPENDENT numerical check of the construction: build Phi(y,p) by")
    print("  integrating R_d T(y,p) d ln p at two neighbouring latitudes and")
    print("  differentiate numerically.")
    print("   p (hPa)   u_g analytic   u_g by finite difference   difference")
    dy = 5.0e4
    for pl in (850.0, 500.0, 200.0):
        pp = pl * 100.0
        n = 4000
        pgrid = np.linspace(P_SURF, pp, n + 1)
        # Phi = int_p^p_surf R_d T d ln p = -int_{p_surf}^{p} R_d T d ln p
        phi_plus = -np.trapezoid(R_D * (T_profile(pgrid) + T_GRAD_Y * dy) / pgrid,
                                 pgrid)
        phi_minus = -np.trapezoid(R_D * (T_profile(pgrid) - T_GRAD_Y * dy) / pgrid,
                                  pgrid)
        dphidy = (phi_plus - phi_minus) / (2 * dy)
        ug_fd = -dphidy / coriolis(45.0)
        print(f"  {pl:8.0f}   {u_geostrophic(pp, 45.0):11.4f}   {ug_fd:23.4f}   "
              f"{u_geostrophic(pp, 45.0) - ug_fd:+.2e}")
    print("  Magnitude: a 1 K per 100 km temperature gradient produces about 3.4")
    print("  m/s of westerly shear per kilometre, i.e. roughly 30 m/s across the")
    print("  troposphere - the observed strength of the mid-latitude jet stream,")
    print("  and the reason the jet sits where the surface temperature gradient is")
    print("  steepest.")

    section("7. The Rossby radius of deformation")
    print("  L_R = N H / f: the scale at which rotation and stratification balance.")
    print("   N (1e-3 /s)   H (km)   latitude   L_R (km)")
    for N, H, lat in ((11.0e-3, 10.0, 45.0), (11.0e-3, 10.0, 20.0),
                      (11.0e-3, 10.0, 60.0), (5.0e-3, 10.0, 45.0),
                      (11.0e-3, 5.0, 45.0)):
        LR = N * H * 1e3 / coriolis(lat)
        print(f"  {N * 1e3:11.1f}   {H:7.1f}   {lat:8.0f}   {LR / 1e3:9.1f}")
    print("  Disturbances much larger than L_R are geostrophically balanced and")
    print("  long-lived; much smaller ones radiate gravity waves and disperse.")
    print("  This is the length scale that sets the size of the weather systems")
    print("  visible on a synoptic chart (lesson 16-03-01).")


if __name__ == "__main__":
    main()
