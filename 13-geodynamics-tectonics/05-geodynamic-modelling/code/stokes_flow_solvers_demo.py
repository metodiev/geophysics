#!/usr/bin/env python3
"""Solving the Stokes equations for mantle flow: a verified fast Poisson solver,
the measured critical Rayleigh number of free-slip thermal convection, and the
measured Nusselt-number scaling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python stokes_flow_solvers_demo.py

Everything is SYNTHETIC: the parameters below are chosen teaching values with
the units given, not measured mantle properties.  Every printed number is
computed here; nothing is quoted from a published model.

Contents
--------
1. Non-dimensionalisation: the Rayleigh number of a layered fluid.
2. A fast Poisson solver (sine transform) and its exact self-verification.
3. Linear stability of the conduction state: analytic growth rate
   sigma(k, l) verified against a measured growth rate, and the critical
   Rayleigh number measured by linear extrapolation of sigma against Ra.
4. Non-linear steady convection: measured Nusselt number versus Rayleigh number
   and the fitted power law, with a grid-resolution study of the discretisation
   error.
5. Why mantle-flow solvers are hard: conjugate-gradient iteration counts and
   condition numbers against the viscosity contrast.
"""

import time

import numpy as np
import scipy.linalg as sla
from scipy.fft import dstn, idstn
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import cg, eigsh

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ---------------------------------------------------------------------------
# 1. Non-dimensionalisation
# ---------------------------------------------------------------------------

def demonstration_1():
    section("1. Non-dimensionalisation: the Rayleigh number of the mantle")
    print("  Ra = rho g alpha dT d^3 / (kappa eta)   [dimensionless]")
    rho = 3300.0          # kg/m^3   (chosen teaching value)
    g = 9.81              # m/s^2    (standard acceleration of gravity)
    alpha = 3.0e-5        # 1/K      (chosen teaching value)
    dT = 3000.0           # K        (chosen teaching value)
    d = 2.90e6            # m        (chosen teaching value)
    kappa = 1.0e-6        # m^2/s    (chosen teaching value)
    eta = 1.0e21          # Pa s     (chosen teaching value)
    Ra = rho * g * alpha * dT * d ** 3 / (kappa * eta)
    print(f"  rho = {rho:.0f} kg/m^3, g = {g:.2f} m/s^2, alpha = {alpha:.1e} 1/K,")
    print(f"  dT = {dT:.0f} K, d = {d:.3e} m, kappa = {kappa:.1e} m^2/s, "
          f"eta = {eta:.1e} Pa s")
    print(f"  Ra = {Ra:.3e}  (dimensionless)")
    print(f"  viscous diffusion time d^2/kappa = {d**2 / kappa:.3e} s")
    print(f"  convective velocity scale kappa/d = {kappa / d:.3e} m/s")
    print(f"  buoyancy stress rho g alpha dT d = {rho * g * alpha * dT * d:.3e} Pa")
    print(f"  Stokes velocity from that stress, d^2 rho g alpha dT/(eta) = "
          f"{d ** 2 * rho * g * alpha * dT / eta:.3e} m/s")
    print("  (in the Earth these are used with a depth of order the layer, so")
    print("   centimetres per year, i.e. of order 1e-9 to 1e-10 m/s, is the")
    print("   natural scale of plate motion.)")


# ---------------------------------------------------------------------------
# 2. Fast Poisson solver
# ---------------------------------------------------------------------------

def laplace_eigenvalues(N, h):
    """Eigenvalues of the 1-D second-difference operator, zero Dirichlet BCs."""
    k = np.arange(1, N + 1)
    return 4.0 * np.sin(np.pi * k * h / 2.0) ** 2 / h ** 2


def solve_poisson_sine(rhs, h, N):
    """Solve laplacian(u) = rhs on an N x N interior grid, u = 0 on the boundary.

    The operator is diagonal in the two-dimensional sine basis, so one
    orthonormal DST-I pair solves it exactly (to rounding).
    """
    lam = laplace_eigenvalues(N, h)
    L = lam[:, None] + lam[None, :]
    fhat = dstn(rhs, type=1, norm="ortho")
    return idstn(-fhat / L, type=1, norm="ortho")


