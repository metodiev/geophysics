"""Weak solutions, variational forms, adjoints and well-posedness.

Run:  python3 weak_solutions.py
Requires: Python standard library only.

Companion to lesson 01-09-08 (Weak Solutions, Variational Forms and
Well-Posedness).

Sections
    1. From the strong form to the weak form, by hand
    2. Ritz-Galerkin with hat functions: assembly, solve, convergence orders
    3. The discrete equations ARE the weak statement; coercivity check
    4. Adjoints, boundary terms, and differentiation as an unbounded operator

All problems are SYNTHETIC, one-dimensional and linear.
"""

import math
import random


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Gauss-Legendre quadrature on a reference element
# ----------------------------------------------------------------------

GL4_X = (-0.8611363115940526, -0.3399810435848563,
         0.3399810435848563, 0.8611363115940526)
GL4_W = (0.3478548451374538, 0.6521451548625461,
         0.6521451548625461, 0.3478548451374538)


def exact_u(x):
    return math.sin(math.pi * x)


def exact_du(x):
    return math.pi * math.cos(math.pi * x)


def exact_f(x):
    return math.pi ** 2 * math.sin(math.pi * x)


# ----------------------------------------------------------------------
# 1. Strong form -> weak form
# ----------------------------------------------------------------------

def report_weak_form() -> None:
    section("1. From the strong form to the weak form, by hand")
    print("Strong form:   -u''(x) = f(x) on (0,1),  u(0) = u(1) = 0.")
    print("The strong form asks for two derivatives and pointwise equality at")
    print("every x. Multiply by a test function v that vanishes at the endpoints,")
    print("integrate over (0,1) and integrate by parts:")
    print("    integral u' v' dx  =  integral f v dx      for every admissible v.")
    print("The boundary term u'(1)v(1) - u'(0)v(0) vanishes because v(0)=v(1)=0,")
    print("so no derivative of u beyond the first appears and no boundary flux is")
    print("imposed by hand: for this problem the natural boundary condition is")
    print("v = 0 on the boundary (an essential condition) and the Neumann flux is")
    print("what appears in the boundary term when it is not zero.")
    print("\n  Verify the identity numerically for v = x(1-x) times a smooth factor")
    print("  and u = sin(pi x):")
    n_q = 20000
    h = 1.0 / n_q
    lhs = 0.0
    rhs = 0.0
    for i in range(n_q):
        x = (i + 0.5) * h
        v = x * (1.0 - x)
        dv = 1.0 - 2.0 * x
        lhs += exact_du(x) * dv * h
        rhs += exact_f(x) * v * h
    print(f"    integral u' v' dx = {lhs:.10f}")
    print(f"    integral f  v  dx = {rhs:.10f}")
    print(f"    difference        = {abs(lhs - rhs):.3e}")
    print("\n  A weak solution is a function whose first (weak) derivative exists and")
    print("  satisfies this identity. Every such function also satisfies the strong")
    print("  form wherever the strong form makes sense; the converse fails, which is")
    print("  exactly what allows discontinuities (shocks, material interfaces, point")
    print("  sources) in weak solutions.")


# ----------------------------------------------------------------------
# 2. Ritz-Galerkin with linear elements
# ----------------------------------------------------------------------

