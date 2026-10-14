"""Norms on function spaces, and why the choice of norm is a physical choice.

Run:  python3 function_spaces.py
Requires: Python standard library only.

Companion to lesson 01-16-01 (Vector Spaces of Functions, Norms and Inner
Products).

Sections
    1. The three working norms of a function, against closed forms
    2. Minkowski and Holder, checked numerically
    3. Convergence in one norm and not another
    4. The unit ball depends on the norm; norm equivalence in finite dimensions
    5. The physical consequence: L2, L1 and Linf fits of a travel-time pick
       containing one gross error
"""

import math
import random

NGRID = 200001


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def grid(a=0.0, b=1.0, n=NGRID):
    """Uniform grid of n nodes on [a, b] and the weight of each (trapezoid)."""
    h = (b - a) / (n - 1)
    xs = [a + i * h for i in range(n)]
    w = [h] * n
    w[0] = w[-1] = 0.5 * h
    return xs, w


def norm_p(f, xs, w, p):
    if p == math.inf:
        return max(abs(f(x)) for x in xs)
    return sum(wi * abs(f(x)) ** p for x, wi in zip(xs, w)) ** (1.0 / p)


def inner(f, g, xs, w):
    return sum(wi * f(x) * g(x) for x, wi in zip(xs, w))


# ----------------------------------------------------------------------
# 1. The three working norms
# ----------------------------------------------------------------------

def norms_of_a_function():
    section("1. L1, L2 and Linf norms of f(x) = x(1-x) on [0, 1]")

    f = lambda x: x * (1.0 - x)
    xs, w = grid()

    l1 = norm_p(f, xs, w, 1.0)
    l2 = norm_p(f, xs, w, 2.0)
    linf = norm_p(f, xs, w, math.inf)

    exact_l1 = 1.0 / 6.0
    exact_l2 = math.sqrt(1.0 / 30.0)
    exact_linf = 0.25

    print(f"    {'norm':>6}{'quadrature':>16}{'closed form':>16}{'abs error':>14}")
    for name, num, ex in (("L1", l1, exact_l1), ("L2", l2, exact_l2),
                          ("Linf", linf, exact_linf)):
        print(f"    {name:>6}{num:>16.10f}{ex:>16.10f}{abs(num - ex):>14.2e}")

    print("    closed forms: L1 = 1/6, L2^2 = 1/30 (from int x^2(1-x)^2 dx),")
    print("                  Linf = 1/4 (max of x(1-x) at x = 1/2)")
    print(f"    ratios: L1/L2 = {l1 / l2:.6f}, Linf/L2 = {linf / l2:.6f}, "
          f"Linf/L1 = {linf / l1:.6f}")


# ----------------------------------------------------------------------
# 2. Minkowski and Holder
# ----------------------------------------------------------------------

def inequalities():
    section("2. Minkowski and Holder, checked numerically")

    random.seed(20261014)
    xs, w = grid(b=1.0, n=20001)
    f = lambda x: math.exp(-8.0 * (x - 0.35) ** 2)
    g = lambda x: math.sin(3.0 * math.pi * x) ** 2

    print("    (a) Minkowski: ||f+g||_p <= ||f||_p + ||g||_p")
    print(f"    {'p':>5}{'||f+g||_p':>14}{'||f||_p+||g||_p':>18}{'slack':>12}")
    for p in (1.0, 2.0, 4.0, math.inf):
        lhs = norm_p(lambda x: f(x) + g(x), xs, w, p)
        rhs = norm_p(f, xs, w, p) + norm_p(g, xs, w, p)
        ptxt = "inf" if p == math.inf else "%g" % p
        print(f"    {ptxt:>5}{lhs:>14.6f}{rhs:>18.6f}{rhs - lhs:>12.3e}")
    print("    slack >= 0 always: Minkowski is the triangle inequality for the norm")

    print("\n    (b) Holder: |<f, g>| <= ||f||_p ||g||_q with 1/p + 1/q = 1")
    print(f"    {'p':>6}{'q':>6}{'|<f,g>|':>14}{'||f||_p ||g||_q':>18}{'ratio':>10}")
    for p in (1.0, 1.5, 2.0, 3.0, math.inf):
        q = 1.0 if p == math.inf else (math.inf if p == 1.0 else 1.0 / (1.0 - 1.0 / p))
        ip = abs(inner(f, g, xs, w))
        rhs = norm_p(f, xs, w, p) * norm_p(g, xs, w, q)
        ptxt = "inf" if p == math.inf else "%g" % p
        qtxt = "inf" if q == math.inf else "%g" % q
        print(f"    {ptxt:>6}{qtxt:>6}{ip:>14.6f}{rhs:>18.6f}{ip / rhs:>10.4f}")
    print("    the ratio never exceeds 1; it equals 1 only in the equality cases")
    print("    of Holder (g proportional to sign(f)|f|^{p-1} in the p < inf case)")


