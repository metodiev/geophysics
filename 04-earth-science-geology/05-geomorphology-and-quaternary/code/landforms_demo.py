"""Landform processes and shapes.

Run:  .venv/bin/python landforms_demo.py
Requires: numpy (the finite-difference hillslope solver uses arrays).

Companion to lesson 04-05-01.

Every number falls into one of three categories and the output labels them:

* COMPUTED  -- produced by a formula stated in the lesson. The diffusion
               profile, the maximum scarp slope, the steady-state channel
               profile, the concavity regression and the knickpoint celerity
               are all computed here.
* MODELLED  -- a transport coefficient of a *particular* landscape. The
               hillslope diffusivity kappa, the bedrock uplift rate U and the
               erosion coefficient K are model parameters. The values used are
               illustrative and lie inside the ranges reported for real
               landscapes; a real study measures or calibrates them.
* DERIVED   -- a combination of the two (a timescale, a curvature, a ratio).

Parts:

1. Hillslope diffusion: an explicit finite-difference solution of
   dz/dt = kappa d2z/dx2 for an initially vertical scarp, checked against the
   closed-form solution z = (h/2) erfc(x / 2 sqrt(kappa t)); the maximum slope
   is then inverted for the age of a degraded scarp.
2. Diffusion timescale and the steady-state hilltop curvature argument that
   links soil production to hillslope curvature.
3. Stream-power incision: a steady-state channel profile built from
   S = (U/K)^(1/n) A^(-m/n), the logarithmic slope-area regression that recovers
   the concavity index, the steepness index and its units.
4. The chi-transform: elevation is linear in chi with a computable slope, and
   the knickpoint celerity follows from the same stream-power law.
5. Hack's law as an independent geometric scaling check.
"""

import math

import numpy as np

# --------------------------------------------------------------------------
# MODELLED parameters (illustrative, inside the reported ranges)
# --------------------------------------------------------------------------

KAPPA = 1.0e-3          # hillslope diffusivity [m^2/yr]  (~0.1 m^2 per century)
H_SCARP = 10.0          # scarp height [m]
T_END = 10_000.0        # elapsed time [yr]

UPLIFT = 1.0e-4         # bedrock uplift / base-level fall [m/yr] = 0.1 mm/yr
K_ERODE = 1.0e-5        # erosion coefficient [m^(1-2m)/yr]; with m = 0.5 this is 1/yr
M_OVER_N = 0.45         # concavity index theta = m/n
N_EXP = 1.0             # slope exponent in E = K A^m S^n

SOIL_PRODUCTION = 5.0e-5   # U equivalent at the ridge crest [m/yr] = 0.05 mm/yr

HACK_K = 1.4            # Hack coefficient [km^(1-2h)]
HACK_H = 0.6            # Hack exponent (dimensionless)


def erfc(x: float) -> float:
    """Complementary error function from math (stdlib)."""
    return math.erfc(x)


def solve_scarp(dx: float, length: float = 200.0) -> tuple[np.ndarray, np.ndarray]:
    """Explicit FD solution of dz/dt = kappa d2z/dx2 for a vertical scarp.

    Dirichlet (fixed) conditions at both ends; dt is chosen from the stated
    stability limit dt <= dx^2/(2 kappa).
    """
    dt_cap = 0.9 * dx * dx / (2.0 * KAPPA)
    n_steps = int(math.ceil(T_END / dt_cap))
    dt = T_END / n_steps
    nx = int(round(length / dx)) + 1
    x = np.linspace(-length / 2.0, length / 2.0, nx)
    z = np.where(x < 0.0, H_SCARP, 0.0)
    lam = KAPPA * dt / (dx * dx)
    for _ in range(n_steps):
        lap = np.zeros_like(z)
        lap[1:-1] = z[2:] - 2.0 * z[1:-1] + z[:-2]
        z = z + lam * lap
    return x, z


