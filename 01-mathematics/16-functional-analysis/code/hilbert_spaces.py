"""Hilbert-space geometry: projections, orthogonal expansions and bases.

Run:  python3 hilbert_spaces.py
Requires: Python standard library only.

Companion to lesson 01-16-02 (Hilbert Spaces and Orthogonal Expansions).

Sections
    1. The best approximation depends on the norm
    2. A Fourier expansion is a projection, and Parseval is Pythagoras
    3. The projection is optimal: the orthogonality condition, checked
    4. Gram-Schmidt on monomials reproduces the Legendre basis
    5. Spherical harmonics are orthonormal, and the addition theorem holds
"""

import math

NGRID = 200001


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def grid(a=0.0, b=1.0, n=NGRID):
    h = (b - a) / (n - 1)
    xs = [a + i * h for i in range(n)]
    w = [h] * n
    w[0] = w[-1] = 0.5 * h
    return xs, w


def inner(f, g, xs, w):
    return sum(wi * f(x) * g(x) for x, wi in zip(xs, w))


def norm(f, xs, w):
    return math.sqrt(max(0.0, inner(f, f, xs, w)))


# ----------------------------------------------------------------------
# 1. Best approximation in two norms
# ----------------------------------------------------------------------

def best_approximation_in_two_norms():
    section("1. Best approximation of one function in two different norms")

    f = lambda x: x
    xs, w = grid()

    print("    f(x) = x on [0, 1]; approximate by a constant c")

    # L2: minimise int (x - c)^2 dx  ->  c = mean = 1/2.
    c_l2 = 1.0 / 2.0
    e_l2 = norm(lambda x: f(x) - c_l2, xs, w)
    print(f"    L2 optimum:  c = {c_l2:.6f}, ||f - c||_L2 = {e_l2:.6f}")
    print(f"                 closed form 1/sqrt(12) = {1.0 / math.sqrt(12.0):.6f}")

    # Linf: minimise max |x - c|  ->  c = 1/2, error = 1/2.
    c_linf = 0.5
    e_linf = max(abs(x - c_linf) for x in xs)
    print(f"    Linf optimum: c = {c_linf:.6f}, ||f - c||_Linf = {e_linf:.6f}")
    print(f"                 closed form 1/2 = {0.5:.6f}")

    # L1: minimise int |x - c| dx  ->  any median c = 1/2, error = 1/4.
    e_l1 = sum(wi * abs(x - 0.5) for x, wi in zip(xs, w))
    print(f"    L1 optimum:  c = {0.5:.6f}, ||f - c||_L1 = {e_l1:.6f}")
    print(f"                 closed form 1/4 = {0.25:.6f}")
    print("    all three give c = 1/2 here, but the error and the reason differ:")
    print("    L2 balances squared error, L1 is insensitive to outliers and")
    print("    the median, Linf equioscillates. Section 5 of the companion demo")
    print("    function_spaces.py shows a case where the fitted parameters")
    print("    themselves differ between norms.")


# ----------------------------------------------------------------------
# 2. Fourier expansion as a projection
# ----------------------------------------------------------------------