# ----------------------------------------------------------------------
# 3. Convergence in one norm, not in another
# ----------------------------------------------------------------------

def convergence_in_norms():
    section("3. Convergence in L2 is not convergence in Linf")

    print("    f_n(x) = x^n on [0, 1]")
    print(f"    {'n':>6}{'||f_n||_L2':>16}{'1/sqrt(2n+1)':>16}{'||f_n||_Linf':>15}"
          f"{'f_n(1)':>10}")
    xs, w = grid(n=100001)
    for n in (1, 2, 5, 10, 50, 100, 1000):
        f = lambda x, n=n: x ** n
        l2 = norm_p(f, xs, w, 2.0)
        print(f"    {n:>6}{l2:>16.8f}{1.0 / math.sqrt(2 * n + 1):>16.8f}"
              f"{norm_p(f, xs, w, math.inf):>15.6f}{f(1.0):>10.1f}")
    print("    ||f_n||_L2 -> 0 like 1/sqrt(2n), but ||f_n||_Linf = 1 and f_n(1) = 1")
    print("    for every n: the sequence converges in L2 and nowhere pointwise")
    print("    except at x = 0. This is why 'the model is close to the data' is")
    print("    an incomplete statement until the norm is named.")

    xs2, w2 = grid(n=200001)
    print("\n    The same function sequence measured in L1:")
    print(f"    {'n':>6}{'||f_n||_L1':>16}{'1/(n+1)':>16}")
    for n in (1, 10, 100, 1000):
        f = lambda x, n=n: x ** n
        print(f"    {n:>6}{norm_p(f, xs2, w2, 1.0):>16.8f}{1.0 / (n + 1):>16.8f}")


# ----------------------------------------------------------------------
# 4. The unit ball, and norm equivalence
# ----------------------------------------------------------------------

def unit_balls_and_equivalence():
    section("4. The unit ball depends on the norm; finite-dimensional equivalence")

    print("    (a) area of the unit ball in the plane, measured by grid counting")
    print(f"    {'p':>6}{'measured area':>16}{'closed form':>16}")
    n = 3001
    span = 1.0
    for p, exact, label in ((1.0, 2.0, "2"), (2.0, math.pi, "pi"),
                            (math.inf, 4.0, "4")):
        h = 2.0 * span / (n - 1)
        count = 0
        for i in range(n):
            x = -span + i * h
            for j in range(n):
                y = -span + j * h
                if p == math.inf:
                    ok = max(abs(x), abs(y)) <= 1.0
                else:
                    ok = abs(x) ** p + abs(y) ** p <= 1.0
                if ok:
                    count += 1
        area = count * h * h
        print(f"    {label:>6}{area:>16.6f}{exact:>16.6f}")
    print("    the unit ball is a diamond for p = 1, a disk for p = 2 and a")
    print("    square for p = inf, so the geometry of 'small' is norm-dependent")

    print("\n    (b) equivalence constants in R^n, measured on random vectors")
    random.seed(7)
    dims = [10, 100, 1000, 10000]
    print(f"    {'n':>7}{'max ||x||_1/||x||_2':>22}{'sqrt(n)':>12}"
          f"{'max ||x||_2/||x||_inf':>24}")
    for dim in dims:
        r1 = r2 = 0.0
        for _ in range(200):
            v = [random.gauss(0.0, 1.0) for _ in range(dim)]
            n1 = sum(abs(t) for t in v)
            n2 = math.sqrt(sum(t * t for t in v))
            ninf = max(abs(t) for t in v)
            r1 = max(r1, n1 / n2)
            r2 = max(r2, n2 / ninf)
        print(f"    {dim:>7}{r1:>22.6f}{math.sqrt(dim):>12.4f}{r2:>24.6f}")
    print("    ||x||_2 <= ||x||_1 <= sqrt(n) ||x||_2 and")
    print("    ||x||_inf <= ||x||_2 <= sqrt(n) ||x||_inf. The constants grow with")
    print("    n, which is the precise sense in which all norms on a")
    print("    finite-dimensional space are equivalent but not equally useful.")