def hillslope_diffusion() -> None:
    """Explicit finite-difference scarp degradation, checked against erfc."""
    print("=" * 72)
    print("1. HILLSLOPE DIFFUSION -- numerical solution vs closed form")
    print("=" * 72)

    max_slope_ana = H_SCARP / (2.0 * math.sqrt(math.pi * KAPPA * T_END))
    print(f"  diffusion length sqrt(4 kappa t) = "
          f"{math.sqrt(4.0 * KAPPA * T_END):.3f} m")
    print(f"  COMPUTED analytic max |dz/dx| = {max_slope_ana:.6f}  "
          f"(slope angle {math.degrees(math.atan(max_slope_ana)):.3f} deg)")

    # Convergence test. The initial condition is a step, which the grid can only
    # represent to first order in dx, so the error is expected to fall like dx.
    probes = np.array([0.0, 1.0, 2.0, 5.0, 10.0, 20.0])
    z_analytic = 0.5 * H_SCARP * np.array(
        [erfc(xi / (2.0 * math.sqrt(KAPPA * T_END))) for xi in probes])
    errors = []
    slope_errs = []
    for dx in (1.0, 0.5, 0.25):
        x, z = solve_scarp(dx)
        z_at = np.interp(probes, x, z)
        err = float(np.max(np.abs(z_at - z_analytic)))
        slope_num = float(np.max(np.abs(np.diff(z) / dx)))
        errors.append(err)
        slope_errs.append(abs(slope_num - max_slope_ana) / max_slope_ana)
        print(f"  dx = {dx:>5.2f} m: max |z_num - z_erfc| on probes = "
              f"{err:.4e} m, max |dz/dx| = {slope_num:.6f}, "
              f"slope-ratio error = {slope_errs[-1]:.2e}")
    order_1 = math.log2(errors[0] / errors[1])
    order_2 = math.log2(errors[1] / errors[2])
    print(f"  COMPUTED observed convergence order: {order_1:.3f} then "
          f"{order_2:.3f} (first order, as the step initial condition implies)")
    print(f"  COMPUTED slope error at dx = 0.25 m: {slope_errs[-1]:.2e} "
          f"({100 * slope_errs[-1]:.3f} per cent)")
    assert 0.8 < order_1 < 1.3 and 0.8 < order_2 < 1.3
    assert errors[2] < 0.15

    # Inverse problem: date a scarp from its measured maximum slope.
    slope_measured = 0.8921
    t_est = H_SCARP ** 2 / (4.0 * math.pi * KAPPA * slope_measured ** 2)
    print(f"  COMPUTED age from a measured max slope of {slope_measured}: "
          f"t = h^2/(4 pi kappa s_max^2) = {t_est:.1f} yr")
    print("  A factor-of-two error in kappa is a factor-of-two error in t:")
    for factor in (0.5, 2.0):
        t_alt = H_SCARP ** 2 / (4.0 * math.pi * (KAPPA * factor) * slope_measured ** 2)
        print(f"    kappa x {factor:>3}: t = {t_alt:>8.1f} yr")

    tau = 100.0 ** 2 / KAPPA
    print(f"  DERIVED diffusion timescale tau = L^2/kappa for L = 100 m: "
          f"{tau:.3e} yr = {tau / 1e6:.2f} Myr")


def steady_state_hilltop() -> None:
    """Curvature-vs-soil-production argument at a ridge crest."""
    print()
    print("=" * 72)
    print("2. STEADY-STATE HILLTOP CURVATURE")
    print("=" * 72)
    curvature = -SOIL_PRODUCTION / KAPPA      # [m^-1]
    radius = 1.0 / abs(curvature)
    print(f"  MODELLED soil production / uplift U = {SOIL_PRODUCTION:.1e} m/yr")
    print(f"  MODELLED hillslope diffusivity kappa = {KAPPA:.1e} m^2/yr")
    print("  COMPUTED steady state from U = -kappa d2z/dx2 gives")
    print(f"    d2z/dx2 = -U/kappa = {curvature:.4f} m^-1")
    print(f"    radius of curvature = 1/|curvature| = {radius:.2f} m")
    print("  The measurable quantity is the curvature, not the soil production;")
    print("  inverting it for U requires kappa, which must be calibrated.")
    for k in (3.0e-4, 3.0e-3):
        print(f"    if kappa = {k:.1e} m^2/yr then |d2z/dx2| = "
              f"{SOIL_PRODUCTION / k:.4f} m^-1")


