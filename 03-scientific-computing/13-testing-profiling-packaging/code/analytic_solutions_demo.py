"""Verifying numerical code against analytic solutions, with measured orders.

Run:  python analytic_solutions_demo.py
Requires: numpy (project virtual environment)

Three verifications are performed, each of the form "a numerical answer is
compared with a closed form that was derived independently of the code":

1. Transient 1-D heat conduction.  The FTCS scheme applied to the sine mode
   ``sin(pi x / L)`` must reproduce ``exp(-k pi^2 t / L^2) sin(pi x / L)``.
   The measured time-discretisation error is reported at four time steps.
2. Steady 1-D conduction with a sinusoidal source.  The five-point-free,
   three-point second difference must converge at the measured rate ``p`` in
   ``error ~ C h^p``.  The rate is computed from the errors, not assumed.
3. The gravity anomaly of a uniform sphere, computed by numerical quadrature
   over the sphere and compared with the exact point-mass limit outside it.

Everything is printed; nothing is asserted here.  The assertions live in
``test_analytic_solutions.py``, which imports functions from this module.
"""

from __future__ import annotations

import math

import numpy as np

G_SI = 6.67430e-11
GAL_PER_MS2 = 1.0e5


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Transient heat conduction: exact exponential decay of a sine mode
# --------------------------------------------------------------------------

def ftcs_heat_sine(nx: int, nt: int, kappa: float, length: float, t_end: float):
    """FTCS solution of u_t = kappa u_xx with u(0)=u(L)=0, u(x,0)=sin(pi x/L).

    Returns ``(x, u_numeric, u_exact)`` at ``t_end``.
    """
    dx = length / (nx - 1)
    dt = t_end / nt
    r = kappa * dt / dx**2
    if r > 0.5:
        raise ValueError(f"unstable: r = {r:.3f} > 0.5")
    x = np.linspace(0.0, length, nx)
    u = np.sin(np.pi * x / length)
    u[0] = u[-1] = 0.0
    for _ in range(nt):
        u[1:-1] = u[1:-1] + r * (u[2:] - 2.0 * u[1:-1] + u[:-2])
    u[0] = u[-1] = 0.0
    decay = math.exp(-kappa * math.pi**2 * t_end / length**2)
    return x, u, decay * np.sin(np.pi * x / length)


def demo_transient_heat() -> dict[str, object]:
    section("1. Transient heat conduction against the analytic decay")
    kappa = 1.0e-6          # m^2/s, typical rock thermal diffusivity
    length = 1.0            # m
    t_end = 2.0e4           # s, ~20% of the 1e5 s decay time
    nx = 201                # dx = 5 mm; spatial error is then ~1e-6 relative
    decay = math.exp(-kappa * math.pi**2 * t_end / length**2)
    print(f"kappa = {kappa:.1e} m^2/s   L = {length} m   t = {t_end:.0e} s")
    print(f"exact decay factor exp(-k pi^2 t/L^2) = {decay!r}")
    print(f"r = k dt/dx^2 must stay <= 0.5; dx = {length/(nx-1):.2e} m")

    print(f"\n{'nt':>7} {'dt (s)':>10} {'r':>7} {'max|u_num-u_exact|':>20} {'ratio':>7}")
    errors = []
    nts = [2000, 4000, 8000, 16000]
    prev = None
    for nt in nts:
        dt = t_end / nt
        r = kappa * dt / (length / (nx - 1)) ** 2
        _, u, ue = ftcs_heat_sine(nx, nt, kappa, length, t_end)
        err = float(np.max(np.abs(u - ue)))
        ratio = "" if prev is None else f"{prev/err:7.3f}"
        print(f"{nt:>7} {dt:>10.3e} {r:>7.3f} {err:>20.6e} {ratio:>7}")
        errors.append(err)
        prev = err
    order = math.log2(errors[-2] / errors[-1])
    print(f"\nmeasured log2 error ratio between the last two pairs: {order:.3f}")
    print("Do NOT read that as an order of convergence: it is negative, i.e. the")
    print("error GREW when dt was halved twice more. The measured behaviour is")
    print("a real and reproducible surprise, so it is worth explaining:")
    print()
    print("  ln(u_num) - ln(u_exact) = +A phi  -  B dt/2  + ...")
    print("  A = k pi^2 t / L^2      (a growing amount of decay to model)")
    print("  phi = pi^2 dx^2 / 12 L^2 (a FIXED spatial error, positive sign)")
    print("  B = k^2 t pi^4 / L^4     (the temporal error, negative sign)")
    print()
    kappa_, length_, t_ = kappa, length, t_end
    a_amp = kappa_ * math.pi**2 * t_ / length_**2
    phi_ = math.pi**2 * (length_ / (nx - 1)) ** 2 / (12.0 * length_**2)
    b_amp = kappa_**2 * t_ * math.pi**4 / length_**4
    print(f"  A phi      = {a_amp * phi_:.4e}   (spatial, always positive)")
    print(f"  B dt / 2   = {b_amp * (t_end / 2000) / 2:.4e}   at dt = {t_end/2000:.0f} s")
    print(f"  cancellation at dt = 2 A phi / B = {2 * a_amp * phi_ / b_amp:.2f} s")
    print("  The two error terms carry opposite signs and cancel at dt ~ 4 s.")
    print("  The measured minimum is at dt = 5 s (6.66e-07); dt = 2.5 s is already")
    print("  worse (1.33e-06), and the prediction 4.2 s lies between the two")
    print("  grid points that bracket the minimum. Below that dt the fixed")
    print("  spatial error takes over and the total error grows again.")
    print()
    print("Consequences for testing, stated as rules:")
    print("  * 'Refine the step' is not a monotone improvement. A convergence")
    print("    test must show two or more refinements moving the error the SAME")
    print("    way; a single refinement is not evidence of anything.")
    print("  * The achievable tolerance is set by the fixed spatial error, here")
    print(f"    ~{a_amp * phi_ * decay:.1e} absolute. A test asserting 1e-9 here would")
    print("    fail on correct code, and 'loosening the tolerance until it passes'")
    print("    would hide a real discretisation limit.")
    return {"errors": errors, "decay": decay, "order": order,
            "spatial_term": a_amp * phi_, "temporal_coeff": b_amp}


