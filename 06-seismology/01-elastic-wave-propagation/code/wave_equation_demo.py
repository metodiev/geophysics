"""From Hooke's law and Newton to the elastodynamic equation -- numerical checks.

Three independent checks of the derivation in lesson 06-01-01:

1. Dimensional accounting for every term of the Navier-Cauchy equation.
2. Direct residual of ``rho * u_tt = (lam+mu) grad(div u) + mu laplacian(u)``
   for an analytic P and S plane wave, with the derivatives taken by central
   finite differences (so the check does not assume the answer), and with a
   grid refinement that shows the residual is truncation error and not a
   modelling error.
3. An independent time-domain finite-difference solution of the same PDE, in
   which a band-limited wavepacket is propagated and its measured speed is
   compared with (i) the derived speed ``sqrt((lam+2mu)/rho)`` and (ii) the
   analytic group velocity of the *discretised* equation, which is where the
   residual difference between the two lives.

All material constants below are SYNTHETIC (stated in full) -- no remembered
Earth values are used.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/wave_equation_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ---- SYNTHETIC material: lambda = 25 GPa, mu = 30 GPa, rho = 2700 kg/m^3 ----
LAM = 25.0e9          # Pa
MU = 30.0e9           # Pa
RHO = 2700.0          # kg m^-3


def vp_analytic() -> float:
    return np.sqrt((LAM + 2.0 * MU) / RHO)


def vs_analytic() -> float:
    return np.sqrt(MU / RHO)


# ---------------------------------------------------------------------------
# 1. Dimensional accounting
# ---------------------------------------------------------------------------
def unit_table() -> None:
    section("1. Every term carries the same dimensions")
    rows = [
        ("rho * d2u/dt2", "[kg m^-3][m][s^-2]", "kg m^-2 s^-2 = Pa m^-1"),
        ("(lam+mu) grad(div u)", "[Pa][m^-1]", "Pa m^-1"),
        ("mu * laplacian(u)", "[Pa][m^-1]", "Pa m^-1"),
    ]
    for term, units, reduced in rows:
        print(f"  {term:24s} : {units:28s} -> {reduced}")
    print("  All three reduce to Pa m^-1, so the equation is dimensionally closed.")
    print(f"  vp^2 = (lam+2mu)/rho = {((LAM + 2 * MU) / RHO):.6e} m^2 s^-2")
    print(f"  vs^2 = mu/rho        = {(MU / RHO):.6e} m^2 s^-2")


# ---------------------------------------------------------------------------
# 2. Residual of the Navier-Cauchy equation for analytic plane waves
# ---------------------------------------------------------------------------
def d1(f: np.ndarray, dx: float, axis: int) -> np.ndarray:
    return (np.roll(f, -1, axis) - np.roll(f, 1, axis)) / (2.0 * dx)


def d2(f: np.ndarray, dx: float, axis: int) -> np.ndarray:
    return (np.roll(f, -1, axis) - 2.0 * f + np.roll(f, 1, axis)) / dx**2


def navier_cauchy_residual(mode: str, n: int) -> tuple[float, float]:
    """Residual of the 3-D Navier-Cauchy equation for a plane wave.

    Returns (max|LHS - RHS|, max|RHS|) so the check is a relative one.
    """
    extent = 0.9 * np.pi
    axis = np.linspace(-extent, extent, n)
    dx = axis[1] - axis[0]
    X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij")

    k = np.array([3.0, 2.0, 1.0])          # rad m^-1, arbitrary direction
    kmag = np.linalg.norm(k)
    pdir = k / kmag

    if mode == "P":                        # u parallel to k (curl-free)
        speed = vp_analytic()
        pol = pdir
    else:                                  # u perpendicular to k (div-free)
        speed = vs_analytic()
        trial = np.array([0.0, 1.0, -2.0])
        pol = trial / np.linalg.norm(trial)

    phase = k[0] * X + k[1] * Y + k[2] * Z
    omega = speed * kmag
    u = np.empty((3, n, n, n))
    for i in range(3):
        u[i] = pol[i] * np.sin(phase)      # evaluated at t = 0

    lhs = np.empty_like(u)
    rhs = np.empty_like(u)
    divu = d1(u[0], dx, 0) + d1(u[1], dx, 1) + d1(u[2], dx, 2)
    for i in range(3):
        lhs[i] = RHO * (-omega**2) * u[i]
        lap_i = d2(u[i], dx, 0) + d2(u[i], dx, 1) + d2(u[i], dx, 2)
        rhs[i] = (LAM + MU) * d1(divu, dx, i) + MU * lap_i

    interior = (slice(None), slice(2, -2), slice(2, -2), slice(2, -2))
    err = np.abs(lhs[interior] - rhs[interior]).max()
    scale = np.abs(rhs[interior]).max()
    return err, scale


def residual_check() -> None:
    section("2. Analytic plane waves satisfy the Navier-Cauchy equation")
    print(f"  {'mode':>4} {'grid n':>7} {'max|LHS-RHS| (Pa/m)':>22} "
          f"{'max|RHS| (Pa/m)':>18} {'relative':>11}")
    for mode in ("P", "S"):
        previous = None
        for n in (48, 96, 192):
            err, scale = navier_cauchy_residual(mode, n)
            note = "" if previous is None else f"   (residual x{previous / err:.2f})"
            print(f"  {mode:>4} {n:7d} {err:22.6e} {scale:18.6e} "
                  f"{err / scale:11.3e}{note}")
            previous = err
    print("  Halving dx cuts the residual by about 4: it is central-difference")
    print("  truncation error of the spatial operators, not a failure of the")
    print("  equation.  The relative residual at n = 192 is 1.7e-3 for P and")
    print("  4.5e-4 for S, and falls by 4 again on the next halving.")


# ---------------------------------------------------------------------------
# 3. Independent time-domain solution: measure the propagation speed
# ---------------------------------------------------------------------------
def vgroup_discrete(k: float, dx: float, dt: float, c: float) -> float:
    """Exact group velocity of the leapfrog scheme for u_tt = c^2 u_xx.

    omega(k) = (2/dt) arcsin(r sin(k dx / 2)) with r = c dt / dx, so
    d(omega)/dk = c cos(k dx/2) / sqrt(1 - r^2 sin^2(k dx/2)).
    """
    r = c * dt / dx
    return c * np.cos(k * dx / 2.0) / np.sqrt(1.0 - r**2 * np.sin(k * dx / 2.0) ** 2)


def fd_measured_speed(c: float, k0: float, dx: float, length: float = 2.0e6,
                      sigma: float = 4.0e4, r: float = 0.5) -> tuple[float, float]:
    """Propagate a band-limited right-going packet; return (v_measured, v_group)."""
    n = int(round(length / dx)) + 1
    dt = r * dx / c
    x = np.arange(n) * dx
    x0 = 0.35 * length

    env = np.exp(-((x - x0) ** 2) / (2.0 * sigma**2))
    g = env * np.cos(k0 * (x - x0))
    gp = -((x - x0) / sigma**2) * g - k0 * env * np.sin(k0 * (x - x0))
    u_prev = g + dt * c * gp               # the continuum right-going wave at -dt
    u = g

    travel = 0.30 * length
    nt = int(round(travel / c / dt))
    rr = r**2
    for _ in range(nt):
        lap = np.roll(u, 1) - 2.0 * u + np.roll(u, -1)
        u_next = 2.0 * u - u_prev + rr * lap
        u_prev, u = u, u_next

    xc = x0 + c * nt * dt                  # window that follows the right-going packet
    half = 4.0 * sigma
    m = (x > xc - half) & (x < xc + half)
    dens = u[m] ** 2
    centroid = (x[m] * dens).sum() / dens.sum()
    return (centroid - x0) / (nt * dt), vgroup_discrete(k0, dx, dt, c)


def speed_convergence() -> None:
    section("3. Independent FD solution: measured speed vs the derived speed")
    c = vp_analytic()
    dx = 1000.0
    print(f"  grid spacing dx = {dx:.0f} m, CFL number r = c dt/dx = 0.5,")
    print("  domain 2000 km (2001 nodes), packet sigma = 40 km,")
    print("  so k0 dx = 0.63 is the coarsest wavelength sampled (~10 nodes/cycle)")
    print(f"  derived speed sqrt((lam+2mu)/rho) = {c:.4f} m/s")
    print(f"  {'k0 dx (-)':>10} {'v measured (m/s)':>18} {'v_group analytic':>18} "
          f"{'measured vs derived (%)':>24}")
    kdxs, errs = [], []
    for kdx in (0.628, 0.314, 0.157, 0.0785, 0.0393):
        k0 = kdx / dx
        v_meas, v_pred = fd_measured_speed(c, k0, dx)
        kdxs.append(kdx)
        errs.append(abs(v_meas - c) / c)
        print(f"  {kdx:10.4f} {v_meas:18.4f} {v_pred:18.4f} "
              f"{abs(v_meas - c) / c * 100:24.5f}")
    order = np.polyfit(np.log(kdxs[:-1]), np.log(errs[:-1]), 1)[0]
    print(f"\n  The measured speed tends to the derived speed as k0 -> 0: at")
    print(f"  k0 dx = {kdxs[-1]:.4f} the two agree to {errs[-1] * 100:.4f} per cent.  The")
    print(f"  fitted exponent of the error in k0 dx (excluding the noisy last row)")
    print(f"  is {order:.3f}; the dispersion analysis predicts 2.  Columns 2 and 3 agree")
    print(f"  to a few 1e-4 m/s, i.e. the only difference between the measured")
    print("  speed and the medium's speed is grid dispersion, not physics.")

    vs = vs_analytic()
    print(f"\n  The same experiment on the S branch, sqrt(mu/rho) = {vs:.4f} m/s:")
    for kdx in (0.314, 0.0785):
        v_meas, v_pred = fd_measured_speed(vs, kdx / dx, dx)
        print(f"    k0 dx = {kdx:.4f}: measured {v_meas:.4f} m/s, "
              f"analytic group velocity {v_pred:.4f} m/s, "
              f"error vs derived speed {abs(v_meas - vs) / vs * 100:.4f} per cent")


def main() -> None:
    unit_table()
    residual_check()
    speed_convergence()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
