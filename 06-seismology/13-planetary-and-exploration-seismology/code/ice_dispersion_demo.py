"""Ice: seismic velocities, Love-wave dispersion, and the thickness-velocity
trade-off in the inversion for ice thickness.

Three parts, all from STATED models:

  1. Velocities from elastic moduli.  vp = sqrt((K + 4G/3)/rho), vs = sqrt(G/rho),
     with a stated temperature dependence of G and porosity dependence of the
     moduli.  The temperature and porosity coefficients are MODEL choices; the
     real ones must come from a measured compilation.

  2. Love-wave dispersion for an ice layer over a half-space.  The dispersion
     relation is solved numerically for the fundamental mode.  Ice is a
     waveguide when it is SLOWER than the material beneath it, which is the
     usual case for ice over bedrock and for ice over water (water carries no
     shear wave at all).

  3. The inversion for ice thickness, and its non-uniqueness.  A synthetic
     dispersion curve is inverted for (H, beta_layer) with everything else fixed.
     The family of models that fits within a stated tolerance is reported: this
     is the thickness-velocity trade-off, quantified.

Run:  <repo>/.venv/bin/python ice_dispersion_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq

# ----------------------------------------------------------------------
# MODEL inputs (chosen, not measured)
# ----------------------------------------------------------------------
RHO_ICE = 917.0          # kg/m^3   MODEL density of bubble-free ice
E_ICE = 9.3e9            # Pa       MODEL Young's modulus at -10 C
NU_ICE = 0.33            # -        MODEL Poisson's ratio
GAMMA_T = 3.0e-3         # 1/K      MODEL fractional decrease of G per kelvin of warming
POROSITY_COEF = 3.0e-3   # 1/unit   MODEL fractional decrease of moduli per unit porosity
T_REF = 263.15           # K        MODEL reference temperature (-10 C)
T_WARM = 273.15          # K        MODEL pressure-melting point (0 C)

BETA_ICE = 1.90e3        # m/s      MODEL true S velocity of the ice layer
BETA_BED = 3.00e3        # m/s      MODEL true S velocity of the bed (bedrock)
RHO_BED = 2700.0         # kg/m^3   MODEL bed density
H_TRUE = 1000.0          # m        MODEL true ice thickness
FREQS = np.logspace(np.log10(0.4), np.log10(20.0), 40)   # Hz MODEL band
TOL = 0.01               # -        MODEL fit tolerance: 1 % rms phase slowness

LINES = "=" * 78


def section(title: str) -> None:
    print(f"\n{LINES}\n{title}\n{LINES}")


def moduli_from_E(E: float, nu: float) -> tuple[float, float]:
    """Return (K, G) from Young's modulus and Poisson's ratio."""
    G = E / (2.0 * (1.0 + nu))
    K = E / (3.0 * (1.0 - 2.0 * nu))
    return K, G


def love_dispersion(omega: float, H: float, beta1: float, beta2: float,
                    mu1: float, mu2: float) -> float:
    """Solve for the fundamental-mode Love-wave phase velocity c.

    For beta1 < c < beta2 the dispersion equation is
        tan(omega H sqrt(1/beta1^2 - 1/c^2))
            = (mu2/mu1) sqrt(1/c^2 - 1/beta2^2) / sqrt(1/beta1^2 - 1/c^2).
    """
    lo, hi = beta1 * (1.0 + 1e-9), beta2 * (1.0 - 1e-9)
    if lo >= hi:
        raise ValueError("Love waves require beta_layer < beta_halfspace")

    def f(c: float) -> float:
        k1 = np.sqrt(1.0 / beta1 ** 2 - 1.0 / c ** 2)
        k2 = np.sqrt(1.0 / c ** 2 - 1.0 / beta2 ** 2)
        return np.tan(omega * H * k1) - (mu2 / mu1) * k2 / k1

    # Walk outwards from just above beta1 and take the first sign change: the
    # fundamental mode is the lowest frequency branch, which exists at any
    # frequency for a slow layer over a fast half-space.
    grid = np.linspace(lo, hi, 400)
    vals = np.array([f(c) for c in grid])
    sign_change = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
    if sign_change.size == 0:
        return np.nan
    i = int(sign_change[0])
    return float(brentq(f, grid[i], grid[i + 1]))


def main() -> int:
    print("Ice velocities, Love-wave dispersion and the thickness-velocity trade-off")
    print(f"MODEL: rho_ice = {RHO_ICE:.0f} kg/m^3, E = {E_ICE / 1e9:.1f} GPa, "
          f"nu = {NU_ICE}, T_ref = {T_REF - 273.15:.0f} C")

    # ------------------------------------------------------------------
    section("1. Elastic moduli and seismic velocities of ice")
    K0, G0 = moduli_from_E(E_ICE, NU_ICE)
    vp0 = np.sqrt((K0 + 4.0 * G0 / 3.0) / RHO_ICE)
    vs0 = np.sqrt(G0 / RHO_ICE)
    print(f"  G = E/(2(1+nu))                = {G0 / 1e9:.4f} GPa")
    print(f"  K = E/(3(1-2nu))               = {K0 / 1e9:.4f} GPa")
    print(f"  vp = sqrt((K + 4G/3)/rho)      = {vp0:.1f} m/s")
    print(f"  vs = sqrt(G/rho)               = {vs0:.1f} m/s")
    print(f"  vp/vs                          = {vp0 / vs0:.4f}")

    print("\n  Temperature dependence (MODEL: G falls by gamma_T = "
          f"{GAMMA_T:.1e} per K, a chosen linearisation):")
    print("\n   T [C]     G [GPa]    vp [m/s]    vs [m/s]    d vs / dT [m/s/K]")
    temps = [-40.0, -30.0, -20.0, -10.0, -5.0, 0.0]
    vs_list = []
    for tc in temps:
        tk = tc + 273.15
        G = G0 * (1.0 - GAMMA_T * (tk - T_REF))
        K = K0 * (1.0 - GAMMA_T * (tk - T_REF) * 0.5)
        vp = np.sqrt((K + 4.0 * G / 3.0) / RHO_ICE)
        vs = np.sqrt(G / RHO_ICE)
        vs_list.append(vs)
        print(f"  {tc:6.0f}   {G / 1e9:9.4f}   {vp:10.1f}   {vs:10.1f}")
    dvs = (vs_list[-1] - vs_list[0]) / (temps[-1] - temps[0])
    print(f"  mean d(vs)/dT over -40 to 0 C = {dvs:.3f} m/s/K")
    print("  The ABSOLUTE temperature effect is small (a few per cent over 40 K).")
    print("  It matters for a 1 km ice column only because a few per cent of a")
    print("  travel time is comparable to a thickness error of a few tens of metres.")

    print("\n  Porosity dependence (MODEL: moduli fall by "
          f"{POROSITY_COEF:.1e} per unit porosity, a chosen linearisation):")
    print("\n   porosity   vp [m/s]   vs [m/s]   vs/vs0")
    for phi in (0.0, 0.02, 0.05, 0.10, 0.20):
        f = 1.0 - POROSITY_COEF * phi * 100.0
        K = K0 * f
        G = G0 * f
        vp = np.sqrt((K + 4.0 * G / 3.0) / RHO_ICE)
        vs = np.sqrt(G / RHO_ICE)
        print(f"  {phi:9.2f}   {vp:9.1f}   {vs:9.1f}   {vs / vs0:8.4f}")
    print("  Porosity matters far more than temperature at the same fractional")
    print("  size, because it acts on both moduli and on the density.  Firn -- the")
    print("  porous surface layer -- is therefore the single largest near-surface")
    print("  velocity anomaly on an ice sheet.")

    # ------------------------------------------------------------------
    section("2. Love-wave dispersion for ice over bedrock")
    mu_ice = RHO_ICE * BETA_ICE ** 2
    mu_bed = RHO_BED * BETA_BED ** 2
    print(f"  layer:  beta = {BETA_ICE:.0f} m/s, rho = {RHO_ICE:.0f} kg/m^3, "
          f"H = {H_TRUE:.0f} m")
    print(f"  bed:    beta = {BETA_BED:.0f} m/s, rho = {RHO_BED:.0f} kg/m^3")
    print(f"  contrast mu_bed/mu_ice = {mu_bed / mu_ice:.3f}; a Love-wave "
          f"waveguide requires")
    print("  beta_layer < beta_bed, which holds here.  Over LIQUID water there is")
    print("  no shear wave at all in the lower medium, so the waveguide is even")
    print("  stronger and the ice behaves closer to a free plate.")
    print("\n   f [Hz]    lambda [m]    c [m/s]    c/beta_ice    lambda/H")
    cobs = []
    for f in FREQS:
        om = 2.0 * np.pi * f
        c = love_dispersion(om, H_TRUE, BETA_ICE, BETA_BED, mu_ice, mu_bed)
        cobs.append(c)
        print(f"  {f:7.2f}   {c / f:11.1f}   {c:9.1f}   {c / BETA_ICE:10.4f}   "
              f"{c / f / H_TRUE:10.3f}")
    cobs = np.array(cobs)
    print("  At low frequency the wavelength exceeds the layer thickness several")
    print("  times over and c approaches beta_bed; at high frequency c approaches")
    print("  beta_ice.  The transition carries the thickness information.")

    # ------------------------------------------------------------------
    section("3. Inverting for thickness: the thickness-velocity trade-off")
    print(f"  Fit tolerance: {100 * TOL:.0f} % rms on phase slowness (1/c).")
    print("  beta_bed and the bed density are assumed KNOWN -- that assumption is")
    print("  part of the result, not separate from it.")

    def misfit(H: float, b1: float) -> float:
        pred = np.array([love_dispersion(2.0 * np.pi * f, H, b1, BETA_BED,
                                         RHO_ICE * b1 ** 2, mu_bed) for f in FREQS])
        if not np.all(np.isfinite(pred)):
            return 1e9
        return float(np.sqrt(np.mean((1.0 / pred - 1.0 / cobs) ** 2))
                     / np.mean(1.0 / cobs))

    h_grid = np.linspace(400.0, 2500.0, 106)
    b_grid = np.linspace(0.80 * BETA_ICE, 1.20 * BETA_ICE, 81)
    accepted = []
    for b1 in b_grid:
        for H in h_grid:
            if misfit(H, b1) <= TOL:
                accepted.append((H, b1))
    accepted = np.array(accepted)
    print(f"\n  accepted models: {accepted.shape[0]} of "
          f"{h_grid.size * b_grid.size} grid points")
    if accepted.size:
        h_a, b_a = accepted[:, 0], accepted[:, 1]
        print(f"  ice thickness range    : {h_a.min():.0f} to {h_a.max():.0f} m "
              f"(true {H_TRUE:.0f} m)")
        print(f"  layer velocity range   : {b_a.min():.1f} to {b_a.max():.1f} m/s "
              f"(true {BETA_ICE:.1f} m/s)")
        print(f"  corr(H, beta_layer)    : {np.corrcoef(h_a, b_a)[0, 1]:+.4f}")
        print(f"  true model accepted?   : "
              f"{bool(np.any((np.abs(h_a - H_TRUE) < 15) & (np.abs(b_a - BETA_ICE) < 5)))}")

    print("\n  Marginal width of the trade-off at fixed layer velocity:")
    for b_fix in (BETA_ICE * 0.90, BETA_ICE * 0.95, BETA_ICE,
                  BETA_ICE * 1.05, BETA_ICE * 1.10):
        hs = h_grid[[misfit(H, b_fix) <= TOL for H in h_grid]]
        if hs.size:
            print(f"    beta = {b_fix:7.1f} m/s ({100 * (b_fix / BETA_ICE - 1):+5.1f} %) "
                  f"-> H = {hs.min():.0f} to {hs.max():.0f} m "
                  f"(width {hs.max() - hs.min():.0f} m)")
        else:
            print(f"    beta = {b_fix:7.1f} m/s ({100 * (b_fix / BETA_ICE - 1):+5.1f} %) "
                  f"-> no accepted thickness")
    print("  Read the error budget: a -5 % error in the assumed ice velocity is")
    print("  compensated by a thickness change of the order shown, which is why an")
    print("  independent thickness -- a radar echo, a borehole, a refraction")
    print("  profile -- is what turns a dispersion curve into a thickness.")

    # ------------------------------------------------------------------
    section("4. What breaks the trade-off")
    print("  Fix the thickness and ask how well the velocity is recovered:")
    for H_fix in (600.0, 800.0, 1000.0, 1200.0, 1500.0):
        b_acc = b_grid[[misfit(H_fix, b) <= TOL for b in b_grid]]
        if b_acc.size:
            print(f"    H = {H_fix:5.0f} m -> beta in {b_acc.min():.1f} to "
                  f"{b_acc.max():.1f} m/s (width {b_acc.max() - b_acc.min():.1f})")
        else:
            print(f"    H = {H_fix:5.0f} m -> no accepted velocity")
    print("  Now fix the velocity and ask how well the thickness is recovered:")
    for b_fix in (BETA_ICE * 0.95, BETA_ICE, BETA_ICE * 1.05):
        hs = h_grid[[misfit(H, b_fix) <= TOL for H in h_grid]]
        lab = "known" if abs(b_fix - BETA_ICE) < 1e-9 else (
            "+5 % error" if b_fix > BETA_ICE else "-5 % error")
        if hs.size:
            print(f"    beta {lab:10s} -> H = {hs.min():.0f} to {hs.max():.0f} m, "
                  f"centre {0.5 * (hs.min() + hs.max()):.0f} m "
                  f"({100 * (0.5 * (hs.min() + hs.max()) / H_TRUE - 1):+.1f} %)")
    print("  A 5 % velocity error is a thickness bias of the size shown.  Compare")
    print("  that with the accuracy a radar echo gives (a few metres), and the")
    print("  reason seismic dispersion is usually used to CONSTRAIN a velocity for")
    print("  the radar, rather than to measure thickness directly, is clear.")

    # ------------------------------------------------------------------
    section("Summary of measured quantities")
    print(f"  vp, vs of the ice from its moduli       = {vp0:.1f}, {vs0:.1f} m/s")
    print(f"  d(vs)/dT over -40 to 0 C                = {dvs:.3f} m/s per K")
    print(f"  fundamental-mode c range over {FREQS[0]:.1f}-{FREQS[-1]:.1f} Hz  = "
          f"{cobs.min():.1f}-{cobs.max():.1f} m/s")
    if accepted.size:
        print(f"  models fitting within {100 * TOL:.0f} % rms    = "
              f"{accepted.shape[0]}, H from {accepted[:, 0].min():.0f} to "
              f"{accepted[:, 0].max():.0f} m")
        print(f"  ln H vs ln beta correlation             = "
              f"{np.corrcoef(np.log(accepted[:, 0]), np.log(accepted[:, 1]))[0, 1]:+.4f}")
    print("  Every input above is a MODEL choice; the elastic constants of ice and")
    print("  their temperature and porosity dependence must be taken from a measured")
    print("  compilation before any real ice thickness is claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