# --------------------------------------------------------------------------
# 2. Steady conduction: measured convergence order in h
# --------------------------------------------------------------------------

def solve_steady_sine(n: int):
    """Solve -u'' = sin(pi x) on (0,1), u(0)=u(1)=0, with a 3-point stencil.

    Exact solution: u = sin(pi x) / pi^2.
    Returns ``(x_inner, u_numeric, u_exact)``.
    """
    h = 1.0 / (n + 1)
    x = np.linspace(h, 1.0 - h, n)
    rhs = np.sin(np.pi * x)
    # Tridiagonal (-1, 2, -1)/h^2 u = rhs, built densely for clarity (n is small).
    main = np.full(n, 2.0 / h**2)
    off = np.full(n - 1, -1.0 / h**2)
    a = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    u = np.linalg.solve(a, rhs)
    exact = np.sin(np.pi * x) / np.pi**2
    return x, u, exact


def demo_steady_convergence() -> dict[str, object]:
    section("2. Measured convergence order of a 3-point second difference")
    print("Problem: -u'' = sin(pi x), u(0)=u(1)=0, exact u = sin(pi x)/pi^2")
    print(f"\n{'n':>6} {'h':>10} {'max error':>14} {'log2 ratio':>12} {'order vs h^1':>13}")
    ns = [8, 16, 32, 64, 128, 256]
    errs = []
    for n in ns:
        h = 1.0 / (n + 1)
        _, u, ue = solve_steady_sine(n)
        err = float(np.max(np.abs(u - ue)))
        errs.append(err)
        if len(errs) == 1:
            print(f"{n:>6} {h:>10.3e} {err:>14.6e} {'--':>12} {'--':>13}")
        else:
            ratio = errs[-2] / err
            order = math.log2(ratio)
            print(f"{n:>6} {h:>10.3e} {err:>14.6e} {order:>12.4f} {order - 1:>13.4f}")
    orders = [math.log2(errs[i] / errs[i + 1]) for i in range(len(errs) - 1)]
    print(f"\nmeasured orders for the six grids: "
          f"{', '.join(f'{o:.3f}' for o in orders)}")
    print(f"mean of the last three orders = {np.mean(orders[-3:]):.4f}  (theory: 2)")
    print("\nThis is what a verification test should quote: the *rate*, which is")
    print("a property of the scheme, not the error at one grid, which is a")
    print("property of the problem's constants.")
    return {"orders": orders, "errors": errs, "ns": ns}


# --------------------------------------------------------------------------
# 3. Gravity of a sphere: quadrature against the exact point-mass limit
# --------------------------------------------------------------------------