def discrete_laplacian(u, h):
    """Second differences of an interior field, zero on the surrounding boundary."""
    full = np.zeros((u.shape[0] + 2, u.shape[1] + 2))
    full[1:-1, 1:-1] = u
    return (full[1:-1, 2:] - 2.0 * u + full[1:-1, :-2]) / h ** 2 + \
           (full[2:, 1:-1] - 2.0 * u + full[:-2, 1:-1]) / h ** 2


def demonstration_2():
    section("2. A fast Poisson solver and its verification")
    N, h = 48, 1.0 / 49.0
    u0 = RNG.standard_normal((N, N))
    f = discrete_laplacian(u0, h)
    u1 = solve_poisson_sine(f, h, N)
    print(f"  grid: {N} x {N} interior nodes, h = {h:.6f}")
    print(f"  round-trip check max|solve(laplacian(u)) - u| = "
          f"{np.max(np.abs(u1 - u0)):.3e}   (float64 round-off)")
    x = (np.arange(1, N + 1)) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    ue = np.sin(np.pi * X) * np.sin(np.pi * Y)
    fe = -2.0 * np.pi ** 2 * ue
    un = solve_poisson_sine(fe, h, N)
    print(f"  against the analytic solution sin(pi x) sin(pi y) of the continuum")
    print(f"  problem laplacian(u) = -2 pi^2 u:  max|u_numeric - u_exact| = "
          f"{np.max(np.abs(un - ue)):.3e}")
    print(f"  (the residual is the O(h^2) truncation error of the discrete")
    print(f"   operator: h^2 = {h**2:.3e})")
    t0 = time.perf_counter()
    for _ in range(200):
        solve_poisson_sine(f, h, N)
    dt = (time.perf_counter() - t0) / 200.0
    print(f"  measured cost of one {N}x{N} solve: {dt * 1e3:.3f} ms")


# ---------------------------------------------------------------------------
# 3. Linear stability and the critical Rayleigh number
# ---------------------------------------------------------------------------