def fourier_projection_and_parseval():
    section("2. The sine series of f(x) = 1 is a projection; Parseval is Pythagoras")

    print("    orthonormal basis e_n(x) = sqrt(2) sin(n pi x) on (0, 1)")
    print("    projection of f = 1:  c_n = <f, e_n> = sqrt(2)(1 - cos n pi)/(n pi)")
    xs, w = grid()
    f = lambda x: 1.0

    def e(n):
        return lambda x: math.sqrt(2.0) * math.sin(n * math.pi * x)

    c = {}
    for n in range(1, 41):
        c[n] = inner(f, e(n), xs, w)

    print(f"\n    {'n':>4}{'c_n':>16}{'closed form':>16}{'c_n^2':>14}")
    for n in (1, 2, 3, 4, 5):
        closed = (2.0 * math.sqrt(2.0) / (n * math.pi)) if n % 2 else 0.0
        print(f"    {n:>4}{c[n]:>16.8f}{closed:>16.8f}{c[n] ** 2:>14.8f}")

    print(f"\n    {'N':>4}{'sum_{n<=N} c_n^2':>20}{'||S_N||^2 - 1':>18}"
          f"{'||f - S_N||_L2':>18}")
    for N in (1, 3, 5, 11, 21, 39):
        partial = sum(c[n] ** 2 for n in range(1, N + 1))
        err = math.sqrt(max(0.0, 1.0 - partial))
        print(f"    {N:>4}{partial:>20.8f}{partial - 1.0:>18.3e}{err:>18.8f}")
    print("    Parseval: sum c_n^2 = ||f||^2 = 1. The partial sums increase to 1")
    print("    like 1 - 8/(pi^2 N) for odd N, because the tail sum over odd")
    print("    n > N of 8/(n^2 pi^2) behaves like 8/(pi^2 N).")

    def tail_closed(N):
        """Exact tail sum_{odd n > N} 8/(n^2 pi^2), using sum_odd 1/n^2 = pi^2/8."""
        s = sum(1.0 / (k * k) for k in range(1, N + 1) if k % 2)
        return 8.0 / math.pi ** 2 * (math.pi ** 2 / 8.0 - s)

    print(f"\n    {'N':>4}{'1 - partial (measured)':>24}{'exact tail sum':>16}"
          f"{'ratio':>10}")
    for N in (1, 3, 5, 11, 21, 39):
        partial = sum(c[n] ** 2 for n in range(1, N + 1))
        t = tail_closed(N)
        print(f"    {N:>4}{1.0 - partial:>24.8f}{t:>16.8f}{(1.0 - partial) / t:>10.6f}")

    print("\n    The best L2 approximation by a partial sum is orthogonal to the")
    print("    residual: <f - S_N, e_m> = 0 for m <= N.")
    print(f"    {'N':>4}" + "".join(f"{'<f-S_%d, e_m>' % N:>16}" for N in (5, 11)))
    for m in (1, 2, 3, 5, 11):
        vals = []
        for N in (5, 11):
            S = lambda x, N=N: sum(c[n] * e(n)(x) for n in range(1, N + 1))
            vals.append(inner(lambda x: f(x) - S(x), e(m), xs, w) if m <= N else float("nan"))
        print(f"    {m:>4}" + "".join(
            f"{'   --   ' if v != v else '%16.3e' % v}" for v in vals))


# ----------------------------------------------------------------------
# 3. The projection really is the closest point
# ----------------------------------------------------------------------

def projection_is_optimal():
    section("3. The orthogonal projection is the closest point in the subspace")

    xs, w = grid()
    f = lambda x: 1.0

    def e(n):
        return lambda x: math.sqrt(2.0) * math.sin(n * math.pi * x)

    c = {n: inner(f, e(n), xs, w) for n in range(1, 12)}
    N = 5
    S = lambda x: sum(c[n] * e(n)(x) for n in range(1, N + 1))

    base = norm(lambda x: f(x) - S(x), xs, w)
    print(f"    N = {N}; ||f - S_N||_L2 = {base:.10f}")

    print(f"\n    {'perturbation g = S_N + d e_k':>34}{'||f - g||_L2':>16}"
          f"{'minus base':>14}")
    for k, d in ((1, 0.1), (3, 0.1), (5, 0.1), (3, -0.1), (3, 0.5)):
        g = lambda x, k=k, d=d: S(x) + d * e(k)(x)
        val = norm(lambda x: f(x) - g(x), xs, w)
        # Predict via Pythagoras: ||f - g||^2 = ||f - S||^2 + d^2
        pred = math.sqrt(base ** 2 + d ** 2)
        print(f"    {'add ' + ('%+.2f' % d) + ' e_%d' % k:>34}{val:>16.10f}"
              f"{val - base:>14.3e}")
        print(f"    {'  Pythagoras sqrt(base^2 + d^2)':>34}{pred:>16.10f}"
              f"{pred - base:>14.3e}")
    print("    every perturbation of the projection increases the error, and the")
    print("    increase matches Pythagoras to quadrature error: the residual is")
    print("    orthogonal to the subspace, so adding any component of it back")
    print("    changes the error by sqrt(||r||^2 + d^2), never reducing it.")


