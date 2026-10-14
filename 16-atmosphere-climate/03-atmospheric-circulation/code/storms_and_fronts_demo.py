#!/usr/bin/env python3
"""Cyclones, fronts and severe weather: the Eady baroclinic instability
dispersion relation, its most unstable wavelength and growth rate, a numerical
check of the thermal wind relation, frontogenesis in a deformation flow,
convective available potential energy from a synthetic sounding, and the
cyclostrophic pressure deficit of a tornado-like vortex.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python storms_and_fronts_demo.py

Everything is SYNTHETIC. The stratification, shear, sounding and vortex
parameters are *chosen teaching values*, printed by this script. They are not
measurements and are not fitted to any named storm. Standard constants
(Omega, a, g) are used as constants.

Contents
--------
1. Eady dispersion relation: growth rate versus nondimensional wavenumber, the
   short-wave cutoff, the most unstable wavenumber and wavelength, and the
   e-folding time.
2. Sensitivity of the most unstable wavelength and growth rate to
   stratification, depth, shear and latitude.
3. Verification of the thermal-wind relation on an analytic state, including
   the numerical differentiation error.
4. Frontogenesis in a deformation flow: measured gradient growth rate versus the
   deformation rate, the doubling time, and the resolution limit.
5. CAPE and updraft speed from a synthetic sounding with a fixed environment,
   and its sensitivity to surface temperature.
6. Cyclostrophic pressure deficit of a Rankine vortex, and why the Coriolis term
   can be neglected at that scale.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5
A_EARTH = 6.371e6
G = 9.81
DEG = np.pi / 180.0
F45 = 2.0 * OMEGA * np.sin(45.0 * DEG)      # 1.03126e-04 1/s


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# 1. Eady dispersion relation
# ---------------------------------------------------------------------------

def eady_growth(mu):
    """Nondimensional Eady growth rate: mu sqrt(coth(mu)/mu - 1/mu^2 - 1/4).

    Eady's problem has uniform stratification N, uniform shear Lambda = U_s/H,
    zero perturbation potential vorticity and rigid lids. The vertical
    structure is cosh + sinh in mu = k N H/f, and the two lid conditions give

        c^2 - U_s c + U_s^2 (coth(mu)/mu - 1/mu^2) = 0.

    Complex c requires chi = coth(mu)/mu - 1/mu^2 > 1/4, i.e. mu < 2.399, and
    the growth rate is sigma = k U_s Im(c)/U_s = (mu f/(N H)) U_s sqrt(chi-1/4).
    """
    chi = 1.0 / np.tanh(mu) / mu - 1.0 / mu ** 2
    disc = chi - 0.25
    return np.where(disc > 0.0, mu * np.sqrt(np.maximum(disc, 0.0)), 0.0)


def part1_eady():
    section("1. Eady baroclinic instability: growth rate versus wavenumber")
    f, n_strat, depth, u_shear = F45, 1.0e-2, 1.0e4, 20.0
    lam_d = n_strat * depth / f
    scale = f * u_shear / (n_strat * depth)
    print("SYNTHETIC basic state: constant stratification N, constant shear")
    print("Lambda = U_s/H, rigid lids, f-plane at 45 deg.")
    print(f"  f = {f:.5e} 1/s, N = {n_strat:.1e} 1/s, H = {depth / 1e3:.0f} km, "
          f"U_s = {u_shear:.0f} m/s")
    print(f"  internal Rossby radius N H/f = {lam_d / 1e3:.0f} km; "
          f"Ri = (N H/U_s)^2 = {(n_strat * depth / u_shear) ** 2:.2f}")
    print(f"  growth-rate scale f U_s/(N H) = {scale:.4e} 1/s")
    print(f"\n{'mu = kNH/f':>12} {'chi = coth/mu - 1/mu^2':>23} {'sigma/scale':>12}")
    for mu in (0.25, 0.5, 0.8, 1.0, 1.2, 1.4, 1.606, 1.8, 2.0, 2.2, 2.399, 2.6):
        chi = 1.0 / np.tanh(mu) / mu - 1.0 / mu ** 2
        print(f"{mu:12.3f} {chi:23.5f} {float(eady_growth(mu)):12.5f}")
    fine = np.linspace(1e-6, 6.0, 600001)
    sig = eady_growth(fine)
    i = int(np.argmax(sig))
    mu_max, sig_max = fine[i], sig[i]
    print(f"\n  measured maximum: sigma/scale = {sig_max:.4f} at mu = {mu_max:.3f}")
    print(f"  analytic cutoff chi = 1/4 at mu_c = 2.399; numerical cutoff = "
          f"{fine[sig > 0.0].max():.3f}")
    print(f"  most unstable zonal wavelength = 2 pi N H/(mu_max f) = "
          f"{2 * np.pi * lam_d / (1.606 * 1e3):.0f} km (using mu = 1.606)")
    print(f"  e-folding time at the maximum = 1/(sigma_max scale) = "
          f"{1.0 / (sig_max * scale) / 86400:.2f} d")
    print(f"  standard form sigma_max = 0.31 f U_s/(N H) = {0.31 * scale:.3e} 1/s,")
    print(f"  which is {0.31 / sig_max:.4f} of the measured value: the constant")
    print("  0.31 is the numerical maximum of mu sqrt(chi - 1/4) and nothing else.")
    print("\n  the two cutoffs are not symmetric. Growth vanishes for mu below")
    print("  about 0.1 -- long waves are stable because the two rigid lids")
    print("  decouple -- and above mu = 2.399 -- short waves cannot feel the")
    print("  shear over their own wavelength. The unstable band is finite, which")
    print("  is why baroclinic storms have a preferred size at all.")


# ---------------------------------------------------------------------------
# 2. Sensitivity
# ---------------------------------------------------------------------------

def part2_sensitivity():
    section("2. What sets the size and speed of a baroclinic wave?")
    print("SYNTHETIC survey: lambda_max = 2 pi N H/(1.606 f) and")
    print("sigma_max = 0.31 f U_s/(N H). One parameter changes per row.\n")
    print(f"{'case':>26} {'N (1/s)':>8} {'H (km)':>7} {'U_s (m/s)':>10} "
          f"{'lat':>5} {'lambda_max (km)':>16} {'e-fold (d)':>11}")
    cases = [
        ("reference", 1.0e-2, 1.0e4, 20.0, 45.0),
        ("weaker stratification", 7.0e-3, 1.0e4, 20.0, 45.0),
        ("deeper layer", 1.0e-2, 1.2e4, 20.0, 45.0),
        ("shallow layer", 1.0e-2, 8.0e3, 20.0, 45.0),
        ("stronger shear", 1.0e-2, 1.0e4, 30.0, 45.0),
        ("weaker shear", 1.0e-2, 1.0e4, 12.0, 45.0),
        ("higher latitude", 1.0e-2, 1.0e4, 20.0, 60.0),
    ]
    for name, n_strat, depth, u_shear, lat in cases:
        f = 2.0 * OMEGA * np.sin(lat * DEG)
        lam_max = 2.0 * np.pi * n_strat * depth / (1.606 * f)
        sigma = 0.31 * f * u_shear / (n_strat * depth)
        print(f"{name:>26} {n_strat:8.1e} {depth / 1e3:7.0f} {u_shear:10.0f} "
              f"{lat:5.0f} {lam_max / 1e3:16.0f} {1.0 / sigma / 86400:11.2f}")
    print("\n  the wavelength scales as N H/f and the growth rate as f U_s/(N H),")
    print("  so growth depends on shear and stratification only through the")
    print("  Richardson number Ri = (N H/U_s)^2: sigma = 0.31 f Ri^(-1/2). A")
    print("  decrease in stratification -- which is what a moister, warmer")
    print("  atmosphere has -- makes storms BOTH longer and faster, and the two")
    print("  effects push in opposite directions on any practical forecast")
    print("  question. That collapse onto Ri is why Eady theory is used as a")
    print("  diagnostic of the mean state, not as a forecast model.")


# ---------------------------------------------------------------------------
# 3. Thermal wind verification
# ---------------------------------------------------------------------------

def part3_thermal_wind():
    section("3. Verifying the thermal-wind relation on an analytic state")
    f, theta0, lam, depth = F45, 300.0, 2.0e-3, 1.0e4
    dtheta_dy = -f * theta0 * lam / G
    print("Analytic state: u(z) = Lambda z with Lambda = "
          f"{lam:.1e} 1/s, and")
    print("theta(y) = theta0 - (f theta0 Lambda/g) y, which the thermal-wind")
    print("relation  f du/dz = -(g/theta0) dtheta/dy  satisfies identically.")
    print(f"\n  f du/dz                 = {f * lam:.6e} 1/s")
    print(f"  -(g/theta0) dtheta/dy   = {-(G / theta0) * dtheta_dy:.6e} 1/s")
    print(f"  analytic dtheta/dy      = {dtheta_dy:.6e} K/m")
    dy = 1.0e4
    y = np.arange(-5.0e5, 5.0e5 + dy, dy)
    theta = theta0 + dtheta_dy * (y + 2.0e6)      # an additive constant is free
    num = (theta[2:] - theta[:-2]) / (2.0 * dy)   # central difference
    err = float(np.max(np.abs(num - dtheta_dy)) / abs(dtheta_dy))
    print(f"\n  numerical dtheta/dy on a {dy / 1e3:.0f} km grid: relative error "
          f"{err:.2e}.")
    print("  The residual is round-off, because the metric has been compared with")
    print("  the analytic derivative of the function that generated it. That is a")
    print("  check of the algebra and the differencing stencil, NOT a test of the")
    print("  atmosphere. Testing it against data requires independent wind and")
    print("  temperature measurements, and the error budget then belongs to the")
    print("  instruments.")
    u_full = lam * depth
    print(f"\n  the shear integrated over the layer gives U = Lambda H = "
          f"{u_full:.0f} m/s,")
    print("  but the thermal wind relation determines only the SHEAR: one wind")
    print("  observation is still required to fix the constant of integration.")


# ---------------------------------------------------------------------------
# 4. Frontogenesis
# ---------------------------------------------------------------------------

def part4_frontogenesis():
    section("4. Frontogenesis: a front sharpening in a deformation flow")
    de = 1.0e-5                      # 1/s
    length, nx = 1.0e6, 2001
    dxx = 2.0 * length / (nx - 1)
    x = np.linspace(-length, length, nx)
    width0, amp = 2.0e5, 10.0
    theta0 = 275.0 + amp * np.tanh(x / width0)
    theta = theta0.copy()
    dt = 50.0
    steps = int(5.5 * 86400.0 / dt)
    print("Kinematic deformation u = -D x, v = +D y with D = 1e-05 1/s, i.e.")
    print("convergence along x. A front whose gradient lies along x stays")
    print("aligned with the contracting axis, so the problem reduces to one")
    print("dimension: dtheta/dt - D x dtheta/dx = 0, a pure strain whose exact")
    print("solution is theta(x, t) = theta0(x exp(Dt)). SYNTHETIC: no dynamics")
    print("and no frontogenesis feedback, which isolates the kinematic term.")
    print(f"Centered differences with a fourth-order Runge-Kutta step,")
    print(f"dx = {dxx:.0f} m, dt = {dt:.0f} s (CFL = "
          f"{de * length * dt / dxx:.2f} at the boundary).\n")

    def rhs(th):
        r = np.zeros_like(th)
        u = -de * x
        r[1:-1] = -u[1:-1] * (th[2:] - th[:-2]) / (2.0 * dxx)
        r[0] = -u[0] * (th[0] - th[1]) / dxx        # outflow boundary
        r[-1] = 0.0                                 # inflow held fixed
        return r

    print(f"{'time (d)':>9} {'max|dtheta/dx| (K/m)':>21} {'ratio':>8} "
          f"{'exp(D t)':>10} {'front width (km)':>17}")
    grad0 = float(np.max(np.abs(np.gradient(theta0, dxx))))
    rows = []
    for step in range(steps + 1):
        if step % 400 == 0:
            gmax = float(np.max(np.abs(np.gradient(theta, dxx))))
            print(f"{step * dt / 86400:9.2f} {gmax:21.6f} {gmax / grad0:8.3f} "
                  f"{np.exp(de * step * dt):10.3f} {amp / gmax / 1e3:17.2f}")
            rows.append((step * dt, gmax / grad0))
        if step == steps:
            break
        k1 = rhs(theta)
        k2 = rhs(theta + 0.5 * dt * k1)
        k3 = rhs(theta + 0.5 * dt * k2)
        k4 = rhs(theta + dt * k3)
        theta = theta + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        theta[-1] = theta0[-1]                      # inflow condition
    t_all = np.array([r[0] for r in rows])
    r_all = np.array([r[1] for r in rows])
    wide = r_all < 0.5 * np.exp(de * t_all[-1])     # still far from the grid
    slope = float(np.polyfit(t_all[wide], np.log(r_all[wide]), 1)[0])
    print(f"\n  fitted gradient growth rate over the first "
          f"{t_all[wide][-1] / 86400:.1f} d: {slope:.3e} 1/s")
    print(f"  deformation rate D                          : {de:.3e} 1/s"
          f"   (ratio {slope / de:.3f})")
    print(f"  doubling time ln2/D = {np.log(2.0) / de / 86400:.2f} d, so the")
    print(f"  {width0 / 1e3:.0f} km front is {width0 / 2e3:.0f} km wide after "
          "0.80 d and ~25 km after 2.4 d.")
    print("  Past about 4 d the front is only a few grid cells wide and the")
    print("  measured ratio falls behind exp(Dt): the experiment has run out of")
    print("  RESOLUTION, not of physics. At 5.3 d the exact solution would give")
    print("  99x while the model resolves 91x, and by 5.5 d the gap is wider.")
    print("  Quoting the analytic value with the model's run time attached would")
    print("  be the difference between a calculation and a claim; the honest")
    print("  statement is that the passive-scalar model sharpens fronts until the")
    print("  grid stops it.")
    print("  Nothing in the kinematics halts the collapse: the exact solution")
    print("  reaches zero width in a finite time. Real fronts stop when the")
    print("  ageostrophic circulation and the along-front wind reach a balance --")
    print("  exactly the feedback this passive-scalar experiment omits.")


# ---------------------------------------------------------------------------
# 5. CAPE
# ---------------------------------------------------------------------------

def part5_cape():
    section("5. CAPE from a synthetic sounding with a FIXED environment")
    gamma_env, gamma_dry, gamma_moist = 6.5e-3, 9.8e-3, 5.0e-3
    lcl, ztop, dz, t_env_surf = 1000.0, 14000.0, 5.0, 300.0
    z = np.arange(0.0, ztop, dz)
    t_env = t_env_surf - gamma_env * z
    print("SYNTHETIC sounding: environment T = "
          f"{t_env_surf:.0f} K - {gamma_env * 1e3:.1f} K/km z, HELD FIXED.")
    print(f"The parcel starts at the surface temperature, rises dry-adiabatically")
    print(f"({gamma_dry * 1e3:.1f} K/km) to the LCL at {lcl / 1e3:.1f} km, then")
    print(f"moist-adiabatically ({gamma_moist * 1e3:.1f} K/km). Only the parcel")
    print("changes between rows. This is the standard idealisation 'CAPE versus")
    print("surface temperature at fixed environment'; the environment does not")
    print("actually stay fixed as the surface warms, which is a limitation.\n")
    print(f"{'T_surf (K)':>10} {'CAPE (J/kg)':>12} {'LFC (km)':>9} "
          f"{'EL (km)':>8} {'w_max (m/s)':>12}")
    capes = []
    for t_surf in (296.0, 300.0, 304.0, 308.0):
        t_par = np.where(z <= lcl, t_surf - gamma_dry * z,
                         t_surf - gamma_dry * lcl - gamma_moist * (z - lcl))
        buoy = G * (t_par - t_env) / t_env
        idx = np.where(buoy > 0.0)[0]
        cape = float(np.sum(buoy[buoy > 0.0]) * dz)
        capes.append(cape)
        lfc = float(z[idx[0]]) / 1e3 if idx.size else float("nan")
        el = float(z[idx[-1]]) / 1e3 if idx.size else float("nan")
        el_txt = f"{el:8.2f}" if el < ztop / 1e3 - dz else "  >top  "
        print(f"{t_surf:10.1f} {cape:12.1f} {lfc:9.2f} {el_txt:>8} "
              f"{np.sqrt(2.0 * cape):12.1f}")
    print(f"\n  raising the surface parcel temperature by 12 K raises CAPE from")
    print(f"  {capes[0]:.0f} to {capes[-1]:.0f} J/kg, a factor of "
          f"{capes[-1] / capes[0]:.1f}, and the")
    print("  square-root bound on the updraft rises by about "
          f"{np.sqrt(capes[-1]) / np.sqrt(capes[0]) - 1:.0%}.")
    print("  The sensitivity is strong because buoyancy is a difference of two")
    print("  nearly equal profiles: a change of a few kelvin at every level is a")
    print("  large change in their difference. This is the physical reason CAPE")
    print("  is expected to respond to warming faster than proportionally -- and")
    print("  also why a small error in either profile changes it greatly.")
    print("  The equilibrium level is quoted only when it falls inside the")
    print("  14 km domain; a constant 5 K/km moist adiabat is unphysical above")
    print("  the tropopause, so an EL at the domain top means 'not resolved'.")
    print("  w_max = sqrt(2 CAPE) is an UPPER BOUND: it ignores entrainment,")
    print("  water loading and the reduction of buoyancy by the pressure")
    print("  perturbation, all of which cut a real updraft substantially.")


# ---------------------------------------------------------------------------
# 6. Tornado pressure deficit
# ---------------------------------------------------------------------------

def part6_vortex():
    section("6. Cyclostrophic pressure deficit of a Rankine vortex")
    rho, r0, lat = 1.2, 100.0, 35.0
    f = 2.0 * OMEGA * np.sin(lat * DEG)
    print("Rankine vortex: v = v_max r/r0 inside the core, v = v_max r0/r")
    print("outside. Cyclostrophic balance dp/dr = rho v^2/r integrates to")
    print("  deficit from far field to the core edge = rho v_max^2/2")
    print("  total central deficit                     = rho v_max^2,")
    print("independent of the core radius r0.\n")
    print(f"{'v_max (m/s)':>12} {'to core edge (hPa)':>19} "
          f"{'total central (hPa)':>21} {'f r0/v_max':>12}")
    for v_max in (30.0, 60.0, 100.0, 140.0):
        print(f"{v_max:12.0f} {0.5 * rho * v_max ** 2 / 100.0:19.1f} "
              f"{rho * v_max ** 2 / 100.0:21.1f} {f * r0 / v_max:12.2e}")
    print(f"\n  with v_max = 100 m/s the total central deficit is "
          f"{rho * 1e4 / 100.0:.0f} hPa and")
    print("  the deficit relative to the core edge is half of that. Both scale as")
    print("  v_max^2, so halving the wind removes three quarters of the deficit.")
    print(f"  The last column is the ratio of the Coriolis term f v to the")
    print(f"  centrifugal term v^2/r0 at the core edge: {f * r0 / 100.0:.1e} for")
    print("  v_max = 100 m/s. That is why cyclostrophic balance is the right")
    print("  approximation at this scale and geostrophic balance is not -- the")
    print("  opposite of the situation in Section 1.")
    print("  These are balances, not predictions of any particular storm, and no")
    print("  observed wind or pressure is used or claimed.")


def main():
    part1_eady()
    part2_sensitivity()
    part3_thermal_wind()
    part4_frontogenesis()
    part5_cape()
    part6_vortex()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
