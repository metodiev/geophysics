#!/usr/bin/env python3
"""Isostasy: the Airy root and the gravity it predicts, the exact finite-root
geometry versus the infinite-plate approximation, the Pratt column model and its
model dependence, and the flexural (elastic plate) response as a function of load
width.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python isostasy_demo.py

Everything is SYNTHETIC: the densities, elastic constants, topography and
compensation depths are chosen teaching values.  The only exact quantity is
G = 6.67430e-11 m^3 kg^-1 s^-2.  No real mountain belt, station or dataset is used.

Contents
--------
1. The Airy root for a range of topography, and the Bouguer anomaly it predicts.
2. Why the infinite-plate (thin-slab) isostatic correction is self-cancelling,
   and how much the exact finite-root geometry changes that.
3. The Pratt model: column densities, deficit and the model dependence of the
   predicted isostatic anomaly.
4. Flexure: rigidity, flexural parameter, and the compensation fraction as a
   function of load wavelength.
5. The three models compared on one SYNTHETIC station, with the residual each
   leaves.
6. Non-uniqueness: root thickness versus density contrast, and the depth error
   from a wrong contrast.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11
RHO_CRUST = 2670.0          # kg/m^3, SYNTHETIC
RHO_MANTLE = 3270.0         # kg/m^3, SYNTHETIC
DRHO = RHO_MANTLE - RHO_CRUST
E_YOUNG = 70.0e9            # Pa, SYNTHETIC crustal Young modulus
NU = 0.25                   # SYNTHETIC Poisson ratio
TE_KM = 25.0                # km, SYNTHETIC elastic thickness
PRATT_D_KM = 30.0           # km, SYNTHETIC Pratt compensation depth
ROOT_RADIUS_KM = 100.0      # km, SYNTHETIC lateral extent of a root


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def airy_root(h_m):
    """Airy root thickness in metres for topography h_m."""
    return h_m * RHO_CRUST / DRHO


def cylinder_attraction(drho, thickness, radius):
    """Attraction at the centre of the top face of a cylinder, m/s^2.

    Standard result for a uniform cylinder of density contrast drho, thickness
    `thickness` and radius `radius`, observed on the axis at its top face:
        2 pi G drho [ h + R - sqrt(R^2 + h^2) ].
    """
    return 2.0 * np.pi * G * drho * (
        thickness + radius - np.sqrt(radius ** 2 + thickness ** 2))


def main():
    slab_coef = 2.0 * np.pi * G * RHO_CRUST * 1e5       # mGal per metre of rock
    print("SYNTHETIC densities: crust "
          f"{RHO_CRUST:.0f} kg/m^3, mantle {RHO_MANTLE:.0f} kg/m^3, "
          f"contrast {DRHO:.0f} kg/m^3")
    print(f"2 pi G rho_crust = {slab_coef:.6f} mGal/m")

    section("1. The Airy root and the Bouguer anomaly it predicts")
    print("  Airy: t = h rho_c / (rho_m - rho_c); a mass deficit of "
          "(rho_m - rho_c) t")
    print("  per unit area balances the topography's excess rho_c h.")
    print("   h (km)   root t (km)   deficit (kg/m^2)   Bouguer anomaly expected (mGal)")
    for h_km in (0.5, 1.0, 2.0, 3.0, 5.0):
        h = h_km * 1e3
        t = airy_root(h)
        deficit = DRHO * t
        boug = -2.0 * np.pi * G * deficit * 1e5
        print(f"   {h_km:6.2f}   {t / 1e3:11.3f}   {deficit:16.0f}   {boug:28.3f}")
    h_test = 3.0e3
    t_test = airy_root(h_test)
    print(f"  check for h = 3 km: t = {t_test / 1e3:.3f} km and "
          f"(rho_m-rho_c) t = {DRHO * t_test:.0f} kg/m^2")
    print(f"  equals rho_c h = {RHO_CRUST * h_test:.0f} kg/m^2: the compensation is")
    print("  EXACT by construction, which is why the thin-slab isostatic anomaly")
    print("  of a perfectly Airy-compensated plateau is zero to this order.")

    section("2. Infinite plate versus a finite root")
    print(f"  The slab result uses an infinite plate.  With a cylindrical root of")
    print(f"  radius R = {ROOT_RADIUS_KM:.0f} km the exact attraction at the centre is")
    print("    2 pi G d rho [ t + R - sqrt(R^2 + t^2) ],")
    print("  and the isostatic anomaly becomes 2 pi G d rho [ sqrt(R^2+t^2) - R ].")
    print("   h (km)   t (km)   exact root (mGal)   slab root (mGal)   residual (mGal)")
    for h_km in (1.0, 3.0, 5.0):
        h = h_km * 1e3
        t = airy_root(h)
        Rr = ROOT_RADIUS_KM * 1e3
        exact = cylinder_attraction(DRHO, t, Rr) * 1e5
        slab = 2.0 * np.pi * G * DRHO * t * 1e5
        resid = 2.0 * np.pi * G * DRHO * (np.sqrt(Rr ** 2 + t ** 2) - Rr) * 1e5
        print(f"   {h_km:6.2f}   {t / 1e3:8.3f}   {exact:17.3f}   {slab:16.3f}   "
              f"{resid:16.3f}")
    t3 = airy_root(3.0e3)
    Rr = ROOT_RADIUS_KM * 1e3
    print(f"  MEASURED: for t = {t3 / 1e3:.2f} km and R = {ROOT_RADIUS_KM:.0f} km the")
    print("  finite geometry leaves a residual of about "
          f"{2.0 * np.pi * G * DRHO * (np.sqrt(Rr ** 2 + t3 ** 2) - Rr) * 1e5:.1f} mGal,")
    print("  which is 2.2% of the slab compensation at h = 1 km, 6.6% at 3 km and")
    print("  11.0% at 5 km.  The isostatic anomaly of a")
    print("  'perfectly compensated' mountain is therefore not zero; it is as large")
    print("  as the geometric approximation it was built on.  Widening R reduces the")
    print("  residual: the value above is what a 100 km-wide root produces.")

    section("3. The Pratt model and its model dependence")
    print("  Pratt: a column of height (D + h) above the compensation depth has")
    print("  density rho(h) = rho_0 D / (D + h), so the deficit per unit area is")
    print("  D (rho_0 - rho(h)) = D rho_0 h / (D + h).")
    print(f"  SYNTHETIC compensation depth D = {PRATT_D_KM:.0f} km, rho_0 = "
          f"{RHO_CRUST:.0f} kg/m^3")
    print("   h (km)   rho(h) (kg/m^3)   Pratt deficit (kg/m^2)   Airy deficit   difference (%)")
    for h_km in (0.5, 1.0, 2.0, 3.0, 5.0):
        h = h_km * 1e3
        rho_h = RHO_CRUST * PRATT_D_KM * 1e3 / (PRATT_D_KM * 1e3 + h)
        deficit_p = PRATT_D_KM * 1e3 * (RHO_CRUST - rho_h)
        deficit_a = RHO_CRUST * h
        print(f"   {h_km:6.2f}   {rho_h:15.1f}   {deficit_p:21.0f}   "
              f"{deficit_a:13.0f}   {(deficit_p - deficit_a) / deficit_a * 100:+13.2f}")
    h3 = 3.0e3
    rho_h3 = RHO_CRUST * PRATT_D_KM * 1e3 / (PRATT_D_KM * 1e3 + h3)
    resid_pratt = 2.0 * np.pi * G * (RHO_CRUST * h3
                                     - PRATT_D_KM * 1e3 * (RHO_CRUST - rho_h3)) * 1e5
    print(f"  At h = 3 km, Pratt's deficit is "
          f"{PRATT_D_KM * 1e3 * (RHO_CRUST - rho_h3):.0f} kg/m^2 against Airy's")
    print(f"  {RHO_CRUST * h3:.0f} kg/m^2, a shortfall of "
          f"{(RHO_CRUST * h3 - PRATT_D_KM * 1e3 * (RHO_CRUST - rho_h3)):.0f} kg/m^2")
    print(f"  equivalent to {resid_pratt:.2f} mGal of uncancelled gravity signal.")
    print("  CHOOSING the compensation model therefore changes the predicted isostatic")
    print("  anomaly at the tens of milligal for the same topography and the same")
    print("  densities: the model, not the data, sets that part of the answer.")

    section("4. Flexure: an elastic plate instead of local compensation")
    te = TE_KM * 1e3
    rigidity = E_YOUNG * te ** 3 / (12.0 * (1.0 - NU ** 2))
    alpha = (rigidity / (DRHO * 9.81)) ** 0.25
    w_airy_1km = 1.0e3 * RHO_CRUST / DRHO
    print(f"  D = E Te^3 / (12 (1 - nu^2)) with E = {E_YOUNG:.1e} Pa, nu = {NU:.2f},")
    print(f"  Te = {TE_KM:.0f} km:  D = {rigidity:.4e} N m")
    print(f"  flexural parameter alpha = (D / (d rho g))^1/4 = {alpha / 1e3:.3f} km")
    print(f"  Airy root for h = 1 km would be {w_airy_1km / 1e3:.3f} km")
    print("  For a sinusoidal load of wavelength lambda the deflection is")
    print("  w = w_Airy / (1 + (2 pi / lambda)^4 alpha^4), so the transition from")
    print("  local (Airy-like) to regional (plate-like) support is at lambda = 2 pi alpha.")
    print(f"  that transition wavelength = {2.0 * np.pi * alpha / 1e3:.1f} km")
    print("   lambda (km)   lambda/alpha   deflection w (km)   fraction of Airy root")
    for lam_km in (50.0, 100.0, 200.0, 400.0, 800.0, 1600.0):
        lam = lam_km * 1e3
        frac = 1.0 / (1.0 + (2.0 * np.pi / lam) ** 4 * alpha ** 4)
        print(f"   {lam_km:11.0f}   {lam / alpha:12.2f}   "
              f"{w_airy_1km * frac / 1e3:17.3f}   {frac:22.4f}")
    print("  Short loads are carried by the plate and produce almost no root; long")
    print("  loads are compensated almost locally.  A single 'depth of compensation'")
    print("  is therefore a wavelength-dependent statement, not a property of a")
    print("  mountain belt.")

    section("5. The three models on one SYNTHETIC station")
    h_st = 2000.0            # m
    lam_st = 300.0e3         # m, width of the SYNTHETIC load
    t_airy = airy_root(h_st)
    frac_st = 1.0 / (1.0 + (2.0 * np.pi / lam_st) ** 4 * alpha ** 4)
    print(f"  SYNTHETIC station on a plateau of height {h_st:.0f} m, load width "
          f"{lam_st / 1e3:.0f} km")
    print("   model        predicted root     Bouguer anomaly     isostatic residual")
    print(f"   no support   {0.0:10.3f} km     {2.0 * np.pi * G * RHO_CRUST * h_st * 1e5:14.3f} mGal"
          f"     {2.0 * np.pi * G * RHO_CRUST * h_st * 1e5:14.3f} mGal")
    print(f"   Airy (slab)  {t_airy / 1e3:10.3f} km     "
          f"{-2.0 * np.pi * G * DRHO * t_airy * 1e5:14.3f} mGal     {0.0:14.3f} mGal")
    print(f"   flexure      {t_airy * frac_st / 1e3:10.3f} km     "
          f"{-2.0 * np.pi * G * DRHO * t_airy * frac_st * 1e5:14.3f} mGal     "
          f"{-2.0 * np.pi * G * DRHO * t_airy * (1 - frac_st) * 1e5:14.3f} mGal")
    print("  The last column is the part of the Bouguer anomaly that the model does")
    print("  NOT explain: zero for a perfect infinite slab, fully unexplained for an")
    print("  uncompensated load, and only partly explained for flexure.  It is a")
    print("  residual against a hypothesis, not a measurement of the rocks.")

    section("6. Non-uniqueness: root thickness versus density contrast")
    print("  The same deficit (rho_m - rho_c) t can be produced by many (d rho, t)")
    print("  pairs.  For a measured Bouguer anomaly of a compensated plateau, only")
    print("  the product is constrained:")
    for h_km in (1.0, 3.0):
        h = h_km * 1e3
        print(f"   topography {h_km:.1f} km: required (rho_m - rho_c) t = "
              f"{RHO_CRUST * h:.0f} kg/m^2")
        for drho_try in (300.0, 600.0, 900.0):
            print(f"     contrast {drho_try:6.0f} kg/m^3 -> t = "
                  f"{RHO_CRUST * h / drho_try / 1e3:7.3f} km")
    drho_bad = 500.0
    t_bad = RHO_CRUST * h_test / drho_bad
    print(f"  With the true contrast {DRHO:.0f} kg/m^3 the root under 3 km of relief is")
    print(f"  {t_test / 1e3:.3f} km; with {drho_bad:.0f} kg/m^3 it is "
          f"{t_bad / 1e3:.3f} km, a difference of {(t_bad - t_test) / 1e3:.3f} km,")
    print("  and gravity alone cannot tell the two apart.  Only an independent")
    print("  velocity-, density- or seismological constraint separates them.")


if __name__ == "__main__":
    main()