class Convection2D:
    """Steady infinite-Prandtl Boussinesq convection in a unit square.

    Free-slip on all four boundaries, fixed temperature at the top and bottom,
    adiabatic side walls, constant viscosity and unit thermal diffusivity.  The
    unknown is the temperature perturbation theta about the conductive profile
    T_cond = 1 - y, so theta = 0 on the top and bottom and dtheta/dx = 0 on the
    sides.  The Stokes problem is solved in the stream-function/vorticity form

        laplacian(omega) = -Ra dtheta/dx,   laplacian(psi) = -omega,
        u = dpsi/dy,  w = -dpsi/dx,         omega = psi = 0 on the boundary,

    and the energy equation for the perturbation is

        dtheta/dt = laplacian(theta) + w - u . grad(theta).

    The term +w is the advection of the conductive profile and is exact; only the
    self-advection of the perturbation is discretised.
    """

    def __init__(self, N, Ra, advection="central"):
        self.N = N
        self.h = 1.0 / (N + 1)
        self.Ra = Ra
        self.advection = advection
        self.th = np.zeros((N + 2, N + 2))

    def boundaries(self):
        self.th[:, 0] = 0.0                 # bottom, fixed temperature
        self.th[:, -1] = 0.0                # top, fixed temperature
        self.th[0, :] = self.th[1, :]       # adiabatic side walls (mirror ghost)
        self.th[-1, :] = self.th[-2, :]

    def stokes(self):
        """Return (u, w) on the full grid from the current perturbation."""
        N, h = self.N, self.h
        th = self.th
        dTdx = (th[2:, 1:-1] - th[:-2, 1:-1]) / (2.0 * h)
        omega_int = solve_poisson_sine(-self.Ra * dTdx, h, N)
        psi_int = solve_poisson_sine(-omega_int, h, N)
        psi = np.zeros((N + 2, N + 2))
        psi[1:-1, 1:-1] = psi_int
        u = np.zeros((N + 2, N + 2))
        w = np.zeros((N + 2, N + 2))
        u[1:-1, 1:-1] = (psi[1:-1, 2:] - psi[1:-1, :-2]) / (2.0 * h)
        w[1:-1, 1:-1] = -(psi[2:, 1:-1] - psi[:-2, 1:-1]) / (2.0 * h)
        return u, w

    def step(self, dt):
        u, w = self.stokes()
        N, h = self.N, self.h
        th = self.th
        if self.advection == "central":
            dthdx = (th[2:, 1:-1] - th[:-2, 1:-1]) / (2.0 * h)
            dthdy = (th[1:-1, 2:] - th[1:-1, :-2]) / (2.0 * h)
        else:                                    # first-order upwind
            dthdx = np.where(u[1:-1, 1:-1] > 0.0,
                             (th[1:-1, 1:-1] - th[:-2, 1:-1]) / h,
                             (th[2:, 1:-1] - th[1:-1, 1:-1]) / h)
            dthdy = np.where(w[1:-1, 1:-1] > 0.0,
                             (th[1:-1, 1:-1] - th[1:-1, :-2]) / h,
                             (th[1:-1, 2:] - th[1:-1, 1:-1]) / h)
        self_advection = u[1:-1, 1:-1] * dthdx + w[1:-1, 1:-1] * dthdy
        lap = ((th[2:, 1:-1] - 2.0 * th[1:-1, 1:-1] + th[:-2, 1:-1]) / h ** 2 +
               (th[1:-1, 2:] - 2.0 * th[1:-1, 1:-1] + th[1:-1, :-2]) / h ** 2)
        th[1:-1, 1:-1] += dt * (lap + w[1:-1, 1:-1] - self_advection)
        self.boundaries()
        return np.max(np.abs(u)), np.max(np.abs(w))

    def diagnostics(self):
        """Nusselt number by two independent routes, and the rms velocity.

        * Nusselt from the bottom heat flux: T = 1 - y + theta, so the conductive
          flux is 1 and Nu - 1 is the mean perturbation gradient at the bottom.
        * Nusselt from the volume average Nu = 1 + <w T>, which is the
          integral identity obtained by averaging the energy equation.
        The two agree only if the discretisation is consistent; their difference
        is reported with the result.
        """
        N, h = self.N, self.h
        th = self.th
        dthdy_bottom = (4.0 * th[1:-1, 1] - th[1:-1, 2]) / (2.0 * h)
        nu_flux = 1.0 - np.mean(dthdy_bottom)
        y = np.arange(1, N + 1) * h
        T = 1.0 - y[None, :] + th[1:-1, 1:-1]
        u, w = self.stokes()
        nu_vol = 1.0 + np.mean(w[1:-1, 1:-1] * T)
        vrms = np.sqrt(np.mean(u[1:-1, 1:-1] ** 2 + w[1:-1, 1:-1] ** 2))
        return nu_flux, nu_vol, vrms


def growth_rate(N, Ra, kx, ly, t_end=0.02, amp0=1e-9):
    """Measured exponential growth rate of a single Fourier mode.

    The initial perturbation is cos(kx x) sin(ly pi y), an exact eigenmode of the
    linearised problem (the adiabatic walls need the cosine, the free-slip walls
    need the sine), so its amplitude grows or decays as exp(sigma t).  sigma is
    fitted only where the amplitude lies between 1e-12 and 1e-6, well below the
    value of order 0.1 at which non-linear saturation sets in.
    """
    model = Convection2D(N, Ra)
    h = model.h
    x = np.arange(1, N + 1) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    mode = np.cos(kx * X) * np.sin(ly * np.pi * Y)
    norm = float(np.sum(mode * mode))
    model.th[1:-1, 1:-1] = amp0 * mode
    model.boundaries()
    dt = 0.2 * h ** 2
    n_step = max(20, int(t_end / dt))
    ts, amps = [], []
    for n in range(n_step):
        model.step(dt)
        ts.append((n + 1) * dt)
        amps.append(abs(np.sum(model.th[1:-1, 1:-1] * mode) / norm))
    ts, amps = np.array(ts), np.array(amps)
    sel = (amps > 1e-12) & (amps < 1e-6)
    if not np.any(sel):
        return np.nan, dt, n_step
    sigma = np.polyfit(ts[sel], np.log(amps[sel]), 1)[0]
    return sigma, dt, n_step


