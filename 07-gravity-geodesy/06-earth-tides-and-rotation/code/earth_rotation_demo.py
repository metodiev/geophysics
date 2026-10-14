#!/usr/bin/env python3
"""Earth rotation, part 3: the axial angular-momentum budget for length-of-day
changes, and the polar motion equations for wobble and its excitation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earth_rotation_demo.py

Everything here is SYNTHETIC or a stated rounded standard constant.  The Earth
model is a two-layer sphere (no ellipticity, no mantle density gradient), the
winds and the mass redistribution are chosen teaching fields, and the observed
values are never quoted.

Contents
--------
1. A two-layer Earth model: mass, mean moment of inertia, C/(M R^2).
2. The axial angular momentum of a thin shell: verification of (2/3)M Omega R^2
   for solid-body rotation, then a synthetic zonal jet.
3. Length-of-day: the budget dLOD/LOD = -dH/(C Omega), and the wind needed for
   1 ms.
4. Polar motion: the linearised wobble equations, the rigid Euler period, the
   free wobble measured by numerical integration, and the forced response.
5. Excitation: what mass redistribution is needed for a stated pole displacement.
"""

import numpy as np
from scipy.integrate import solve_ivp

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G = 6.67430e-11
GM_EARTH = 3.986004418e14       # m^3 s^-2
R_EARTH = 6371.0e3              # m, rounded mean radius
OMEGA = 7.2921150e-5            # rad s^-1, standard Earth rotation rate
SIDEREAL_DAY = 2 * np.pi / OMEGA
M_ATMOSPHERE = 5.15e18          # kg, rounded standard total atmospheric mass

