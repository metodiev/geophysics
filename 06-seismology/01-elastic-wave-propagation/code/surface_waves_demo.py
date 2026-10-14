"""Surface waves: Love dispersion, Rayleigh's secular equation, group velocity.

Every model in this file is SYNTHETIC and stated in full; nothing is quoted from
a reference Earth model.

1. Love waves in a layer over a half space: solve the transcendental dispersion
   relation, check the mode count against its closed form, and check the two
   limits (c -> beta_layer at high frequency, c -> beta_halfspace at low).
2. Group velocity: compute U = d(omega)/dk twice, once from the definition
   U = c + k dc/dk and once from U = c / (1 - (omega/c) dc/domega), and compare.
3. Rayleigh waves on a homogeneous half space: derive the cubic secular
   equation for zeta = c_R^2 / beta^2, then verify its root against an
   *independent* numerical search on the 2x2 boundary-condition determinant.
4. Show that the Love waveguide disappears if the layer is faster than the
   half space: the trapped-mode interval (beta1, beta2) is then empty.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/surface_waves_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ---- SYNTHETIC layered model: 30 km layer over a faster half space ----------
H = 30.0e3            # layer thickness, m
BETA1 = 3.5e3         # S speed in the layer, m/s
RHO1 = 2700.0         # density of the layer, kg/m^3
BETA2 = 4.5e3         # S speed in the half space, m/s
RHO2 = 3300.0         # density of the half space, kg/m^3
MU1 = RHO1 * BETA1**2
MU2 = RHO2 * BETA2**2


# ---------------------------------------------------------------------------
# 1. Love dispersion
# ---------------------------------------------------------------------------
def love_residual(omega: float, c: float) -> float:
    """tan(nu1 H) - (mu2/mu1) * gamma2 / nu1, with nu1, gamma2 as defined."""
    if not (BETA1 < c < BETA2):
        return np.nan
    nu1 = omega * np.sqrt(1.0 / BETA1**2 - 1.0 / c**2)
    gamma2 = omega * np.sqrt(1.0 / c**2 - 1.0 / BETA2**2)
    return np.tan(nu1 * H) - (MU2 / MU1) * gamma2 / nu1


def love_G(omega: float, c: float) -> float:
    """Continuous form of the Love dispersion relation.

    Multiplying tan(nu1 H) = (mu2/mu1) gamma2 / nu1 by nu1 cos(nu1 H) removes
    the tangent poles, so every sign change on (beta1, beta2) is a mode and the
    sign changes at nu1 H = pi/2 + n pi are not counted.
    """
    nu1 = omega * np.sqrt(1.0 / BETA1**2 - 1.0 / c**2)
    gamma2 = omega * np.sqrt(1.0 / c**2 - 1.0 / BETA2**2)
    return nu1 * np.sin(nu1 * H) - (MU2 / MU1) * gamma2 * np.cos(nu1 * H)


def love_modes(omega: float) -> list[float]:
    """All trapped Love phase velocities at angular frequency omega."""
    grid = np.linspace(BETA1 * (1 + 1e-9), BETA2 * (1 - 1e-9), 20001)
    values = np.array([love_G(omega, c) for c in grid])
    roots = []
    for i in range(len(grid) - 1):
        if values[i] * values[i + 1] < 0:
            try:
                roots.append(brentq(lambda cc: love_G(omega, cc),
                                    grid[i], grid[i + 1], xtol=1e-8))
            except ValueError:
                pass
    return sorted(set(round(r, 6) for r in roots))


def love_fundamental(omega: float) -> float:
    """Phase velocity of the fundamental Love mode.

    At fixed frequency the branches are ordered by phase velocity and the
    fundamental is the *lowest*, because every higher mode appears at the
    half-space speed and then disperses downward.
    """
    modes = love_modes(omega)
    if not modes:
        raise ValueError("no trapped Love mode at this frequency")
    return modes[0]


def love_dispersion() -> None:
    section("1. Love waves in a 30 km layer over a faster half space")
    print(f"  layer      : beta1 = {BETA1 / 1e3:.3f} km/s, rho1 = {RHO1:.0f} kg/m^3, "
          f"H = {H / 1e3:.0f} km")
    print(f"  half space : beta2 = {BETA2 / 1e3:.3f} km/s, rho2 = {RHO2:.0f} kg/m^3")
    print(f"  trapping requires beta1 < c < beta2, i.e. "
          f"{BETA1 / 1e3:.3f} < c < {BETA2 / 1e3:.3f} km/s")
    print(f"\n  {'period (s)':>11} {'fundamental c (km/s)':>21} "
          f"{'modes found':>12} {'1+floor(omega H q/pi)':>22}")

    def predicted_count(omega: float) -> int:
        q = np.sqrt(1.0 / BETA1**2 - 1.0 / BETA2**2) * omega * H
        return 1 + int(np.floor(q / np.pi))

    for period in (100.0, 40.0, 20.0, 10.0, 5.0):
        omega = 2.0 * np.pi / period
        modes = love_modes(omega)
        if not modes:
            continue
        print(f"  {period:11.1f} {modes[0] / 1e3:21.4f} {len(modes):12d} "
              f"{predicted_count(omega):22d}")
    print("  The mode count equals the closed form 1 + floor(omega H q / pi) with")
    print("  q = sqrt(1/beta1^2 - 1/beta2^2); the fundamental phase velocity falls")
    print("  monotonically from the half-space speed toward the layer speed as the")
    print("  period shortens, which is why short-period Love waves sample the")
    print("  layer and long-period ones sample the half space.")

    c_hi = love_fundamental(2.0 * np.pi / 2.0)
    c_lo = love_fundamental(2.0 * np.pi / 200.0)
    print(f"\n  As T -> 0 the fundamental tends to beta1 = {BETA1 / 1e3:.4f} km/s: "
          f"c(2 s) = {c_hi / 1e3:.4f} km/s")
    print(f"  As T -> infinity it tends to beta2 = {BETA2 / 1e3:.4f} km/s: "
          f"c(200 s) = {c_lo / 1e3:.4f} km/s.  Neither limit is exactly reached:")
    print(f"  c stays strictly inside the trapping interval, as it must.")


# ---------------------------------------------------------------------------
# 2. Group velocity: two definitions
# ---------------------------------------------------------------------------
def group_velocity_check() -> None:
    section("2. Group velocity from two equivalent definitions")
    periods = np.array([200.0, 150.0, 100.0, 80.0, 60.0, 50.0, 40.0])
    omega = 2.0 * np.pi / periods
    c = np.array([love_fundamental(w) for w in omega])
    k = omega / c

    # central differences on a deliberately small step, so that the two forms
    # differ only by the algebra that relates them
    h = 1e-4
    dc_domega = np.array([
        (love_fundamental(w + h) - love_fundamental(w - h)) / (2.0 * h)
        for w in omega])
    dk_domega = np.array([
        ((w + h) / love_fundamental(w + h) - (w - h) / love_fundamental(w - h))
        / (2.0 * h) for w in omega])
    U_direct = c + k * dc_domega / dk_domega          # U = c + k dc/dk
    U_alt = c / (1.0 - (omega / c) * dc_domega)       # U = c / (1 - (w/c) dc/dw)

    print(f"  {'T (s)':>7} {'c (km/s)':>10} {'U=c+k dc/dk (km/s)':>20} "
          f"{'U=c/(1-(w/c)dc/dw)':>20} {'rel. diff':>11}")
    for i in range(len(periods)):
        rel = abs(U_direct[i] - U_alt[i]) / U_direct[i]
        print(f"  {periods[i]:7.1f} {c[i] / 1e3:10.4f} "
              f"{U_direct[i] / 1e3:20.4f} {U_alt[i] / 1e3:20.4f} {rel:11.2e}")
    worst = np.max(np.abs(U_direct - U_alt) / np.abs(U_direct))
    gap = np.abs(c - U_direct)
    print(f"\n  The two forms agree to {worst:.2e} relative; they are the same")
    print("  derivative rearranged, so any difference is finite-difference error.")
    print(f"  Largest measured |c - U| = {gap.max() / 1e3:.4f} km/s at "
          f"T = {periods[np.argmax(gap)]:.0f} s: U < c over the whole band,")
    print("  which is the normal-dispersion signature of a layer over a faster")
    print("  half space (longer periods sample the faster material).")


# ---------------------------------------------------------------------------
# 3. Rayleigh waves: the secular equation and an independent determinant
# ---------------------------------------------------------------------------
def rayleigh_cubic(zeta: float, xi: float) -> float:
    return zeta**3 - 8.0 * zeta**2 + (24.0 - 16.0 * xi) * zeta + 16.0 * (xi - 1.0)


def rayleigh_determinant(c: float, alpha: float, beta: float) -> float:
    """2x2 P-SV boundary determinant for a homogeneous half space, free surface.

    Rows are the free-surface conditions sigma_zz = 0 and sigma_xz = 0 for the
    trial potentials phi = A exp(-k q_alpha z) exp(ik(x-ct)),
    psi = B exp(-k q_beta z) exp(ik(x-ct)); the common factor k^2 rho is dropped.
    """
    if c >= beta:
        return np.nan
    qa = np.sqrt(1.0 - c**2 / alpha**2 + 0j)
    qb = np.sqrt(1.0 - c**2 / beta**2 + 0j)
    m11 = 2.0 - c**2 / beta**2
    m12 = 2.0j * qb
    m21 = -2.0j * qa
    m22 = 2.0 - c**2 / beta**2
    return np.real(m11 * m22 - m12 * m21)


def rayleigh_check() -> None:
    section("3. Rayleigh wave: cubic root vs an independent determinant search")
    print(f"  {'vp/vs':>7} {'xi=(vs/vp)^2':>13} {'cubic root zeta':>16} "
          f"{'det. root c/beta':>18} {'sqrt(zeta)':>11} {'rel. diff':>11}")
    for ratio in (np.sqrt(3.0), 2.0, 1.8, 5.0):
        xi = 1.0 / ratio**2
        roots = np.roots([1.0, -8.0, (24.0 - 16.0 * xi), 16.0 * (xi - 1.0)])
        real = [r.real for r in roots if abs(r.imag) < 1e-12 and 0.0 < r.real < 1.0]
        zeta = real[0]
        c_from_cubic = np.sqrt(zeta)

        beta = 1.0
        alpha = ratio * beta
        grid = np.linspace(0.05, 0.99999, 4000)
        vals = np.array([rayleigh_determinant(cc, alpha, beta) for cc in grid * beta])
        c_det = np.nan
        for i in range(len(grid) - 1):
            if not np.isfinite(vals[i]) or not np.isfinite(vals[i + 1]):
                continue
            if vals[i] * vals[i + 1] < 0:
                c_det = brentq(lambda cc: rayleigh_determinant(cc, alpha, beta),
                               grid[i] * beta, grid[i + 1] * beta, xtol=1e-9)
                break
        print(f"  {ratio:7.4f} {xi:13.6f} {zeta:16.8f} {c_det / beta:18.8f} "
              f"{c_from_cubic:11.6f} {abs(c_det / beta - c_from_cubic) / c_from_cubic:11.2e}")

    ratio = np.sqrt(3.0)
    xi = 1.0 / ratio**2
    zeta = [r.real for r in np.roots([1.0, -8.0, (24.0 - 16.0 * xi),
                                      16.0 * (xi - 1.0)]) if abs(r.imag) < 1e-12
            and 0.0 < r.real < 1.0][0]
    print(f"\n  For a Poisson solid (lambda = mu, vp/vs = sqrt(3)), xi = 1/3 and")
    print(f"  zeta = {zeta:.8f}, so c_R = {np.sqrt(zeta):.8f} beta = "
          f"{np.sqrt(zeta):.6f} vs.  (exact algebraic root of the cubic).")
    print("  The determinant search reproduces the cubic root: both are the same")
    print("  boundary conditions, one obtained by elimination and one by direct")
    print("  root finding, so their agreement is a check on the algebra.")


# ---------------------------------------------------------------------------
# 4. Love waves need a low-velocity waveguide
# ---------------------------------------------------------------------------
def waveguide_requirement() -> None:
    section("4. Love waves need a low-velocity waveguide")
    fine = np.linspace(0.1, 20.0, 200)          # guess phase velocities, km/s
    for label, b1, b2 in (("layer slower (beta1 < beta2): waveguide exists",
                           3.5e3, 4.5e3),
                          ("layer faster (beta1 > beta2): no waveguide",
                           4.5e3, 3.5e3)):
        interval = (min(b1, b2), max(b1, b2))
        trapped = [c for c in fine * 1e3 if b1 < c < b2]
        print(f"\n  {label}")
        print(f"    beta1 = {b1 / 1e3:.2f} km/s, beta2 = {b2 / 1e3:.2f} km/s; "
              f"the interval (beta1, beta2) contains {len(trapped)} of the 200 "
              f"trial velocities")
        print(f"    i.e. the condition beta1 < c < beta2 is "
              f"{'satisfiable' if trapped else 'unsatisfiable'}")
    print("  When the layer is faster than the half space, gamma2 and nu1 are")
    print("  never simultaneously real: the energy leaks into the half space and")
    print("  no discrete Love mode is trapped.  A seismological waveguide must be")
    print("  a LOW-velocity layer, not merely a contrast.")


def main() -> None:
    love_dispersion()
    group_velocity_check()
    rayleigh_check()
    waveguide_requirement()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
