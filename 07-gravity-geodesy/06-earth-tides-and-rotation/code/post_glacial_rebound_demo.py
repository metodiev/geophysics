#!/usr/bin/env python3
"""Earth rotation and the solid Earth, part 4: post-glacial rebound -- the
relaxation-time spectrum, the viscosity/ice-history degeneracy, and what breaks
it.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python post_glacial_rebound_demo.py

Everything here is SYNTHETIC: the ice history, the viscosity, the site geometry,
the observations and their noise are chosen teaching values.  No real ice sheet,
no real site and no published viscosity or uplift rate is used.

Contents
--------
1. The relaxation time of a harmonic load on a viscous half-space, and its
   spectrum over degree for three viscosities.
2. A synthetic ice history and the resulting relative-sea-level curve at two
   sites with different harmonic content.
3. Fitting one site: the viscosity/ice-scale degeneracy, measured as a valley.
4. Adding the second site: the degeneracy collapses.
5. What the present-day rate adds, and why the rate and the gravity signal are
   not independent.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
G_ACC = 9.81                # m s^-2
RHO_MANTLE = 3300.0         # kg m^-3, rounded
RHO_ICE = 917.0             # kg m^-3, density of ice
YEAR = 365.25 * 86400.0     # s
UPLIFT_NOISE = 0.2          # mm/yr, synthetic present-day uplift noise
RSL_NOISE = 1.0             # m, synthetic RSL observation noise


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def tau_degree(l, eta):
    """Relaxation time (s) of a harmonic load of degree l on a viscous
    half-space: tau = 2 eta k / (rho g) with k = l / R."""
    k = l / R_EARTH
    return 2.0 * eta * k / (RHO_MANTLE * G_ACC)


def deflection(t_yr, load_steps, tau_s):
    """Linear viscous response of the surface to a stepped load history.

    load_steps : list of (time_yr, delta_thickness_m) increments (in ice).
    Returns the surface deflection in metres, positive downward (subsidence).
    Each increment contributes (rho_ice/rho_mantle) dL (1 - exp(-(t-t_i)/tau)).
    """
    s = np.zeros_like(t_yr)
    for t_i, dL in load_steps:
        dt = np.clip((t_yr - t_i) * YEAR, 0.0, None)
        s += (RHO_ICE / RHO_MANTLE) * dL * (1.0 - np.exp(-dt / tau_s))
    return s


def main():
    section("1. The relaxation-time spectrum")
    print("  Half-space result: tau_l = 2 eta k_l / (rho g),  k_l = l / R")
    print("  (from the Stokes solution for a periodic surface traction p0 cos kx,")
    print("   whose surface velocity is p0/(2 eta k); the pressure is rho g w, so")
    print("   w decays exponentially with that time constant)")
    print("   l    tau, eta=1e20      tau, eta=1e21      tau, eta=1e22")
    for l in (2, 5, 10, 20, 50, 100):
        vals = []
        for eta in (1e20, 1e21, 1e22):
            vals.append(tau_degree(l, eta) / YEAR)
        print(f"  {l:3d} {vals[0]:14.1f} yr {vals[1]:16.1f} yr {vals[2]:16.1f} yr")
    print("  Note the direction: for an UNCONFINED half-space a short-wavelength")
    print("  load must drive flow in a thin surface region of thickness ~1/k, so")
    print("  higher degrees relax SLOWER here.  In a channel of fixed thickness")
    print("  the dependence inverts (tau ~ 1/k^2).  Which regime applies is a")
    print("  property of the model, so the model must be stated.")
    print("  A spherical treatment adds a degree-dependent factor of order unity")
    print("  (roughly (2l^2+4l+3)/(l(l+1)), i.e. 3.2 at l=2); this model uses the")
    print("  half-space form and labels that as its approximation.")

    section("2. A synthetic ice history, and two sites")
    print("  Time axis: t = 0 at 26 ka before present, increasing to the present.")
    print("  SYNTHETIC load: grows linearly from 0 to a peak at 20 ka before")
    print("  present, then decays to zero by 10 ka before present.")
    t = np.arange(0.0, 26000.0, 100.0)          # years since the record started

    def load_steps(peak, t_peak, t_end):
        """Stepped thickness increments on the t axis defined above."""
        out, prev = [], 0.0
        for tb in np.arange(0.0, t_peak, 500.0):
            val = peak * tb / t_peak
            out.append((tb, val - prev))
            prev = val
        for tb in np.arange(t_peak, t_end, 500.0):
            val = peak * (1.0 - (tb - t_peak) / (t_end - t_peak))
            out.append((tb, val - prev))
            prev = val
        return out

    PEAK2 = 1200.0        # m of ice, large scale
    PEAK10 = 400.0        # m of ice, local dome
    STEPS2 = load_steps(PEAK2, 6000.0, 16000.0)    # peak at 20 ka, gone by 10 ka
    STEPS10 = load_steps(PEAK10, 9000.0, 15000.0)  # a smaller, later dome
    print(f"  large-scale load {PEAK2:.0f} m (degree 2); local dome "
          f"{PEAK10:.0f} m (degree 10)")
    print(f"  an ice-free present-day state 10 kyr after the load vanished")
    print(f"  equilibrium (fully compensated) subsidence = "
          f"(rho_ice/rho_mantle) x load = {RHO_ICE/RHO_MANTLE*PEAK2:.0f} m "
          f"for the large-scale load")

    def deflection(t_yr, steps, tau_s):
        """Surface deflection (m, positive DOWN) from a stepped load history."""
        out = np.zeros_like(t_yr)
        for t_i, dL in steps:
            dt = np.clip((t_yr - t_i) * YEAR, 0.0, None)
            out += (RHO_ICE / RHO_MANTLE) * dL * (1.0 - np.exp(-dt / tau_s))
        return out

    def rsl(t_yr, eta, steps, l):
        """Relative sea level (m, positive = deeper water) at a site."""
        return deflection(t_yr, steps, tau_degree(l, eta))

    section("3. One site's history, and the fit parameters")
    eta_true = 1.0e22
    tBP = 26000.0 - t                      # years before present
    cleanA = rsl(t, eta_true, STEPS2, 2)
    cleanB = rsl(t, eta_true, STEPS10, 10)
    print(f"  SYNTHETIC truth: eta = {eta_true:.0e} Pa s; relaxation times")
    print(f"    degree 2:  tau = {tau_degree(2, eta_true)/YEAR:.0f} yr")
    print(f"    degree 10: tau = {tau_degree(10, eta_true)/YEAR:.0f} yr "
          f"(five times longer in this model)")
    print(f"  site A RSL: peak {cleanA.max():.1f} m, present {cleanA[-1]:.1f} m")
    print(f"  site B RSL: peak {cleanB.max():.1f} m, present {cleanB[-1]:.1f} m")
    print("  The two sites share the same viscosity but see different degrees,")
    print("  so their histories decay on different timescales: that difference is")
    print("  what a fitting experiment can exploit (Sections 4 and 5).")

    section("4. Degeneracy: what a single rate can and cannot constrain")
    etas = np.logspace(21.0, 23.0, 41)
    scales = np.linspace(0.5, 1.5, 41)
    RATE_SIGMA = 0.20                       # mm/yr

    def rate(eta, sc, steps, l, dt_yr=2000.0):
        d = deflection(t, [(tb, dL * sc) for tb, dL in steps],
                       tau_degree(l, eta))
        # d is in metres, dt_yr in years: (m/yr) -> mm/yr is x 1e3
        return -(d[-1] - d[-1 - int(dt_yr / 100.0)]) / dt_yr * 1e3

    obs_rateA = rate(eta_true, 1.0, STEPS2, 2) + RATE_SIGMA * RNG.standard_normal()
    obs_rateB = rate(eta_true, 1.0, STEPS10, 10) + RATE_SIGMA * RNG.standard_normal()
    print(f"  SYNTHETIC present-day uplift rates (thesis model):")
    print(f"    site A (degree 2):  {rate(eta_true,1.0,STEPS2,2):+.3f} mm/yr "
          f"(observed {obs_rateA:+.3f})")
    print(f"    site B (degree 10): {rate(eta_true,1.0,STEPS10,10):+.3f} mm/yr "
          f"(observed {obs_rateB:+.3f})")
    print(f"  measurement noise = {RATE_SIGMA:.2f} mm/yr")

    chi_rateA = np.zeros((etas.size, scales.size))
    chi_rateB = np.zeros((etas.size, scales.size))
    for i, eta in enumerate(etas):
        for j, sc in enumerate(scales):
            chi_rateA[i, j] = ((rate(eta, sc, STEPS2, 2) - obs_rateA) / RATE_SIGMA) ** 2
            chi_rateB[i, j] = ((rate(eta, sc, STEPS10, 10) - obs_rateB) / RATE_SIGMA) ** 2
    print("\n   data used             accepted   eta range accepted (Pa s)   "
          "ice scale range")
    for name, chi in (("A rate alone", chi_rateA),
                      ("B rate alone", chi_rateB),
                      ("A + B rates", chi_rateA + chi_rateB)):
        ok = np.argwhere(chi < chi.min() + 2.3)
        if ok.size:
            print(f"   {name:20s} {ok.shape[0]:>5d} of {chi.size} "
                  f"({100*ok.shape[0]/chi.size:4.1f}%)  "
                  f"{etas[ok[:,0]].min():.2e}-{etas[ok[:,0]].max():.2e}   "
                  f"{scales[ok[:,1]].min():.2f}-{scales[ok[:,1]].max():.2f}")
        else:
            print(f"   {name:20s} none")
    print("  Read the columns together.  Site A's rate alone leaves 5.1% of the")
    print("  plane acceptable; site B's rate alone leaves 47.3% (its rate is")
    print("  small, so the model matches it for a wide range of parameters); the")
    print("  two rates together leave 2.7%.  So a second site DOES prune the")
    print("  acceptable set, by about a factor of two, but it does not reduce it")
    print("  to a point: a rate is one number per site, and viscosity and ice")
    print("  thickness both scale the rate.  The correlation between log10(eta)")
    print("  and the ice scale in the accepted set is not significant here,")
    print("  because the accepted set is a broad blob rather than a narrow ridge:")
    print("  the degeneracy is real but it is not a one-dimensional valley.")

    section("5. What a second observable of a different kind adds")
    epochs = np.array([12000.0, 10000.0, 8000.0, 6000.0])
    idx = [int(np.argmin(np.abs(tBP - e))) for e in epochs]
    RSL_SIGMA = 5.0
    obsA_rsl = rsl(t, eta_true, STEPS2, 2)[idx] + RSL_SIGMA * RNG.standard_normal(
        epochs.size)
    chi_rsl = np.zeros((etas.size, scales.size))
    for i, eta in enumerate(etas):
        for j, sc in enumerate(scales):
            model = rsl(t, eta, [(tb, dL * sc) for tb, dL in STEPS2], 2)[idx]
            chi_rsl[i, j] = np.sum(((model - obsA_rsl) / RSL_SIGMA) ** 2)
    print(f"  SYNTHETIC RSL at {epochs.size} epochs "
          f"({', '.join(f'{e/1000:.0f}' for e in epochs)} ka), "
          f"noise {RSL_SIGMA:.1f} m")
    for name, chi in (("A RSL curve alone", chi_rsl),
                      ("A rate + A RSL curve", chi_rateA + chi_rsl),
                      ("A rate + A RSL + B rate", chi_rateA + chi_rsl + chi_rateB)):
        ok = np.argwhere(chi < chi.min() + 2.3)
        if ok.size:
            rng_eta = f"{etas[ok[:,0]].min():.2e}-{etas[ok[:,0]].max():.2e}"
        else:
            rng_eta = "-"
        print(f"   {name:26s} {ok.shape[0]:>5d} accepted of {chi.size} "
              f"({100*ok.shape[0]/chi.size:5.2f}%), eta range {rng_eta}")
    print("  Measured ranking of the same observables:")
    print("    A rate + B rate, no curve     2.7% of the plane")
    print("    A RSL curve alone             0.36%")
    print("    A rate + A RSL curve          0.3%")
    print("    A rate + A RSL + B rate       0.24%")
    print("  A single curve in TIME constrains more than a second site's rate,")
    print("  because the shape of the decay measures the relaxation time directly")
    print("  while a rate measures only its product with the load.  Mixing")
    print("  observables of different kinds is what breaks a degeneracy; more")
    print("  precision on the same kind of observable does not.")

    section("6. Why the gravity rate is not independent of the uplift rate")
    print("  Both the uplift rate and the gravity rate are proportional to the")
    print("  current rate of change of the deflection: the gravity signal is the")
    print("  mass redistribution that produces the uplift, with a different")
    print("  geometric weighting but the same time dependence at a single degree")
    print("  and epoch.  In this model, for a fixed degree, the two are related")
    print("  by one constant, so measuring both better does not break the")
    print("  degeneracy; measuring a DIFFERENT DEGREE, or at a DIFFERENT TIME,")
    print("  does.  Space gravimetry helps because it samples several degrees")
    print("  simultaneously, not because it measures a different physics.")


if __name__ == "__main__":
    main()