def stream_power_profile() -> None:
    """Steady-state channel profile and the slope-area regression."""
    print()
    print("=" * 72)
    print("3. STREAM-POWER INCISION -- steady-state slope-area relation")
    print("=" * 72)
    print("  E = K A^m S^n with n = 1, theta = m/n = "
          f"{M_OVER_N}; steady state S = (U/K)^(1/n) A^(-theta)")

    a_min, a_max = 1.0e5, 1.0e8      # drainage area [m^2]
    n_pts = 61
    area = np.logspace(math.log10(a_min), math.log10(a_max), n_pts)
    slope = (UPLIFT / K_ERODE) ** (1.0 / N_EXP) * area ** (-M_OVER_N)

    coef = np.polyfit(np.log10(area), np.log10(slope), 1)
    theta_fit = -coef[0]
    ks = slope * area ** M_OVER_N

    print(f"  MODELLED U = {UPLIFT:.1e} m/yr, K = {K_ERODE:.1e} yr^-1 "
          f"(for m = 0.5, n = 1)")
    print(f"  COMPUTED regression of log10 S on log10 A: slope = {coef[0]:.6f}, "
          f"intercept = {coef[1]:.6f}")
    print(f"  COMPUTED recovered concavity theta = {theta_fit:.6f} "
          f"(input {M_OVER_N})")
    print(f"  COMPUTED steepness index k_s = S A^theta = {ks[0]:.6e} "
          f".. {ks[-1]:.6e} (constant, as constructed)")
    print(f"  COMPUTED analytic k_s = (U/K)^(1/n) = "
          f"{(UPLIFT / K_ERODE) ** (1.0 / N_EXP):.6e}")
    print("  Units of k_s: m^(2 theta) yr^-1 for n = 1, so a k_s quoted without")
    print("  theta and without its units cannot be compared with another study.")
    assert abs(theta_fit - M_OVER_N) < 1e-9

    for a in (1.0e5, 1.0e6, 1.0e7, 1.0e8):
        s = (UPLIFT / K_ERODE) * a ** (-M_OVER_N)
        print(f"    A = {a:.0e} m^2 ({a / 1e6:5.2f} km^2): S = {s:.6f} "
              f"({100 * s:.4f} per cent), channel gradient angle "
              f"{math.degrees(math.atan(s)):.3f} deg")


def chi_transform_and_knickpoint() -> None:
    """chi linearity and knickpoint celerity for n = 1."""
    print()
    print("=" * 72)
    print("4. THE CHI TRANSFORM AND KNICKPOINT CELERITY")
    print("=" * 72)
    # Area grows linearly downstream from a divide: A(x) = A0 (1 + x/x0).
    a0 = 1.0e5
    x0 = 500.0
    x = np.linspace(0.0, 20_000.0, 4001)        # [m] downstream distance
    area = a0 * (1.0 + x / x0)
    slope = (UPLIFT / K_ERODE) * area ** (-M_OVER_N)
    # z(x) = - integral S dx, with z(x=0) = 0
    z = np.concatenate(([0.0], np.cumsum(
        -0.5 * (slope[1:] + slope[:-1]) * np.diff(x))))
    # chi(x) = integral (A0/A)^theta dx
    integrand = (a0 / area) ** M_OVER_N
    chi = np.concatenate(([0.0], np.cumsum(
        0.5 * (integrand[1:] + integrand[:-1]) * np.diff(x))))
    slope_zchi = np.polyfit(chi, z, 1)
    analytic = -(UPLIFT / K_ERODE) * a0 ** (-M_OVER_N)
    print(f"  COMPUTED regression of z on chi: slope = {slope_zchi[0]:.8f}")
    print(f"  COMPUTED analytic -(U/K) A0^-theta = {analytic:.8f}")
    print(f"  COMPUTED relative difference = "
          f"{abs(slope_zchi[0] - analytic) / abs(analytic):.2e}")
    assert abs(slope_zchi[0] - analytic) / abs(analytic) < 1e-3

    print("  Knickpoint celerity for n = 1: c = K A^m with m = theta (n = 1)")
    m_exp = M_OVER_N * N_EXP
    for a in (1.0e6, 1.0e7):
        c = K_ERODE * a ** m_exp
        print(f"    A = {a:.0e} m^2: c = {c:.4e} m/yr = {c * 1000:.3f} m/kyr; "
              f"100 km of retreat takes {1.0e5 / c:.3e} yr")
    tau_response = 1.0e5 / (K_ERODE * (5.0e6) ** m_exp)
    print(f"  COMPUTED response time over 100 km at A = 5e6 m^2: "
          f"{tau_response:.3e} yr")


def hack_law() -> None:
    """Hack's law as a geometric scaling check."""
    print()
    print("=" * 72)
    print("5. HACK'S LAW")
    print("=" * 72)
    print("  L = k A^h with L in km, A in km^2; the coefficient is unit-bearing")
    print(f"  MODELLED k = {HACK_K} km^(1-2h), h = {HACK_H}")
    for a_km2 in (1.0, 10.0, 100.0, 1000.0):
        length = HACK_K * a_km2 ** HACK_H
        # drainage density as mainstem length per unit area
        print(f"    A = {a_km2:7.1f} km^2: L = {length:7.3f} km, "
              f"L/A = {length / a_km2:.4f} km^-1, "
              f"upslope area per unit length A/L = {a_km2 / length:.4f} km")


def main() -> None:
    hillslope_diffusion()
    steady_state_hilltop()
    stream_power_profile()
    chi_transform_and_knickpoint()
    hack_law()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