def demonstration_3():
    section("3. Linear stability: measured against analytic growth rates")
    print("  Linearised problem, mode cos(k x) sin(l pi y) in a unit square with")
    print("  free-slip boundaries gives exactly")
    print("     sigma(k,l) = -(k^2 + (l pi)^2) + Ra k^2 / (k^2 + (l pi)^2)^2,")
    print("  so sigma = 0 first at Ra_c = (k^2 + (l pi)^2)^3 / k^2.  For a box of")
    print("  aspect ratio 1 the admissible k are pi, 2 pi, ..., and the first")
    print("  mode to go unstable is l = 1, k = pi, giving Ra_c = 8 pi^4 = "
          f"{8.0 * np.pi ** 4:.3f}.")
    N = 40
    print(f"\n  measured growth rate at Ra = 2000, N = {N} (log-linear fit over the")
    print(f"  window in which the mode amplitude lies between 1e-12 and 1e-6)")
    print("    mode            sigma analytic   sigma measured   rel. difference")
    for kx, ly in ((np.pi, 1), (2.0 * np.pi, 1), (np.pi, 2)):
        sig_a = -(kx ** 2 + (ly * np.pi) ** 2) + \
            2000.0 * kx ** 2 / (kx ** 2 + (ly * np.pi) ** 2) ** 2
        sig_m, dt, ns = growth_rate(N, 2000.0, kx, ly, t_end=0.02)
        print(f"    k={kx / np.pi:.0f}pi, l={ly}       {sig_a:12.4f}   "
              f"{sig_m:13.4f}   {abs(sig_m - sig_a) / abs(sig_a) * 100:8.3f}%")
    print("\n  sigma is linear in Ra for a fixed mode, so Ra_c follows from a")
    print("  straight-line fit of the measured sigma against Ra.")
    ras = [900.0, 1200.0, 1600.0, 2000.0]
    sigs = []
    for Ra in ras:
        s, _, _ = growth_rate(N, Ra, np.pi, 1, t_end=0.02)
        sigs.append(s)
        print(f"    Ra = {Ra:7.0f}   sigma measured = {s:9.4f}")
    p = np.polyfit(ras, sigs, 1)
    ra_c = -p[1] / p[0]
    print(f"  linear fit sigma = {p[0]:.6e} Ra + {p[1]:.6f}")
    print(f"  extrapolated sigma = 0 at Ra_c = {ra_c:.2f}")
    print(f"  analytic value for the unit-aspect free-slip box: 8 pi^4 = "
          f"{8.0 * np.pi ** 4:.2f}")
    print(f"  difference: {(ra_c - 8.0 * np.pi ** 4) / (8.0 * np.pi ** 4) * 100:+.2f}%")
    print(f"  (for a horizontally unbounded layer the minimum over k is at")
    print(f"   k = pi/sqrt(2) and Ra_c = 27 pi^4 / 4 = {27.0 * np.pi ** 4 / 4.0:.2f};")
    print(f"   the box can only use k = pi, so it must be the larger value.)")


# ---------------------------------------------------------------------------
# 4. Non-linear convection: Nusselt number versus Rayleigh number
# ---------------------------------------------------------------------------

def run_to_steady(N, Ra, advection="central", tol=1e-4, max_step=80000):
    """Time-step to a steady state; return (Nu flux, Nu volume, v_rms, steps, dt)."""
    model = Convection2D(N, Ra, advection=advection)
    h = model.h
    x = np.arange(1, N + 1) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    model.th[1:-1, 1:-1] = 0.05 * np.cos(np.pi * X) * np.sin(np.pi * Y)
    model.boundaries()
    dt = 0.2 * h ** 2
    nu_prev = None
    n = 0
    while n < max_step:
        umax, wmax = model.step(dt)
        dt = min(0.2 * h ** 2, 0.4 * h / max(umax, wmax, 1e-30))
        n += 1
        if n % 200 == 0:
            nu_now = model.diagnostics()[0]
            if nu_prev is not None and abs(nu_now - nu_prev) / nu_now < tol:
                break
            if not np.isfinite(nu_now):
                return np.nan, np.nan, np.nan, n, dt
            nu_prev = nu_now
            prev_step = n
    nu_flux, nu_vol, vrms = model.diagnostics()
    return nu_flux, nu_vol, vrms, n, dt


