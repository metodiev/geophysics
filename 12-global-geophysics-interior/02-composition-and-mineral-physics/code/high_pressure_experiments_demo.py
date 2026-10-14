#!/usr/bin/env python3
"""High-pressure experiments and diamond anvil cells: how a pressure is made,
how it is measured, and what an equation-of-state fit can and cannot deliver.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python high_pressure_experiments_demo.py

Everything is SYNTHETIC.  Loads, culet sizes, calibration constants, volumes and
elastic parameters are chosen teaching values.  No laboratory measurement, sample or
calibration is reproduced, and the ruby scale used here is a SYNTHETIC linear scale
with a chosen sensitivity, not the published one.

Contents
--------
1. Pressure from force and area: what a diamond anvil cell can reach and why the
   real limit is lower.
2. A synthetic pressure scale, its precision, and the dependence of that precision
   on the pressure.
3. The third-order Birch-Murnaghan equation of state: synthetic data, a least-squares
   fit, the parameter uncertainties and the K0-K0' trade-off.
4. Truncating the pressure range: the systematic error it produces.
5. Thermal pressure: what heating does to the measured compression.
6. What the experiment measures and what the model supplies.
"""

import numpy as np
from scipy.optimize import curve_fit

RNG = np.random.default_rng(20261014)

V0_TRUE, K0_TRUE, K0P_TRUE = 40.00, 160.0, 4.10   # A^3, GPa, dimensionless
# SYNTHETIC pressure-scale calibration: P = (dlambda/lambda0) / SCALE
SCALE = 5.26e-4            # fractional wavelength shift per GPa (chosen)
LAMBDA0 = 694.0            # nm, the reference wavelength of the synthetic scale
DLAMBDA_RES = 0.05         # nm, the resolution of the wavelength measurement


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def birch_murnaghan_p(v, v0, k0, k0p):
    """Third-order Birch-Murnaghan pressure in GPa for a volume in A^3."""
    x = (v0 / v) ** (2.0 / 3.0)
    return 1.5 * k0 * (x ** 3.5 - x ** 2.5) * (1.0 + 0.75 * (k0p - 4.0) * (x - 1.0))


def birch_murnaghan_p_f(v, v0, k0, k0p):
    """The same third-order EOS written with the Eulerian strain f.

    P = 3 K0 f (1 + 2f)^{5/2} [1 + 3/2 (K0' - 4) f],
    f = [(V0/V)^{2/3} - 1]/2.  Algebraically identical to the (V0/V) form used
    above; the two are compared in the validation below.
    """
    f = 0.5 * ((v0 / v) ** (2.0 / 3.0) - 1.0)
    return 3.0 * k0 * f * (1.0 + 2.0 * f) ** 2.5 * (1.0 + 1.5 * (k0p - 4.0) * f)


