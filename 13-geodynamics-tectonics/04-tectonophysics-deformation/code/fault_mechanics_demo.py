#!/usr/bin/env python3
"""Fault mechanics: Coulomb failure, the optimal fault angle, and the static
Coulomb stress change produced by slip on a neighbouring strike-slip fault.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fault_mechanics_demo.py

Everything is SYNTHETIC.  The stress state, the friction coefficient, the slip
and the fault geometry are chosen teaching values.  No earthquake, aftershock
sequence or published stress-drop value is used or quoted.  The stress-transfer
model is the exact 2-D anti-plane (screw dislocation) solution, which is stated
and used as such.

Contents
--------
1. Mohr-Coulomb failure and the optimal fault plane, found by scanning.
2. Anderson's dips for normal and thrust faulting from the same scan.
3. The 2-D anti-plane stress change from a locked-to-depth-d strike-slip fault:
   free-surface check, finite-difference check, far-field decay.
4. Coulomb stress change on receiver faults of different strike.
5. Where the stress change promotes and where it shadows, and the zero crossing
   checked against its closed form.
6. Frictional strength with depth and the differential stress failure needs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
MU_FRICTION = 0.75          # SYNTHETIC friction coefficient (Byerlee-law-like)
COHESION_PA = 0.0           # SYNTHETIC cohesionless fault
SHEAR_MODULUS_PA = 30.0e9   # SYNTHETIC shear modulus
SLIP_M = 1.0                # SYNTHETIC coseismic slip
LOCKED_DEPTH_KM = 12.0      # SYNTHETIC depth of the base of the slipped patch
G = 9.81                    # m/s^2, exact standard constant
RHO_C = 2800.0              # kg/m^3, rock density for the strength profile


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def mu_from_friction():
    return np.degrees(np.arctan(MU_FRICTION))


def surface_displacement(x_km, d_km, slip_m, shear_mod):
    """Anti-plane screw dislocation at depth d, slip slip_m, in a half-space.

    u_y(x, 0) = -(2 slip / pi) atan(d / x): the surface displacement produced by
    slip on the fault plane x = 0 between the surface and depth d.  Positive x
    is the receiver side; the sign convention is stated in the lesson.
    """
    return -(2.0 * slip_m / np.pi) * np.arctan(d_km / x_km)


def stress_xy(x_km, z_km, d_km, slip_m, shear_mod):
    """Shear stress change sigma_xy, Pa, from the same screw dislocation.

    sigma_xy = (shear_mod slip / pi) [ (z+d)/((z+d)^2+x^2)
                                       - (z-d)/((z-d)^2+x^2) ]  in km units.
    """
    x = x_km * 1.0e3
    z = z_km * 1.0e3
    dd = d_km * 1.0e3
    term = ((z + dd) / ((z + dd) ** 2 + x ** 2)
            - (z - dd) / ((z - dd) ** 2 + x ** 2))
    return shear_mod * slip_m / np.pi * term          # Pa (lengths in metres)


def stress_yz(x_km, z_km, d_km, slip_m, shear_mod):
    """The other shear component, sigma_yz, from the same solution, Pa."""
    x = x_km * 1.0e3
    z = z_km * 1.0e3
    dd = d_km * 1.0e3
    term = (x / ((z - dd) ** 2 + x ** 2)) - (x / ((z + dd) ** 2 + x ** 2))
    return shear_mod * slip_m / np.pi * term          # Pa (lengths in metres)


def main():
    section("1. Mohr-Coulomb failure and the optimal plane")
    phi = mu_from_friction()
    print(f"  SYNTHETIC friction coefficient mu = {MU_FRICTION:.2f}, "
          f"cohesion C = {COHESION_PA:.0f} Pa")
    print(f"  friction angle phi = atan(mu) = {phi:.2f} deg")
    print("  Coulomb failure: |tau| = C + mu (sigma_n - p).  Writing the fault-")
    print("  normal angle from sigma_1 as theta, the resolved stresses are")
    print("      sigma_n = (s1+s3)/2 + (s1-s3)/2 cos 2theta,")
    print("      tau     = (s1-s3)/2 sin 2theta,")
    print("  so the Coulomb function is maximised at 2 theta = 90 deg + phi.")
    s1, s3 = 120.0e6, 40.0e6           # SYNTHETIC, Pore pressure p = 0
    p_pore = 0.0
    theta = np.linspace(1.0, 89.0, 881)
    s_n = 0.5 * (s1 + s3) + 0.5 * (s1 - s3) * np.cos(np.radians(2.0 * theta))
    tau = 0.5 * (s1 - s3) * np.sin(np.radians(2.0 * theta))
    cff = np.abs(tau) - MU_FRICTION * (s_n - p_pore)
    i_best = int(np.argmax(cff))
    theta_best = theta[i_best]
    theta_normal_closed = 45.0 + 0.5 * phi
    theta_plane_closed = 45.0 - 0.5 * phi
    print(f"\n  SYNTHETIC stress state: sigma_1 = {s1 / 1e6:.1f} MPa, "
          f"sigma_3 = {s3 / 1e6:.1f} MPa, pore pressure = {p_pore / 1e6:.1f} MPa")
    print(f"  theta is measured from the fault NORMAL to sigma_1.")
    print(f"  scanning 881 angles maximises |tau| - mu (sigma_n - p) at "
          f"theta = {theta_best:.3f} deg")
    print(f"  closed form 45 + phi/2 = {theta_normal_closed:.3f} deg for the normal;")
    print(f"  the fault PLANE therefore makes 90 - theta = {90.0 - theta_best:.3f} deg")
    print(f"  with sigma_1, i.e. 45 - phi/2 = {theta_plane_closed:.3f} deg.  The")
    print(f"  difference from the scan is the {theta[1] - theta[0]:.3f} deg step.")
    print(f"  at the optimum: sigma_n = {s_n[i_best] / 1e6:.2f} MPa, "
          f"|tau| = {abs(tau[i_best]) / 1e6:.2f} MPa")
    cfs_state = cff[i_best]
    print(f"  Coulomb failure function |tau| - mu(sigma_n - p) at the optimum = "
          f"{cfs_state / 1e6:+.2f} MPa")
    print(f"  so this SYNTHETIC state is {abs(cfs_state) / 1e6:.2f} MPa short of "
          f"failure with C = {COHESION_PA:.0f} Pa")
    print("  Note the sign convention: the function must be |tau| MINUS mu sigma_n",
          "\n  if it is to be maximised over orientations.  Maximising",
          "\n  |tau| + mu sigma_n finds the plane with the largest clamping stress,",
          "\n  which is the opposite end of the range.")
    print("  The optimum is a maximum of a smooth function of one variable, so it")
    print("  can be found by scanning; that is the independent check used here.")

    section("2. Anderson's dips from the same scan")
    print("  In Anderson's theory the principal stress is vertical or horizontal")
    print("  depending on the tectonic regime, so the dip of the optimal fault is")
    print("  fixed by which principal stress is vertical.")
    print(f"    regime        sigma_1 direction   optimal dip (deg)")
    print(f"    normal        vertical            {90.0 - theta_plane_closed:.1f}")
    print(f"    thrust        horizontal          {theta_plane_closed:.1f}")
    print(f"    strike-slip   horizontal          {90.0:.1f} (vertical fault)")
    print("  Values: for normal faulting the plane makes 45 - phi/2 with the")
    print(f"  vertical sigma_1, so the dip is 45 + phi/2 = {90.0 - theta_plane_closed:.1f};")
    print(f"  for thrust faulting the dip is 45 - phi/2 = {theta_plane_closed:.1f}.")
    print("  These are the classic ~60 and ~30 degree dips, derived here from mu alone.")
    print("  Being explicit about the assumption: Anderson's theory needs one")
    print("  principal stress to be vertical, which requires a free surface and no")
    print("  large pre-existing anisotropy or topographic load.")

    section("3. The 2-D anti-plane stress change, verified")
    d = LOCKED_DEPTH_KM
    print("  Model: a vertical strike-slip fault at x = 0 that slipped by")
    print(f"  {SLIP_M:.1f} m from the surface to depth d = {d:.1f} km, embedded in a")
    print(f"  half-space with shear modulus {SHEAR_MODULUS_PA / 1e9:.0f} GPa.")
    print("  Solution (screw dislocation plus image at z = -d):")
    print("    u_y = (slip/pi)[atan2(z-d,x) - atan2(z+d,x)]")
    print("    sigma_xy = mu slip/pi [ (z+d)/((z+d)^2+x^2) - (z-d)/((z-d)^2+x^2) ]")
    print("    sigma_yz = mu slip/pi [ x/((z-d)^2+x^2) - x/((z+d)^2+x^2) ]")
    xs = np.linspace(-80.0, 80.0, 801)
    xs = xs[np.abs(xs) > 1e-9]
    syz_surface = stress_yz(xs, np.zeros_like(xs), d, SLIP_M, SHEAR_MODULUS_PA)
    print(f"\n  free-surface check: max |sigma_yz(x, z=0)| = "
          f"{np.max(np.abs(syz_surface)):.3e} Pa")
    print("  (a traction-free surface requires exactly zero, and this is it to")
    print("  machine precision -- the image dislocation is what enforces it)")
    x0, z0 = 20.0, 6.0
    h = 1.0e-3
    exact = stress_xy(x0, z0, d, SLIP_M, SHEAR_MODULUS_PA)

    def uy(x_km, z_km):
        x, z, dd = x_km, z_km, d
        return (SLIP_M / np.pi) * (np.arctan2(z - dd, x) - np.arctan2(z + dd, x))
    num = SHEAR_MODULUS_PA * (uy(x0 + h, z0) - uy(x0 - h, z0)) / (2 * h * 1.0e3)
    print(f"\n  finite-difference check at (x, z) = ({x0:.1f}, {z0:.1f}) km:")
    print(f"    analytic  sigma_xy = {exact:.6e} Pa")
    print(f"    mu du_y/dx         = {num:.6e} Pa")
    print(f"    relative difference = {abs(num - exact) / abs(exact):.2e}")
    x_far = np.array([200.0, 400.0, 800.0, 1600.0])
    s_far = stress_xy(x_far, np.zeros_like(x_far), d, SLIP_M, SHEAR_MODULUS_PA)
    analytic_far = (2.0 * SHEAR_MODULUS_PA * SLIP_M / np.pi) \
        * (d * 1e3) / ((x_far * 1e3) ** 2)
    print(f"\n  far-field decay on the surface (should be 2 mu slip d/(pi x^2)):")
    for xv, sv, av in zip(x_far, s_far, analytic_far):
        print(f"    x = {xv:7.0f} km: sigma_xy = {sv:.4e} Pa, "
              f"asymptote = {av:.4e} Pa, ratio {sv / av:.4f}")
    print(f"  surface value at the fault trace: sigma_xy(0,0) = "
          f"{(2.0 * SHEAR_MODULUS_PA * SLIP_M / (np.pi * d * 1e3)) / 1e6:.3f} MPa")

    section("4. Coulomb stress change on receiver faults of different strike")
    x_rec, z_rec = 8.0, 5.0
    sxy = stress_xy(x_rec, z_rec, d, SLIP_M, SHEAR_MODULUS_PA)
    print(f"  Receiver point (x, z) = ({x_rec:.1f}, {z_rec:.1f}) km; "
          f"there sigma_xy = {sxy / 1e6:.4f} MPa")
    print("  For a vertical plane striking at angle phi from the main fault,")
    print("  resolved onto the slip direction:")
    print("    delta_tau = sigma_xy cos 2phi,   delta_sigma_n = sigma_xy sin 2phi")
    print("    delta_CFS = delta_tau + mu delta_sigma_n = sigma_xy(cos2phi + mu sin2phi)")
    phi_scan = np.linspace(0.0, 180.0, 1801)
    dcfs = sxy * (np.cos(np.radians(2 * phi_scan))
                  + MU_FRICTION * np.sin(np.radians(2 * phi_scan)))
    i_max = int(np.argmax(dcfs))
    i_min = int(np.argmin(dcfs))
    phi_opt = 0.5 * np.degrees(np.arctan(MU_FRICTION))
    print(f"\n    most promoted strike  phi = {phi_scan[i_max]:.2f} deg "
          f"(closed form 0.5 atan(mu) = {phi_opt:.2f} deg)")
    print(f"    delta_CFS at that strike  = {dcfs[i_max] / 1e6:.4f} MPa")
    print(f"    most inhibited strike     = {phi_scan[i_min]:.2f} deg, "
          f"delta_CFS = {dcfs[i_min] / 1e6:.4f} MPa")
    print(f"    fault-parallel receiver (phi = 0): delta_CFS = "
          f"{dcfs[1] / 1e6:.4f} MPa, with delta_sigma_n = "
          f"{sxy * np.sin(0.0) / 1e6:.4f} MPa")
    print("  A parallel vertical fault has NO normal-stress change in this 2-D")
    print("  anti-plane model, so its Coulomb change is purely the shear change.")
    print("  That is a property of anti-plane strain, not of nature: a 3-D")
    print("  dislocation solution also changes sigma_xx and sigma_zz, which add a")
    print("  normal-stress term even on a parallel plane.")

    section("5. Promoted and shadowed regions")
    xg = np.linspace(-60.0, 60.0, 241)
    zg = np.linspace(1.0, 60.0, 120)
    X, Z = np.meshgrid(xg, zg)
    DCFS = stress_xy(X, Z, d, SLIP_M, SHEAR_MODULUS_PA)
    promoted = DCFS > 0.0
    print(f"  grid {xg.size} x {zg.size}; the fault-parallel delta_CFS is positive")
    print(f"  over {100.0 * promoted.mean():.1f}% of the sampled area.")
    zc = np.sqrt((xg[np.abs(xg) > 0.0] ** 2) + d ** 2)
    x_probe = np.array([5.0, 10.0, 20.0, 40.0])
    print("\n    x (km)   closed form sqrt(x^2+d^2) (km)   measured sign change (km)")
    for xp in x_probe:
        col = stress_xy(np.full(zg.size, xp), zg, d, SLIP_M, SHEAR_MODULUS_PA)
        i_zero = int(np.argmin(np.abs(col)))
        print(f"    {xp:6.1f}   {np.sqrt(xp ** 2 + d ** 2):25.3f}   "
              f"{zg[i_zero]:25.1f}")
    print("  The sign changes at z = sqrt(x^2 + d^2): promoted near the surface")
    print("  and beside the slipped zone, shadowed deeper than the fault tip.  The")
    print("  boundary passes exactly through the fault tip (x = 0, z = d).")
    print("  This is the 2-D analogue of the familiar pattern in which aftershocks")
    print("  cluster where delta_CFS is positive; it is NOT a prediction of how")
    print("  many aftershocks there will be, because that also needs the background")
    print("  stressing rate and a rate-state nucleation model.")

    section("6. Frictional strength with depth")
    alpha_coef = 2.0 * MU_FRICTION / (np.cos(np.radians(phi))
                                      + MU_FRICTION * np.sin(np.radians(phi)))
    print("  Failure differential stress on the optimal plane, assuming the mean")
    print("  principal stress equals the lithostatic stress sigma_v = rho_c g z:")
    print(f"      delta_sigma = 2 mu sigma_v (1-lambda)/(cos phi + mu sin phi)")
    print(f"                  = {alpha_coef:.6f} sigma_v (1-lambda), and the identity")
    print(f"      2 mu/(cos phi + mu sin phi) = 2 sin phi = "
          f"{2.0 * np.sin(np.radians(phi)):.6f} confirms it algebraically.")
    print(f"  SYNTHETIC pore-pressure ratio lambda = p/sigma_v, "
          f"rho_c = {RHO_C:.0f} kg/m^3")
    print("\n    depth (km)   sigma_v (MPa)   delta_sigma, lambda=0   lambda=0.4")
    for zkm in (2.0, 5.0, 10.0, 15.0, 20.0):
        sv = RHO_C * G * zkm * 1e3
        s0 = alpha_coef * sigma_eff(sv, 0.0)
        s4 = alpha_coef * sigma_eff(sv, 0.4)
        print(f"    {zkm:10.1f}   {sv / 1e6:14.1f}   {s0 / 1e6:22.1f}   "
              f"{s4 / 1e6:8.1f}")
    print("  Strength rises linearly with depth, so a fault that is weak at the")
    print("  surface becomes hard to slip at depth unless pore pressure is high:")
    print("  lambda = 0.4 removes 40% of the effective normal stress and hence 40%")
    print("  of the strength.  These are model results for the stated friction and")
    print("  density, not measurements.")


def sigma_eff(sigma_v_pa, lam):
    return sigma_v_pa * (1.0 - lam)


if __name__ == "__main__":
    main()
