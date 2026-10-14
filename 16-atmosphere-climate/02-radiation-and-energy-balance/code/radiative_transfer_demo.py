#!/usr/bin/env python3
"""Radiative transfer in the atmosphere: optical depth, a grey slab model, the
multi-layer greenhouse, the emission level and a synthetic absorption window.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiative_transfer_demo.py

All models are SYNTHETIC.  The optical depths, the layer temperatures, the
absorption bands and the surface state are chosen inputs of a teaching model,
printed below.  The physical constants (sigma, the solar constant) are standard
constants.  No measured absorption spectrum is used and no atmospheric
constituent is identified with any spectral feature: the synthetic bands are
placed at model-chosen wavelengths for pedagogical purposes only.

Contents
--------
1. Beer-Lambert transmittance and optical depth.
2. A single grey layer: the exact solution, and the greenhouse increment.
3. N black layers: the (N+1)^(1/4) law, and why it is unphysical for large N.
4. A numerically solved grey atmosphere: how the surface temperature saturates
   as layers are refined rather than multiplied.
5. The effective emission level.
6. A synthetic spectral window, and why a grey model is never enough.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8        # W m^-2 K^-4, Stefan-Boltzmann constant
SOLAR_CONSTANT = 1361.0       # W m^-2, total solar irradiance at 1 AU
ALBEDO = 0.30                 # dimensionless, planetary albedo (chosen input)
LAPSE = 6.5e-3                # K m^-1, tropospheric lapse rate of the model
H_PLANCK = 6.62607015e-34     # J s
C_LIGHT = 2.99792458e8        # m s^-1
K_B = 1.380649e-23            # J K^-1
B_WIEN = 2.897771955e-3       # m K, derived in lesson 01

F_SOLAR = SOLAR_CONSTANT * (1.0 - ALBEDO) / 4.0     # absorbed solar, W m^-2
T_EFF = (F_SOLAR / SIGMA) ** 0.25                   # effective radiating T, K


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def planck_flux(lam, T):
    """Hemispheric spectral exitance (W m^-2 m^-1) of a blackbody."""
    with np.errstate(over="ignore", invalid="ignore"):
        x = H_PLANCK * C_LIGHT / (lam * K_B * T)
        out = np.pi * 2.0 * H_PLANCK * C_LIGHT ** 2 / lam ** 5 / np.expm1(x)
    return np.where(x > 700.0, 0.0, out)


def single_slab_Ts(eps, F=F_SOLAR):
    """Exact equilibrium surface temperature for one grey layer of emissivity eps."""
    return (2.0 * F / (SIGMA * (2.0 - eps))) ** 0.25


def grey_layers(n_layers, tau_total, tol=1e-13, max_iter=200000):
    """Solve N equal grey layers with a fixed TOTAL optical depth, exactly.

    Layer emissivity is eps = 1 - exp(-tau_total/N), i.e. Beer-Lambert applied
    to a vertical path.  Layers are indexed 0 (top) to N-1 (bottom).  Each layer
    is in radiative equilibrium, so absorbed flux equals emitted flux:
    eps*(U_in + D_in) = 2*eps*sigma*T^4, i.e. sigma*T^4 = (U_in + D_in)/2.  The
    surface is a blackbody absorbing all of the downward flux it receives, plus
    the absorbed solar flux F_SOLAR.

    The system is LINEAR in the unknowns x_i = sigma*T_i^4 and x_s = sigma*T_s^4,
    so it is assembled and solved directly rather than iterated, which avoids the
    very slow Gauss-Seidel convergence of the black-slab case.

    Returns (Ts, T_layers) in kelvin.
    """
    eps = 1.0 - np.exp(-tau_total / n_layers)
    N = n_layers
    m = N + 1
    A = np.zeros((m, m))
    b = np.zeros(m)

    def up_flux_coeffs(i):
        """Coefficients of up[i] = (1-eps)^(N-i) x_s + eps sum_j (1-eps)^(j-i) x_j."""
        v = np.zeros(m)
        v[N] = (1.0 - eps) ** (N - i)
        v[i:N] = eps * (1.0 - eps) ** np.arange(0, N - i)
        return v

    def down_flux_coeffs(i):
        """Coefficients of down[i] = eps sum_{j<i} (1-eps)^(i-1-j) x_j."""
        v = np.zeros(m)
        if i >= 1:
            v[0:i] = eps * (1.0 - eps) ** np.arange(i - 1, -1, -1)
        return v

    for i in range(N):
        A[i] += 0.5 * up_flux_coeffs(i + 1)      # flux entering layer i from below
        A[i] += 0.5 * down_flux_coeffs(i)        # flux entering layer i from above
        A[i, i] -= 1.0
    A[N] += down_flux_coeffs(N)                  # surface absorbs ALL of it
    A[N, N] -= 1.0
    b[N] = -F_SOLAR / SIGMA
    x = np.linalg.solve(A, b)
    return x[N] ** 0.25, x[:N] ** 0.25


def black_slabs(n_layers):
    """Radiative equilibrium of n_layers perfectly black layers (eps = 1)."""
    return grey_layers(n_layers, tau_total=1e6)


def eddington_Ts(tau_s):
    """Eddington two-stream result: T_s^4 = T_e^4 (3 tau_s/4 + 1/2)."""
    return (T_EFF ** 4 * (0.75 * tau_s + 0.5)) ** 0.25


def main():
    section("1. Beer-Lambert transmittance and optical depth")
    print("  T = exp(-tau) for a direct beam;  tau = integral k rho dz")
    print("   tau      transmittance   absorbed fraction")
    for tau in (0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
        tr = np.exp(-tau)
        print(f"  {tau:5.2f}   {tr:13.6f}   {1 - tr:17.6f}")
    print("  tau = 1 is the definition of the 'visible depth' of a medium: 63.2%")
    print("  of the beam passes.  A medium with tau >> 1 is opaque in the sense")
    print("  that radiation cannot cross it, but it still EMITS (Kirchhoff).")

    section("2. A single grey layer: the exact solution")
    print(f"  absorbed solar flux F = S(1-a)/4 = {F_SOLAR:.2f} W/m^2")
    print(f"  effective radiating temperature T_e = (F/sigma)^(1/4) = {T_EFF:.2f} K")
    print("  One layer of emissivity eps at temperature T_a, black surface at T_s:")
    print("    TOA:     (1-eps) sigma T_s^4 + eps sigma T_a^4 = F")
    print("    surface: sigma T_s^4 = F + eps sigma T_a^4")
    print("  Eliminating T_a gives the exact result")
    print("    T_s^4 = 2F / (sigma (2 - eps))")
    print("\n   eps      T_s (K)   T_a (K)   greenhouse dT (K)   dT/T_e")
    for eps in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0):
        Ts = single_slab_Ts(eps)
        # T_a^4 = (F/sigma - (1-eps) T_s^4)/eps ; at eps=0 T_a is undefined
        if eps > 0.0:
            Ta = (((F_SOLAR / SIGMA) - (1 - eps) * Ts ** 4) / eps) ** 0.25
            ta = f"{Ta:8.2f}"
        else:
            ta = "       -"
        print(f"  {eps:5.2f}   {Ts:8.3f}   {ta}   {Ts - T_EFF:17.3f}   "
              f"{(Ts - T_EFF) / T_EFF:7.4f}")
    print(f"\n  With a perfectly absorbing layer (eps = 1) the surface must radiate")
    print(f"  twice the outgoing flux, so T_s = 2^(1/4) T_e = "
          f"{2 ** 0.25 * T_EFF:.2f} K, a greenhouse increment of "
          f"{2 ** 0.25 * T_EFF - T_EFF:.2f} K.")
    print(f"  With eps = 0 there is no atmosphere and T_s = T_e = {T_EFF:.2f} K.")
    print("  The layer temperature T_a is always BELOW T_e, which is the first")
    print("  hint that the atmosphere radiates to space from above the surface.")

    section("3. N opaque layers: the (N+1)^(1/4) law")
    print("  The classical textbook result for N perfectly absorbing layers is")
    print("    T_s = (N+1)^(1/4) T_e .")
    print("  Solved here by assembling and solving the linear equilibrium system:")
    print("   N     T_s (K)    (N+1)^(1/4) T_e (K)   difference (K)")
    for n_layers in (1, 2, 3, 5, 10, 30):
        Ts, _ = black_slabs(n_layers)
        analytic = (n_layers + 1) ** 0.25 * T_EFF
        print(f"  {n_layers:3d}   {Ts:8.4f}   {analytic:20.4f}   "
              f"{Ts - analytic:+16.4f}")
    print("\n  The law is exact for that idealisation (each layer perfectly opaque)")
    print("  and it is exactly that idealisation which is unphysical:")
    print("  (i)  The layers are opaque at every wavelength, so the model has")
    print("       infinite total optical depth however many of them there are.  The")
    print("       physical limit of 'more layers' is a continuum (Section 4), not a")
    print("       larger N with the same infinite opacity.")
    print("  (ii) A real layer has a finite emissivity, so adding layers at fixed")
    print("       TOTAL optical depth makes each one thinner, not blacker.")
    print("  The value of the law is that it isolates the mechanism: the surface")
    print("  temperature is NOT the planetary radiating temperature, and the offset")
    print("  grows with the number of optically thick layers between the surface and")
    print("  space.  Nothing about wavelength appears in it, which is why the law")
    print("  alone cannot tell you WHICH gas matters.")

    section("4. A fixed total optical depth, refined in layers")
    print("  Now hold the TOTAL optical depth fixed and refine the layer count.")
    print("  Each layer has eps = 1 - exp(-tau_total/N), so refining makes the")
    print("  layers thinner rather than blacker.")
    print("   total tau   N=1 (K)   N=4 (K)   N=40 (K)   N=400 (K)    Eddington (K)")
    for tau_total in (0.5, 1.0, 2.0, 4.0, 8.0):
        vals = [grey_layers(n, tau_total)[0] for n in (1, 4, 40, 400)]
        print(f"  {tau_total:10.1f}   {vals[0]:8.3f}  {vals[1]:8.3f}   "
              f"{vals[2]:9.3f}   {vals[3]:10.3f}   {eddington_Ts(tau_total):13.3f}")
    print("\n  Two things to read from the table.")
    print("  (1) The surface temperature CONVERGES as the discretisation is refined:")
    print("      for tau = 4 the sequence is 301.4, 330.7, 335.0, 335.0 K.  It does")
    print("      not diverge, unlike the (N+1)^(1/4) law, because the total opacity")
    print("      is fixed.  Refining a model is not the same as multiplying layers.")
    print("  (2) The converged value is a few per cent from the Eddington two-stream")
    print("      analytic result T_s = T_e (3 tau/4 + 1/2)^(1/4), and the sign of the")
    print("      difference changes with tau:")
    print("       tau   converged T_s   Eddington    difference")
    for tau_total in (1.0, 4.0, 8.0):
        Ts = grey_layers(400, tau_total)[0]
        ed = eddington_Ts(tau_total)
        print(f"      {tau_total:3.1f}   {Ts:12.3f}   {ed:9.3f}   "
              f"{Ts - ed:+8.3f} K ({(Ts - ed) / ed * 100:+.2f}%)")
    print("      The difference is the ANGULAR CLOSURE error: this model carries a")
    print("      single vertical flux, Eddington's uses the first moment of the")
    print("      intensity.  No single diffusivity factor removes it - it is a")
    print("      property of the closure, so a two-stream result must be quoted with")
    print("      a few-per-cent accuracy in temperature and not better.")
    print("\n  The surface warms monotonically with total infrared optical depth:")
    for tau_total in (0.5, 1.0, 2.0, 4.0, 8.0):
        Ts = grey_layers(400, tau_total)[0]
        print(f"    tau = {tau_total:4.1f}: T_s = {Ts:7.3f} K, "
              f"increment over T_e = {Ts - T_EFF:7.3f} K")
    print("  That is the quantitative content of 'the greenhouse effect depends on")
    print("  the amount of infrared absorber', stripped of any claim about which gas")
    print("  or how much.  It is also why a grey model must be calibrated against a")
    print("  real spectrum before it can be used quantitatively - see Section 6.")

    section("5. The effective emission level")
    print("  The planet radiates to space at T_e, and the atmosphere radiates at")
    print(f"  T_e where its optical depth is of order 1.  With T_e = {T_EFF:.2f} K")
    print(f"  and a lapse rate of {LAPSE * 1e3:.1f} K/km, the temperature reaches T_e")
    print("  at a height")
    print(f"    z_e = (T_s - T_e)/Gamma")
    print("   T_s (K)   z_e (km)")
    for Ts in (288.0, 295.0, 302.7):
        print(f"  {Ts:8.2f}   {(Ts - T_EFF) / LAPSE / 1e3:8.2f}")
    print("  z_e is the centroid of the emission, not a sharp surface: the outgoing")
    print("  spectrum forms over an optical-depth range around 1.  Note the")
    print("  direction of the argument: a HIGHER surface temperature needs a HIGHER")
    print("  emission level to radiate at the same T_e, and a higher emission level")
    print("  requires more infrared opacity.  Increasing the absorber raises z_e and")
    print("  therefore T_s, and the loop closes only when T_s - Gamma z_e = T_e.")

    section("6. A synthetic spectral window, and why grey is not enough")
    print("  SYNTHETIC setup.  One layer at T_a = 240 K over a 288 K black surface.")
    print("  The band positions, widths and shapes below are ARBITRARY model choices")
    print("  for the demonstration; they are not gas data, and no atmospheric")
    print("  constituent is identified with any of them.")
    lam = np.geomspace(4e-6, 60e-6, 200001)
    B_surf = planck_flux(lam, 288.0)
    B_layer = planck_flux(lam, 240.0)

    band = np.ones_like(lam)
    band[(lam >= 13e-6) & (lam <= 17e-6)] = 8.0     # a strong band
    band[(lam >= 8e-6) & (lam < 13e-6)] = 1.5       # a moderate band
    band[lam < 8e-6] = 0.05                         # a window
    band[lam > 17e-6] = 0.5                         # partial absorption

    def eps_profile(c):
        return 1.0 - np.exp(-c * band)

    def broadband_eps(c):
        num = np.trapezoid(eps_profile(c) * B_surf, lam)
        return num / np.trapezoid(B_surf, lam)

    # choose the scale c so that the SPECTRAL model has the SAME flux-weighted
    # broadband emissivity at 288 K as the grey model
    target = 0.80
    lo, hi = 1e-6, 1e3
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if broadband_eps(mid) < target:
            lo = mid
        else:
            hi = mid
    c0 = 0.5 * (lo + hi)
    eps_grey_value = target
    print(f"  grey model: emissivity {eps_grey_value:.3f} at every wavelength")
    print(f"  spectral model: scale c = {c0:.6f}, flux-weighted emissivity at 288 K")
    print(f"    = {broadband_eps(c0):.6f} (matched to the grey value by construction)")

    def olr_grey(eps):
        return np.trapezoid(eps * B_layer + (1.0 - eps) * B_surf, lam)

    def olr_spec(c):
        e = eps_profile(c)
        return np.trapezoid(e * B_layer + (1.0 - e) * B_surf, lam)

    print("\n   model                     OLR (W/m^2)")
    print(f"   grey, eps = {eps_grey_value:.2f}          {olr_grey(eps_grey_value):12.3f}")
    print(f"   spectral, matched eps        {olr_spec(c0):12.3f}")
    print(f"   difference                   {olr_spec(c0) - olr_grey(eps_grey_value):12.3f}")
    print("\n  Now increase the absorber by the SAME factor in both models:")
    print("   factor    grey dOLR (W/m^2)   spectral dOLR (W/m^2)   ratio")
    for fac in (1.02, 1.10, 1.50):
        eps2 = 1.0 - (1.0 - eps_grey_value) ** fac
        d_grey = olr_grey(eps2) - olr_grey(eps_grey_value)
        d_spec = olr_spec(c0 * fac) - olr_spec(c0)
        print(f"   {fac:6.2f}   {d_grey:17.4f}   {d_spec:21.4f}   "
              f"{d_spec / d_grey:6.2f}")
    print("\n  The two models have identical broadband emissivity and yet differ in")
    print("  both their outgoing flux and their SENSITIVITY to more absorber.  The")
    print("  reason is that the window lets the surface radiate directly to space in")
    print("  a part of the spectrum, where adding absorber changes little, while the")
    print("  strong band saturates where the surface is brightest.  A single optical")
    print("  depth cannot reproduce two different functions of wavelength.")
    print("  That is why radiative transfer in climate models is done band by band")
    print("  (line-by-line or correlated-k schemes) rather than with a grey opacity.")

if __name__ == "__main__":
    main()