# ----------------------------------------------------------------------
# 5. The physical choice of norm
# ----------------------------------------------------------------------

def fit_cost(a, b, x, t, p):
    if p == math.inf:
        return max(abs(a + b * xi - ti) for xi, ti in zip(x, t))
    return sum(abs(a + b * xi - ti) ** p for xi, ti in zip(x, t)) ** (1.0 / p)


def fit_line(x, t, p):
    """Two-stage grid refinement of the minimiser of sum |a + b x - t|^p."""
    a_lo, a_hi, b_lo, b_hi = -1.0, 6.0, 0.0, 1.0
    for _ in range(3):
        na, nb = 81, 81
        best = (math.inf, 0.0, 0.0)
        for i in range(na):
            a = a_lo + (a_hi - a_lo) * i / (na - 1)
            for j in range(nb):
                b = b_lo + (b_hi - b_lo) * j / (nb - 1)
                c = fit_cost(a, b, x, t, p)
                if c < best[0]:
                    best = (c, a, b)
        _, a_best, b_best = best
        da, db = (a_hi - a_lo) / (na - 1), (b_hi - b_lo) / (nb - 1)
        a_lo, a_hi = a_best - da, a_best + da
        b_lo, b_hi = b_best - db, b_best + db
    return best[1], best[2], best[0]


def physical_choice_of_norm():
    section("5. L2, L1 and Linf fits of a pick set with one gross error")

    print("    Data are a refraction-style travel-time pick set:")
    print("    t = 0.20 + 0.50 x (s) with one mispick of +2.0 s at x = 10")
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    t = [0.70, 1.20, 1.70, 2.20, 2.70, 3.20, 3.70, 4.20, 4.70, 7.00]
    t_true = [0.20 + 0.50 * xi for xi in x]
    print(f"    {'x (km)':>9}{'true t (s)':>13}{'pick t (s)':>13}{'pick - true':>13}")
    for xi, ti, tt in zip(x, t, t_true):
        print(f"    {xi:>9.1f}{tt:>13.2f}{ti:>13.2f}{ti - tt:>13.2f}")

    print(f"\n    {'criterion':>10}{'intercept (s)':>16}{'slope (s/km)':>15}"
          f"{'cost':>12}{'residual at x=10':>19}")
    for p, name in ((2.0, "L2"), (1.0, "L1"), (math.inf, "Linf")):
        a, b, c = fit_line(x, t, p)
        resid = a + b * 10.0 - 7.00
        print(f"    {name:>10}{a:>16.4f}{b:>15.4f}{c:>12.4f}{resid:>19.4f}")

    print("    true model: intercept 0.2000, slope 0.5000")
    print("    L2 splits the error: it accepts a biased model so that no single")
    print("    residual is large. L1 fits the ten good picks almost exactly and")
    print("    lets the outlier carry the whole error. Linf holds the maximum")
    print("    residual as small as possible, again at the cost of the good picks.")
    print("    Which is right is a statement about the noise model, not about")
    print("    mathematics: L2 is the maximum-likelihood choice for Gaussian")
    print("    errors, L1 for Laplacian (heavy-tailed, outlier-prone) errors.")


if __name__ == "__main__":
    norms_of_a_function()
    inequalities()
    convergence_in_norms()
    unit_balls_and_equivalence()
    physical_choice_of_norm()
