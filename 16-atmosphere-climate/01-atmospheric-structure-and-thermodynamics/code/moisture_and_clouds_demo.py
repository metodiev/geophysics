#!/usr/bin/env python3
"""Moisture, humidity variables, the saturated (moist) adiabat and cloud
formation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moisture_and_clouds_demo.py

All models are SYNTHETIC teaching models.  The Clausius-Clapeyron reference
state, the latent heat and the gas constants are standard constants, listed
below; the surface state, the relative humidity and the environmental lapse rate
are chosen inputs, printed below.  No quantity here is a measurement made by this
module.

Contents
--------
1. Saturation vapour pressure from Clausius-Clapeyron, and its ~7%/K sensitivity.
2. Conversion table between the humidity variables w, q, e, RH, dewpoint.
3. Lifting condensation level: exact root-finding versus the 125 m/K rule.
4. The saturated adiabatic lapse rate versus temperature, and the dry limit.
5. An integrated moist adiabat: theta conservation below the LCL, why moist
   static energy is NOT exactly conserved, and the energy identity that locates
   the approximation inside the standard moist-lapse-rate formula.
6. Convective available potential energy, and its sensitivity to surface
   relative humidity.
7. Latent heat released by a given condensation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_D = 287.041          # J kg^-1 K^-1, dry-air gas constant (derived in lesson 01)
R_V = 461.5            # J kg^-1 K^-1, water-vapour gas constant = R*/M_w
CP = 1004.64           # J kg^-1 K^-1, dry-air specific heat (lesson 01)
G0 = 9.80665           # m s^-2, standard gravity
EPS = R_D / R_V        # 0.622, ratio of gas constants
L_V = 2.501e6          # J kg^-1, latent heat of vaporisation at 0 degC
E_S0 = 611.2           # Pa, saturation vapour pressure at 273.15 K (reference state)
T0C = 273.15           # K
P_REF = 100000.0       # Pa, potential-temperature reference

# --- SYNTHETIC surface state and environment (chosen inputs) ----------------
T_SURF = 288.15        # K
P_SURF = 101325.0      # Pa
RH_SURF = 0.80         # dimensionless, illustrative surface relative humidity
GAMMA_ENV = 6.5e-3     # K m^-1, environmental lapse rate
Z_TROP = 11000.0       # m, the environment is isothermal above this (model choice)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def e_sat(T):
    """Saturation vapour pressure over a plane water surface (Pa), Clausius-Clapeyron."""
    return E_S0 * np.exp(L_V / R_V * (1.0 / T0C - 1.0 / T))


def mixing_ratio(e, p):
    """Water-vapour mass mixing ratio w = eps e/(p-e), kg/kg."""
    return EPS * e / (p - e)


def vapour_pressure(w, p):
    """Invert the mixing-ratio definition: e = w p/(eps + w), Pa."""
    return w * p / (EPS + w)


def dewpoint(e):
    """Invert Clausius-Clapeyron for the temperature at which e is saturated (K)."""
    return 1.0 / (1.0 / T0C - (R_V / L_V) * np.log(e / E_S0))


def sat_mixing_ratio(T, p):
    return mixing_ratio(e_sat(T), p)


def env_T(z, gamma=GAMMA_ENV, T0=T_SURF):
    """Environment temperature (K); constant lapse to Z_TROP, isothermal above."""
    z = np.asarray(z, dtype=float)
    return np.where(z <= Z_TROP, T0 - gamma * z, T0 - gamma * Z_TROP)


def env_p(z, gamma=GAMMA_ENV, T0=T_SURF, p0=P_SURF):
    """Environment pressure (Pa); polytropic below Z_TROP, isothermal above."""
    z = np.asarray(z, dtype=float)
    p_trop = p0 * (1.0 - gamma * Z_TROP / T0) ** (G0 / (R_D * gamma))
    T_trop = T0 - gamma * Z_TROP
    below = p0 * (1.0 - gamma * np.minimum(z, Z_TROP) / T0) ** (G0 / (R_D * gamma))
    above = p_trop * np.exp(-np.maximum(z - Z_TROP, 0.0) * G0 / (R_D * T_trop))
    return np.where(z <= Z_TROP, below, above)


def gamma_moist(T, p):
    """Standard saturated adiabatic lapse rate (K/m): w_s ~ eps e_s/p."""
    ws = sat_mixing_ratio(T, p)
    A = L_V * ws / (R_D * T)
    B = L_V ** 2 * ws / (CP * R_V * T ** 2)
    return (G0 / CP) * (1.0 + A) / (1.0 + B)


def parcel_moist_dTdz(Tp, Te, p):
    """Exact saturated-parcel lapse rate (K/m) in an environment at (Te, p).

    Derived from c_p dT - (1/rho)dp = -L_v dw_s with the environment's pressure
    gradient dp/dz = -p g/(R_d Te) and w_s = eps e_s/(p - e_s).
    """
    ws = sat_mixing_ratio(Tp, p)
    num = Tp + L_V * ws / R_D
    den = CP + L_V ** 2 * ws / (R_V * Tp ** 2)
    return -(G0 / Te) * num / den


def moist_trajectory(theta_p, w, z_end, dz=1.0):
    """Lift a parcel through the model environment; return z, T, p, w arrays."""
    th = theta_p
    z, T, p, w_arr, saturated = [], [], [], [], []
    zz = 0.0
    sat = False
    while zz <= z_end:
        pe = float(env_p(zz))
        Te = float(env_T(zz))
        if not sat:
            Tp = th * (pe / P_REF) ** (R_D / CP)
            if sat_mixing_ratio(Tp, pe) <= w:
                sat = True
        else:
            # second-order step on dT/dz with the environment's pressure field
            k1 = parcel_moist_dTdz(Tp, Te, pe)
            Te_mid = float(env_T(zz + dz / 2))
            p_mid = float(env_p(zz + dz / 2))
            k2 = parcel_moist_dTdz(Tp + dz / 2 * k1, Te_mid, p_mid)
            Tp = Tp + dz * k2
        wp = min(w, sat_mixing_ratio(Tp, pe))
        z.append(zz)
        T.append(Tp)
        p.append(pe)
        w_arr.append(wp)
        saturated.append(sat)
        zz += dz
    return (np.array(z), np.array(T), np.array(p), np.array(w_arr),
            np.array(saturated, dtype=bool))


def main():
    section("1. Saturation vapour pressure and the Clausius-Clapeyron sensitivity")
    print(f"  e_s(T) = e_s0 exp[(L_v/R_v)(1/T0 - 1/T)],  e_s0 = {E_S0:.1f} Pa at "
          f"{T0C:.2f} K")
    print("   T (K)    T (C)     e_s (hPa)   de_s/dT (hPa/K)   (1/e_s)de_s/dT (%/K)")
    for T in (263.15, 273.15, 283.15, 288.15, 293.15, 303.15):
        es = e_sat(T)
        des = L_V * es / (R_V * T ** 2)
        print(f"  {T:7.2f}  {T - T0C:7.2f}   {es / 100:11.4f}   {des / 100:15.6f}   "
              f"{des / es * 100:16.3f}")
    print("  The relative sensitivity is the Clausius-Clapeyron result")
    print("  (1/e_s) de_s/dT = L_v/(R_v T^2): 6.5%/K at 288 K, falling slowly with")
    print("  temperature.  A 1 K warmer atmosphere holds about 6-7% more water")
    print("  vapour at saturation.  This is thermodynamics, not a model result.")

    section("2. The humidity variables at the surface, and their conversions")
    e = RH_SURF * e_sat(T_SURF)
    w = mixing_ratio(e, P_SURF)
    q = w / (1.0 + w)
    Td = dewpoint(e)
    print(f"  state: T = {T_SURF:.2f} K, p = {P_SURF:.1f} Pa, "
          f"RH = {RH_SURF * 100:.0f}%")
    print(f"    e_s = {e_sat(T_SURF):.2f} Pa")
    print(f"    vapour pressure   e  = RH e_s      = {e:.2f} Pa")
    print(f"    mixing ratio      w  = eps e/(p-e) = {w:.6f} kg/kg = "
          f"{w * 1e3:.3f} g/kg")
    print(f"    specific humidity q  = w/(1+w)     = {q:.6f} kg/kg")
    print(f"    dewpoint          Td = {Td:.3f} K = {Td - T0C:.2f} C")
    print(f"    dewpoint depression  = {T_SURF - Td:.3f} K")
    print(f"    mole fraction of water vapour = e/p = {e / P_SURF:.6f}")
    print(f"    Check: w - q = w^2/(1+w) = {w - q:.3e} = {w ** 2 / (1 + w):.3e}  OK")
    print(f"    Check: w from the vapour pressure = "
          f"{mixing_ratio(vapour_pressure(w, P_SURF), P_SURF):.6f} kg/kg  OK")

    section("3. Lifting condensation level: exact, and against the rule of thumb")
    theta_p = T_SURF * (P_REF / P_SURF) ** (R_D / CP)
    lo, hi = 0.0, 6000.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        Tp = theta_p * (float(env_p(mid)) / P_REF) ** (R_D / CP)
        if sat_mixing_ratio(Tp, float(env_p(mid))) > w:
            lo = mid
        else:
            hi = mid
    z_lcl = 0.5 * (lo + hi)
    T_lcl = theta_p * (float(env_p(z_lcl)) / P_REF) ** (R_D / CP)
    print(f"  parcel lifted dry-adiabatically (theta_p = {theta_p:.3f} K), "
          f"w = {w * 1e3:.3f} g/kg conserved")
    print(f"    LCL height       z_L  = {z_lcl:.1f} m")
    print(f"    LCL temperature  T_L  = {T_lcl:.3f} K = {T_lcl - T0C:.2f} C")
    print(f"    w_s there             = {sat_mixing_ratio(T_lcl, float(env_p(z_lcl))) * 1e3:.4f}"
          f" g/kg (equals w to the bisection tolerance)")
    print(f"    environment T at z_L  = {float(env_T(z_lcl)):.3f} K "
          f"-> parcel is {T_lcl - float(env_T(z_lcl)):+.3f} K relative to it")
    rule = 125.0 * (T_SURF - Td)
    print(f"\n  rule of thumb 125 m/K predicts {rule:.0f} m for a "
          f"{T_SURF - Td:.2f} K depression; exact minus rule = "
          f"{z_lcl - rule:+.1f} m ({(z_lcl - rule) / z_lcl * 100:+.2f}%)")
    print("  The rule is a linearisation; it is a useful forecaster's number, not")
    print("  a physical law, and its error grows with the dewpoint depression.")

    section("4. The saturated adiabatic lapse rate")
    print("  Gamma_m = (g/c_p)[1 + L_v w_s/(R_d T)] / [1 + L_v^2 w_s/(c_p R_v T^2)]")
    print("   T (K)    p (hPa)   w_s (g/kg)   Gamma_m (K/km)   Gamma_d (K/km)   ratio")
    for T, p in ((303.15, 101325.0), (293.15, 101325.0), (288.15, 101325.0),
                 (283.15, 90000.0), (273.15, 80000.0), (253.15, 60000.0),
                 (233.15, 40000.0)):
        gm = gamma_moist(T, p)
        print(f"  {T:7.2f}  {p / 100:8.0f}   {sat_mixing_ratio(T, p) * 1e3:11.3f}   "
              f"{gm * 1e3:15.4f}   {G0 / CP * 1e3:15.4f}   {gm / (G0 / CP):7.4f}")
    print("\n  Warm saturated air has a lapse rate near 4-5 K/km, roughly half the")
    print("  dry value; cold saturated air approaches the dry adiabat because w_s")
    print("  vanishes.  That limit is an independent check of the formula:")
    for T, p in ((213.15, 20000.0), (193.15, 10000.0)):
        ws = sat_mixing_ratio(T, p)
        print(f"    T = {T:.2f} K, p = {p / 100:.0f} hPa: w_s = {ws * 1e6:.4f} mg/kg, "
              f"Gamma_m/Gamma_d = {gamma_moist(T, p) / (G0 / CP):.6f}")

    section("5. An integrated moist adiabat, and what is really conserved")
    zz, TT, pp, ww, sat = moist_trajectory(theta_p, w, 12000.0, dz=1.0)
    h = CP * TT + G0 * zz + L_V * ww
    th_traj = TT * (P_REF / pp) ** (R_D / CP)
    i_lcl = int(np.argmax(sat))
    print("   z(km)      T(K)     p(hPa)   w(g/kg)   theta(K)   h = c_p T+g z+L_v w")
    print("                                                              (kJ/kg)")
    for target in (0, 1, 2, 3, 5, 8, 12):
        idx = int(np.argmin(np.abs(zz - target * 1000.0)))
        tag = "saturated" if sat[idx] else "dry      "
        print(f"  {zz[idx] / 1e3:6.1f}  {TT[idx]:8.3f}  {pp[idx] / 100:8.2f}  "
              f"{ww[idx] * 1e3:8.3f}  {th_traj[idx]:9.4f}  {h[idx] / 1e3:14.4f}"
              f"  {tag}")
    print(f"\n  (a) theta below the LCL (z < {zz[i_lcl]:.0f} m) is conserved:")
    print(f"      span over {i_lcl} levels = "
          f"{th_traj[:i_lcl].max() - th_traj[:i_lcl].min():.3e} K  <- machine precision")
    Te = env_T(zz)
    buoy = G0 * (TT - Te) / Te
    drift = h[-1] - h[0]
    minus_buoy = -np.trapezoid(buoy, zz)
    print(f"\n  (b) h = c_p T + g z + L_v w is NOT conserved here:")
    print(f"      drift of h over {zz[-1] / 1e3:.0f} km      = {drift:+.2f} J/kg")
    print(f"      -integral of buoyancy dz = {minus_buoy:+.2f} J/kg")
    print(f"      difference = {drift - minus_buoy:+.2f} J/kg "
          f"({(drift - minus_buoy) / minus_buoy * 100:+.2f}%), the quadrature error")
    print("      d(c_p T + g z + L_v w)/dz = g(1 - rho_e/rho_p) = -buoyancy, exactly,")
    print("      because the parcel is not at the environment's temperature and so")
    print("      gains or loses enthalpy through the imposed pressure field.  Moist")
    print("      static energy is conserved only to first order in the buoyancy;")
    print("      theta (equivalently entropy) is the exactly conserved quantity.")
    print("\n  (c) the first-law identity just above the LCL, per metre.")
    print("      (50 m above, not AT the LCL: the saturated and dry branches meet")
    print("      there with a kink, so a finite difference across it is meaningless.)")
    i_ev = i_lcl + 50
    zl, Tl, pl = zz[i_ev], TT[i_ev], pp[i_ev]
    Tel = float(env_T(zl))
    ws = sat_mixing_ratio(Tl, pl)
    dTdz = parcel_moist_dTdz(Tl, Tel, pl)
    lhs = CP * dTdz + (Tl / Tel) * G0
    dln_es_dz = (L_V / (R_V * Tl ** 2)) * dTdz
    dln_p_dz = -G0 / (R_D * Tel)
    dw_approx = ws * (dln_es_dz - dln_p_dz)
    dw_exact = (ww[i_ev + 1] - ww[i_ev - 1]) / (zz[i_ev + 1] - zz[i_ev - 1])
    print(f"    at z = {zl:.0f} m, T_p = {Tl:.3f} K, p = {pl / 100:.2f} hPa, "
          f"T_e = {Tel:.3f} K, w_s = {ws * 1e3:.3f} g/kg")
    print(f"      c_p dT/dz + (rho_e/rho_p) g              = {lhs:.6f} J/kg/m")
    print(f"      -L_v dw_s/dz with w_s ~ eps e_s/p         = {-L_V * dw_approx:.6f} "
          f"J/kg/m   residual {lhs + L_V * dw_approx:+.3e}")
    print(f"      -L_v dw_s/dz with w_s = eps e_s/(p-e_s)   = {-L_V * dw_exact:.6f} "
          f"J/kg/m   residual {lhs + L_V * dw_exact:+.4f}")
    print(f"      fractional residual = "
          f"{abs((lhs + L_V * dw_exact) / lhs):.5f}, close to e_s/p = "
          f"{e_sat(Tl) / pl:.5f}")
    print("    So Gamma_m is exact under its own approximation, and the residual is")
    print("    the size of that approximation.  Never quote a moist-adiabat energy")
    print("    budget to a precision finer than e_s/p, about 1% at the surface.")

    section("6. Convective available potential energy, and its moisture sensitivity")
    print("  environment: Gamma = "
          f"{GAMMA_ENV * 1e3:.1f} K/km up to {Z_TROP / 1e3:.0f} km, then isothermal")
    print("  RH     w (g/kg)   LCL (m)   LFC (m)   LNB (m)   CAPE (J/kg)  2 CAPE (m/s)")
    for rh in (0.60, 0.70, 0.80, 0.85, 0.90):
        e_rh = rh * e_sat(T_SURF)
        w_rh = mixing_ratio(e_rh, P_SURF)
        z2, T2, p2, w2, s2 = moist_trajectory(theta_p, w_rh, 14000.0, dz=1.0)
        T2e = env_T(z2)
        b2 = G0 * (T2 - T2e) / T2e
        j_lcl = int(np.argmax(s2))
        lfc2 = None
        for i in range(1, len(z2)):
            if b2[i] > 0.0 and b2[i - 1] <= 0.0:
                lfc2 = z2[i]
                break
        if lfc2 is None:
            print(f"  {rh:4.2f}   {w_rh * 1e3:8.2f}   {z2[j_lcl]:7.0f}         -"
                  f"         -             -             -")
            continue
        lnb2 = None
        for i in range(len(z2) - 1, 0, -1):
            if b2[i] > 0.0:
                lnb2 = z2[i]
                break
        sel = (z2 >= lfc2) & (z2 <= lnb2)
        cape = np.trapezoid(b2[sel], z2[sel])
        print(f"  {rh:4.2f}   {w_rh * 1e3:8.2f}   {z2[j_lcl]:7.0f}   {lfc2:7.0f}   "
              f"{lnb2:7.0f}   {cape:11.1f}   {np.sqrt(2 * cape):10.2f}")
    print("  Note what the table measures: nothing about the environment changed,")
    print("  yet a change of surface relative humidity from 0.70 to 0.90 turns a")
    print("  convectively dead sounding into one with hundreds of J/kg of CAPE.")
    print("  CAPE is controlled by the LOW-LEVEL MOISTURE, and that is why")
    print("  parameterising it from a model's humidity field is delicate.")
    print("  Every value here assumes no mixing, no drag and no loading by condensed")
    print("  water, so it is an UPPER BOUND on the buoyant energy a real updraught")
    print("  can use; the gap is the subject of convective parameterisation.")

    section("7. Latent heat released by condensation")
    for dw in (1.0e-3, 5.0e-3, 1.0e-2):
        print(f"  condensing {dw * 1e3:5.2f} g/kg releases {L_V * dw / 1e3:8.3f} kJ/kg")
    print(f"  Lifting 1 kg of air 1 km costs g x 1000 = {G0 * 1000 / 1e3:.2f} kJ/kg of")
    print("  potential energy, so one gram per kilogram of condensate pays for about")
    print(f"  {L_V * 1e-3 / (G0 * 1000):.2f} km of lift.  That is the quantitative reason")
    print("  moist convection reaches the tropopause while dry convection does not.")


if __name__ == "__main__":
    main()
