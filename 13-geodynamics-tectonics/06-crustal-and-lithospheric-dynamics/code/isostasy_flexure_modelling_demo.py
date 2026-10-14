#!/usr/bin/env python3
"""Isostasy and flexure: Airy roots, flexural rigidity and deflection, the
compensation wavelength, the gravity admittance of a compensated load, and the
(elastic thickness, compensation depth) trade-off.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python isostasy_flexure_modelling_demo.py

Everything is SYNTHETIC: the densities, elastic thicknesses and loads below are
chosen teaching values with the units given, not measured lithospheres.  Every
printed number is computed here.

Contents
--------
1. Airy isostasy: crustal roots and the mass balance of a compensated load.
2. Flexural rigidity D, flexural parameter alpha, and the deflection under an
   applied line load, for several elastic thicknesses.
3. The compensation wavelength: where a plate stops behaving locally.
4. The gravity admittance of a compensated load, and the trade-off between
   elastic thickness and compensation depth that it leaves open.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


G = 6.674e-11          # m^3 kg^-1 s^-2, CODATA value of the gravitational constant
G_MGAL = G * 1e5       # 1 m/s^2 = 1e5 mGal
RHO_CRUST = 2700.0     # kg/m^3, chosen teaching value
RHO_MANTLE = 3300.0    # kg/m^3, chosen teaching value
E_YOUNG = 70.0e9       # Pa, chosen teaching value for the lithosphere
NU_POISSON = 0.25      # dimensionless, Poisson's ratio (standard elastic constant)
G_EARTH = 9.81         # m/s^2, standard acceleration of gravity


def rigidity(te_km):
    """Flexural rigidity D = E Te^3 / (12 (1 - nu^2)) in N m."""
    te = te_km * 1e3
    return E_YOUNG * te ** 3 / (12.0 * (1.0 - NU_POISSON ** 2))


def flexural_parameter(d_rig, drho):
    """alpha = (D / (drho g))^(1/4) in metres."""
    return (d_rig / (drho * G_EARTH)) ** 0.25


def demonstration_1():
    section("1. Airy isostasy: the root under a compensated load")
    print("  Local (Airy) compensation: the weight of the topography is balanced")
    print("  by the buoyancy of the crustal root,\n")
    print("    rho_c h = (rho_m - rho_c) r,   so   r = [rho_c/(rho_m - rho_c)] h")
    print(f"\n  rho_c = {RHO_CRUST:.0f} kg/m^3, rho_m = {RHO_MANTLE:.0f} kg/m^3, "
          f"so the ratio is")
    ratio = RHO_CRUST / (RHO_MANTLE - RHO_CRUST)
    print(f"  r/h = {RHO_CRUST:.0f}/{RHO_MANTLE - RHO_CRUST:.0f} = {ratio:.3f}\n")
    print("    h (km)   root r (km)   Moho depth (km)   mass excess (kg/m^2)")
    for h in (0.5, 1.0, 2.0, 3.0, 5.0):
        r = ratio * h
        excess = RHO_CRUST * h * 1e3
        print(f"    {h:6.1f}   {r:11.2f}   {r + 35.0:15.1f}   {excess:19.3e}")
    print("  (the reference crust there is 35 km thick, a chosen value, so the")
    print("   Moho depth is 35 km plus the root.)")
    print("\n  Gravity effect: the Bouguer slab of the topography and the")
    print("  compensating root, each a slab, cancel except for the difference in")
    print("  their depth of compensation.  For a sinusoidally corrugated interface")
    print("  at depth z, the attraction is exactly 2 pi G drho h exp(-k z).")
    lam = 200.0e3
    k = 2.0 * np.pi / lam
    h = 2.0e3
    r = ratio * h
    g_top = 2.0 * np.pi * G * RHO_CRUST * h * 1e5
    g_root = 2.0 * np.pi * G * (RHO_MANTLE - RHO_CRUST) * r * np.exp(-k * 35.0e3) * 1e5
    print(f"\n  for a periodic load of wavelength {lam / 1e3:.0f} km and amplitude")
    print(f"  {h / 1e3:.1f} km over a 35 km crust:")
    print(f"    surface topography attraction  = {g_top:8.3f} mGal")
    print(f"    root attraction (depth 35 km)  = {-g_root:8.3f} mGal")
    print(f"    residual (isostatic anomaly)   = {g_top - g_root:8.3f} mGal")
    print(f"    uncompensated attraction       = {g_top:.3f} mGal")
    print(f"  the residual is "
          f"{(g_top - g_root) / g_top * 100:.1f}% of the uncompensated value:")
    print("  compensation does not remove the anomaly, it reduces it, and the")
    print("  reduction depends on the depth of compensation.")


def demonstration_2():
    section("2. Flexural rigidity and the deflection under a line load")
    print("  D = E Te^3 / (12 (1 - nu^2)),   alpha = (D / (drho g))^(1/4),")
    print("  w(x) = (V0 alpha^3 / 8D) exp(-x/alpha) [cos(x/alpha) + sin(x/alpha)]")
    print("  for a line load V0 (force per unit length) on a plate over a fluid")
    print(f"  of density contrast drho.\n")
    print(f"  E = {E_YOUNG / 1e9:.0f} GPa, nu = {NU_POISSON:.2f}")
    drho = 600.0
    V0 = 1.0e12
    print(f"  drho = {drho:.0f} kg/m^3 (mantle minus crust), V0 = {V0:.1e} N/m\n")
    print("   Te (km)   D (N m)      alpha (km)   w(0) (km)   w(alpha)/w(0)  "
          "w(3alpha)/w(0)")
    for te in (5.0, 10.0, 25.0, 50.0):
        D = rigidity(te)
        a = flexural_parameter(D, drho)
        w0 = V0 * a ** 3 / (8.0 * D)
        w1 = w0 * np.exp(-1.0) * (np.cos(1.0) + np.sin(1.0))
        w3 = w0 * np.exp(-3.0) * (np.cos(3.0) + np.sin(3.0))
        print(f"   {te:7.1f}   {D:.4e}   {a / 1e3:11.1f}   {w0 / 1e3:10.2f}   "
              f"{w1 / w0:12.4f}   {w3 / w0:12.4f}")
    print("\n  the local (Airy) deflection for the same force spread over a width")
    print("  of one alpha is V0/(drho g alpha).  Its ratio to the line-load value")
    print("  w(0) = V0 alpha^3/(8D) is exactly alpha^4 drho g/(8D) = 1/8, because")
    print("  alpha is defined by alpha^4 = D/(drho g): the ratio is a constant,")
    print("  not a limit, and the measured ratio below is a check of the algebra.\n")
    print("   Te (km)   w(0) flexural (km)   V0/(drho g alpha) (km)   ratio")
    for te in (5.0, 10.0, 25.0, 50.0):
        D = rigidity(te)
        a = flexural_parameter(D, drho)
        w0 = V0 * a ** 3 / (8.0 * D)
        w_airy = V0 / (drho * G_EARTH * a)
        print(f"   {te:7.1f}   {w0 / 1e3:18.2f}   {w_airy / 1e3:23.2f}   "
              f"{w0 / w_airy:7.4f}")
    print("  The ratio is 1/8 in every row, as the algebra requires.  The")
    print("  physically interesting quantity is not this ratio but how the")
    print("  deflection *profile* depends on Te relative to the load width, which")
    print("  is what the next section measures.")


def demonstration_3():
    section("3. The compensation wavelength: where the plate stops being local")
    print("  For a periodic load of wavenumber k the flexural equation gives the")
    print("  deflection reduction factor 1/(1 + X) with X = D k^4 / (drho g),")
    print("  so the plate behaves locally (Airy) when X << 1 and rigidly when")
    print("  X >> 1.  The transition, X = 1, is at\n")
    print("    lambda_c = 2 pi (4 D / (drho g))^(1/4) = 2 pi sqrt(2) alpha\n")
    drho = 600.0
    print("   Te (km)   alpha (km)   lambda_c (km)   reduction factor at"
          " lambda = 500 km")
    for te in (5.0, 10.0, 25.0, 50.0):
        D = rigidity(te)
        a = flexural_parameter(D, drho)
        lam_c = 2.0 * np.pi * (4.0 * D / (drho * G_EARTH)) ** 0.25
        k500 = 2.0 * np.pi / 500.0e3
        red = 1.0 / (1.0 + D * k500 ** 4 / (drho * G_EARTH))
        print(f"   {te:7.1f}   {a / 1e3:11.1f}   {lam_c / 1e3:14.1f}   {red:30.4f}")
    print("\n  the reduction factor is the fraction of the Airy deflection that")
    print("  the plate actually achieves.  Wavelengths shorter than lambda_c are")
    print("  filtered out by the plate, which is why the gravity admittance of a")
    print("  region carries information about Te only over a limited band.")
    print("\n  and the deflection profile under the periodic load versus Te:")
    lam = 300.0e3
    k = 2.0 * np.pi / lam
    print(f"  (lambda = {lam / 1e3:.0f} km)")
    print("   Te (km)   w/Airy deflection")
    for te in (1.0, 5.0, 10.0, 25.0, 50.0):
        D = rigidity(te)
        X = D * k ** 4 / (drho * G_EARTH)
        print(f"   {te:7.1f}   {1.0 / (1.0 + X):18.5f}")


def demonstration_4():
    section("4. The admittance and the (Te, compensation depth) trade-off")
    print("  Model: a surface load of amplitude h at the surface of a crust of")
    print("  density rho_c over a mantle, with the compensation expressed as a")
    print("  Moho deflection at depth t.  The attraction of a sinusoidally")
    print("  corrugated interface of density contrast drho and amplitude a at")
    print("  depth z is 2 pi G drho a exp(-k z), so\n")
    print("    Z(k) = 2 pi G rho_c [ 1 - exp(-k t) / (1 + D k^4/(drho g)) ]")
    print("\n  target: a synthetic measurement of Z(k) built with Te = 25 km and")
    print("  t = 35 km, sampled over a band of wavelengths with 1% noise.\n")
    te_true, t_true = 25.0, 35.0e3
    lams = np.array([100.0, 150.0, 200.0, 300.0, 500.0, 800.0]) * 1e3
    ks = 2.0 * np.pi / lams

    def admittance(te_km, t_m, k):
        D = rigidity(te_km)
        return 2.0 * np.pi * G * RHO_CRUST * (
            1.0 - np.exp(-k * t_m) / (1.0 + D * k ** 4 / (600.0 * G_EARTH)))

    z_true = admittance(te_true, t_true, ks)
    z_obs = z_true * (1.0 + 0.01 * RNG.standard_normal(ks.size))
    print("    lambda (km)   Z (mGal/km)   noisy Z")
    for lam, zt, zo in zip(lams / 1e3, z_true * 1e5, z_obs * 1e5):
        print(f"    {lam:11.0f}   {zt:12.4f}   {zo:9.4f}")
    print("\n  now search the (Te, t) plane.  For each Te the compensation depth is")
    print("  fitted to the noisy data; the rms misfit is reported in per cent.\n")
    print("    Te (km)   best t (km)   rms misfit (%)")
    ts = np.linspace(5.0e3, 120.0e3, 2000)
    grid = []
    for te in (10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 60.0, 100.0):
        errs = np.array([np.sqrt(np.mean(((admittance(te, t, ks) - z_obs) / z_obs) ** 2))
                         for t in ts])
        i = int(np.argmin(errs))
        grid.append((te, ts[i] / 1e3, errs[i] * 100))
        print(f"    {te:7.1f}   {ts[i] / 1e3:12.1f}   {errs[i] * 100:14.4f}")
    print("\n  the compensation depth demanded by the data falls as Te rises: the")
    print("  data constrain the combination exp(-k t)/(1 + D k^4/(drho g)), so a")
    print("  shallower compensation can be traded against a larger elastic")
    print("  thickness.  The misfit does not grow without bound along that ridge,")
    print("  which is what makes it a genuine ambiguity rather than a resolved")
    print("  parameter.\n")
    te_fine = np.linspace(5.0, 60.0, 111)
    best = []
    for te in te_fine:
        errs = np.array([np.sqrt(np.mean(((admittance(te, t, ks) - z_obs) / z_obs) ** 2))
                         for t in ts])
        i = int(np.argmin(errs))
        best.append((te, ts[i] / 1e3, errs[i]))
    best = np.array(best)
    admitted = best[best[:, 2] <= 0.02]
    if admitted.size:
        print(f"  accepted set at the 2% level (twice the injected 1% noise):")
        print(f"    Te from {admitted[0, 0]:.1f} to {admitted[-1, 0]:.1f} km, "
              f"with t from {admitted[0, 1]:.1f} to {admitted[-1, 1]:.1f} km")
        print(f"    {admitted.shape[0]} of {te_fine.size} trial elastic thicknesses")
        print("  A result quoted as a single elastic thickness omits the range of")
        print("  compensation depths that fits the same data equally well, and that")
        print("  range is comparable with the thickness range itself.")
    print("\n  one further assumption is hidden in this model and worth naming:")
    print("  the load is at the surface and the compensation is a single interface.")
    print("  A buried load or a distributed compensation changes the relation")
    print("  between Z(k) and Te, so the admitted set above is conditional on the")
    print("  model, not a property of the data alone.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
