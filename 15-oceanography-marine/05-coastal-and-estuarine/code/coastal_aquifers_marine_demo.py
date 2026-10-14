#!/usr/bin/env python3
"""Coastal aquifers and submarine groundwater discharge: the Ghyben-Herzberg
relation and the island freshwater lens, pumping-induced upconing, the
conductivity contrast that makes the interface mappable, and the partition of
submarine discharge into fresh and recirculated components.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_aquifers_marine_demo.py

Everything here is SYNTHETIC.  The island, the aquifer properties and the
conductivity model are teaching models with the stated model constants.  No real
island, aquifer, well, beach or survey is referenced, and no number is quoted from
a published measurement.

Contents
--------
1. Ghyben-Herzberg and the Dupuit island lens: the analytic solution, a numerical
   check, the lens volume and the residence time.
2. Pumping-induced upconing: the drawdown that brings the interface to the screen
   and the pumping rate it corresponds to.
3. Salinity, conductivity and Archie: the bulk-resistivity contrast and the
   electrode spacing needed to see the interface.
4. Fresh versus recirculated submarine discharge: the tidal decay length and the
   ratio of the two fluxes.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 9.80665
RHO_F = 1000.0            # kg/m^3, fresh water
RHO_S = 1025.0            # kg/m^3, seawater
SEC_PER_YR = 3.15576e7
T_TIDE_H = 12.42          # h, principal lunar semidiurnal period
OMEGA_TIDE = 2.0 * np.pi / (T_TIDE_H * 3600.0)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def gh_factor(rho_f=RHO_F, rho_s=RHO_S):
    """Interface depth per unit of water-table head above sea level."""
    return rho_f / (rho_s - rho_f)


def lens_head(x, L, w, K, dRho=None, rho_s=RHO_S):
    """Dupuit island-lens head above sea level, m, at position x from the centre."""
    dRho = (rho_s - RHO_F) if dRho is None else dRho
    a2 = w * dRho / (K * rho_s)
    return np.sqrt(np.maximum(a2 * (L ** 2 / 4.0 - x ** 2), 0.0))


def main():
    section("1. Ghyben-Herzberg and the island freshwater lens")
    f_gh = gh_factor()
    print(f"  densities (model): fresh {RHO_F:.0f}, seawater {RHO_S:.0f} "
          f"kg/m^3, drho = {RHO_S - RHO_F:.0f}")
    print(f"  Ghyben-Herzberg: z = [rho_f/(rho_s-rho_f)] h = {f_gh:.1f} h")
    print("  i.e. one metre of fresh head holds up forty metres of fresh water")
    print("  below sea level, which is why the interface is so sensitive to")
    print("  pumping and so easy to misjudge.")
    print("\n   head h (m)   interface depth z (m)   lens thickness h+z (m)")
    for h in (0.5, 1.0, 2.0, 5.0, 10.0):
        print(f"   {h:10.1f}   {f_gh * h:22.1f}   {h + f_gh * h:20.1f}")

    L, w, K = 5000.0, 0.5, 50.0
    w_s = w / SEC_PER_YR
    K_s = K / (24.0 * 3600.0)
    print(f"\n  model island: width {L / 1e3:.0f} km, recharge {w:.2f} m/yr, "
          f"K = {K:.0f} m/day")
    print(f"    recharge = {w_s:.3e} m/s, K = {K_s:.3e} m/s, "
          f"w drho/(K rho_s) = {w_s * (RHO_S - RHO_F) / (K_s * RHO_S):.3e} 1/m")
    h0 = lens_head(0.0, L, w_s, K_s)
    print(f"    analytic head at the centre: h(0) = {h0:.3f} m")
    print(f"    interface depth at the centre: {f_gh * h0:.1f} m; lens thickness "
          f"{h0 * (1 + f_gh):.1f} m = {RHO_S / (RHO_S - RHO_F):.2f} h(0)")
    print("\n   x (km)   h (m)   interface depth (m)")
    for x_km in (-2.5, -1.5, -0.5, 0.0, 0.5, 1.5, 2.5):
        hx = lens_head(x_km * 1e3, L, w_s, K_s)
        print(f"   {x_km:6.1f}   {hx:5.3f}   {f_gh * hx:19.1f}")

    # verification: check the analytic solution against the Boussinesq residual
    xg = np.linspace(-L / 2, L / 2, 2001)
    hg = lens_head(xg, L, w_s, K_s)
    b = RHO_S / (RHO_S - RHO_F) * hg
    q = -K_s * b * np.gradient(hg, xg)
    dqdx = np.gradient(q, xg)
    inner = (np.abs(xg) < 0.9 * L / 2) & (hg > 1e-6)
    res = np.max(np.abs(dqdx[inner] - w_s)) / w_s
    print(f"\n  verification: the analytic solution satisfies the steady Boussinesq")
    print(f"  equation dq/dx = w to a maximum relative residual of {res:.2e}")
    print(f"  (the residual is finite-difference error in np.gradient, not a")
    print(f"  modelling error).")

    # mass balance and residence time
    recharge = w * L                 # m^2/yr per metre of shoreline
    discharge = recharge             # all of it leaves as fresh SGD (steady state)
    volume = RHO_S / (RHO_S - RHO_F) * np.trapezoid(hg, xg)
    print(f"\n  mass balance: recharge over the {L / 1e3:.0f} km width = "
          f"{recharge:.0f} m^2/yr,")
    print(f"  i.e. {discharge:.0f} m^3/yr per metre of shoreline (steady state:"
          f" all of it")
    print("  discharges as fresh submarine groundwater)")
    print(f"  fresh lens volume = {volume:.0f} m^3 per metre of shoreline")
    print(f"  residence time = volume / recharge = {volume / recharge:.0f} yr")
    print("  a centennial residence time is typical of a small island lens, and it")
    print("  is the number that matters for contamination: a pollutant entering")
    print("  the lens today is still there in a century.")

    section("2. Pumping-induced upconing")
    z_interface, z_screen = 40.0, 20.0
    s_max = (z_interface - z_screen) / f_gh
    print(f"  interface at {z_interface:.0f} m, well screen at {z_screen:.0f} m")
    print(f"  the interface rises {f_gh:.1f} m for each metre of drawdown, so the")
    print(f"  drawdown that brings it to the screen is")
    print(f"    s_max = ({z_interface:.0f} - {z_screen:.0f}) / {f_gh:.1f} = "
          f"{s_max:.3f} m")
    T_aq = K_s * z_interface
    R_infl, r_well = 500.0, 0.2
    Q_max = 2.0 * np.pi * T_aq * s_max / np.log(R_infl / r_well)
    print(f"\n  transmissivity T = K b = {T_aq:.4f} m^2/s; Thiem equation")
    print(f"    s(r) = Q/(2 pi T) ln(R/r_w), ln({R_infl:.0f}/{r_well:.1f}) = "
          f"{np.log(R_infl / r_well):.3f}")
    print(f"    Q_max = 2 pi T s_max / ln(R/r_w) = {Q_max:.5f} m^3/s = "
          f"{Q_max * 86400:.0f} m^3/day")
    print("  a well in this lens can therefore pump only a few hundred cubic")
    print("  metres per day before it draws salt water to its screen, and the")
    print("  limit is set by the 40-fold amplification in the Ghyben-Herzberg")
    print("  relation, not by the aquifer's permeability.")
    print("  model limitation: the sharp-interface relation overestimates the")
    print("  rise because a real interface has a transition zone tens of metres")
    print("  thick and mixing slows the upconing; the model gives the order and")
    print("  the scaling, not the operational limit.")

    section("3. Salinity, conductivity and Archie")
    a_sigma, m_archie, n_archie, phi = 0.114, 1.8, 2.0, 0.35
    print(f"  model pore-fluid conductivity sigma_f = {a_sigma:.3f} S (g/kg)^-1")
    print(f"  Archie: rho_b = rho_f phi^(-m) S_w^(-n) with m = {m_archie:.1f}, "
          f"n = {n_archie:.1f}, phi = {phi:.2f}")
    print(f"  phi^(-m) = {phi ** -m_archie:.2f}")
    print("\n   S (g/kg)   sigma_f (S/m)   rho_f (ohm m)   rho_b (ohm m)")
    for S in (0.1, 1.0, 5.0, 10.0, 35.0):
        sf = a_sigma * S
        rf = 1.0 / sf
        print(f"   {S:8.1f}   {sf:13.3f}   {rf:14.2f}   {rf * phi ** -m_archie:14.2f}")
    rb_fresh = (1.0 / (a_sigma * 1.0)) * phi ** -m_archie
    rb_sea = (1.0 / (a_sigma * 35.0)) * phi ** -m_archie
    print(f"\n  contrast between a 1 g/kg and a 35 g/kg pore fluid: "
          f"{rb_fresh / rb_sea:.1f}x")
    print("  a factor of this size is what makes resistivity and EM methods the")
    print("  natural tool for the interface - and it is also what makes the")
    print("  inversion so sensitive to the assumptions: a clay-rich sediment has")
    print("  surface conduction that Archie's law ignores, so the true resistivity")
    print("  is lower than predicted and an Archie inversion overestimates the")
    print("  salinity.  Conductivity is not salinity.")
    for a_elec in (20.0, 40.0, 80.0):
        print(f"  electrode spacing {a_elec:5.0f} m -> median depth of")
        print(f"    investigation about {0.52 * a_elec:.0f} m and a minimum array")
        print(f"    length of 3a = {3 * a_elec:.0f} m")
    print("  (the 0.52 factor is a model value for a Wenner array; it is stated")
    print("   here so that the depth claim can be checked, not assumed.)")

    section("4. Fresh versus recirculated submarine discharge")
    S_stor = 0.2
    lam = np.sqrt(2.0 * T_aq / (S_stor * OMEGA_TIDE))
    print(f"  tidal pumping: the pore-pressure signal decays with the skin")
    print(f"  length lambda = sqrt(2T/(S omega)) with")
    print(f"    T = {T_aq:.4f} m^2/s, S = {S_stor:.2f}, omega = {OMEGA_TIDE:.3e} "
          f"rad/s")
    print(f"    lambda = {lam:.1f} m")
    amp, cycles = 1.0, 2.0 / 1.035
    exch = 2.0 * amp * lam * S_stor * cycles
    print(f"\n  exchange per metre of shoreline per day, for a {amp:.1f} m tidal")
    print(f"  amplitude over {cycles:.2f} tidal cycles:")
    print(f"    volume = 2 A lambda S x cycles = {exch:.1f} m^3/day per m")
    print(f"    = {exch * 365.25:.0f} m^3/yr per m of shoreline")
    print(f"  fresh discharge from the lens model = {discharge:.0f} m^3/yr per m")
    print(f"    ratio recirculated/fresh = {exch * 365.25 / discharge:.1f}")
    print("  the recirculated component is several times the fresh component, so a")
    print("  tracer-based SGD estimate measures both unless it separates them:")
    print("  salinity distinguishes fresh from seawater but not recent seawater")
    print("  from old, and a radium or radon budget must be interpreted with the")
    print("  same partition in mind.")

    section("5. Worked examples used in the lesson")
    print(f"(a) Ghyben-Herzberg factor = {f_gh:.1f}; a 2 m head holds the")
    print(f"    interface at {f_gh * 2:.0f} m below sea level")
    print(f"(b) lens head at the centre of a {L / 1e3:.0f} km island with "
          f"{w:.2f} m/yr recharge and K = {K:.0f} m/day: {h0:.3f} m, interface at")
    print(f"    {f_gh * h0:.1f} m, residence time {volume / recharge:.0f} yr")
    print(f"(c) upconing: s_max = {s_max:.3f} m gives Q_max = "
          f"{Q_max * 86400:.0f} m^3/day")
    print(f"(d) Archie contrast 1 to 35 g/kg: {rb_fresh / rb_sea:.1f}x "
          f"({rb_fresh:.2f} to {rb_sea:.2f} ohm m)")
    print(f"(e) tidal decay length {lam:.1f} m; recirculated discharge "
          f"{exch * 365.25 / discharge:.1f}x the fresh")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