def assemble_and_solve(n: int):
    """-u'' = f on (0,1), u(0)=u(1)=0, linear hat basis on n interior nodes."""
    h = 1.0 / (n + 1)
    diag = 2.0 / h
    off = -1.0 / h
    # load vector: b_i = integral f phi_i dx, by 4-point Gauss on each element
    b = [0.0] * n
    for element in range(n + 1):                 # elements [x_e, x_{e+1}]
        x_e = element * h
        for node in (element, element + 1):
            if node < 1 or node > n:
                continue
            total = 0.0
            for qx, qw in zip(GL4_X, GL4_W):
                x = x_e + 0.5 * h * (qx + 1.0)
                phi = 1.0 - abs(x / h - node)    # hat function, support |x-node*h|<=h
                if phi > 0.0:
                    total += qw * exact_f(x) * phi
            b[node - 1] += 0.5 * h * total
    # Thomas algorithm for the symmetric tridiagonal system
    lower = [off] * (n - 1)
    upper = [off] * (n - 1)
    a = [diag] * n
    c = b[:]
    for i in range(1, n):
        m = lower[i - 1] / a[i - 1]
        a[i] -= m * upper[i - 1]
        c[i] -= m * c[i - 1]
    x = [0.0] * n
    x[-1] = c[-1] / a[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (c[i] - upper[i] * x[i + 1]) / a[i]
    return x, h, diag, off


def report_fem() -> None:
    section("2. Ritz-Galerkin with hat functions: convergence orders")
    print("Test space: piecewise-linear functions on a uniform grid of n interior")
    print("nodes, h = 1/(n+1). The stiffness matrix is tridiagonal with 2/h on the")
    print("diagonal and -1/h off it; the load vector is assembled by 4-point Gauss")
    print("quadrature on each element.")
    print("\n  Exact solution u = sin(pi x), so f = pi^2 sin(pi x).")
    print(f"\n  {'n':>6}{'h':>11}{'L2 error':>13}{'order':>7}"
          f"{'H1 error':>13}{'order':>7}")
    prev_l2 = prev_h1 = None
    for n in (10, 20, 40, 80, 160):
        u, h, _diag, _off = assemble_and_solve(n)
        l2 = 0.0
        h1 = 0.0
        for element in range(n + 1):
            x_e = element * h
            for qx, qw in zip(GL4_X, GL4_W):
                x = x_e + 0.5 * h * (qx + 1.0)
                jac = 0.5 * h
                uh, duh = interpolate(u, h, n, x)
                l2 += qw * jac * (uh - exact_u(x)) ** 2
                h1 += qw * jac * (duh - exact_du(x)) ** 2
        l2 = math.sqrt(l2)
        h1 = math.sqrt(h1)
        o_l2 = "" if prev_l2 is None else f"{math.log2(prev_l2 / l2):.2f}"
        o_h1 = "" if prev_h1 is None else f"{math.log2(prev_h1 / h1):.2f}"
        print(f"  {n:>6}{h:>11.5f}{l2:>13.3e}{o_l2:>7}{h1:>13.3e}{o_h1:>7}")
        prev_l2, prev_h1 = l2, h1
    print("\n  Observed orders: 2 in L2 and 1 in the energy norm H1. That split is")
    print("  universal for piecewise-linear finite elements: the interpolation")
    print("  error is O(h^2) in value and O(h) in slope, and the Galerkin solution")
    print("  is the best approximation in the energy norm, so it inherits both.")
    print("\n  Two remarks worth keeping:")
    print("    * if f is constant, the 1-D linear-element solution is exact AT THE")
    print("      NODES (the discrete second difference reproduces a quadratic), so")
    print("      the remaining L2 error is pure interpolation error;")
    print("    * the energy norm error is the quantity the variational method")
    print("      actually minimises, which is why error estimates are quoted in H1")
    print("      far more often than in the maximum norm.")


def interpolate(u, h, n, x):
    """Piecewise-linear finite-element function and its derivative at x."""
    s = x / h
    element = int(math.floor(s))
    if element >= n:                       # last element, nodes n and n+1(=0)
        element = n
    local = s - element
    left = u[element - 1] if 1 <= element <= n else 0.0
    right = u[element] if element + 1 <= n else 0.0
    value = (1.0 - local) * left + local * right
    slope = (right - left) / h
    return value, slope


# ----------------------------------------------------------------------
# 3. The discrete equations are the weak statement
# ----------------------------------------------------------------------

def report_weak_residual() -> None:
    section("3. The assembled equations ARE the weak statement")
    print("Assembling the stiffness matrix and load vector is not an approximation")
    print("of the weak form: each equation is exactly")
    print("    integral u_h' phi_i' dx = integral f phi_i dx,")
    print("with u_h the piecewise-linear solution. Check that directly.")
    n = 40
    u, h, diag, off = assemble_and_solve(n)
    worst = 0.0
    for i in range(1, n + 1):
        # u_h' phi_i' integrated elementwise (both are piecewise smooth)
        lhs = 0.0
        rhs = 0.0
        for element in range(n + 1):
            x_e = element * h
            for qx, qw in zip(GL4_X, GL4_W):
                x = x_e + 0.5 * h * (qx + 1.0)
                jac = 0.5 * h
                _uh, duh = interpolate(u, h, n, x)
                dphi = hat_derivative(h, i, x)
                phi = hat_value(h, i, x)
                lhs += qw * jac * duh * dphi
                rhs += qw * jac * exact_f(x) * phi
        worst = max(worst, abs(lhs - rhs))
    print(f"\n  n = {n}, largest |integral u_h' phi_i' - integral f phi_i| = {worst:.3e}")
    print("  That is round-off: the linear system is the weak form, discretised,")
    print("  not a different problem.")
    print("\n  Coercivity (the hypothesis of the Lax-Milgram theorem). The stiffness")
    print("  matrix A is symmetric, and its smallest eigenvalue is")
    print("    4 sin^2(pi h / 2) / h^2 > 0,")
    print("  the discrete analogue of the Poincare inequality |v| <= (1/pi)|v'|")
    print("  that makes the bilinear form coercive on H^1_0. Check positive")
    print("  definiteness directly with random vectors:")
    random.seed(20261014)
    print(f"\n  {'trial':>8}{'v^T A v':>20}{'v^T v':>18}{'ratio':>14}")
    for trial in range(1, 4):
        v = [random.uniform(-1.0, 1.0) for _ in range(n)]
        av = [0.0] * n
        for i in range(n):
            av[i] = diag * v[i]
            if i > 0:
                av[i] += off * v[i - 1]
            if i < n - 1:
                av[i] += off * v[i + 1]
        quad = sum(v[i] * av[i] for i in range(n))
        norm = sum(v[i] * v[i] for i in range(n))
        print(f"  {trial:>8}{quad:>20.6f}{norm:>18.6f}{quad/norm:>14.6f}")
    print("\n  The ratio v^T A v / v^T v is bounded below by the smallest eigenvalue")
    print(f"  4 sin^2(pi h/2)/h^2 = "
          f"{4.0*math.sin(math.pi*h/2)**2/h**2:.6f} for h = {h:.5f}, so the form is")
    print("  coercive. Lax-Milgram then guarantees a unique weak solution bounded")
    print("  by the data: continuous dependence, which is precisely the condition")
    print("  that the backward heat problem of lesson 07 violates.")


def hat_value(h, node, x):
    s = abs(x - node * h)
    return max(0.0, 1.0 - s / h)


def hat_derivative(h, node, x):
    d = x - node * h
    if d < -h or d > h:
        return 0.0
    return -1.0 / h if d > 0.0 else 1.0 / h


# ----------------------------------------------------------------------
# 4. Adjoints
# ----------------------------------------------------------------------

def report_adjoints() -> None:
    section("4. Adjoints, boundary terms, and differentiation as unbounded")
    print("Integration by parts is how the adjoint is computed. For the first")
    print("derivative on (0,1) with the L2 inner product,")
    print("    integral (Du) v dx = [u v]_0^1 - integral u (D* v) dx,")
    print("so D* = -D plus the boundary term. Two consequences follow.")
    n = 50
    h = 1.0 / n
    random.seed(7)
    u = [random.uniform(-1.0, 1.0) for _ in range(n + 1)]
    v = [random.uniform(-1.0, 1.0) for _ in range(n + 1)]

    def inner_sum(a, b, count):
        """h * sum a_i b_i over i = 0..count-1."""
        return h * sum(a[i] * b[i] for i in range(count))

    def forward(f, count):
        return [(f[i + 1] - f[i]) / h for i in range(count)]

    def backward(f, count):
        """(f_i - f_{i-1})/h for i = 1..count-1, padded with a zero at i = 0."""
        out = [0.0]
        out.extend((f[i] - f[i - 1]) / h for i in range(1, count))
        return out

    du = forward(u, n)
    dv = backward(v, n)
    lhs = inner_sum(du, v, n)
    rhs = inner_sum(u, dv, n)
    boundary = u[n] * v[n - 1] - u[0] * v[0]
    print(f"\n  (a) For general data on a grid of {n} elements:")
    print(f"      h<Du, v>            = {lhs:.8f}")
    print(f"      h<u, D* v>          = {rhs:.8f}")
    print(f"      sum                 = {lhs + rhs:.8f}")
    print(f"      boundary term       = {boundary:.8f}")
    print(f"      |sum - boundary|    = {abs(lhs + rhs - boundary):.3e}   (round-off)")
    print("      so h<Du, v> = h<u, (-D backward) v> + boundary. The adjoint of the")
    print("      forward difference is minus the backward difference, plus a boundary")
    print("      term, exactly as integration by parts says. Now enforce the boundary")
    print("      conditions u(0) = 0 and v at the last node = 0, which is what a")
    print("      Dirichlet test space does:")
    u2 = u[:]
    v2 = v[:]
    u2[0] = 0.0
    v2[n - 1] = 0.0
    du2 = forward(u2, n)
    dv2 = backward(v2, n)
    lhs2 = inner_sum(du2, v2, n)
    rhs2 = inner_sum(u2, dv2, n)
    print(f"      |h<Du, v> + h<u, D* v>| with the conditions = "
          f"{abs(lhs2 + rhs2):.3e}")
    print("      The boundary term has vanished and the two operators are exact")
    print("      negatives of one another. Boundary conditions and adjoints are")
    print("      inseparable; in inverse theory the adjoint of the forward operator")
    print("      carries the boundary terms of the physical problem with it.")

    print("\n  (b) A differentiation operator is unbounded: its norm grows like 1/h.")
    print("      Perturb smooth data by random noise of amplitude eps and")
    print("      differentiate with a central difference. The Nyquist (alternating)")
    print("      mode is invisible to a central difference on the grid, so random")
    print("      noise is the honest test.")
    print(f"\n  {'h':>9}{'eps':>9}{'noiseless error':>17}"
          f"{'noise amplification':>21}{'eps / h':>11}{'ratio':>8}")
    random.seed(99)
    for npts in (100, 1000, 10000):
        hh = 1.0 / npts
        eps = 1.0e-6
        x = [(i + 1) * hh for i in range(npts - 1)]
        clean = [exact_u(xi) for xi in x]
        noisy = [exact_u(xi) + eps * random.uniform(-1.0, 1.0) for xi in x]

        def central(data):
            return [(data[i + 1] - data[i - 1]) / (2 * hh)
                    for i in range(1, npts - 2)]

        dc = central(clean)
        dn = central(noisy)
        e_clean = max(abs(dc[i] - math.pi * math.cos(math.pi * x[i + 1]))
                      for i in range(len(dc)))
        amplification = max(abs(dn[i] - dc[i]) for i in range(len(dc)))
        print(f"  {hh:>9.0e}{eps:>9.0e}{e_clean:>17.3e}"
              f"{amplification:>21.3e}{eps/hh:>11.3e}"
              f"{amplification/(eps/hh):>8.3f}")
    print("\n  The noise amplification is a fixed multiple of eps/h, so refining")
    print("  the grid makes the differentiated answer WORSE while making the data")
    print("  better: the two errors move in opposite directions. The noiseless")
    print("  column, by contrast, falls like h^2 as a good discretisation should.")
    print("\n  The derivative error is set by eps/h, not by eps, and it grows without")
    print("  bound as the grid is refined. Well-posedness of the forward problem")
    print("  therefore says nothing about the inverse problem: the inverse operator")
    print("  contains a differentiation, and differentiation is unbounded. This is")
    print("  the precise statement behind 'potential-field inversion is non-unique'")
    print("  (lesson 04) and behind the need for regularisation in the")
    print("  inverse-problems folder.")



# ----------------------------------------------------------------------
# 5. A discontinuous coefficient: does the mesh have to see the interface?
# ----------------------------------------------------------------------

def assemble_interface(n: int, k_left: float, k_right: float):
    """-(k u')' = 1 on (0,1), u(0)=u(1)=0, k piecewise constant at x = 0.5."""
    h = 1.0 / (n + 1)

    def kof(x):
        return k_left if x < 0.5 else k_right

    diag = [0.0] * n
    off = [0.0] * (n - 1)
    b = [0.0] * n
    for element in range(n + 1):
        xm = (element + 0.5) * h
        ke = kof(xm)
        for g in (element - 1, element):
            if 0 <= g < n:
                diag[g] += ke / h
                b[g] += h / 2.0
        if 0 <= element - 1 < n and 0 <= element < n:
            off[element - 1] += -ke / h
    ac = diag[:]
    rhs = b[:]
    for i in range(1, n):
        m = off[i - 1] / ac[i - 1]
        ac[i] -= m * off[i - 1]
        rhs[i] -= m * rhs[i - 1]
    u = [0.0] * n
    u[-1] = rhs[-1] / ac[-1]
    for i in range(n - 2, -1, -1):
        u[i] = (rhs[i] - off[i] * u[i + 1]) / ac[i]
    return u, h


def interface_exact(k_left: float = 1.0, k_right: float = 10.0):
    """Exact solution of -(k u')' = 1 with u(0)=u(1)=0 and a jump in k at 0.5."""
    # u = -x^2/(2k) + a x + b on each side; match u and k u' at x = 0.5
    # left: u(0)=0 -> b=0.  right: u(1)=0 -> b_R = 1/(2 k_R) - a_R
    # continuity: -1/8/kL + aL/2 = -1/8/kR + aR/2 + b_R
    # flux:       kL(-1/2/kL + aL) = kR(-1/2/kR + aR)  -> -1/2 + kL aL = -1/2 + kR aR
    # hence kL aL = kR aR.
    aR = None
    # solve the 1x1 system from the continuity relation
    # substitute aL = kR aR / kL
    # -1/(8kL) + (kR aR)/(2kL) = -1/(8kR) + aR/2 + 1/(2kR) - aR
    # -1/(8kL) + (kR aR)/(2kL) = -1/(8kR) + 1/(2kR) - aR/2
    lhs_const = -1.0 / (8.0 * k_left)
    rhs_const = -1.0 / (8.0 * k_right) + 1.0 / (2.0 * k_right)
    coef = k_right / (2.0 * k_left) + 0.5
    aR = (rhs_const - lhs_const) / coef
    aL = k_right * aR / k_left
    bR = 1.0 / (2.0 * k_right) - aR

    def u(x):
        if x <= 0.5:
            return -x * x / (2.0 * k_left) + aL * x
        return -x * x / (2.0 * k_right) + aR * x + bR

    def du(x):
        if x < 0.5:
            return -x / k_left + aL
        return -x / k_right + aR

    return u, du


def report_interface() -> None:
    section("5. A discontinuous coefficient: does the mesh have to see the interface?")
    print("-(k u')' = 1 on (0,1), u(0)=u(1)=0, k = 1 for x<0.5 and k = 10 for")
    print("x>0.5. The exact solution is quadratic on each half with a kink at")
    print("x = 0.5 (u' jumps by a factor of ten), so u is in H^1 but not C^1.")
    print("The weak form handles it directly; the only question is whether the")
    print("mesh resolves the kink.")
    uex, duex = interface_exact()

    for label, nodes in (("mesh ALIGNED with the interface (n odd)", (11, 21, 41, 81, 161)),
                         ("mesh NOT aligned (n even)", (10, 20, 40, 80, 160))):
        print(f"\n  {label}")
        print(f"  {'n':>5}{'h':>11}{'L2 error':>13}{'order':>7}"
              f"{'H1 error':>13}{'order':>7}")
        prev_l2 = prev_h1 = None
        for n in nodes:
            u, h = assemble_interface(n, 1.0, 10.0)
            l2 = h1 = 0.0
            for element in range(n + 1):
                x_e = element * h
                for qx, qw in zip(GL4_X, GL4_W):
                    x = x_e + 0.5 * h * (qx + 1.0)
                    jac = 0.5 * h
                    uh, duh = interpolate(u, h, n, x)
                    l2 += qw * jac * (uh - uex(x)) ** 2
                    h1 += qw * jac * (duh - duex(x)) ** 2
            l2 = math.sqrt(l2)
            h1 = math.sqrt(h1)
            o_l2 = "" if prev_l2 is None else f"{math.log2(prev_l2 / l2):.2f}"
            o_h1 = "" if prev_h1 is None else f"{math.log2(prev_h1 / h1):.2f}"
            print(f"  {n:>5}{h:>11.4f}{l2:>13.3e}{o_l2:>7}{h1:>13.3e}{o_h1:>7}")
            prev_l2, prev_h1 = l2, h1
    print("\n  With the interface ON a node the orders are the usual 2 and 1. With")
    print("  the interface INSIDE an element they halve to 1 and 0.5, and the errors")
    print("  are an order of magnitude larger: the kink is not in the trial space,")
    print("  so no refinement of that mesh can represent the solution's slope jump")
    print("  efficiently. The practical rule is to put element boundaries where the")
    print("  material properties jump, which the weak formulation makes easy: the")
    print("  element integrals simply use the local k.")


def main() -> None:
    report_weak_form()
    report_fem()
    report_weak_residual()
    report_adjoints()
    report_interface()


if __name__ == "__main__":
    main()