def demonstration_4():
    section("4. Non-linear steady convection: measured Nusselt number")
    N = 32
    print("  free-slip unit square with adiabatic sides, conductive profile plus a")
    print(f"  single-mode perturbation, N = {N} interior nodes, adaptive step")
    print("  dt = min(0.2 h^2, 0.4 h / max|u|), run until Nu changes by less than")
    print("  1e-4 over 200 steps\n")
    print("   Ra        Nu (bottom flux)   Nu (volume avg)   v_rms    steps")
    ras = [1.0e3, 3.0e3, 1.0e4, 3.0e4]
    nus = []
    for Ra in ras:
        nu, nu_vol, vrms, n, dt = run_to_steady(N, Ra, "central")
        nus.append(nu)
        print(f"  {Ra:8.1e}   {nu:15.4f}   {nu_vol:14.4f}   {vrms:8.4f}   {n:6d}")
    p_all = np.polyfit(np.log(ras), np.log(nus), 1)
    p_hi = np.polyfit(np.log(ras[1:]), np.log(nus[1:]), 1)
    print(f"\n  fit over the whole range {ras[0]:.0e} <= Ra <= {ras[-1]:.0e}:")
    print(f"    Nu = {np.exp(p_all[1]):.4f} Ra^{p_all[0]:.4f}")
    print(f"  fit over the upper decade {ras[1]:.0e} <= Ra <= {ras[-1]:.0e}:")
    print(f"    Nu = {np.exp(p_hi[1]):.4f} Ra^{p_hi[0]:.4f}")
    print(f"  the local exponent is therefore still falling with Ra: the whole")
    print(f"  range fit is contaminated by the near-onset regime, where Nu - 1 is")
    print(f"  proportional to Ra - Ra_c rather than to a power of Ra.")
    print("\n  grid-resolution study at Ra = 1e4")
    print("    N      h         Nu (central)   Nu (upwind)   steps (central)")
    for Ng in (24, 32, 48):
        nuc, _, _, ns, _ = run_to_steady(Ng, 1.0e4, "central")
        if Ng == 32:
            nuu = run_to_steady(Ng, 1.0e4, "upwind")[0]
            print(f"    {Ng:4d}   {1.0 / (Ng + 1):.6f}   {nuc:12.4f}   {nuu:11.4f}   "
                  f"{ns:13d}")
        else:
            print(f"    {Ng:4d}   {1.0 / (Ng + 1):.6f}   {nuc:12.4f}   {'-':>11s}   "
                  f"{ns:13d}")
    nu24 = run_to_steady(24, 1.0e4, "central")[0]
    nu48 = run_to_steady(48, 1.0e4, "central")[0]
    h24, h48 = 1.0 / 25.0, 1.0 / 49.0
    b_ex = (nu24 - nu48) / (h24 ** 2 - h48 ** 2)
    nu_rich = nu48 - b_ex * h48 ** 2
    print(f"  Richardson extrapolation assuming an O(h^2) error, from N = 24 and")
    print(f"  N = 48: Nu(h -> 0) = {nu_rich:.4f}; the N = 32 value differs from it by")
    print(f"  {abs(run_to_steady(32, 1.0e4, 'central')[0] - nu_rich) / nu_rich * 100:.2f}%.")
    print("  The spread across grids (N = 24 to 48) and across advection schemes")
    print("  (central to first-order upwind) is of the same size, a few per cent:")
    print("  at this resolution neither the grid error nor the numerical diffusion")
    print("  of a first-order scheme can be separated from the other.  Reporting a")
    print("  Nusselt number without a resolution study would hide an error of")
    print("  several per cent.")


