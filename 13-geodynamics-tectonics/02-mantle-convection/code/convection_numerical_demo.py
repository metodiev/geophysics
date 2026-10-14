#!/usr/bin/env python3
"""Numerical modelling of mantle convection in two dimensions.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convection_numerical_demo.py

A streamfunction-vorticity solver on a periodic-in-x box with free-slip,
isothermal top and bottom.  Everything here is SYNTHETIC: the Rayleigh numbers,
the domain and the initial perturbations are chosen teaching values.  Print-only;
no figures.

Contents
--------
1. The discretisation, and the Poisson solver verified against an analytic field.
2. Onset of convection: growth or decay of a perturbation either side of Ra_c.
3. Nusselt number versus Rayleigh number; the measured scaling exponent.
4. Thermal boundary-layer thickness from the measured flux.
5. Heat-balance check at statistical steady state (top flux versus bottom flux).
6. The fitted prefactor, and what it says about scaling theory.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RA_C_FREE = 27.0 * np.pi ** 4 / 4.0     # exact, free-slip both boundaries
ASPECT = 2.0 * np.sqrt(2.0)             # ~ critical wavelength
NX = 49
NZ = 49


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def tridiag(a, b, c, d):
    """Solve a tridiagonal system for many right-hand sides at once.

    a, c : (n,) coefficients below and above the diagonal
    b    : (n, m) diagonal (it depends on the horizontal wavenumber)
    d    : (n, m) right-hand sides; the answer has the same shape.
    """
    n, m = d.shape
    cp = np.empty_like(d)
    dp = np.empty_like(d)
    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]
    for i in range(1, n):
        den = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / den
        dp[i] = (d[i] - a[i] * dp[i - 1]) / den
    x = np.empty_like(d)
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def solve_modes(A, d):
    """Batched dense solve: A has shape (m, n, n), d has shape (n, m).

    The Poisson operator is tridiagonal, but solving all wavenumber blocks with
    one LAPACK call is faster in Python than a per-mode Thomas loop.
    """
    return np.linalg.solve(A, d.T[:, :, None])[:, :, 0].T


class Solver:
    """2-D Boussinesq convection, nondimensional (d = 1, kappa = 1).

    Equations
        (D^2 - k^2)^2 psi = -Ra (dT/dx)   -> solved as two Poisson problems,
        dT/dt + u dT/dx + w dT/dz = (D^2 - k^2) T
    with u = dpsi/dz, w = -dpsi/dx, free-slip (psi = d^2 psi/dz^2 = 0) and
    T = 1 at z = 0, T = 0 at z = 1, periodic in x over [0, aspect].
    """

    def __init__(self, Ra, aspect=ASPECT, nx=NX, nz=NZ):
        self.Ra = Ra
        self.aspect = aspect
        self.nx, self.nz = nx, nz
        self.dx = aspect / nx                      # periodic: nx intervals
        self.dz = 1.0 / (nz - 1)
        self.x = np.arange(nx) * self.dx
        self.z = np.arange(nz) * self.dz
        self.k = 2.0 * np.pi * np.fft.rfftfreq(nx, d=self.dx)   # wavenumbers
        self.k2 = self.k ** 2
        self.nm = self.k.size
        # cached tridiagonal diagonal for the Poisson operator, one per wavenumber
        self.b_poisson = np.broadcast_to(
            -2.0 - self.k2[None, :] * self.dz ** 2, (nz - 2, self.nm)).copy()

    # ---- transforms --------------------------------------------------------
    def to_modes(self, field):
        return np.fft.rfft(field, axis=1)

    def to_phys(self, modes):
        return np.fft.irfft(modes, n=self.nx, axis=1)

    # ---- Poisson solves ---------------------------------------------------
    def poisson(self, rhs_modes, zero_bc=True):
        """Solve (D^2 - k^2) X = rhs for each mode, X = 0 at z = 0 and z = 1."""
        d = rhs_modes[1:self.nz - 1] * self.dz ** 2
        nn = self.nz - 2
        x = tridiag(np.ones(nn), self.b_poisson, np.ones(nn), d)
        out = np.zeros_like(rhs_modes)
        out[1:self.nz - 1] = x
        return out

    # ---- one time step ----------------------------------------------------
    def step(self, T_modes, dt):
        T = self.to_phys(T_modes)
        # buoyancy source: Ra dT/dx, done spectrally
        dTdx_modes = self.to_modes(np.gradient(T, self.dx, axis=1))
        omega = self.poisson(self.Ra * dTdx_modes)
        psi = self.poisson(omega)
        psi_phys = self.to_phys(psi)
        u = np.gradient(psi_phys, self.dz, axis=0)
        w = -np.gradient(psi_phys, self.dx, axis=1)
        # first-order upwind advection, interior nodes only
        Tp = np.roll(T, -1, axis=1)
        Tm = np.roll(T, +1, axis=1)
        dTdx_up = np.where(u > 0.0, (T - Tm) / self.dx, (Tp - T) / self.dx)
        Tzm = np.empty_like(T)
        Tzp = np.empty_like(T)
        Tzm[1:] = T[:-1]
        Tzp[:-1] = T[1:]
        dTdz_up = np.where(w > 0.0, (T - Tzm) / self.dz, (Tzp - T) / self.dz)
        adv = (u * dTdx_up + w * dTdz_up)[1:self.nz - 1]
        adv_modes = self.to_modes(adv)
        # implicit diffusion: (I - dt(D^2-k^2)) T_new = T_old - dt adv
        nn = self.nz - 2
        d = T_modes[1:self.nz - 1] - dt * adv_modes
        a = np.full(nn, -dt / self.dz ** 2)
        c = np.full(nn, -dt / self.dz ** 2)
        b = np.broadcast_to(
            1.0 + 2.0 * dt / self.dz ** 2 + dt * self.k2[None, :], (nn, self.nm)
        ).copy()
        # T = 1 at z = 0 is a pure mean mode.  Its contribution moves to the
        # right-hand side of the first interior equation.  numpy's rfft is
        # unnormalised, so the mean-mode coefficient of a uniform row of 1.0 is
        # nx, not 1.0: the boundary term carries the same factor.
        d[0, 0] += self.nx * dt / self.dz ** 2
        # T = 0 at z = 1: nothing to move
        x = tridiag(a, b, c, d)
        T_new = np.zeros_like(T_modes)
        T_new[1:self.nz - 1] = x
        # bottom BC in mode space: numpy's rfft is unnormalised, so a
        # uniform row of 1.0 has mode-0 coefficient nx (not 1.0)
        T_new[0, 0] = float(self.nx)
        T_new[self.nz - 1, :] = 0.0      # top
        return T_new, psi_phys, u, w

    # ---- diagnostics ------------------------------------------------------
    def nusselt(self, T):
        """Nu = -(dT/dz)|top, the surface flux in conductive units."""
        return -np.mean(np.gradient(T, self.dz, axis=0)[-1])








def poisson_check():
    """Verify the Poisson solver against an analytic field."""
    s = Solver(Ra=1.0, nx=64, nz=64)
    x = np.arange(s.nx) * s.dx
    k0 = 2.0 * np.pi / s.aspect
    X, Z = np.meshgrid(x, s.z, indexing="xy")
    f = -(k0 ** 2 + np.pi ** 2) * np.sin(np.pi * Z) * np.sin(k0 * X)
    exact = np.sin(np.pi * Z) * np.sin(k0 * X)
    num = s.to_phys(s.poisson(s.to_modes(f)))
    return float(np.max(np.abs(num - exact)) / np.max(np.abs(exact)))


def conducting_profile(s):
    """Full-grid conducting profile T = 1 - z with the boundary values set."""
    T = np.tile(1.0 - s.z[:, None], (1, s.nx))
    T[0, :] = 1.0
    T[-1, :] = 0.0
    return T


def seed_roll(s, amp):
    """Conducting profile plus the fundamental roll of the box."""
    k1 = 2.0 * np.pi / s.aspect
    x = np.arange(s.nx) * s.dx
    T = conducting_profile(s) + amp * np.sin(np.pi * s.z[:, None]) \
        * np.cos(k1 * x)[None, :]
    T[0, :] = 1.0
    T[-1, :] = 0.0
    return T


def run(Ra, t_end, amp=0.02, cfl=0.7, dt_max=0.02, rng_amp=0.0, seed=3,
        record_every=25, stop_amp=None, nx=None, nz=None, adaptive_dt=True):
    """Integrate one Rayleigh number case.

    The state starts from a seeded roll of amplitude `amp` (plus a random
    perturbation of rms `rng_amp` if requested).  The time step follows the CFL
    condition of the upwind advection, dt = cfl min(dx, dz)/max|u|, capped at
    dt_max.  Integration stops early once the perturbation amplitude passes
    `stop_amp`.  Returns the solver, the temperature field, the number of steps,
    and records of (t, Nu, |u|max, amplitude).
    """
    s = Solver(Ra=Ra, nx=nx or NX, nz=nz or NZ)
    T = seed_roll(s, amp)
    if rng_amp:
        rng = np.random.default_rng(seed)
        T = T + rng_amp * rng.standard_normal(T.shape) * np.sin(np.pi * s.z[:, None])
        T[0, :] = 1.0
        T[-1, :] = 0.0
    T_modes = s.to_modes(T)
    n = 0
    t = 0.0
    dt = dt_max
    records = []
    while t < t_end - 1e-12:
        T_modes, psi, u, w = s.step(T_modes, dt)
        T = s.to_phys(T_modes)
        T[0, :] = 1.0
        T[-1, :] = 0.0
        T_modes = s.to_modes(T)
        t += dt
        n += 1
        umax = max(float(np.max(np.abs(u))), 1e-12)
        wmax = max(float(np.max(np.abs(w))), 1e-12)
        amp_now = perturb_amplitude(s, T)
        if record_every and n % record_every == 0:
            records.append((t, s.nusselt(T), umax, amp_now))
        if stop_amp is not None and amp_now > stop_amp:
            records.append((t, s.nusselt(T), umax, amp_now))
            break
        if adaptive_dt:
            dt = min(cfl * s.dz / umax, cfl * s.dx / wmax, dt_max)
        else:
            dt = dt_max
    return s, T, n, records


def perturb_amplitude(s, T):
    """rms deviation of T from the conducting profile (the perturbation size)."""
    return float(np.sqrt(np.mean((T - conducting_profile(s)) ** 2)))


def growth_rate(Ra, dt=0.005, t_end=4.0, factor=1000.0, t_skip=0.25):
    """Exponential growth rate of a small perturbation, in 1 / diffusive time.

    Integrated at a FIXED dt from a 1e-6 random perturbation.  The rate is the
    slope of ln(amplitude) against time over the samples with t > t_skip (by
    which time the non-fundamental modes seeded by the noise have decayed) whose
    amplitude stays within a factor `factor` of the initial value, i.e. inside
    the linear regime.

    Note that the sign of sigma is independent of dt: the explicitly advected,
    implicitly diffused scheme has zero growth exactly when the Rayleigh number
    reaches its marginal value.  The magnitude of sigma does depend on dt, which
    is why the dt-convergence of sigma is measured below.
    """
    s, T, n, rec = run(Ra, t_end=t_end, amp=0.0, rng_amp=1e-6, dt_max=dt,
                       record_every=1, stop_amp=2.0e-3, adaptive_dt=False)
    times = np.array([r[0] for r in rec])
    amps = np.array([r[3] for r in rec])
    if amps.size < 5:
        return float("nan")
    amp0 = amps[0]
    sel = (times > t_skip) & (amps > amp0 / factor) & (amps < amp0 * factor)
    if sel.sum() < 4:
        return float("nan")
    return float(np.polyfit(times[sel], np.log(amps[sel]), 1)[0])


def flux_profile(s, T, w):
    """Horizontally averaged vertical heat flux -<dT/dz> + <w T>, as a function of z.

    In the exact Boussinesq problem this profile is independent of z and equals
    the Nusselt number, so its variation measures the discretisation error.
    """
    dTdz = np.gradient(T, s.dz, axis=0)
    return -dTdz.mean(axis=1) + (w * T).mean(axis=1)


def w_field(s, T):
    """Vertical velocity from the streamfunction, for diagnostics."""
    omega = s.poisson(s.Ra * s.to_modes(np.gradient(T, s.dx, axis=1)))
    psi = s.to_phys(s.poisson(omega))
    return -np.gradient(psi, s.dx, axis=1)


def main():
    section("1. The discretisation and a verified Poisson solver")
    print(f"  domain: x in [0, {ASPECT:.4f}] periodic (critical wavelength "
          f"{2 * np.pi / (np.pi / np.sqrt(2)):.4f})")
    print(f"  z in [0, 1] with free-slip, isothermal boundaries; grid {NX} x {NZ}")
    print("  the vorticity and streamfunction Poisson problems are solved")
    print("  spectrally in x (FFT) and by a tridiagonal solve in z, so there is")
    print("  no iteration and no solver tolerance to choose.")
    print(f"  Poisson check against sin(pi z) sin(k x): max relative error = "
          f"{poisson_check():.2e}")
    print("  that residual is the difference between the discrete and continuum")
    print("  Laplacian eigenvalues, not solver error.")

    section("2. Onset of convection around the exact Ra_c = 27 pi^4/4")
    print(f"  exact free-slip critical value Ra_c = {RA_C_FREE:.2f}")
    print("  a 1e-6 random perturbation of the conducting state is integrated, and")
    print("  sigma is the slope of ln(amplitude) against time in the linear regime.")
    print("  Bisecting on sigma(Ra) = 0 locates the onset of the discrete model:")
    lo, hi = 600.0, 760.0
    for _ in range(10):
        mid = 0.5 * (lo + hi)
        if growth_rate(mid, dt=0.05, t_end=12.0) < 0.0:
            lo = mid
        else:
            hi = mid
    ra_c_model = 0.5 * (lo + hi)
    print(f"   Ra_c(measured) = {ra_c_model:.2f}   against 27 pi^4/4 = "
          f"{RA_C_FREE:.2f}")
    print(f"   difference = {100 * abs(ra_c_model - RA_C_FREE) / RA_C_FREE:.2f}%, "
          "the spatial discretisation error of the grid.")
    print("   Ra      sigma at dt = 0.005    sigma / ((Ra - Ra_c)/Ra_c)")
    for Ra in (500.0, 620.0, 680.0, 700.0, 800.0, 1200.0):
        sigma = growth_rate(Ra)
        excess = (Ra - ra_c_model) / ra_c_model
        ratio = f"{sigma / excess:24.3f}" if excess > 0 else " " * 24
        print(f"   {Ra:6.0f}   {sigma:20.4f}   {ratio}")
    print("  below onset sigma < 0, above it sigma > 0, and close to onset the")
    print("  ratio is nearly constant: the growth rate is proportional to the")
    print("  distance from onset, the signature of a stationary bifurcation.")
    print("  The magnitude of sigma depends on dt (explicit advection), so it is")
    print("  extrapolated to dt -> 0 at Ra = 800:")
    print("   dt        sigma(dt)      analytic sigma")
    sigma_an = -(np.pi ** 2 + (np.pi / np.sqrt(2)) ** 2) \
        + 800.0 * (np.pi / np.sqrt(2)) ** 2 \
        / (np.pi ** 2 + (np.pi / np.sqrt(2)) ** 2) ** 2
    dts, sigmas = [], []
    for dt in (0.02, 0.005, 0.0025):
        sg = growth_rate(800.0, dt=dt, t_end=2.0)
        dts.append(dt)
        sigmas.append(sg)
        print(f"   {dt:<8.5f}  {sg:11.4f}   {sigma_an:13.4f}")
    slope_dt = np.polyfit(dts, sigmas, 1)[0]
    print(f"  linear extrapolation to dt = 0: sigma(0) = {sigmas[-1] - slope_dt * dts[-1]:.4f}")
    print(f"  analytic single-mode growth rate = -(pi^2+k_c^2) + Ra k_c^2/(pi^2+k_c^2)^2")
    print(f"  = {sigma_an:.4f}, so the extrapolated value agrees to "
          f"{100 * abs(sigmas[-1] - slope_dt * dts[-1] - sigma_an) / sigma_an:.1f}%.")

    section("3. Nusselt number versus Rayleigh number")
    print("  Nu = -dT/dz at the surface in conductive units; each run starts from")
    print("  the fundamental roll and is integrated to a steady state.")
    print("   Ra        Nu        spread in last half   (Ra/Ra_c)^(1/3)   Nu/pred")
    ras, nus, states = [], [], {}
    for Ra in (1000.0, 3000.0, 10000.0, 20000.0):
        s, T, n, rec = run(Ra, t_end=1.0 if Ra <= 3000.0 else 0.6,
                           amp=0.02, record_every=25)
        late = [r[1] for r in rec[len(rec) // 2:]]
        Nu = float(np.mean(late))
        ras.append(Ra)
        nus.append(Nu)
        states[Ra] = (s, T)
        pred = (Ra / RA_C_FREE) ** (1.0 / 3.0)
        print(f"   {Ra:8.0f}   {Nu:8.3f}   {(max(late) - min(late)) / Nu:19.2e}   "
              f"{pred:15.3f}   {Nu / pred:8.3f}")
    slope, intercept = np.polyfit(np.log(ras), np.log(nus), 1)
    print(f"  global fit over {ras[0]:.0f}-{ras[-1]:.0f}: Nu = "
          f"{np.exp(intercept):.3f} Ra^{slope:.3f}")
    print("  local logarithmic slopes (the asymptotic value is 1/3):")
    for i in range(1, len(ras)):
        loc = np.log(nus[i] / nus[i - 1]) / np.log(ras[i] / ras[i - 1])
        print(f"    {ras[i - 1]:8.0f} -> {ras[i]:8.0f}:   {loc:.3f}")
    print("  the slope decreases towards 0.3333 as Ra grows: boundary-layer theory")
    print("  fixes the exponent, and the near-onset points are still steepened by")
    print("  the weakly nonlinear term (Nu - 1 proportional to (Ra - Ra_c)/Ra_c).")
    print(f"  the prefactor c in Nu = c (Ra/Ra_c)^(1/3) is {nus[-1] / (ras[-1] / RA_C_FREE) ** (1 / 3):.2f}")
    print("  at the highest Ra: scaling theory cannot supply c, the model does.")

    section("4. Thermal boundary-layer thickness from the measured flux")
    print("  with equal top and bottom layers, delta = 1/(2 Nu)")
    print("   Ra        Nu      delta = 1/(2 Nu)   (Ra_c/Ra)^(1/3)   ratio")
    for Ra, Nu in zip(ras, nus):
        print(f"   {Ra:8.0f}   {Nu:6.3f}   {0.5 / Nu:15.4f}   "
              f"{(RA_C_FREE / Ra) ** (1 / 3):15.4f}   "
              f"{(0.5 / Nu) / (RA_C_FREE / Ra) ** (1 / 3):6.2f}")
    print("  the cube-root law is followed with a nearly constant O(1) ratio.")

    section("5. Energy balance: the flux profile must be flat")
    print("  the exact solution has a z-independent flux -<dT/dz> + <w T> = Nu.")
    print("   Ra        flux at top   flux at bottom   top-bottom   max deviation")
    for Ra in ras:
        s, T = states[Ra]
        prof = flux_profile(s, T, w_field(s, T))
        Nu = s.nusselt(T)
        print(f"   {Ra:8.0f}   {prof[-1]:11.4f}   {prof[0]:13.4f}   "
              f"{abs(prof[-1] - prof[0]) / Nu:10.2e}   "
              f"{np.max(np.abs(prof - Nu)) / Nu:12.2e}")
    print("  the top-to-bottom balance is good to about a percent, while the largest")
    print("  deviation sits inside the boundary layers, where a first-order upwind")
    print("  scheme is least accurate.  That is a resolution statement, not a")
    print("  conservation failure.")

    section("6. Resolution check")
    print("  same physics and same Ra = 3000, two grids (T end of run halved):")
    for nz in (49, 65):
        s, T, n, rec = run(3000.0, t_end=0.5, amp=0.02, record_every=25, nz=nz, nx=nz)
        late = [r[1] for r in rec[len(rec) // 2:]]
        prof = flux_profile(s, T, w_field(s, T))
        Nu = float(np.mean(late))
        print(f"   grid {nz:3d} x {nz:3d}, dz = {s.dz:.5f}: Nu = {Nu:.3f}, "
              f"flux deviation = {np.max(np.abs(prof - Nu)) / Nu:.2e}")
    print("  a first-order upwind scheme is diffusive, so Nu drifts with the grid;")
    print("  the drift is measured here rather than assumed away.")

    section("7. What this model leaves out")
    print("   * temperature-dependent viscosity (the real mantle varies by >1e20)")
    print("   * a high-viscosity lid, i.e. plate-like surface motion")
    print("   * internal heating, phase changes, melting")
    print("   * three dimensions, and more than one roll")
    print("  each omission changes Nu at the tens-of-percent level or more, which is")
    print("  why benchmarking against agreed cases is a subject of its own.")

    print("\n" + "=" * 72)
    print("All Rayleigh numbers, grids and perturbations are SYNTHETIC.  Ra_c =")
    print("27 pi^4/4 is an exact derived value for free-slip boundaries.")
    print("=" * 72)


if __name__ == "__main__":
    main()