def gauss_legendre(n):
    """Nodes and weights of n-point Gauss-Legendre quadrature on [-1, 1]."""
    x = [math.cos(math.pi * (i + 0.75) / (n + 0.5)) for i in range(n)]
    w = [0.0] * n
    for _ in range(100):
        for i in range(n):
            p0, p1 = 1.0, x[i]
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x[i] * p1 - (k - 1) * p0) / k
            dp = n * (x[i] * p1 - p0) / (x[i] * x[i] - 1.0)
            dx = -p1 / dp
            x[i] += dx
            w[i] = 2.0 / ((1.0 - x[i] * x[i]) * dp * dp)
    return x, w


GLX, GLW = gauss_legendre(32)


def gl_inner(f, g):
    """Exact for polynomial integrands of degree <= 63 on [-1, 1]."""
    return sum(w * f(x) * g(x) for x, w in zip(GLX, GLW))


def gl_norm(f):
    return math.sqrt(max(0.0, gl_inner(f, f)))


# ----------------------------------------------------------------------
# 4. Gram-Schmidt: monomials to Legendre
# ----------------------------------------------------------------------

def gram_schmidt_legendre():
    section("4. Gram-Schmidt on monomials produces the normalised Legendre basis")

    def legendre(n):
        if n == 0:
            return lambda x: 1.0
        if n == 1:
            return lambda x: x
        Pn2 = legendre(0)
        Pn1 = legendre(1)
        for k in range(1, n):
            Pn2, Pn1 = Pn1, (lambda x, a=Pn1, b=Pn2, k=k:
                             ((2 * k + 1) * x * a(x) - k * b(x)) / (k + 1))
        return Pn1

    basis = []
    print("    inner products evaluated with 32-point Gauss-Legendre, exact for")
    print("    polynomial integrands of degree <= 63")
    print(f"\n    {'n':>3}{'Gram-Schmidt q_n(0)':>22}{'analytic q_n(0)':>18}"
          f"{'max |diff| on [-1,1]':>22}")
    for n in range(0, 6):
        v = lambda x, n=n: x ** n
        q = v
        for prev in basis:
            proj = gl_inner(q, prev)
            q = lambda x, q=q, prev=prev, proj=proj: q(x) - proj * prev(x)
        nq = gl_norm(q)
        q = lambda x, q=q, nq=nq: q(x) / nq
        basis.append(q)

        an = legendre(n)
        an_norm = math.sqrt((2.0 * n + 1.0) / 2.0)
        ana = lambda x, an=an, an_norm=an_norm: an_norm * an(x)
        diff = max(abs(q(x) - ana(x)) for x in [i / 200.0 - 1.0 for i in range(401)])
        print(f"    {n:>3}{q(0.0):>22.10f}{ana(0.0):>18.10f}{diff:>22.3e}")

    print(f"\n    {'(i,j)':>7}{'<q_i, q_j> - delta_ij':>28}   worst off-diagonal")
    worst = 0.0
    for i in range(5):
        for j in range(5):
            val = gl_inner(basis[i], basis[j])
            off = abs(val - (1.0 if i == j else 0.0))
            if i != j:
                worst = max(worst, off)
    print(f"    {'':>7}{'max |<q_i,q_j> - delta_ij|':>28} = {worst:.3e}")
    print("    with exact quadrature the basis is orthonormal to floating-point")
    print("    precision: Gram-Schmidt reproduces the Legendre polynomials")
    print("    because they are the orthogonal polynomials for the flat weight")


# ----------------------------------------------------------------------
# 5. Spherical harmonics
# ----------------------------------------------------------------------