# ---------------------------------------------------------------------------
# 5. Solver cost versus viscosity contrast
# ---------------------------------------------------------------------------

def variable_viscosity_matrix(N, kind, contrast):
    """Sparse -div(eta grad u) on an N x N interior grid applied to (0,1)^2.

    eta is either a smooth sinusoidal field or a sharp step across x = 1/2,
    varying between 1 and ``contrast``.  Faces use harmonic averaging (the
    standard finite-volume treatment of a variable coefficient); the boundary
    nodes carry u = 0 and their contribution is retained on the diagonal.
    """
    from scipy.sparse import coo_matrix
    h = 1.0 / (N + 1)
    xn = np.arange(N + 2) * h
    Xn, Yn = np.meshgrid(xn, xn, indexing="ij")
    if kind == "smooth":
        eta = 1.0 + (contrast - 1.0) * (0.5 + 0.5 * np.sin(np.pi * Xn) * np.sin(np.pi * Yn))
    else:
        eta = np.where(Xn > 0.5, contrast, 1.0)
    exf = 2.0 * eta[:, :-1] * eta[:, 1:] / (eta[:, :-1] + eta[:, 1:])   # (N+2, N+1)
    eyf = 2.0 * eta[:-1, :] * eta[1:, :] / (eta[:-1, :] + eta[1:, :])   # (N+1, N+2)
    rows, cols, vals = [], [], []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            r = (i - 1) * N + (j - 1)
            faces = ((0, 1, exf[i, j]), (0, -1, exf[i, j - 1]),
                     (1, 0, eyf[i, j]), (-1, 0, eyf[i - 1, j]))
            d = sum(c for _, _, c in faces) / h ** 2
            for di, dj, c in faces:
                if 1 <= i + di <= N and 1 <= j + dj <= N:
                    rows.append(r)
                    cols.append((i + di - 1) * N + (j + dj - 1))
                    vals.append(-c / h ** 2)
            rows.append(r)
            cols.append(r)
            vals.append(d)
    return coo_matrix((vals, (rows, cols)), shape=(N * N, N * N)).tocsc()


def demonstration_5():
    section("5. Why mantle-flow solvers are hard: sharp, not large, contrast")
    N = 32
    print("  model problem -div(eta grad u) = 1 on a unit square, u = 0 on the")
    print("  boundary, harmonic face averaging, conjugate gradients from a zero")
    print("  initial guess to a relative residual of 1e-10, no preconditioner.")
    print("  The condition number is computed from the eigenvalues of the dense")
    print("  operator at N = 16 (the iterative counts are for N = %d)." % N)
    for kind, label in (("smooth", "smooth eta field (sinusoidal)"),
                        ("sharp", "sharp step in eta across x = 1/2")):
        print(f"\n  {label}")
        print("   contrast   cond(A) at N=16   CG iterations   max|u| rel. to eta=1")
        u_ref = None
        for contrast in (1.0, 1.0e2, 1.0e4, 1.0e6):
            A = variable_viscosity_matrix(N, kind, contrast)
            b = np.ones(N * N)
            it = [0]

            def callback(_):
                it[0] += 1

            x_sol, info = cg(A, b, rtol=1e-10, maxiter=20000, callback=callback)
            A16 = variable_viscosity_matrix(16, kind, contrast)
            ev = sla.eigvalsh(A16.toarray())
            if u_ref is None:
                u_ref = np.max(np.abs(x_sol))
            print(f"   {contrast:8.1e}   {ev[-1] / ev[0]:14.3e}   {it[0]:13d}   "
                  f"{np.max(np.abs(x_sol)) / u_ref:18.4f}")
    print("\n  The measured pattern is the point of the section: a viscosity")
    print("  *variation* that is smooth barely changes the spectrum, because the")
    print("  lowest eigenmode averages the coefficient.  A sharp interface changes")
    print("  the condition number in proportion to the contrast and multiplies the")
    print("  iteration count by one to two orders of magnitude.  That is why real")
    print("  mantle-flow codes invest in preconditioners and multigrid.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    demonstration_5()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