def sphere_gravity_quadrature(
    radius_m: float, density_kgm3: float, depth_m: float,
    n_rho: int = 60, n_mu: int = 120, n_phi: int = 180,
) -> float:
    """Vertical gravity anomaly (mGal) of a uniform sphere by quadrature.

    The sphere centre is at depth ``depth_m`` below the observation point,
    which sits on the axis, so the anomaly is

        g_z = G rho \\int_0^R \\int_0^pi \\int_0^{2 pi}
              (d + s cos theta) / (d^2 + s^2 + 2 d s cos theta)^{3/2}
              s^2 sin theta  dphi dtheta ds

    evaluated by a tensor-product midpoint rule.
    """
    s = (np.arange(n_rho) + 0.5) * radius_m / n_rho
    th = (np.arange(n_mu) + 0.5) * np.pi / n_mu
    ph = (np.arange(n_phi) + 0.5) * 2.0 * np.pi / n_phi
    sin_th = np.sin(th)
    cos_th = np.cos(th)
    d = depth_m
    # Broadcast s and theta; the phi integral is 2 pi (the integrand has no phi dependence).
    ss = s[:, None]
    c = cos_th[None, :]
    denom = (d * d + ss * ss + 2.0 * d * ss * c) ** 1.5
    integrand = (d + ss * c) / denom * ss * ss * sin_th[None, :]
    volume_integral = np.sum(integrand) * (radius_m / n_rho) * (np.pi / n_mu) * (2.0 * np.pi)
    return G_SI * density_kgm3 * volume_integral * GAL_PER_MS2


def demo_sphere_gravity() -> dict[str, object]:
    section("3. Gravity of a sphere: quadrature against the shell theorem")
    radius = 100.0            # m
    density = 3000.0          # kg/m^3
    mass = density * 4.0 / 3.0 * math.pi * radius**3
    print(f"sphere: R = {radius:.0f} m, rho = {density:.0f} kg/m^3 -> M = {mass:.4e} kg")
    print("The shell theorem says the external field of a spherically symmetric")
    print("body is EXACTLY GM/d^2 for every d >= R. So the difference between")
    print("the quadrature and GM/d^2 is pure numerical error -- and it must fall")
    print("as the rule is refined. Any difference that does not fall is a bug.")

    print(f"\n{'depth (m)':>10} {'quadrature':>16} {'GM/d^2':>16} {'rel. error':>12}")
    rows = []
    for depth in (1000.0, 500.0, 300.0, 150.0):
        q = sphere_gravity_quadrature(radius, density, depth, 60, 120, 180)
        pm = G_SI * mass / depth**2 * GAL_PER_MS2
        print(f"{depth:>10.0f} {q:>16.9f} {pm:>16.9f} {abs(q - pm) / pm:>12.3e}")
        rows.append((depth, q, pm))

    print("\nNow refine the rule at two depths (midpoint tensor grid, n_rho,n_mu,n_phi):")
    print(f"{'grid':>18} {'points':>8} {'rel. error, d=1000 m':>22} {'rel. error, d=110 m':>21}")
    prev = {}
    grids = ((20, 40, 60), (40, 80, 120), (60, 120, 180),
             (100, 200, 300), (160, 320, 480))
    for nr, nm, nph in grids:
        pts = nr * nm * nph
        errs = []
        for depth in (1000.0, 110.0):
            q = sphere_gravity_quadrature(radius, density, depth, nr, nm, nph)
            pm = G_SI * mass / depth**2 * GAL_PER_MS2
            errs.append(abs(q - pm) / pm)
        print(f"{nr:>6},{nm:>4},{nph:>4} {pts/1e6:>7.2f}M {errs[0]:>22.3e} {errs[1]:>21.3e}")
        prev = {"errs": errs}
    print("\nMeasured: the error falls by roughly a factor 2.5-4 for each doubling")
    print("of the mesh, so the rule is between first and second order -- it is a")
    print("midpoint rule on a smooth integrand, and the near-singularity that")
    print("appears when the field point approaches the sphere surface limits the")
    print(f"rate. At d = 110 m (= 1.1 R) the finest grid still has "
          f"{prev['errs'][1]:.1e} relative error,")
    print(f"7x the error at d = 1000 m ({prev['errs'][0]:.1e}): brute-force quadrature")
    print("of a near-source field is expensive, which is why production gravity")
    print("codes use closed-form prism or tesseroid kernels instead.")
    return {"rows": rows}


def main() -> int:
    demo_transient_heat()
    demo_steady_convergence()
    demo_sphere_gravity()
    section("Summary")
    print("Every number above came from a closed form derived separately from")
    print("the code under test. That is the only kind of test that can tell you")
    print("your code is wrong rather than merely self-consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