def plm(l, m, x):
    """Associated Legendre P_l^m(x) with the Condon-Shortley phase."""
    if m < 0 or m > l:
        raise ValueError
    somx2 = math.sqrt(max(0.0, 1.0 - x * x))
    pmm = 1.0
    fact = 1.0
    for _ in range(1, m + 1):
        pmm *= -fact * somx2
        fact += 2.0
    if l == m:
        return pmm
    pmmp1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pmmp1
    pll = 0.0
    for ll in range(m + 2, l + 1):
        pll = ((2 * ll - 1) * x * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm, pmmp1 = pmmp1, pll
    return pll


def real_ylm(l, m, theta, phi):
    """Real spherical harmonic, orthonormal on the unit sphere."""
    am = abs(m)
    norm = math.sqrt((2.0 * l + 1.0) / (4.0 * math.pi)
                     * math.factorial(l - am) / math.factorial(l + am))
    p = plm(l, am, math.cos(theta))
    if m == 0:
        return norm * p
    if m > 0:
        return math.sqrt(2.0) * norm * p * math.cos(am * phi)
    return math.sqrt(2.0) * norm * p * math.sin(am * phi)


def spherical_harmonics():
    section("5. Spherical harmonics: orthonormality and the addition theorem")

    ux, uw = gauss_legendre(48)
    nphi = 96
    phis = [2.0 * math.pi * j / nphi for j in range(nphi)]
    wphi = 2.0 * math.pi / nphi

    def sphere_inner(f, g):
        total = 0.0
        for u, wu in zip(ux, uw):
            theta = math.acos(u)
            row = sum(f(theta, p) * g(theta, p) for p in phis)
            total += wu * wphi * row
        return total

    pairs = [(l, m) for l in range(0, 4) for m in range(-l, l + 1)]
    print(f"    {'(l,m)':>8}{'<(l,m),(l,m)>':>16}")
    for (l, m) in pairs:
        val = sphere_inner(lambda t, p, l=l, m=m: real_ylm(l, m, t, p),
                           lambda t, p, l=l, m=m: real_ylm(l, m, t, p))
        print(f"    {str((l, m)):>8}{val:>16.10f}")

    print(f"\n    off-diagonal inner products, worst 6 of {len(pairs) * (len(pairs) - 1) // 2} pairs")
    offs = []
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            (l1, m1), (l2, m2) = pairs[i], pairs[j]
            v = sphere_inner(lambda t, p, l=l1, m=m1: real_ylm(l, m, t, p),
                             lambda t, p, l=l2, m=m2: real_ylm(l, m, t, p))
            offs.append((abs(v), (l1, m1), (l2, m2)))
    offs.sort(reverse=True)
    print(f"    {'|inner|':>14}{'pair 1':>12}{'pair 2':>12}")
    for v, a, b in offs[:6]:
        print(f"    {v:>14.3e}{str(a):>12}{str(b):>12}")

    print("\n    addition theorem: sum_{m=-l}^{l} Y_lm(theta, phi)^2 = (2l+1)/(4 pi)")
    print(f"    {'l':>3}{'max deviation over sphere':>28}{'(2l+1)/(4 pi)':>18}")
    for l in range(0, 5):
        worst = 0.0
        for u in [x / 20.0 for x in range(-20, 21)]:
            theta = math.acos(max(-1.0, min(1.0, u)))
            for p in [2.0 * math.pi * j / 16 for j in range(16)]:
                s = sum(real_ylm(l, m, theta, p) ** 2 for m in range(-l, l + 1))
                worst = max(worst, abs(s - (2.0 * l + 1.0) / (4.0 * math.pi)))
        print(f"    {l:>3}{worst:>28.3e}{(2.0 * l + 1.0) / (4.0 * math.pi):>18.10f}")
    print("    The addition theorem is the statement that the l-th shell of the")
    print("    basis resolves the identity on that shell; it is what makes a")
    print("    spherical-harmonic expansion of a potential field complete.")


if __name__ == "__main__":
    best_approximation_in_two_norms()
    fourier_projection_and_parseval()
    projection_is_optimal()
    gram_schmidt_legendre()
    spherical_harmonics()