# --- SYNTHETIC model parameters ---------------------------------------------
CORE_RADIUS = 3480.0e3          # m, rounded core radius
RHO_CORE = 10900.0              # kg m^-3, chosen core density
H_DYN = 0.00327                 # synthetic dynamical ellipticity (C-A)/A
JET_SPEED = 30.0                # m s^-1, synthetic peak zonal wind
MASS_SHIFT_FRAC = 1.0e-8        # synthetic mass redistribution, fraction of M


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    section("1. A two-layer Earth model and its moments of inertia")
    M_earth = GM_EARTH / G
    rho_m = (M_earth * 3.0 / (4.0 * np.pi) - RHO_CORE * CORE_RADIUS ** 3) / (
        R_EARTH ** 3 - CORE_RADIUS ** 3)
    A_inertia = (8.0 * np.pi / 3.0) * (
        RHO_CORE * CORE_RADIUS ** 5 + rho_m * (R_EARTH ** 5 - CORE_RADIUS ** 5)) / 5.0
    print(f"  Earth mass from GM/G       M = {M_earth:.4e} kg")
    print(f"  core radius (rounded)      {CORE_RADIUS/1e3:.0f} km, "
          f"density {RHO_CORE:.0f} kg/m^3")
    print(f"  mantle density solved from the mass: {rho_m:.1f} kg/m^3")
    print(f"  moment of inertia (spherical model) C = A = {A_inertia:.4e} kg m^2")
    print(f"  C/(M R^2) = {A_inertia/(M_earth*R_EARTH**2):.5f}")
    print("  This model has no ellipticity and no mantle density gradient, so it")
    print("  overestimates the real ratio: the Earth's is lower because its mass")
    print("  is concentrated toward the centre.  The model's C is used below as a")
    print("  stated synthetic constant, not as a measured property of the Earth.")
    C = A_inertia

    section("2. Axial angular momentum of a thin shell")
    print("  H_3 = integral of rho u (r sin theta) dV for a zonal wind u(theta)")
    th = np.linspace(0.0, np.pi, 200001)
    w = np.gradient(th)

    def shell_H(u, mass):
        """Axial angular momentum (kg m^2/s) of a thin shell of the given mass."""
        sigma = mass / (4.0 * np.pi * R_EARTH ** 2)
        return np.sum(sigma * u * R_EARTH * np.sin(th)
                      * R_EARTH ** 2 * np.sin(th) * w * 2.0 * np.pi)

    solid = shell_H(OMEGA * R_EARTH * np.sin(th), M_ATMOSPHERE)
    print(f"  The shell here is the ATMOSPHERE, not the solid Earth: a wind")
    print(f"  momentum is (atmospheric mass) x (wind speed) x (moment arm), and")
    print(f"  using the Earth's mass instead would inflate it by "
          f"{M_earth/M_ATMOSPHERE:.3e}.")
    print(f"  atmospheric mass (rounded standard) = {M_ATMOSPHERE:.3e} kg")
    print(f"  solid-body rotation: quadrature {solid:.6e} kg m^2/s")
    print(f"  analytic (2/3) M_atm Omega R^2 = "
          f"{(2.0/3.0)*M_ATMOSPHERE*OMEGA*R_EARTH**2:.6e} kg m^2/s")
    print(f"  relative difference = "
          f"{abs(solid-(2.0/3.0)*M_ATMOSPHERE*OMEGA*R_EARTH**2)/solid:.3e}")
    print("  The factor is (2/3) M Omega R^2 -- note R^2, not R^3: the moment arm")
    print("  appears once in r x v, and a common error is to include it twice,")
    print("  which inflates the answer by a factor of R ~ 6.4e6.")

    jet = JET_SPEED * np.sin(th) ** 2
    jet_H = shell_H(jet, M_ATMOSPHERE)
    print(f"  SYNTHETIC zonal wind u = {JET_SPEED:.0f} sin^2(theta) m/s "
          f"(westerlies in both hemispheres)")
    print(f"    H_3 = {jet_H:.6e} kg m^2/s")

    section("3. Length of day")
    print("  Budget: if the non-solid part of the axial angular momentum changes")
    print("  by dH_3, conservation gives dLOD/LOD = +dH_3/(C Omega)  (ignoring the")
    print("  small compliance terms, which the model does not contain).")
    print("  Sign check: the atmosphere gaining westerly momentum slows the Earth,")
    print("  so a POSITIVE dH_3 lengthens the day.")
    for dh in (jet_H, jet_H / 10.0, jet_H / 100.0):
        dlod = SIDEREAL_DAY * dh / (C * OMEGA)
        print(f"  dH_3 = {dh:+.3e} kg m^2/s -> dLOD = {dlod*1e3:+.6f} ms")
    need = C * OMEGA * (1.0e-3 / SIDEREAL_DAY)
    print(f"  a 1 ms change needs dH_3 = C Omega (1 ms/LOD) = {need:.4e} kg m^2/s")
    print(f"  that is {need/jet_H:.4f} of the synthetic jet's angular momentum,")
    print("  i.e. the whole atmosphere's winds, uniformly rearranged, move the")
    print("  day by a few milliseconds -- which is why LOD is a usable window on")
    print("  atmospheric angular momentum and why the solid Earth's own torques")
    print("  are inferred by removing it.")

    section("4. Polar motion: free and forced wobble")
    sigma_c = OMEGA * H_DYN
    T_euler = 2 * np.pi / sigma_c
    print(f"  dynamical ellipticity (C-A)/A (stated) = {H_DYN:.5f}")
    print(f"  rigid-Euler wobble frequency sigma_c = Omega(C-A)/A = "
          f"{sigma_c:.6e} rad/s")
    print(f"  rigid-Euler period = {T_euler/86400:.2f} days")
    print("  The real Earth's observed wobble period is LONGER than this because")
    print("  the Earth is elastic and carries oceans: the rigid value is a lower")
    print("  bound, and the lengthening factor is an Earth-model result our model")
    print("  does not contain.  We therefore report only the rigid value.")

    # linearised wobble equation in complex form, dm/dt + i sigma_c m =
    # i sigma_c chi(t), integrated as a real two-vector [Re m, Im m]:
    #   d(Re m)/dt = sigma_c (Im m - Im chi),  d(Im m)/dt = sigma_c (Re chi - Re m)
    def rhs(t, m, chi_re, chi_im):
        return [sigma_c * (m[1] - chi_im), sigma_c * (chi_re - m[0])]

    years = 3.0
    t_eval = np.linspace(0.0, years * 365.25 * 86400.0, 4000)
    step = (1.0e-7, 0.0)                     # step excitation: Re chi = 1e-7
    sol = solve_ivp(lambda t, m: rhs(t, m, step[0], step[1]),
                    (t_eval[0], t_eval[-1]), [0.0, 0.0], t_eval=t_eval,
                    rtol=1e-12, atol=1e-18)
    m = sol.y[0] + 1j * sol.y[1]
    # measure the period from the phase advance of the complex wobble
    analytic = step[0] * (1.0 - np.exp(-1j * sigma_c * t_eval))
    dev = np.max(np.abs(m - analytic)) / np.max(np.abs(analytic))
    print(f"  verification: the numerical solution matches the analytic")
    print(f"    m(t) = chi(1 - exp(-i sigma_c t)) to {dev:.3e} relative")
    im = m.imag
    peaks = np.where((im[1:-1] > im[:-2]) & (im[1:-1] > im[2:]))[0] + 1
    if peaks.size > 2:
        spacing = np.mean(np.diff(t_eval[peaks]))
        print(f"  free wobble period measured from the maxima of Im(m):")
        print(f"    {spacing/86400:.4f} days, against the analytic "
              f"2 pi/sigma_c = {2*np.pi/sigma_c/86400:.4f} days "
              f"(agreement {abs(spacing-2*np.pi/sigma_c)/(2*np.pi/sigma_c):.2e})")

    print("  Forced response to a periodic excitation chi = chi0 exp(i sigma t):")
    print("    m = chi0/(1 - sigma/sigma_c), amplified near sigma = sigma_c")
    print("   period (d)   frequency ratio sigma/sigma_c   |m|/chi0")
    for per_d in (365.25, 435.0, 300.0, 150.0):
        ratio = (2 * np.pi / (per_d * 86400.0)) / sigma_c
        print(f"   {per_d:9.2f} {ratio:28.4f} {1.0/abs(1.0-ratio):16.4f}")
    print("  The amplification is 1/(1 - sigma/sigma_c): a forcing at the free")
    print("  period produces a large response whatever its amplitude, which is why")
    print("  an excitation's SPECTRUM, not its size, decides the wobble.")

    section("5. Excitation for a stated pole displacement")
    # A mass redistribution that moves a fraction of the excess equatorial
    # moment excites chi of order (the change in the products of inertia)/C.
    dI = MASS_SHIFT_FRAC * M_earth * R_EARTH ** 2
    chi_ex = dI / C
    print(f"  SYNTHETIC redistribution of {MASS_SHIFT_FRAC:.0e} of the Earth's mass")
    print(f"  across R: dI = {dI:.4e} kg m^2, chi = dI/C = {chi_ex:.4e}")
    rho_arcsec = 206264.806                    # arcseconds per radian
    print(f"  step response in the pole position: |m| = |chi| = {chi_ex:.4e} rad")
    print(f"    = {chi_ex*rho_arcsec*1e3:.4f} milliarcsecond")
    print("  A 1.0e-8 M R^2 change in the products of inertia is a few")
    print("  milliarcseconds of pole displacement: polar motion is a measurement")
    print("  of very small mass redistributions, and the budget must account for")
    print("  atmosphere, ocean and hydrology before anything is attributed to the")
    print("  solid Earth.")


if __name__ == "__main__":
    main()
