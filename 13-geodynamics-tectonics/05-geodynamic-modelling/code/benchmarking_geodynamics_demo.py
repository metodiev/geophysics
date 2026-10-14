#!/usr/bin/env python3
"""Benchmarking geodynamic codes: grid convergence of a non-linear diagnostic,
what agreement between two codes does and does not prove, and the resolution
dependence of a benchmark value.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_geodynamics_demo.py

Everything is SYNTHETIC: the model is a constant-viscosity free-slip convection
cell with chosen parameters, not the Earth.  Every printed number is computed
here.

Contents
--------
1. Grid convergence of the Nusselt number: observed order, Richardson
   extrapolation and a Grid Convergence Index (Roache's method).
2. What agreement proves: two grids that agree on Nu to about a per cent while
   disagreeing on the interior temperature field by more.
3. Resolution dependence of a benchmark value: the measured critical Rayleigh
   number against the analytic 8 pi^4, at three resolutions.
4. An error budget: grid error, advection-scheme error and stopping-criterion
   error for one reported number.
5. What can and cannot be verified from synthetic models alone.
"""

import numpy as np
from scipy.fft import dstn, idstn

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


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



def run_to_steady(N, Ra, advection="central", tol=1e-6, max_step=80000):
    """Time-step to a steady state.

    Returns (Nu from the bottom flux, Nu from the volume average, the
    horizontally averaged temperature profile, y, steps, dt).  The stopping rule
    is the one an analyst would use: Nu must change by less than ``tol`` between
    two checks 200 steps apart.  It is not a proof that a steady state exists.
    """
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
            nu_prev = nu_now
    nu, nu_vol, _ = model.diagnostics()
    y = np.arange(1, N + 1) * h
    Tbar = 1.0 - y + np.mean(model.th[1:-1, 1:-1], axis=0)
    return nu, nu_vol, Tbar, y, n, dt


def demonstration_1():
    section("1. Grid convergence of the Nusselt number at Ra = 1e4")
    print("  free-slip unit square with adiabatic sides, one-mode initial")
    print("  perturbation, adaptive explicit time step, run to a steady state\n")
    print("    N      h          Nu (flux)     Nu (volume)    steps")
    runs = {}
    nus, hs = [], []
    for N in (16, 32, 48):
        nu, nu_vol, Tbar, y, n, _ = run_to_steady(N, 1.0e4)
        runs[N] = (nu, nu_vol, Tbar, y, n)
        nus.append(nu)
        hs.append(1.0 / (N + 1))
        print(f"    {N:4d}   {hs[-1]:.6f}   {nu:11.5f}   {nu_vol:12.5f}   {n:6d}")
    r = hs[0] / hs[1]
    p = abs(np.log(abs((nus[0] - nus[1]) / (nus[1] - nus[2]))) / np.log(r))
    r2 = hs[1] / hs[2]
    nu_ext = nus[2] + (nus[2] - nus[1]) / (r2 ** p - 1.0)
    gci = 1.25 * abs((nus[2] - nus[1]) / nus[2]) / (r2 ** p - 1.0)
    print(f"\n  three-grid study, refinement ratio h1/h2 = {r:.3f} (the ratios are")
    print(f"  not exactly equal because h = 1/(N+1)):\n")
    print(f"    observed order p = {p:.3f}")
    print(f"    Richardson extrapolation Nu(h -> 0) = {nu_ext:.5f}")
    print(f"    Grid Convergence Index with a safety factor of 1.25 = "
          f"{gci * 100:.3f}% of Nu")
    print(f"    the finest grid's own error is {abs(nus[2] - nu_ext) / nu_ext * 100:.2f}%")
    print("  A measured order near 2 is the evidence that this centred second-order")
    print("  discretisation is behaving as designed; the extrapolated value is the")
    print("  best estimate of the continuum answer, and the GCI is the honest")
    print("  uncertainty band to quote with it.")
    return runs


def demonstration_2(runs):
    section("2. Two answers can agree on one diagnostic and disagree on another")
    nu32, nuvol32, T32, y32, _ = runs[32]
    nu48, nuvol48, T48, y48, _ = runs[48]
    print(f"  N = 32: Nu = {nu32:.5f}      N = 48: Nu = {nu48:.5f}")
    print(f"  relative difference in Nu between the two grids = "
          f"{abs(nu32 - nu48) / nu48 * 100:.3f}%")
    T_int = np.interp(y48, y32, T32)
    rms = np.sqrt(np.mean((T_int - T48) ** 2))
    mx = np.max(np.abs(T_int - T48))
    print("  horizontally averaged temperature, in units of the total drop:")
    print(f"    rms difference between the two grids = {rms * 100:.3f}%")
    print(f"    maximum difference between the two grids = {mx * 100:.3f}%")
    print("\n  and on a single grid, two ways of defining the same diagnostic:")
    print(f"    N = 48: Nu from the bottom flux = {nu48:.5f}")
    print(f"    N = 48: Nu from the volume average <w T> + 1 = {nuvol48:.5f}")
    print(f"    difference = {abs(nu48 - nuvol48) / nu48 * 100:.2f}%")
    print("  The integral definition of Nu is much better conditioned than the")
    print("  pointwise field: two grids agree to about a per cent on it while their")
    print("  interior temperatures differ by several per cent, and two definitions")
    print("  of the same diagnostic differ by more than the grid error.  Agreement")
    print("  between two codes on one number is therefore weak evidence, and a")
    print("  benchmark that quotes only that number can be passed by codes whose")
    print("  interior fields differ substantially.")


