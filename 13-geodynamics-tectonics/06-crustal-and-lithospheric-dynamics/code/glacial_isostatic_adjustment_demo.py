#!/usr/bin/env python3
"""Glacial isostatic adjustment: the relaxation time of a harmonic load on a
viscous half-space, a synthetic ice history, present-day uplift, relative sea
level, and the (viscosity, ice history) trade-off that the uplift rate leaves.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python glacial_isostatic_adjustment_demo.py

Everything is SYNTHETIC: the ice history is a chosen two-step teaching history,
not a reconstructed ice sheet, and the viscosity is a uniform half-space value.
Every printed number is computed here.

Contents
--------
1. The relaxation of a harmonic surface load: the model, the algebra checked by
   residual, and the relaxation time for a range of viscosities and wavelengths.
2. A synthetic ice history and the resulting present-day uplift rate.
3. Relative sea level at two sites inside the same load.
4. The trade-off: which (viscosity, ice thickness) pairs give the same uplift.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


RHO_MANTLE = 3300.0     # kg/m^3, chosen teaching value
RHO_ICE = 917.0         # kg/m^3, standard density of ice
G_EARTH = 9.81          # m/s^2, standard acceleration of gravity
R_EARTH = 6371.0e3      # m, standard mean radius of the Earth
OCEAN_FRACTION = 0.71   # dimensionless, chosen teaching value for the ocean area
YR = 3.1557e7           # s, standard julian year


def relaxation_time(eta, lam):
    """tau = 4 pi eta / (rho g lambda) in seconds, for the model of Section 1."""
    return 4.0 * np.pi * eta / (RHO_MANTLE * G_EARTH * lam)


def demonstration_1():
    section("1. Relaxation of a harmonic surface load")
    lam = 200.0e3
    print("  Model: a viscous half-space of viscosity eta and density rho, with")
    print("  a surface deflection w(x, t) = w0(t) cos(k x) and no elastic layer.")
    print("  The flow is driven by the deflection, the restoring force is")
    print("  gravity, and the horizontal flow is confined to a depth of order")
    print("  1/k, which gives")
    print("     dw0/dt = -(rho g k / 2 eta) w0,   so   tau = 2 eta / (rho g k)")
    print("            = 4 pi eta / (rho g lambda).\n")
    eta = 1.0e21
    k = 2.0 * np.pi / lam
    A = 1j * RHO_MANTLE * G_EARTH * 1.0 / (2.0 * eta * k ** 2)
    B = -k * A

    def phi(z):
        return (A + B * z) * np.exp(k * z)

    def d4(z, eps=1e-4):
        return (phi(z + 2 * eps) - 4 * phi(z + eps) + 6 * phi(z) -
                4 * phi(z - eps) + phi(z - 2 * eps)) / eps ** 4

    zs = np.array([-1.0, -5.0, -20.0]) / k
    resid_bih = np.max(np.abs(d4(zs) - 2.0 * k ** 2 * m_second(zs, phi, k) +
                              k ** 4 * phi(zs)))
    print("  Algebra check: with the decaying solution phi(z) = (A + B z) exp(k z),")
    print("  B = -k A chosen so that the shear traction vanishes and A set by the")
    print("  normal traction sigma_zz(0) = -rho g w0:")
    print(f"    B + k A                       = {abs(B + k * A):.3e}")
    print(f"    residual of (D^2 - k^2)^2 phi = {resid_bih:.3e}")
    w0 = 1.0
    u_z0 = -RHO_MANTLE * G_EARTH * w0 / (2.0 * eta * k)
    print(f"    surface vertical velocity w(0) for w0 = 1 m, eta = {eta:.0e} Pa s,")
    print(f"    lambda = {lam / 1e3:.0f} km: {u_z0:.6e} m/s")
    print(f"    tau implied by w(0)/w0: {-1.0 / u_z0 / YR:.1f} yr")
    print(f"    tau from the closed form 4 pi eta/(rho g lambda): "
          f"{relaxation_time(eta, lam) / YR:.1f} yr")
    print("  (the two agree because the same algebra is evaluated twice; the")
    print("   residual above is the part that a numerical check can catch.)\n")
    print("   eta (Pa s)   lambda (km)   tau (yr)")
    for eta_i in (1.0e19, 1.0e20, 1.0e21, 1.0e22):
        for lam_i in (1000.0e3, 3000.0e3, 10000.0e3):
            print(f"   {eta_i:10.1e}   {lam_i / 1e3:11.0f}   "
                  f"{relaxation_time(eta_i, lam_i) / YR:9.0f}")
    print("\n  tau is proportional to viscosity and inversely proportional to")
    print("  wavelength: short-wavelength loads relax fast, and the same")
    print("  observation made at two wavelengths in principle gives two")
    print("  constraints on the viscosity profile rather than one.")


def m_second(z, phi, k):
    """Second derivative of phi by second-order finite differences."""
    eps = 1e-5 / k
    return (phi(z + eps) - 2.0 * phi(z) + phi(z - eps)) / eps ** 2


def ice_history(t_yr):
    """Synthetic ice thickness in metres at time t (t = 0 is the present).

    -30 to -20 ka: linear growth to 2.0 km.
    -20 to -12 ka: full thickness.
    -12 to -10 ka: linear removal.
    after -10 ka: ice free.
    Accepts a scalar or an array.
    """
    t = np.atleast_1d(np.asarray(t_yr, dtype=float)) / 1.0e3
    h = np.zeros_like(t)
    g = (t > -30.0) & (t <= -20.0)
    h[g] = 2.0e3 * (t[g] + 30.0) / 10.0
    f = (t > -20.0) & (t <= -12.0)
    h[f] = 2.0e3
    r = (t > -12.0) & (t <= -10.0)
    h[r] = 2.0e3 * (-(t[r] + 10.0)) / 2.0
    h[h < 0.0] = 0.0
    return h if np.ndim(t_yr) else float(h[0])


def integrate(eta, lam, h_max_scale=1.0, t_end_yr=0.0, dt_yr=50.0):
    """Integrate dw/dt = (w_eq(t) - w)/tau from -40 ka to t_end.

    w_eq = (rho_ice/rho_mantle) h_ice is the isostatic deflection the current
    load would produce.  Returns the deflection history and the time axis.
    """
    tau = relaxation_time(eta, lam)
    ratio = RHO_ICE / RHO_MANTLE
    ts = np.arange(-40.0e3, t_end_yr + dt_yr, dt_yr)
    w = np.zeros_like(ts)
    for i in range(1, ts.size):
        h = (ice_history(ts[i - 1]) + ice_history(ts[i])) / 2.0 * h_max_scale
        w_eq = ratio * h
        w[i] = w[i - 1] + dt_yr * (w_eq - w[i - 1]) / (tau / YR)
    return ts, w


def demonstration_2():
    section("2. A synthetic ice history and the present-day uplift rate")
    print("  synthetic ice thickness (chosen, not reconstructed):")
    for t in (-30.0, -25.0, -20.0, -15.0, -12.0, -11.0, -10.0, -5.0, 0.0):
        print(f"    {t:6.0f} ka   h_ice = {ice_history(t * 1e3):7.0f} m")
    w_eq = RHO_ICE / RHO_MANTLE * 2.0e3
    print(f"\n  isostatic deflection of a 2.0 km load: (rho_i/rho_m) h = "
          f"{w_eq:.1f} m")
    print("  (the ratio is the Airy value for a load on a fluid half-space)")
    print("\n   eta (Pa s)   lambda (km)   tau (yr)   w(0) (m)   uplift at present")
    for eta in (1.0e20, 3.0e20, 1.0e21, 3.0e21, 1.0e22, 3.0e22):
        for lam in (3000.0e3,):
            ts, w = integrate(eta, lam)
            rate = -(w[-1] - w[-2]) / (ts[-1] - ts[-2])     # m per year, up
            print(f"   {eta:10.1e}   {lam / 1e3:11.0f}   "
                  f"{relaxation_time(eta, lam) / YR:9.0f}   {w[-1]:9.1f}   "
                  f"{rate * 1e3:12.3f} mm/yr")
    print("\n   wavelength (km)   tau (yr)    w(0) (m)   uplift at present")
    eta = 1.0e21
    for lam in (1000.0e3, 2000.0e3, 3000.0e3, 6000.0e3):
        ts, w = integrate(eta, lam)
        rate = -(w[-1] - w[-2]) / (ts[-1] - ts[-2])
        print(f"   {lam / 1e3:15.0f}   {relaxation_time(eta, lam) / YR:8.0f}   "
              f"{w[-1]:9.1f}   {rate * 1e3:12.3f} mm/yr")
    print("\n  the present-day uplift is the leftover deflection divided by the")
    print("  relaxation time, so it is largest for the intermediate viscosity: a")
    print("  very low viscosity has already finished relaxing by now, and a very")
    print("  high viscosity has barely started.  That non-monotonic dependence is")
    print("  the reason a single uplift rate is a poor constraint on viscosity.")


def demonstration_3():
    section("3. Relative sea level at two sites under the same load")
    print("  A site at the centre of the load sees the full deflection; a site")
    print("  where cos(k x) = 0.5 sees half of it.  Relative sea level at a site")
    print("  is the eustatic change (from the global ice volume) minus the local")
    print("  solid-surface displacement (uplift lowers relative sea level).\n")
    area_ocean = OCEAN_FRACTION * 4.0 * np.pi * R_EARTH ** 2
    lam, eta = 3000.0e3, 1.0e21
    ts, w = integrate(eta, lam, dt_yr=50.0)
    print(f"  ocean area (0.71 of the sphere, R = {R_EARTH / 1e3:.0f} km) = "
          f"{area_ocean:.4e} m^2")
    print(f"  the ice sheet is taken as 1e6 km^2 in area\n")
    for fac, label in ((1.0, "load centre, cos(kx) = 1.0"),
                       (0.5, "flank, cos(kx) = 0.5")):
        print(f"  {label}")
        print("    t (ka)   h_ice (m)   eustatic (m)   deflection (m)   RSL (m)")
        for t_ka in (-30.0, -20.0, -12.0, -10.0, -5.0, 0.0):
            i = int(np.argmin(np.abs(ts - t_ka * 1e3)))
            dV = ice_history(ts[i]) * 1.0e6 * 1.0e3
            eust = -dV / area_ocean
            print(f"    {t_ka:6.0f}   {ice_history(ts[i]):10.0f}   {eust:12.2f}   "
                  f"{fac * w[i]:14.1f}   {(eust - fac * w[i]):8.1f}")
        rsl = -(ice_history(ts) * 1.0e6 * 1.0e3) / area_ocean - fac * w
        rate = -(rsl[-1] - rsl[-2]) / (ts[-1] - ts[-2])
        print(f"    present relative sea-level rate: {rate * 1e3:.3f} mm/yr\n")
    print("  The eustatic term never exceeds a few metres for this ice area,")
    print("  while the solid-surface term reaches hundreds of metres: near a")
    print("  former ice sheet the record is dominated by the local deflection,")
    print("  and two sites on the same coastline record different histories of")
    print("  the same global ice volume.  A sea-level record is therefore not a")
    print("  proxy for ice volume unless the solid-Earth response is modelled.")


def demonstration_4():
    section("4. One uplift rate, many (viscosity, ice) pairs")
    print("  Target: a present-day uplift rate of 10.0 mm/yr.  For each viscosity")
    print("  the required ice-sheet scale factors (relative to the 2 km history of")
    print("  Section 2) are found by bisection; a scale of 6.0 means the search")
    print("  bound was reached and the target cannot be met at all.\n")
    lam = 3000.0e3
    target = 10.0e-3
    print("   eta (Pa s)   tau (yr)   required ice scale   peak ice (km)")
    for eta in (1.0e20, 3.0e20, 6.0e20, 1.0e21, 2.0e21, 5.0e21, 1.0e22):
        lo, hi = 0.05, 6.0
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            ts, w = integrate(eta, lam, h_max_scale=mid, dt_yr=100.0)
            rate = -(w[-1] - w[-2]) / (ts[-1] - ts[-2])
            if rate < target:
                lo = mid
            else:
                hi = mid
        scale = 0.5 * (lo + hi)
        note = "  (search bound: target unreachable)" if scale > 5.9 else ""
        print(f"   {eta:10.1e}   {relaxation_time(eta, lam) / YR:8.0f}   "
              f"{scale:18.3f}   {scale * 2.0:15.2f}{note}")
    print("\n  The required ice thickness is not monotonic in viscosity: it falls")
    print("  from 1.0e21 to about 2.0e21 Pa s and rises again, because the")
    print("  present-day rate is the leftover deflection divided by tau and both")
    print("  factors depend on viscosity in opposite directions.  Two mechanisms")
    print("  therefore fit the same uplift rate: a thinner ice sheet on a")
    print("  lower-viscosity mantle, or a thicker one on a higher-viscosity")
    print("  mantle.  For viscosities below about 1e21 Pa s the target rate cannot")
    print("  be reached at all with a plausible load, which is a real constraint")
    print("  and not a degeneracy.")
    print()
    print("  What breaks the ambiguity is a second observable whose wavelength")
    print("  dependence differs from the uplift's -- the gravity field, the")
    print("  present-day geoid, or the sea-level history at several sites.  It is")
    print("  not broken by measuring the same uplift rate more accurately: the")
    print("  trade-off is between the parameters, not between the noise.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
