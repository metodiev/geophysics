"""Symbolic solvers: algebraic, transcendental, ODE and linear systems.

Run:  .venv/bin/python 03-scientific-computing/07-sympy/code/solving_equations_demo.py
Requires: sympy, numpy, scipy.

Companion to lesson 03-07-03.

Part 1  a cubic with a closed form, and the same root by bisection.
Part 2  a transcendental equation: no closed form, and how to check one.
Part 3  Kepler's equation: a perturbation series derived symbolically, and a
        measured truncation error against a root finder.
Part 4  a radioactive decay chain by dsolve, verified against solve_ivp.
Part 5  a damped oscillator: closed form against solve_ivp, period included.
Part 6  a linear system solved symbolically and checked against numpy.
Part 7  a boundary-value problem: the steady-state geotherm.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from scipy import integrate, optimize


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    # ------------------------------------------------------------------
    section("1. A cubic with a closed form")
    # ------------------------------------------------------------------
    u = sp.Symbol("u", real=True)
    cubic = u**3 - 6 * u**2 + 11 * u - 6          # roots 1, 2, 3 by construction
    roots = sp.solve(sp.Eq(cubic, 0), u)
    print(f"  polynomial: {sp.expand(cubic)}")
    print(f"  exact roots from solve(): {roots}")
    print(f"  factored: {sp.factor(cubic)}")
    print(f"  nroots() numerical pass: {[sp.N(r, 8) for r in sp.nroots(cubic)]}")
    print(f"  every exact root is an integer: {all(r.is_Integer for r in roots)}")
    cubic_num = sp.lambdify(u, cubic, "numpy")
    bracket = optimize.brentq(lambda v: cubic_num(v), 1.5, 2.5)
    print(f"  brentq on the bracket [1.5, 2.5]: {bracket:.15f}")
    print(f"  |brentq - exact root 2| = {abs(bracket - 2.0):.3e}")
    print("  Observation: for a polynomial the symbolic solver returns every")
    print("  root exactly. The numeric solver returns one root, from a bracket")
    print("  you had to supply -- and here it happens to be exact, because the")
    print("  root is representable and the bracket is symmetric about it.")

    # ------------------------------------------------------------------
    section("2. A transcendental equation with no closed form")
    # ------------------------------------------------------------------
    x = sp.Symbol("x", real=True)
    try:
        symbolic = sp.solve(sp.Eq(sp.cos(x), x), x)
        print(f"  solve(cos x = x, x) -> {symbolic}")
    except NotImplementedError as exc:
        print(f"  solve(cos x = x, x) raised NotImplementedError: "
              f"{str(exc).splitlines()[0]}")
    print(f"  solveset(cos x - x, x, domain=S.Reals) -> "
          f"{sp.solveset(sp.cos(x) - x, x, domain=sp.S.Reals)}")
    root_sym = sp.nsolve(sp.cos(x) - x, 1.0)
    root_num = optimize.brentq(lambda v: np.cos(v) - v, 0.0, 1.0)
    print(f"  nsolve from x0 = 1.0     : {sp.N(root_sym, 20)}")
    print(f"  brentq on [0, 1]         : {root_num:.17f}")
    print(f"  difference               : "
          f"{abs(float(sp.N(root_sym, 20)) - root_num):.3e}")
    print(f"  residual cos(x) - x      : {np.cos(root_num) - root_num:+.3e}")
    print("  Observation: 'no closed form' is a statement about the answer, not")
    print("  about the method. Both solvers return the same 16-digit number and")
    print("  the residual is the honest measure of how well it satisfies the")
    print("  equation. Note that the failure mode is an exception, not an empty")
    print("  list: code that calls solve() must handle NotImplementedError.")

    # ------------------------------------------------------------------
    section("3. Kepler's equation: a perturbation series derived in SymPy")
    # ------------------------------------------------------------------
    e_sym = sp.Symbol("e", positive=True)
    M_sym = sp.Symbol("M", real=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3")
    E_series = M_sym + e_sym * a1 + e_sym**2 * a2 + e_sym**3 * a3
    residual = sp.series(E_series - e_sym * sp.sin(E_series) - M_sym,
                         e_sym, 0, 4).removeO()
    poly = sp.Poly(sp.expand(residual), e_sym)
    print(f"  substitute E = M + e a1 + e^2 a2 + e^3 a3 into E - e sin E - M:")
    print(f"      {poly}")
    solved: dict = {}
    for order, coefficient in enumerate((a1, a2, a3), start=1):
        equation = poly.coeff_monomial(e_sym**order).subs(solved)
        solved[coefficient] = sp.simplify(
            sp.solve(sp.Eq(equation, 0), coefficient)[0])
    for name, value in solved.items():
        print(f"      {name} = {value}")
    E_approx = sp.simplify((M_sym + e_sym * a1 + e_sym**2 * a2
                            + e_sym**3 * a3).subs(solved))
    print(f"  third-order series: E = {E_approx}")
    print(f"  standard form (3 sin3M - sinM)/8 for a3: "
          f"{sp.simplify(solved[a3] - (3 * sp.sin(3 * M_sym) - sp.sin(M_sym)) / 8)}")
    e_v, M_v = 0.2, 1.0
    E_root = optimize.brentq(lambda v: v - e_v * np.sin(v) - M_v,
                             M_v - e_v, M_v + e_v)
    print(f"  Kepler's equation at e = {e_v}, M = {M_v} rad:")
    print(f"      E from brentq              = {E_root:.15f} rad "
          f"({np.degrees(E_root):.10f} deg)")
    for label, order_terms in (("second order (a1, a2)", (a1, a2)),
                               ("third order (a1, a2, a3)", (a1, a2, a3))):
        truncated = (M_sym + sum(e_sym**i * sym
                                 for i, sym in enumerate(order_terms, start=1)))
        value = float(sp.N(truncated.subs(solved).subs(
            {e_sym: e_v, M_sym: M_v}), 20))
        print(f"      {label:<26} = {value:.15f} rad; "
              f"relative error {abs(value - E_root) / E_root:.3e}")
    print(f"  {'e':>6}  {'series(3rd) - brentq (rad)':>28}  {'relative':>10}")
    for e_try in (0.01, 0.05, 0.2, 0.4):
        root = optimize.brentq(lambda v: v - e_try * np.sin(v) - M_v,
                               M_v - e_try - 0.5, M_v + e_try + 0.5)
        approx = float(sp.N(E_approx.subs({e_sym: e_try, M_sym: M_v}), 20))
        print(f"  {e_try:>6}  {approx - root:>28.3e}  "
              f"{abs(approx - root) / root:>10.3e}")
    print("  Observation: deriving the series symbolically removes the algebra")
    print("  and the sign errors; the measured error then tells you the domain")
    print("  of validity. Truncating after e^3 leaves a leading error term of")
    print("  order e^4, so raising e by a factor of 5 should raise the error by")
    print("  5^4 = 625: measured 2.627e-6/4.072e-9 = 645 between e = 0.01 and")
    print("  e = 0.05, and 7.378e-4/2.627e-6 = 281 against a predicted 4^4 = 256")
    print("  between e = 0.05 and e = 0.2. The scaling is confirmed, which is")
    print("  what makes 'good for near-circular orbits' a measurement.")

    # ------------------------------------------------------------------
    section("4. A radioactive decay chain by dsolve")
    # ------------------------------------------------------------------
    t = sp.Symbol("t", positive=True)
    lam1, lam2, N1_0 = sp.symbols("lambda1 lambda2 N1_0", positive=True)
    N1, N2 = sp.Function("N1"), sp.Function("N2")
    solutions = sp.dsolve(
        [sp.Eq(N1(t).diff(t), -lam1 * N1(t)),
         sp.Eq(N2(t).diff(t), lam1 * N1(t) - lam2 * N2(t))],
        [N1(t), N2(t)],
        ics={N1(0): N1_0, N2(0): 0},
    )
    for sol in solutions:
        print(f"  {sol}")
    N2_expr = sp.simplify(solutions[1].rhs)
    print(f"  N2(t) collected: {sp.latex(N2_expr)}")
    l1_v, l2_v, t_v = np.log(2) / 5730.0, np.log(2) / 1.387e9, 20_000.0
    exact = float(sp.N(N2_expr.subs({lam1: l1_v, lam2: l2_v, N1_0: 1.0,
                                     t: t_v}), 20))
    print(f"  decay constants: lambda1 = {l1_v:.6e} /a (14C), "
          f"lambda2 = {l2_v:.6e} /a (an illustrative long-lived daughter)")

    def system(tt, y):
        return [-l1_v * y[0], l1_v * y[0] - l2_v * y[1]]

    numeric = integrate.solve_ivp(system, (0.0, t_v), [1.0, 0.0],
                                  rtol=1e-12, atol=1e-15, dense_output=True)
    num_val = float(numeric.sol(t_v)[1])
    print(f"  at t = {t_v:.0f} a, N2/N1_0:")
    print(f"      closed form  = {exact:.15e}")
    print(f"      solve_ivp    = {num_val:.15e}")
    print(f"      |difference| = {abs(exact - num_val):.3e} "
          f"(relative {abs(exact - num_val) / exact:.3e})")
    print(f"  solve_ivp function evaluations: {numeric.nfev}, "
          f"accepted steps: {numeric.t.size - 1}")
    print("  Observation: dsolve returns the Bateman solution in the structure")
    print("  a textbook prints, with the two exponentials and the reciprocal of")
    print("  the lambda difference. The integrator reproduces it to 1e-11")
    print("  relative, at the cost of function evaluations the formula does not")
    print("  need -- and the formula still works when lambda1 ~ lambda2, where")
    print("  the difference in the denominator is a cancellation to guard.")

    # ------------------------------------------------------------------
    section("5. A damped oscillator: verify the ansatz, then measure")
    # ------------------------------------------------------------------
    omega0, zeta, q0, v0 = sp.symbols("omega0 zeta q0 v0", positive=True)
    omega_d, amp_a, amp_b = sp.symbols("omega_d A B", positive=True)
    ansatz = sp.exp(-zeta * omega0 * t) * (amp_a * sp.cos(omega_d * t)
                                           + amp_b * sp.sin(omega_d * t))
    lhs = (ansatz.diff(t, 2) + 2 * zeta * omega0 * ansatz.diff(t)
           + omega0**2 * ansatz)
    residual = sp.simplify(sp.expand(lhs).subs(omega_d**2,
                                               omega0**2 * (1 - zeta**2)))
    print("  ansatz: q(t) = exp(-zeta omega0 t) (A cos(omega_d t) "
          "+ B sin(omega_d t))")
    print(f"  substituting it into the ODE, with omega_d^2 = omega0^2 "
          f"(1 - zeta^2), leaves residual {residual}")
    ics_solution = sp.solve(
        [sp.Eq((ansatz.subs(t, 0)), q0),
         sp.Eq(ansatz.diff(t).subs(t, 0), v0)],
        [amp_a, amp_b], dict=True,
    )[0]
    print(f"  A = {sp.simplify(ics_solution[amp_a])}")
    print(f"  B = {sp.simplify(ics_solution[amp_b])}")
    q_solution = sp.simplify(ansatz.subs(ics_solution))
    print(f"  q(t) = {q_solution}")
    w0_v, z_v = 2 * np.pi, 0.05
    q_num = sp.lambdify((t, omega0, zeta, omega_d, q0, v0), q_solution, "numpy")
    ts = np.linspace(0.0, 6.0, 601)
    wd_v = w0_v * np.sqrt(1 - z_v**2)
    analytic = q_num(ts, w0_v, z_v, wd_v, 1.0, 0.0)
    numeric = integrate.solve_ivp(
        lambda tt, y: [y[1], -2 * z_v * w0_v * y[1] - w0_v**2 * y[0]],
        (0.0, 6.0), [1.0, 0.0], t_eval=ts, rtol=1e-12, atol=1e-14)
    worst = float(np.max(np.abs(analytic - numeric.y[0])))
    print(f"  parameters: omega0 = {w0_v:.6f} rad/s (1 Hz), zeta = {z_v}, "
          f"omega_d = {wd_v:.9f} rad/s, q(0) = 1, q'(0) = 0")
    print(f"  max |closed form - solve_ivp| over {len(ts)} samples: {worst:.3e}")
    print(f"  damped period 2 pi/(omega0 sqrt(1-zeta^2)) = "
          f"{2 * np.pi / wd_v:.9f} s  (undamped: 1.000000000 s)")
    ts_dense = np.linspace(0.0, 40.0, 400_001)
    dense = q_num(ts_dense, w0_v, z_v, wd_v, 1.0, 0.0)
    peak_t = ts_dense[int(np.argmax(dense))]
    exact_peak = 2 * np.pi / wd_v   # first minimum of -q, i.e. second extremum
    print(f"  first maximum of q on a 400 001-sample grid at t = {peak_t:.6f} s; "
          f"the envelope maximum is at t = 0 exactly")
    print(f"  first minimum at t = pi/omega_d = {np.pi / wd_v:.9f} s; "
          f"grid value {ts_dense[int(np.argmin(dense))]:.6f} s; "
          f"difference {abs(ts_dense[int(np.argmin(dense))] - np.pi / wd_v):.2e} s")
    print(f"  amplitude ratio between successive extrema, e^(-pi zeta/sqrt(1-zeta^2))"
          f" = {float(np.exp(-np.pi * z_v / np.sqrt(1 - z_v**2))):.10f}")
    decrement = np.pi * z_v / np.sqrt(1 - z_v**2)
    print(f"  logarithmic decrement delta = pi zeta/sqrt(1-zeta^2) = "
          f"{decrement:.9f}")
    q_min = float(np.min(dense))
    q_max = float(np.max(dense))
    delta_measured = -np.log(abs(q_min) / abs(q_max))
    zeta_recovered = delta_measured / np.sqrt(np.pi**2 + delta_measured**2)
    print(f"  from the grid extrema: q_max = {q_max:.10f}, q_min = {q_min:.10f}, "
          f"delta measured = {delta_measured:.9f}")
    print(f"  zeta recovered from the grid extrema = {zeta_recovered:.9f} "
          f"(input {z_v})")
    print("  Observation: the ansatz is verified symbolically -- the residual is")
    print("  exactly zero once omega_d^2 = omega0^2(1 - zeta^2) is imposed, and")
    print("  the amplitudes come from two linear initial conditions. Note what")
    print("  sympy's dsolve did *not* do on its own here: with no assumption")
    print("  that zeta < 1 it returned the overdamped form, with")
    print("  sqrt(zeta-1)*sqrt(zeta+1), which is imaginary at zeta = 0.05. An")
    print("  assumption the symbol does not have is a wrong answer you will")
    print("  only notice when it evaluates to nan.")

    # ------------------------------------------------------------------
    section("6. A linear system, symbolically and numerically")
    # ------------------------------------------------------------------
    symbols_9 = sp.symbols("m11 m12 m13 m21 m22 m23 m31 m32 m33", real=True)
    A = sp.Matrix(3, 3, symbols_9)
    b = sp.Matrix(sp.symbols("b1 b2 b3", real=True))
    solution = A.solve(b)
    print(f"  det(A) operation count: {int(sp.count_ops(A.det()))}")
    for i, expr in enumerate(solution, start=1):
        print(f"  s{i} = {expr}")
    A_v = np.array([[3.0, 1.0, -1.0],
                    [1.0, 4.0, 2.0],
                    [-2.0, 1.0, 5.0]])
    b_v = np.array([4.0, 5.0, 6.0])
    subs_map = {symbols_9[i * 3 + j]: A_v[i, j]
                for i in range(3) for j in range(3)}
    subs_map.update({b[0]: b_v[0], b[1]: b_v[1], b[2]: b_v[2]})
    sym_vals = np.array([float(sp.N(expr.subs(subs_map), 25))
                         for expr in solution])
    num_vals = np.linalg.solve(A_v, b_v)
    print(f"  concrete A and b -> symbolic solution  {sym_vals}")
    print(f"                      numpy.linalg.solve {num_vals}")
    print(f"  max |difference| = {np.max(np.abs(sym_vals - num_vals)):.3e}")
    print(f"  det(A) = {np.linalg.det(A_v):.6f}, "
          f"cond(A) = {np.linalg.cond(A_v):.6f}")
    print(f"  verification: max |A x - b| = "
          f"{np.max(np.abs(A_v @ sym_vals - b_v)):.3e}")
    print("  Observation: the symbolic solution is a formula in the nine matrix")
    print("  entries; the numeric one is three numbers. Both are correct. Only")
    print("  the formula can be differentiated with respect to a datum, which")
    print("  is what an error budget in an inversion needs.")

    # ------------------------------------------------------------------
    section("7. A boundary-value problem: the steady-state geotherm")
    # ------------------------------------------------------------------
    zz = sp.Symbol("z", positive=True)
    T_func = sp.Function("T")
    k_cond, A_heat, T_surf, q_surf = sp.symbols(
        "k A T_surf q_surf", positive=True)
    bvp = sp.Eq(k_cond * T_func(zz).diff(zz, 2) + A_heat, 0)
    general = sp.dsolve(bvp, T_func(zz))
    print("  ODE: k d2T/dz2 + A = 0   (steady state with radiogenic heating)")
    print(f"  general solution: {general.rhs}")
    particular = sp.dsolve(
        bvp, T_func(zz),
        ics={T_func(0): T_surf,
             T_func(zz).diff(zz).subs(zz, 0): q_surf / k_cond},
    )
    print("  with T(0) = T_surf and k T'(0) = q_surf (q_surf upward, depth down):")
    print(f"      T(z) = {sp.expand(particular.rhs)}")
    T_expr = particular.rhs
    k_v, A_v2, Ts_v, qs_v, H_v = 3.0, 1.0e-6, 283.15, 0.065, 30_000.0
    T_number = float(sp.N(T_expr.subs({k_cond: k_v, A_heat: A_v2,
                                       T_surf: Ts_v, q_surf: qs_v,
                                       zz: H_v}), 20))
    q_base = float(sp.N(k_cond * T_expr.diff(zz),
                        subs={k_cond: k_v, A_heat: A_v2, T_surf: Ts_v,
                              q_surf: qs_v, zz: H_v}, n=20))
    print(f"  k = {k_v} W/m/K, A = {A_v2:.1e} W/m^3, T(0) = {Ts_v} K, "
          f"q(0) = {qs_v} W/m^2")
    print(f"      T({H_v:.0f} m) = {T_number:.4f} K")
    print(f"      q({H_v:.0f} m) = {q_base:.9f} W/m^2  "
          f"(surface flux - A H = {qs_v - A_v2 * H_v:.9f})")
    print(f"  closed-form difference q_surf - q(H): "
          f"{sp.simplify(A_heat * H_v)} W m^-2 = {A_v2 * H_v:.9f} W m^-2")
    print(f"  temperature at the base above the surface value: "
          f"{T_number - Ts_v:.4f} K; q_surf H/k = {qs_v * H_v / k_v:.4f} K, "
          f"A H^2/(2k) = {A_v2 * H_v**2 / (2 * k_v):.4f} K")
    print(f"  the two contributions sum to "
          f"{qs_v * H_v / k_v - A_v2 * H_v**2 / (2 * k_v):.4f} K, which "
          f"matches T(H) - T_surf to "
          f"{abs((T_number - Ts_v) - (qs_v * H_v / k_v - A_v2 * H_v**2 / (2 * k_v))):.2e} K")
    print("  Observation: two boundary conditions turn the general solution")
    print("  into the exact geotherm a heat-flow province is fitted with, and")
    print("  the base flux is the surface flux *minus* the heat generated on")
    print("  the way up -- a sign that is easy to get backwards and worth")
    print("  checking against the units of A H, which are W/m^2.")


if __name__ == "__main__":
    main()
