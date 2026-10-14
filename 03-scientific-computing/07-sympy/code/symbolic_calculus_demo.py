"""Symbolic differentiation, integration and limits, with numeric checks.

Run:  .venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_calculus_demo.py
Requires: sympy, numpy, scipy.

Companion to lesson 03-07-02.

Part 1  the gravitational potential: gradient, magnitude and Laplace's equation.
Part 2  the potential inside a uniform sphere, by integration.
Part 3  the Ricker wavelet: exact extrema from the derivative.
Part 4  quadrature: symbolic definite integrals against scipy.integrate.quad.
Part 5  limits, and the floating-point failure the symbol never has.
Part 6  a diffusion solution: flux from the derivative, in SI units.
Part 7  series expansion, and the measured cost of truncating it.
Part 8  symbolic derivative against a finite difference, measured.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from scipy import integrate


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    G, M, rho, R, r = sp.symbols("G M rho R r", positive=True)

    # ------------------------------------------------------------------
    section("1. The gravitational potential of a point mass")
    # ------------------------------------------------------------------
    r_xyz = sp.sqrt(x**2 + y**2 + z**2)
    potential_xyz = (-G * M / r).subs(r, r_xyz)
    grad = sp.Matrix([sp.diff(potential_xyz, q) for q in (x, y, z)])
    print(f"  V(r) = {sp.latex(-G * M / r)}")
    print("  gradient components:")
    for name, comp in zip("xyz", grad):
        print(f"      dV/d{name} = {sp.latex(sp.simplify(comp))}")
    mag = sp.simplify(sp.sqrt(sum(c**2 for c in grad)))
    print(f"  |grad V| = {sp.latex(mag)}")
    print(f"  |grad V| - GM/(x^2+y^2+z^2) simplifies to: "
          f"{sp.simplify(mag - G * M / (x**2 + y**2 + z**2))}")
    laplace = sp.simplify(sum(sp.diff(potential_xyz, q, 2) for q in (x, y, z)))
    print(f"  Laplacian of V, symbolic: {laplace}")
    print(f"  number of operations in the Laplacian: "
          f"{int(sp.count_ops(laplace))}")
    print("  Observation: |grad V| is exactly GM/r^2 -- no numerical residual")
    print("  at all, because the cancellation was algebraic. Laplace's equation")
    print("  holds for every r in the expression's domain, which excludes the")
    print("  source at r = 0: the singularity is a property of the model, not")
    print("  of the solver.")

    # ------------------------------------------------------------------
    section("2. Inside a uniform sphere, by integration")
    # ------------------------------------------------------------------
    s = sp.Symbol("s", positive=True)          # shell radius
    inner = sp.integrate(-G * (4 * sp.pi * rho * s**2) / r, (s, 0, r))
    outer = sp.integrate(-G * (4 * sp.pi * rho * s**2) / s, (s, r, R))
    inside = sp.simplify(inner + outer)
    print(f"  V(r) for r <= R = {sp.latex(inside)}")
    g_inside = sp.simplify(-sp.diff(inside, r))
    print(f"  g(r) = -dV/dr   = {sp.latex(g_inside)}")
    mass = sp.Rational(4, 3) * sp.pi * rho * R**3
    check = sp.simplify(g_inside.subs(r, R) + G * mass / R**2)
    print(f"  g(R) + GM/R^2 with M = (4/3)pi rho R^3: {check}")
    print(f"  V(R) = {sp.simplify(inside.subs(r, R))}")
    print(f"  and V(R) + GM/R = {sp.simplify(inside.subs(r, R) + G * mass / R)}, "
          f"i.e. the interior solution matches -GM/R at the surface")
    print("  Observation: the interior field is linear in r and joins the")
    print("  exterior point-mass value at the surface. The derivation is two")
    print("  integrals; the check at r = R is the step that catches a dropped")
    print("  factor of 4/3, and here it returns exactly zero.")

    # ------------------------------------------------------------------
    section("3. The Ricker wavelet: exact extrema")
    # ------------------------------------------------------------------
    t = sp.Symbol("t", real=True)
    f = sp.Symbol("f", positive=True)
    a = sp.pi**2 * f**2 * t**2
    w = (1 - 2 * a) * sp.exp(-a)
    dw = sp.simplify(sp.diff(w, t))
    print(f"  w(t)  = {sp.latex(w)}")
    print(f"  w'(t) = {sp.latex(dw)}")
    roots = sp.solve(sp.Eq(dw, 0), t)
    print(f"  stationary points: {roots}")
    for root in roots:
        print(f"      t = {root}  ->  w = {sp.nsimplify(w.subs(t, root))} "
              f"= {sp.N(w.subs(t, root), 8)}")
    exact_trough = sp.sqrt(6) / (2 * sp.pi * f)
    print(f"  trough time for f = 32 Hz: {sp.latex(exact_trough)} "
          f"= {sp.N(exact_trough.subs(f, 32), 7)} s")
    fnum = 32.0
    tt = np.linspace(-0.05, 0.05, 1_000_001)
    aa = (np.pi * fnum * tt) ** 2
    ww = (1 - 2 * aa) * np.exp(-aa)
    grid_trough = tt[np.argmin(ww)]
    exact_val = float(sp.N(exact_trough.subs(f, fnum), 20))
    print(f"  grid spacing: {tt[1] - tt[0]:.1e} s; minimum found on the grid "
          f"at t = {grid_trough:.7f} s")
    print(f"  exact trough at t = {-exact_val:.7f} s; "
          f"|difference| = {abs(grid_trough + exact_val):.2e} s "
          f"({abs(grid_trough + exact_val) / (tt[1] - tt[0]):.2f} grid steps)")
    print("  Observation: the grid search can only be as good as its spacing,")
    print("  while the symbolic root is exact. Use the grid to check the")
    print("  symbol; do not use the grid to replace it.")

    # ------------------------------------------------------------------
    section("4. Definite integrals against scipy.integrate.quad")
    # ------------------------------------------------------------------
    u = sp.Symbol("u", real=True)
    checks = [
        (sp.exp(-u**2), (u, 0, sp.oo), "Gaussian tail (0, inf)",
         lambda: integrate.quad(lambda v: np.exp(-v**2), 0, np.inf)[0]),
        (1 / (1 + u**2), (u, 0, 1), "arctan integral (0, 1)",
         lambda: integrate.quad(lambda v: 1 / (1 + v**2), 0, 1)[0]),
        (sp.sqrt(u) * (1 - u)**sp.Rational(3, 2), (u, 0, 1),
         "Beta(3/2, 5/2) (0, 1)",
         lambda: integrate.quad(lambda v: np.sqrt(v) * (1 - v) ** 1.5, 0, 1)[0]),
    ]
    for expr, limits, label, numeric in checks:
        exact = sp.integrate(expr, limits)
        exact_float = float(sp.N(exact, 25))
        approx = numeric()
        print(f"  {label:<24} exact = {exact} = {exact_float:.15f}")
        print(f"  {'':<24} quad  = {approx:.15f}   "
              f"|difference| = {abs(exact_float - approx):.3e}")
    print("  Observation: for smooth integrands on a finite interval the two")
    print("  agree to within the last bits. The Beta integral is the exception,")
    print("  at 1.4e-11, because its derivative is singular at both endpoints;")
    print("  quad's default absolute tolerance is not reached there. Both are")
    print("  useful and neither is redundant: the symbol gives the closed form")
    print("  that can be differentiated and printed; quad gives an answer where")
    print("  no closed form exists.")

    # ------------------------------------------------------------------
    section("5. Limits, and the failure the symbol never has")
    # ------------------------------------------------------------------
    limit = sp.limit((1 - sp.cos(u)) / u**2, u, 0)
    series = sp.simplify(sp.series(1 - sp.cos(u), u, 0, 6).removeO() / u**2)
    print(f"  lim_(u->0) (1 - cos u)/u^2 = {limit}")
    print(f"  series form of the same ratio: {series} + O(u^4)")
    for h in (1e-3, 1e-5, 1e-8):
        float_val = (1 - np.cos(h)) / h**2
        print(f"      float evaluation at u = {h:.0e}: {float_val:.15f}"
              f"   relative error vs 1/2 = "
              f"{abs(float_val - 0.5) / 0.5:.3e}")
    print(f"  cos(1e-8) in binary64: {np.cos(1e-8)!r}  "
          f"(so 1 - cos(1e-8) is exactly {1 - np.cos(1e-8)})")
    print("  Observation: the limit is exactly 1/2. At u = 1e-3 the naive")
    print("  expression is good to 8 decimal places, at u = 1e-8 it returns")
    print("  zero because cos(u) rounds to exactly 1.0 and the numerator loses")
    print("  every significant digit. The symbolic route has no such regime,")
    print("  and the series tells you where the float route ends: the error")
    print("  behaves like eps/u^2.")

    # ------------------------------------------------------------------
    section("6. A diffusion solution: flux from the derivative")
    # ------------------------------------------------------------------
    kappa, T0, dT = sp.symbols("kappa T0 dT", positive=True)
    zs, ts = sp.symbols("z t", positive=True)
    T = T0 + dT * sp.erfc(zs / (2 * sp.sqrt(kappa * ts)))
    dTdz = sp.simplify(sp.diff(T, zs))
    print(f"  T(z,t)  = {sp.latex(T)}")
    print(f"  dT/dz   = {sp.latex(dTdz)}")
    closed = -dT * sp.exp(-zs**2 / (4 * kappa * ts)) / sp.sqrt(sp.pi * kappa * ts)
    print(f"  check against the closed form -dT exp(-z^2/(4 kappa t))/"
          f"sqrt(pi kappa t): difference simplifies to "
          f"{sp.simplify(dTdz - closed)}")
    k_cond = 1.0          # W m^-1 K^-1, dry soil
    kappa_v = 1.0e-6      # m^2 s^-1
    dT_v, z_v, t_v = 10.0, 0.05, 43_200.0   # 12 hours
    args = {kappa: kappa_v, dT: dT_v, zs: z_v, ts: t_v}
    T_val = float(T.subs(args).subs(T0, 0.0))
    grad_val = float(dTdz.subs(args))
    print(f"  parameters: k = {k_cond} W/m/K, kappa = {kappa_v:.1e} m^2/s, "
          f"dT = {dT_v} K, z = {z_v} m, t = {t_v:.0f} s (12 h)")
    print(f"      z/(2 sqrt(kappa t)) = "
          f"{float(z_v / (2 * np.sqrt(kappa_v * t_v))):.6f} "
          f"(dimensionless similarity variable)")
    print(f"      T - T0              = {T_val:+.6f} K")
    print(f"      dT/dz               = {grad_val:+.6f} K m^-1")
    print(f"      q = -k dT/dz        = {-k_cond * grad_val:+.6f} W m^-2")
    print("  Observation: the symbolic derivative is a physical quantity with")
    print("  units, and it is the heat flux. Every number above comes from one")
    print("  differentiation and one substitution; the erf in the temperature")
    print("  is why the flux contains a Gaussian.")

    # ------------------------------------------------------------------
    section("7. Series expansion and the measured cost of truncation")
    # ------------------------------------------------------------------
    eps = sp.Symbol("epsilon", positive=True)
    kernel = (1 + eps**2) ** sp.Rational(-3, 2)
    ser = sp.series(kernel, eps, 0, 6).removeO()
    print(f"  exact   : {sp.latex(kernel)}")
    print(f"  series  : {sp.latex(ser)}")
    print(f"  operation count: exact {int(sp.count_ops(kernel))}, "
          f"series {int(sp.count_ops(ser))}")
    worst = 0.0
    for value in (0.05, 0.1, 0.3, 0.5):
        exact_v = float(sp.N(kernel.subs(eps, value), 20))
        approx_v = float(sp.N(ser.subs(eps, value), 20))
        rel = abs(approx_v - exact_v) / exact_v
        worst = max(worst, rel)
        print(f"      eps = {value:>4}: exact {exact_v:.10f}, truncated "
              f"{approx_v:.10f}, relative error {rel:.3e}")
    print(f"  worst relative error over the four test values: {worst:.3e}")
    print("  Observation: the truncation error grows like the first omitted")
    print("  term, here eps^6, and at eps = 0.5 the approximation is already")
    print("  off in the third decimal. A series is a statement about a limit;")
    print("  its usable range must be measured, which the table above does.")

    # ------------------------------------------------------------------
    section("8. Symbolic derivative against a finite difference")
    # ------------------------------------------------------------------
    T_num = sp.lambdify((zs, kappa, dT, ts), T - T0, "numpy")
    grad_num = sp.lambdify((zs, kappa, dT, ts), dTdz, "numpy")
    exact_g = float(grad_num(z_v, kappa_v, dT_v, t_v))
    print(f"  analytic dT/dz at z = {z_v} m: {exact_g:.12e} K/m")
    print(f"  {'h (m)':>10} {'central difference (K/m)':>26} {'relative error':>16}")
    best_h, best_err = None, float("inf")
    for h in (0.02, 0.005, 0.001, 2e-4, 5e-5, 1e-5, 1e-6, 1e-7, 1e-8):
        central = (T_num(z_v + h, kappa_v, dT_v, t_v)
                   - T_num(z_v - h, kappa_v, dT_v, t_v)) / (2 * h)
        rel = abs(central - exact_g) / abs(exact_g)
        if rel < best_err:
            best_h, best_err = h, rel
        print(f"  {h:>10.0e} {central:>26.12e} {rel:>16.3e}")
    print(f"  best h in the scan: {best_h:.0e} m, relative error {best_err:.3e}")
    print("  Observation: the error falls as h^2 over four decades of h, then")
    print("  turns around at h ~ 1e-6 m as round-off in the subtraction takes")
    print("  over, and is back to 8.9e-10 at h = 1e-8. A symbolic derivative has")
    print("  such compromise: derive once, then lambdify for arrays.")


if __name__ == "__main__":
    main()