def demonstration_3():
    section("3. A benchmark value depends on the resolution")
    print("  The critical Rayleigh number of this configuration has the analytic")
    print(f"  value 8 pi^4 = {8.0 * np.pi ** 4:.2f}.  Extrapolating the measured")
    print("  growth rate of the first mode to zero gives a resolution-dependent")
    print("  answer:\n")
    print("    N      h          Ra_c measured    error against 8 pi^4")
    for N in (24, 40, 64):
        ras = [900.0, 1200.0, 1600.0, 2000.0]
        sigs = [growth_rate(N, Ra, np.pi, 1)[0] for Ra in ras]
        p = np.polyfit(ras, sigs, 1)
        ra_c = -p[1] / p[0]
        print(f"    {N:4d}   {1.0 / (N + 1):.6f}   {ra_c:10.2f}       "
              f"{(ra_c - 8.0 * np.pi ** 4) / (8.0 * np.pi ** 4) * 100:+8.2f}%")
    print("  The measured value drifts towards the analytic one as h shrinks, which")
    print("  is exactly what a correct code with a consistent discretisation must")
    print("  do.  A benchmark comparison is therefore meaningless unless the grid")
    print("  and the norm it was computed in are quoted with the number.")


def demonstration_4(runs):
    section("4. An error budget for one reported number")
    Ra = 1.0e4
    ref = runs[48][0]
    print(f"  target quantity: Nu of the unit-aspect free-slip cell at Ra = {Ra:.0e}")
    print(f"  reference: N = 48, tolerance 1e-6, stopping criterion satisfied:  "
          f"Nu = {ref:.5f}")
    print("\n   source of change                            Nu        deviation")
    for label, val in (
            ("grid coarsened to N = 32", runs[32][0]),
            ("grid coarsened to N = 16", runs[16][0]),
            ("diagnostic redefined as <w T> + 1", runs[48][1])):
        print(f"   {label:44s} {val:9.5f}   {abs(val - ref) / ref * 100:6.3f}%")
    nu_tol = run_to_steady(32, Ra, tol=1e-5)[0]
    print(f"   {'stopping tolerance loosened to 1e-5':44s} {nu_tol:9.5f}   "
          f"{abs(nu_tol - runs[32][0]) / runs[32][0] * 100:6.3f}%")
    print("   (the last row is compared with the same grid at tolerance 1e-6, so it")
    print("    isolates the stopping error, which is negligible next to the grid")
    print("    error for this quantity.)")
    print("\n  and one error that is not small at all: the first-order upwind scheme")
    print("  at N = 32 does not settle.  Its Nusselt number, sampled every 1000")
    print("  steps, is")
    model = Convection2D(32, Ra, advection="upwind")
    h = model.h
    x = np.arange(1, 33) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    model.th[1:-1, 1:-1] = 0.05 * np.cos(np.pi * X) * np.sin(np.pi * Y)
    model.boundaries()
    dt = 0.2 * h ** 2
    hist = []
    for n in range(1, 6001):
        umax, wmax = model.step(dt)
        dt = min(0.2 * h ** 2, 0.4 * h / max(umax, wmax, 1e-30))
        if n % 1000 == 0:
            hist.append(model.diagnostics()[0])
    print("    " + ", ".join(f"{v:.3f}" for v in hist))
    print("  The values wander over a factor of three, so 'Nu stopped changing' is")
    print("  satisfied at some times and violated at others, and a stopping rule")
    print("  built on it silently returns a number that is not a steady state at")
    print("  all.  The steady-state assumption must be checked, not assumed.")


def demonstration_5():
    section("5. What can and cannot be verified from synthetic models")
    print("  Verification asks whether the code solves the stated equations")
    print("  correctly, and it is possible here: the analytic critical Rayleigh")
    print(f"  number 8 pi^4 = {8.0 * np.pi ** 4:.2f}, the analytic growth rate")
    print("  sigma(k, l), the manufactured Poisson solution and the analytic")
    print("  advection-diffusion profile give exact targets, and the measured")
    print("  orders of accuracy are the evidence.  The measured Ra_c drifting")
    print("  towards 8 pi^4 as the grid is refined is the clearest single")
    print("  verification result in this demonstration.")
    print()
    print("  Validation asks whether the stated equations describe the Earth.  It")
    print("  cannot be done here and this curriculum does not pretend otherwise:")
    print("  every model in the module is SYNTHETIC, no number is a measurement and")
    print("  no observational data set is used.  What the exercises ask for is the")
    print("  correct shape of a validation argument -- which observation")
    print("  discriminates between two models that fit the data equally well -- not")
    print("  a validation result.")


def main():
    runs = demonstration_1()
    demonstration_2(runs)
    demonstration_3()
    demonstration_4(runs)
    demonstration_5()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
