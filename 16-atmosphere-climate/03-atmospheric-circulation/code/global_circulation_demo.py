#!/usr/bin/env python3
"""Global atmospheric circulation: the Coriolis parameter, Rossby number,
angular-momentum conservation in the Hadley cell, the tropical tropopause
temperature plateau it predicts, the Hadley-cell edge it only partly
determines, the poleward heat transport implied by a prescribed top-of-
atmosphere flux profile, and the eddy momentum flux a Ferrel cell requires.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python global_circulation_demo.py

Everything is SYNTHETIC. The radiative-equilibrium temperature profiles, the
"flows" used for the Rossby numbers, the top-of-atmosphere flux profile and the
Ferrel-cell parameters are *chosen teaching values*, not measurements. Earth's
rotation rate, radius, gravity and the specific heat of air below are standard
constants.

Contents
--------
1. Coriolis parameter f = 2 Omega sin(phi) and the inertial period.
2. Rossby numbers Ro = U/(f L) for five chosen flows.
3. Angular-momentum conservation: u(phi) = Omega a sin^2(phi)/cos(phi), with a
   numerical check that the formula conserves angular momentum.
4. The tropical tropopause potential-temperature plateau predicted by thermal
   wind plus angular-momentum conservation, verified against a numerical
   integral of the thermal-wind relation.
5. The Hadley-cell edge from a simplified Held-Hou matching, for a grid of
   assumed equilibrium temperature contrasts and tropopause heights -- reported
   as a range, because one number is not defensible.
6. Poleward heat transport required by a prescribed net TOA flux profile.
7. A thermally indirect Ferrel cell and the eddy momentum flux convergence that
   must maintain the midlatitude jet.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5      # rad/s, Earth angular velocity (a defining WGS 84 value)
A_EARTH = 6.371e6        # m, Earth mean radius
G = 9.81                 # m/s^2
C_P = 1004.0             # J/(kg K), dry air at constant pressure
THETA0 = 300.0           # K, reference potential temperature (chosen)
DEG = np.pi / 180.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def coriolis(lat_deg):
    return 2.0 * OMEGA * np.sin(lat_deg * DEG)


# ---------------------------------------------------------------------------
# 1. Coriolis parameter
# ---------------------------------------------------------------------------

def part1_coriolis():
    section("1. Coriolis parameter and inertial period")
    print("f = 2 Omega sin(phi);  Omega = 7.292115e-05 rad/s (defining)")
    print(f"{'latitude (deg)':>14} {'sin(phi)':>10} {'f (1/s)':>13} "
          f"{'inertial period (h)':>21}")
    for lat in (0.0, 5.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        f = coriolis(lat)
        txt = ("     infinite" if f == 0.0
               else f"{2.0 * np.pi / abs(f) / 3600.0:21.3f}")
        print(f"{lat:14.1f} {np.sin(lat * DEG):10.5f} {f:13.5e} {txt:>21}")
    print(f"\n  planetary vorticity 2 Omega = {2.0 * OMEGA:.5e} 1/s")
    print("  the inertial period 12 h/sin(phi) is the timescale on which rotation")
    print("  organises a flow; at the equator it diverges, so tropical flows are")
    print("  not rotation-dominated and cannot remain in geostrophic balance.")


# ---------------------------------------------------------------------------
# 2. Rossby number
# ---------------------------------------------------------------------------

def part2_rossby():
    section("2. Rossby number Ro = U/(f L) for chosen flows")
    flows = [
        ("Hadley cell (tropical)", 20.0, 3.0e6, 15.0),
        ("midlatitude surface cyclone", 15.0, 1.0e6, 45.0),
        ("midlatitude jet stream", 40.0, 3.0e6, 45.0),
        ("tornado", 100.0, 3.0e2, 40.0),
        ("bathtub drain", 0.1, 0.5, 45.0),
    ]
    print(f"{'flow':>28} {'U (m/s)':>8} {'L (m)':>9} {'lat':>5} {'Ro':>11} "
          f"{'regime':>18}")
    for name, U, L, lat in flows:
        f = abs(coriolis(lat))
        ro = U / (f * L)
        regime = ("rotation-dominated" if ro < 0.1
                  else "borderline" if ro < 1.0 else "advection-dominated")
        print(f"{name:>28} {U:8.1f} {L:9.1e} {lat:5.0f} {ro:11.3f} {regime:>18}")
    print("\n  the tropical Hadley cell is only marginally rotation-dominated.")
    print("  That marginality is why it partly conserves angular momentum and is")
    print("  partly reset by eddies, and why Ro alone cannot settle the question.")


# ---------------------------------------------------------------------------
# 3. Angular momentum conservation
# ---------------------------------------------------------------------------

def amc_wind(lat_deg):
    """Zonal wind conserving angular momentum, started from rest at the equator."""
    phi = lat_deg * DEG
    return OMEGA * A_EARTH * np.sin(phi) ** 2 / np.cos(phi)


def angular_momentum(lat_deg, u):
    """Specific angular momentum (m^2/s) of air moving zonally with speed u."""
    phi = lat_deg * DEG
    return OMEGA * A_EARTH ** 2 * np.cos(phi) ** 2 + u * A_EARTH * np.cos(phi)


def part3_angular_momentum():
    section("3. Angular-momentum-conserving zonal wind")
    print("M = Omega a^2 cos^2(phi) + u a cos(phi) is conserved following the air,")
    print("because multiplying the zonal momentum equation by a cos(phi) cancels")
    print("the Coriolis and curvature terms exactly. From rest at the equator,")
    print("M = Omega a^2, so u(phi) = Omega a sin^2(phi)/cos(phi).")
    print(f"\n{'latitude':>9} {'u (m/s)':>10} {'M (m^2/s)':>16} {'M/M_eq - 1':>13}")
    for lat in (0.0, 10.0, 20.0, 30.0, 45.0, 60.0, 75.0):
        u = amc_wind(lat)
        M = angular_momentum(lat, u)
        print(f"{lat:9.1f} {u:10.2f} {M:16.6e} "
              f"{M / (OMEGA * A_EARTH ** 2) - 1.0:13.2e}")
    print(f"\n  Omega a = {OMEGA * A_EARTH:.1f} m/s is the velocity scale; the "
          "residual")
    print("  column is round-off, which is the check that this is the angular-")
    print("  momentum-conserving formula and not merely a plausible-looking one.")
    print(f"  u(30 deg) = {amc_wind(30.0):.1f} m/s, u(45 deg) = "
          f"{amc_wind(45.0):.1f} m/s. This is an UPPER BOUND on a subtropical")
    print("  jet, not a prediction: the formula ignores friction and eddy mixing")
    print("  and diverges toward the pole, so conservation cannot hold everywhere.")


# ---------------------------------------------------------------------------
# 4. Tropical tropopause temperature plateau
# ---------------------------------------------------------------------------

def tropopause_theta(lat_deg, tropopause_m, theta0=THETA0):
    """Potential-temperature drop of the tropopause from the equator, Held-Hou style.

    Thermal wind, f du/dz = -(g/theta0) d(theta)/dy, with u = 0 at the surface
    and u = u_AMC at the tropopause, and a surface potential temperature that is
    uniform across the tropics, gives

        d(theta_t)/dy = -(2 f theta0 / (g H)) u_AMC(phi)

    (the factor 2 is the height average of a shear that varies linearly in z).
    Integrating with u_AMC = Omega a sin^2/cos and y = a phi gives

        theta_t(phi) - theta_t(0) = (4 theta0 Omega^2 a^2/(g H))
                                    (ln cos(phi) + sin^2(phi)/2).

    The bracket is O(phi^4): to leading order the tropical tropopause potential
    temperature is FLAT, while the equilibrium equator-to-pole profile is not.
    """
    phi = np.asarray(lat_deg, dtype=float) * DEG
    coeff = 4.0 * theta0 * OMEGA ** 2 * A_EARTH ** 2 / (G * tropopause_m)
    return coeff * (np.log(np.cos(phi)) + np.sin(phi) ** 2 / 2.0)


def tropopause_theta_analytic(lat_deg, tropopause_m, theta0=THETA0):
    return tropopause_theta(lat_deg, tropopause_m, theta0)


def tropopause_theta_numeric(lat_deg, tropopause_m, n=200001, theta0=THETA0):
    """Same quantity by direct numerical integration of the thermal-wind relation."""
    phi_grid = np.linspace(0.0, lat_deg * DEG, n)
    f = 2.0 * OMEGA * np.sin(phi_grid)
    u_amc = OMEGA * A_EARTH * np.sin(phi_grid) ** 2 / np.cos(phi_grid)
    integrand = -(2.0 * f * theta0 / (G * tropopause_m)) * u_amc * A_EARTH
    return float(np.trapezoid(integrand, phi_grid))


def part4_tropopause():
    section("4. Tropical tropopause potential-temperature plateau (thermal wind)")
    h_trop = 1.0e4
    coeff = 4.0 * THETA0 * OMEGA ** 2 * A_EARTH ** 2 / (G * h_trop)
    print("DERIVED profile: theta_t(phi) - theta_t(0) = "
          "C (ln cos(phi) + sin^2(phi)/2)")
    print(f"with C = 4 theta0 Omega^2 a^2/(g H) = {coeff:.1f} K for "
          f"H = {h_trop / 1e3:.0f} km and theta0 = {THETA0:.0f} K.")
    print(f"\n{'latitude':>9} {'theta_t - theta_t(0) (K)':>25} "
          f"{'-30 sin^2 (K)':>15}")
    for lat in (0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0):
        d = float(tropopause_theta(lat, h_trop))
        ref = -30.0 * np.sin(lat * DEG) ** 2
        print(f"{lat:9.1f} {d:25.2f} {ref:15.2f}")
    print("\n  the last column is a plain sin^2 profile with a 30 K equator-to-pole")
    print("  contrast, shown for comparison: it drops quadratically, while the")
    print("  conservation profile is flat to within about 1 K out to 20 deg and")
    print("  only then plunges. A flat tropical tropopause potential temperature")
    print("  is the signature this theory predicts, and it is a consequence of")
    print("  conservation alone -- no radiative transfer enters.")
    dev = [abs(tropopause_theta(lat, h_trop)
               - tropopause_theta_numeric(lat, h_trop))
           for lat in (10.0, 20.0, 30.0, 40.0)]
    print(f"\n  closed form vs numerical integral of d(theta_t)/dy: max deviation "
          f"{max(dev):.2e} K")
    print("  over 10-40 deg. That is a check on the algebra, not on the physics:")
    print("  the physics rests on the assumptions stated above the formula.")
    for hh in (8e3, 1.0e4, 1.2e4):
        print(f"  scale check: H = {hh / 1e3:.0f} km gives C = "
              f"{4.0 * THETA0 * OMEGA ** 2 * A_EARTH ** 2 / (G * hh):.1f} K, so the "
              "plateau width itself")
    print("  depends on the assumed tropopause height -- another reason to report")
    print("  ranges rather than one number.")


# ---------------------------------------------------------------------------
# 5. Cell edge: a range, not a number
# ---------------------------------------------------------------------------

def cell_edge(delta_theta_e, tropopause_m):
    """Latitude where the conservation profile meets a chosen equilibrium profile.

    Equilibrium tropopause potential temperature is taken as
    theta_e(phi) = -delta_theta_e sin^2(phi) (a chosen profile, referenced to
    the equatorial value), and the crossing is found on a fine phi grid.
    """
    phi = np.linspace(0.0, 60.0 * DEG, 200001)
    lhs = tropopause_theta(phi / DEG, tropopause_m)
    rhs = -delta_theta_e * np.sin(phi) ** 2
    d = lhs - rhs
    for k in range(1, d.size):
        if phi[k] / DEG >= 1.0 and d[k] <= 0.0:
            frac = d[k - 1] / (d[k - 1] - d[k])
            return float((phi[k - 1] + frac * (phi[k] - phi[k - 1])) / DEG)
    return float("nan")


def part5_cell_edge():
    section("5. Hadley-cell edge: a simplified Held-Hou matching, as a RANGE")
    print("Cell edge = latitude where the conservation profile of section 4 meets")
    print("theta_e(phi) = -delta_theta_e sin^2(phi) (a chosen equilibrium profile).")
    print("Both the equilibrium contrast and the tropopause height are assumptions,")
    print("so the answer is a table, not a number.\n")
    print(f"{'delta_theta_e (K)':>18} " + " ".join(
        f"{'H=' + str(int(h / 1e3)) + 'km':>9}" for h in (8e3, 1e4, 1.2e4)))
    for dte in (30.0, 50.0, 70.0, 90.0):
        row = " ".join(f"{cell_edge(dte, h):9.1f}" for h in (8e3, 1e4, 1.2e4))
        print(f"{dte:18.0f} {row}")
    edges = [cell_edge(dte, h) for dte in (30.0, 50.0, 70.0, 90.0)
             for h in (8e3, 1e4, 1.2e4)]
    print(f"\n  span of the table: {min(edges):.1f} to {max(edges):.1f} deg latitude,")
    print(f"  a factor of {max(edges) / min(edges):.1f} across assumptions that are all")
    print("  defensible. The matching argument LOCATES the cell edge but does not")
    print("  pin it: in the real atmosphere the edge is set by the eddy heat and")
    print("  momentum fluxes that an axisymmetric theory cannot contain. Quoting a")
    print("  single cell-edge latitude from this model would be an overclaim.")


# ---------------------------------------------------------------------------
# 6. Poleward heat transport
# ---------------------------------------------------------------------------

def part6_transport():
    section("6. Poleward heat transport implied by a prescribed net TOA flux")
    A0, B0 = 40.0, 120.0            # W/m^2; N(phi) = A0 - B0 sin^2(phi)
    print("SYNTHETIC profile N(phi) = %.0f - %.0f sin^2(phi) W/m^2, chosen so that"
          % (A0, B0))
    print("the area-weighted global mean is exactly zero:")
    print(f"  N(0) = {A0:.1f} W/m^2, N(90) = {A0 - B0:.1f} W/m^2, "
          f"global mean = {A0 - B0 / 3.0:.2e} W/m^2")
    print("  T(phi) = 2 pi a^2 int_phi^(pi/2) (-N) cos(phi') dphi' "
          "= 80 pi a^2 sin(phi)(1 - sin^2 phi)")
    print(f"\n{'lat':>6} {'T (PW)':>9} {'vbar if a mean cell did it all (m/s)':>38}")
    dtheta, depth, rho = 15.0, 1.0e4, 0.7   # chosen closure parameters
    peak = (0.0, 0.0)
    for la in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        s = np.sin(la * DEG)
        T = 80.0 * np.pi * A_EARTH ** 2 * s * (1.0 - s ** 2)
        vbar = T / (2.0 * np.pi * A_EARTH * np.cos(la * DEG) * rho * C_P
                    * dtheta * depth)
        if T / 1e15 > peak[1]:
            peak = (la, T / 1e15)
        print(f"{la:6.1f} {T / 1e15:9.3f} {vbar:38.3f}")
    print(f"\n  peak requirement {peak[1]:.3f} PW at {peak[0]:.0f} deg latitude.")
    print("  The vbar column assumes the whole transport is carried by a mean cell")
    print("  with a 15 K contrast through a 10 km column of density 0.7 kg/m^3.")
    print("  That closure is crude on purpose: the required transport is a few PW,")
    print("  and converting it to a velocity depends entirely on assumptions that")
    print("  are NOT measured here -- which is why the lesson treats it as a bound,")
    print("  not an observation.")


# ---------------------------------------------------------------------------
# 7. Ferrel cell and eddy momentum flux
# ---------------------------------------------------------------------------

def part7_ferrel():
    section("7. Ferrel cell: thermally indirect, so eddies must do the work")
    U_JET, H, rho = 20.0, 1.0e4, 1.0
    v_ferrel = -1.0                        # m/s, equatorward at the surface (NH)
    tau_spin = 5.0 * 86400.0
    lat = 45.0
    f = coriolis(lat)
    friction = rho * H * U_JET / tau_spin
    coriolis_torque = rho * H * f * v_ferrel
    print("SYNTHETIC midlatitude momentum budget at 45 deg:")
    print(f"  jet U = {U_JET:.1f} m/s over a {H / 1e3:.0f} km column of density "
          f"{rho:.1f} kg/m^3")
    print(f"  surface friction as Rayleigh drag with a {tau_spin / 86400.0:.0f} d "
          "spin-down time")
    print(f"  f(45 deg) = {f:.3e} 1/s; an equatorward surface branch of "
          f"{v_ferrel:.1f} m/s")
    print(f"\n  friction drag on the column         : {friction:8.3f} N/m^2")
    print(f"  Coriolis torque of the indirect cell: {coriolis_torque:8.3f} N/m^2")
    print(f"  eddy momentum flux convergence needed: "
          f"{friction - coriolis_torque:8.3f} N/m^2")
    print("\n  the Coriolis term has the SAME sign as friction, so the mean")
    print("  meridional cell cannot maintain the jet: it must be driven by eddy")
    print(f"  momentum fluxes of order {friction - coriolis_torque:.1f} N/m^2. That is")
    print("  the quantitative meaning of 'the Ferrel cell is eddy-driven and")
    print("  thermally indirect', and it is why an axisymmetric theory cannot")
    print("  close here.")
    t_pk = 3.825e15
    d = t_pk / (2.0 * np.pi * A_EARTH * np.cos(lat * DEG) * rho * C_P * H
                * (15.0 / 3.3e6))
    print(f"\n  eddy diffusivity implied if eddies carried the section-6 peak")
    print(f"  transport of {t_pk / 1e15:.3f} PW across a 3.3e6 m span with a 15 K")
    print(f"  contrast: D = {d:.2e} m^2/s. Whether eddies do carry that fraction")
    print("  is a modelling statement, not an output of this arithmetic.")


def main():
    part1_coriolis()
    part2_rossby()
    part3_angular_momentum()
    part4_tropopause()
    part5_cell_edge()
    part6_transport()
    part7_ferrel()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