def main():
    section("0. Validation of the equation of state against its second form")
    v_test = np.linspace(V0_TRUE * 0.5, V0_TRUE, 500)
    p_a = birch_murnaghan_p(v_test, V0_TRUE, K0_TRUE, K0P_TRUE)
    p_b = birch_murnaghan_p_f(v_test, V0_TRUE, K0_TRUE, K0P_TRUE)
    print("  the two standard forms of the third-order Birch-Murnaghan EOS")
    print("  (the Eulerian strain form and the (V0/V) form) are both integrated:")
    print(f"    maximum absolute difference over {v_test.size} volumes from")
    print(f"    V/V0 = 0.5 to 1.0: {np.max(np.abs(p_a - p_b)):.3e} GPa")
    print(f"    maximum at the most compressed volume (P = {p_a.max():.1f} GPa)")
    print("  agreement at the rounding level means the two expressions are the")
    print("  same function, so a fitted K0 cannot be blamed on the algebraic form.")

    section("1. Pressure from force and area")
    print("  the idealised estimate is P = F/A, with A the culet area.")
    print("    culet (um)   area (m^2)      P at 500 N (GPa)")
    for culet_um in (1000, 500, 300, 200, 100, 50):
        a = np.pi * (culet_um * 1e-6 / 2.0) ** 2
        p = 500.0 / a / 1e9
        print(f"  {culet_um:11.0f}   {a:.3e}   {p:16.1f}")
    print("  the estimate says a 50 um culet reaches hundreds of GPa at a load a")
    print("  human arm can produce.  Three reasons the real limit is lower:")
    print("    * the pressure is not uniform: it concentrates on the culet edges,")
    print("      so the sample sees a gradient of 10-50 % across a few tens of um;")
    print("    * the diamond itself yields or fractures, setting a ceiling that")
    print("      depends on the anvil geometry rather than on the load;")
    print("    * the gasket deforms, so the loaded area is not the culet area.")
    print("  A quoted sample pressure is therefore an average over a gradient, and")
    print("  the gradient is the largest single uncertainty in the experiment.")

    section("2. A synthetic pressure scale and its precision")
    print(f"  SYNTHETIC scale: P = (dlambda/lambda0)/{SCALE:.2e} per GPa, with")
    print(f"  lambda0 = {LAMBDA0:.1f} nm and a wavelength resolution of "
          f"{DLAMBDA_RES:.2f} nm.")
    dp = (DLAMBDA_RES / LAMBDA0) / SCALE
    print(f"  the corresponding pressure resolution is {dp:.4f} GPa, independent")
    print("  of the pressure itself.  As a relative error:")
    print("    pressure (GPa)   relative error (%)")
    for p in (1.0, 5.0, 20.0, 100.0, 200.0):
        print(f"  {p:14.1f}   {100.0 * dp / p:18.2f}")
    print("  the scale is precise in absolute terms and coarse at low pressure:")
    print("  a 1 GPa measurement carries 14 % of pressure uncertainty (plus whatever")
    print("  the calibration slope itself is uncertain by), while a 200 GPa")
    print("  measurement carries 0.07 %.  The calibration slope, not the")
    print("  wavelength resolution, dominates the systematic error, and it is a")
    print("  *chosen* number in this demonstration.")

    section("3. Birch-Murnaghan: synthetic data and a least-squares fit")
    print(f"  SYNTHETIC truth: V0 = {V0_TRUE:.2f} A^3, K0 = {K0_TRUE:.1f} GPa, "
          f"K0' = {K0P_TRUE:.2f}")
    pressures = np.linspace(0.0, 120.0, 30)
    v_obs = []
    for p in pressures:
        lo, hi = V0_TRUE * 0.4, V0_TRUE * 1.001
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if birch_murnaghan_p(mid, V0_TRUE, K0_TRUE, K0P_TRUE) < p:
                hi = mid
            else:
                lo = mid
        v_obs.append(0.5 * (lo + hi))
    v_obs = np.array(v_obs) * (1.0 + RNG.normal(0.0, 0.002, pressures.size))
    p_obs = pressures * (1.0 + RNG.normal(0.0, 0.005, pressures.size))
    sigma = 0.005 * pressures + 0.05
    print(f"  data: {pressures.size} points to {pressures.max():.0f} GPa, with")
    print("  volume noise 0.2 % and pressure noise 0.5 % (independent, Gaussian)")
    popt, pcov = curve_fit(birch_murnaghan_p, v_obs, p_obs,
                           p0=[V0_TRUE, 140.0, 4.0], sigma=sigma)
    err = np.sqrt(np.diag(pcov))
    corr = pcov[1, 2] / np.sqrt(pcov[1, 1] * pcov[2, 2])
    print("    parameter     true        fitted      1 sigma     error (%)")
    for name, t, f, e in (("V0 (A^3)", V0_TRUE, popt[0], err[0]),
                          ("K0 (GPa)", K0_TRUE, popt[1], err[1]),
                          ("K0'", K0P_TRUE, popt[2], err[2])):
        print(f"    {name:12s} {t:10.3f}  {f:11.3f}  {e:10.3f}  "
              f"{100 * abs(f - t) / t:9.3f}")
    print(f"    correlation between K0 and K0': {corr:+.4f}")
    print("  a correlation near -1 is the signature of the trade-off: K0 and K0'")
    print("  are not separately determined by the data, only a combination of")
    print("  them.  The uncertainties above are the *formal* ones from the fit and")
    print("  are always smaller than the systematic error of the pressure scale.")

    section("4. Truncating the pressure range")
    print("  refitting with V0 fixed at its measured value (the usual practice)")
    print("  and using only the points below a stated maximum pressure:")

    def eos_fixed_v0(v, k0, k0p):
        return birch_murnaghan_p(v, V0_TRUE, k0, k0p)

    print("    P_max (GPa)   points   K0 (GPa)   1 sigma   K0'     1 sigma")
    for p_max in (20.0, 30.0, 40.0, 60.0, 90.0, 120.0):
        m = pressures <= p_max
        popt2, pcov2 = curve_fit(eos_fixed_v0, v_obs[m], p_obs[m],
                                 p0=[150.0, 4.0], sigma=sigma[m])
        e2 = np.sqrt(np.diag(pcov2))
        print(f"  {p_max:12.0f}   {int(m.sum()):6d}   {popt2[0]:10.2f}   "
              f"{e2[0]:8.2f}   {popt2[1]:5.2f}   {e2[1]:7.3f}")
    print(f"  the true values are K0 = {K0_TRUE:.1f} GPa and K0' = {K0P_TRUE:.2f}.")
    print("  Restricted to the low-pressure part, the fit cannot separate")
    print("  compression from curvature: K0' collapses, K0 absorbs the difference,")
    print("  and BOTH uncertainties grow by an order of magnitude even though the")
    print("  misfit stays small.  This is why reported K0 values are only")
    print("  comparable when the pressure range and the fitted K0' are quoted")
    print("  alongside; a 'K0' without a range is a statement about an experiment,")
    print("  not about a mineral.")

    section("5. Thermal pressure")
    alpha = 3.0e-5          # K^-1, chosen thermal expansion
    k_t = 130.0e9           # Pa, chosen isothermal bulk modulus
    print(f"  with alpha = {alpha:.1e} K^-1 and K_T = {k_t / 1e9:.0f} GPa, the")
    print("  thermal pressure at constant volume is P_th ~ alpha K_T dT:")
    print("    dT (K)    P_th (GPa)   equivalent compression (km of mantle)")
    for dt in (500.0, 1000.0, 1500.0, 2000.0):
        p_th = alpha * k_t * dt / 1e9
        print(f"  {dt:9.0f}   {p_th:10.2f}   {p_th / 0.033:26.1f}")
    print("  heating a sample by 1500 K adds several GPa of internal pressure:")
    print("  an experiment that compares a hot volume with a cold equation of state")
    print("  without removing P_th will report a bulk modulus that is too small.")
    print("  Equivalently, laser-heated experiments trade a pressure uncertainty")
    print("  for a temperature uncertainty, and the temperature is usually the")
    print("  larger of the two.")

    section("6. What the experiment measures and what the model supplies")
    print("    quantity                     measured or modelled?")
    print("    unit-cell volume V           measured (diffraction), 0.1-0.3 %")
    print("    pressure P                   measured through a CALIBRATION")
    print("    temperature T                measured, often to 10 % at 2000 K")
    print("    V0, K0, K0'                  fitted parameters of an assumed EOS")
    print("    thermal pressure P_th        modelled (alpha, K_T, their dT dependence)")
    print("    the sample's composition      assumed, not measured in situ")
    print("  the equation of state is the model that connects them, and it is")
    print("  assumed rather than tested: the fit tells you the parameters of that")
    print("  model, not whether the model is right.  Fitting a different EOS form")
    print("  to the same data would give different K0 and K0' with the same misfit.")


if __name__ == "__main__":
    main()
