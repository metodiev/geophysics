"""Numerical differentiation: stencils, truncation versus round-off.

Run:  python3 numerical_differentiation.py
Requires: Python standard library only.

Companion to lesson 01-12-03 (Numerical Differentiation and Finite-Difference
Stencils).

The central quantitative result of this lesson is the *optimal step size*. For
a forward difference the total error is

    E(h) ~ |f''| h / 2  +  u |f| / h ,        so   h* ~ u^(1/2) ,

and for a centred difference it is

    E(h) ~ |f'''| h^2 / 6  +  u |f| / h ,     so   h* ~ u^(1/3) ,

with u the unit roundoff of the arithmetic. This script *measures* both
exponents by simulating reduced precision (rounding every function value to a
multiple of u), locating the error-minimising h for each u, and fitting a
straight line to log h* against log u. The two exponents are different and it
matters which one is being quoted.

It then differentiates a synthetic gravity profile to obtain a vertical
gradient, and shows how observational noise destroys the result long before
round-off would: the two error sources are separate and only one of them can be
fixed by choosing h well.
"""

import math
import random


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Stencils
# ----------------------------------------------------------------------

def forward(f, x, h):
    return (f(x + h) - f(x)) / h


def backward(f, x, h):
    return (f(x) - f(x - h)) / h


def centred(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def centred_second(f, x, h):
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)


def richardson_forward(f, x, h):
    """Two forward differences at h and h/2, eliminating the O(h) term."""
    return 2.0 * forward(f, x, h / 2.0) - forward(f, x, h)


def richardson_centred(f, x, h):
    """Two centred differences at h and h/2, eliminating the O(h^2) term."""
    return (4.0 * centred(f, x, h / 2.0) - centred(f, x, h)) / 3.0


def round_to(value: float, u: float) -> float:
    """Model a floating-point system of unit roundoff u (absolute here)."""
    return u * round(value / u)


def least_squares_slope(xs, ys):
    """Slope of the best-fit line y = m x + c (here y = log h*, x = log u)."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den


# ----------------------------------------------------------------------
# 1. Stencils are exact on polynomials of the matching degree
# ----------------------------------------------------------------------

def report_polynomial_exactness() -> None:
    section("1. Each stencil is exact on polynomials up to a stated degree")
    x0, h = 0.7, 0.1
    print(f"  Monomials f(x) = x^p at x = {x0}, h = {h}")
    print(f"  {'p':>3}{'exact df/dx':>16}{'forward':>14}{'centred':>14}"
          f"{'exact d2f/dx2':>16}{'centred2':>14}")
    for p in (1, 2, 3, 4):
        f = lambda x, p=p: x ** p
        df = p * x0 ** (p - 1)
        d2f = p * (p - 1) * x0 ** (p - 2) if p >= 2 else 0.0
        print(f"  {p:>3}{df:>16.6f}{forward(f, x0, h):>14.6f}"
              f"{centred(f, x0, h):>14.6f}{d2f:>16.6f}"
              f"{centred_second(f, x0, h):>14.6f}")
    print("  Forward d/dx fails for p >= 2 (error = h/2 * p(p-1)x^(p-2)).")
    print("  Centred d/dx fails only for p >= 3; centred d2/dx2 fails for")
    print("  p >= 4. The degree of exactness is the *design order* of the")
    print("  stencil -- what it was built to reproduce exactly -- and it is")
    print("  what fixes the leading truncation term in the error.")


# ----------------------------------------------------------------------
# 2. Error versus step, at full precision
# ----------------------------------------------------------------------

def report_error_curve() -> None:
    section("2. Error versus step size for a smooth function at u ~ 1e-16")
    x0 = 1.0
    exact = math.cos(x0)
    print(f"  f(x) = sin x at x = {x0}:  exact derivative = {exact!r}")
    print("  'trunc' columns are the leading truncation predictions")
    print("    forward: |f''| h / 2 ;  centred: |f'''| h^2 / 6")
    print(f"  {'h':>10}{'fwd error':>13}{'fwd trunc':>13}"
          f"{'ctr error':>13}{'ctr trunc':>13}")
    for k in range(1, 18):
        h = 10.0 ** (-k / 2.0)
        ef = forward(math.sin, x0, h)
        ec = centred(math.sin, x0, h)
        t_f = abs(-math.sin(x0)) * h / 2.0
        t_c = abs(-math.cos(x0)) * h * h / 6.0
        print(f"  {h:>10.2e}{abs(ef - exact):>13.3e}{t_f:>13.3e}"
              f"{abs(ec - exact):>13.3e}{t_c:>13.3e}")
    print("  At large h the error matches the truncation formula exactly:")
    print("  the stencil's order is visible. As h shrinks the observed error")
    print("  decouples from the truncation prediction and starts to rise like")
    print("  1/h: round-off has become the dominant term. Note the rise does")
    print("  not happen at the same h for the two stencils, because the h at")
    print("  which round-off overtakes truncation depends on the truncation")
    print("  order -- which is the whole content of the next section.")


# ----------------------------------------------------------------------
# 3. Measured scaling of the optimal step
# ----------------------------------------------------------------------

def find_optimal_h(stencil, f, x0, exact, u, lo=0.6, hi=-16.0, n=4001):
    best_h, best_e = None, float("inf")
    for k in range(n):
        logh = lo + (hi - lo) * k / (n - 1)
        h = 10.0 ** logh
        fu = lambda x: round_to(f(x), u)
        e = abs(stencil(fu, x0, h) - exact)
        if e < best_e:
            best_e, best_h = e, h
    return best_h, best_e


def report_optimal_scaling() -> None:
    section("3. Measured optimal step: forward ~ u^(1/2), centred ~ u^(1/3)")
    x0s = (0.9, 1.0, 1.15, 1.3, 1.45)
    exact = {x: math.cos(x) for x in x0s}
    us = [10.0 ** (-e) for e in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)]
    print("  For each u the estimate is the geometric mean of the minimising h")
    print("  over five evaluation points, because a single h* is quantised by")
    print("  the scan grid and jumps between adjacent grid values.")
    print(f"  {'u':>10}{'h* forward':>14}{'h* u^-0.5':>14}"
          f"{'h* centred':>14}{'h* u^-0.333':>16}")
    lx, lyf, lyc = [], [], []
    for u in us:
        hfs, hcs = [], []
        for x0 in x0s:
            hf, _ = find_optimal_h(forward, math.sin, x0, exact[x0], u)
            hc, _ = find_optimal_h(centred, math.sin, x0, exact[x0], u)
            hfs.append(math.log(hf))
            hcs.append(math.log(hc))
        lf = sum(hfs) / len(hfs)
        lc = sum(hcs) / len(hcs)
        hf, hc = math.exp(lf), math.exp(lc)
        lx.append(math.log(u))
        lyf.append(lf)
        lyc.append(lc)
        print(f"  {u:>10.1e}{hf:>14.3e}{hf / u ** 0.5:>14.4f}"
              f"{hc:>14.3e}{hc / u ** (1.0 / 3.0):>16.4f}")
    sf = least_squares_slope(lx, lyf)
    sc = least_squares_slope(lx, lyc)
    print(f"\n  fitted log-log slope, forward  = {sf:+.4f}  (theory +0.5000)")
    print(f"  fitted log-log slope, centred  = {sc:+.4f}  (theory +0.3333)")
    print("  So the forward difference wants a step of order u^(1/2) and the")
    print("  centred difference a step of order u^(1/3). For u = 2.2e-16 these")
    print(f"  are {2.2e-16 ** 0.5:.2e} and {2.2e-16 ** (1.0 / 3.0):.2e}: the centred")
    print("  formula tolerates a step about 10^3 times larger. That is the")
    print("  practical reason the centred stencil is preferred when the")
    print("  function is cheap, and it is a consequence of the *order of the")
    print("  leading truncation term*, not of 'smaller h being better'.")
    print("  Conflating the two exponents is a real and common error.")


# ----------------------------------------------------------------------
# 4. Richardson extrapolation
# ----------------------------------------------------------------------

def report_richardson() -> None:
    section("4. Richardson extrapolation raises the order by one")
    x0 = 1.0
    exact = math.cos(x0)
    print(f"  {'h':>10}{'forward':>14}{'R(forward)':>14}"
          f"{'centred':>14}{'R(centred)':>14}")
    prev = {}
    for k in range(1, 9):
        h = 2.0 ** (-k)
        a = abs(forward(math.sin, x0, h) - exact)
        b = abs(richardson_forward(math.sin, x0, h) - exact)
        c = abs(centred(math.sin, x0, h) - exact)
        d = abs(richardson_centred(math.sin, x0, h) - exact)
        row = f"  {h:>10.6f}{a:>14.3e}{b:>14.3e}{c:>14.3e}{d:>14.3e}"
        if prev:
            row += (f"   orders {math.log2(prev['a'] / a):.2f}"
                    f" {math.log2(prev['b'] / b):.2f}"
                    f" {math.log2(prev['c'] / c):.2f}"
                    f" {math.log2(prev['d'] / d):.2f}")
        print(row)
        prev = dict(a=a, b=b, c=c, d=d)
    print("  Forward order 1 -> Richardson order 2; centred order 2 ->")
    print("  Richardson order 4. One extra evaluation of the same stencil buys")
    print("  a whole order, which is the cheapest accuracy in numerical work.")
    print("  The price: two stencils must be evaluated and a subtraction adds")
    print("  round-off, so the usable h shifts upward.")


# ----------------------------------------------------------------------
# 5. Geophysical application: gravity gradient, with and without noise
# ----------------------------------------------------------------------

def report_gravity_gradient() -> None:
    section("5. Gravity gradient of a buried sphere, with and without noise")
    # Vertical attraction of a point mass on the axis, g_z(d) = G M / d^2,
    # for d = sqrt(x^2 + z0^2). Units: mGal (1 mGal = 1e-5 m/s^2).
    g_const = 6.674e-11
    mass = 1.0e12          # kg, a compact orebody
    z0 = 500.0             # m depth
    to_mgal = 1.0e5        # (m/s^2) -> mGal

    def gz(x):
        d2 = x * x + z0 * z0
        return g_const * mass / d2 * to_mgal

    def dgz_dx_exact(x):
        d = math.sqrt(x * x + z0 * z0)
        return -2.0 * g_const * mass * x / d ** 4 * to_mgal

    x0 = 250.0
    print(f"  SYNTHETIC sphere: M = {mass:.0e} kg at depth {z0:.0f} m,")
    print(f"  profile sampled at x = {x0:.0f} m; exact gradient = "
          f"{dgz_dx_exact(x0):.6e} mGal/m")
    print(f"\n  {'spacing h (m)':>14}{'centred error':>18}"
          f"{'relative error':>18}")
    for h in (1.0, 5.0, 20.0, 100.0, 250.0):
        got = centred(gz, x0, h)
        err = abs(got - dgz_dx_exact(x0))
        print(f"  {h:>14.1f}{err:>18.3e}{err / abs(dgz_dx_exact(x0)):>18.3e}")
    print("  Larger spacing means more truncation error -- but the profile is")
    print("  cheap, so we can take h small.")

    print("\n  Now add OBSERVED-LIKE noise of 0.01 mGal (s.d.) to the profile.")
    print("  Each entry is the RMS error over 40 noise realisations, because a")
    print("  single realisation scatters and can hide the trend.")
    step = 5.0
    sigma = 0.01
    xs = [k * step for k in range(-200, 201)]
    base = {x: gz(x) for x in xs}
    h_list = (step, 2 * step, 5 * step, 10 * step, 20 * step)
    errs = {h: [] for h in h_list}
    for seed in range(40):
        rng = random.Random(seed)
        noisy = {x: base[x] + rng.gauss(0.0, sigma) for x in xs}

        def f_noisy(x, noisy=noisy):
            key = round(x / step) * step
            return noisy.get(key, gz(x))

        for h in h_list:
            got = centred(f_noisy, x0, h)
            errs[h].append((got - dgz_dx_exact(x0)) ** 2)
    print(f"  {'h (m)':>10}{'RMS error':>14}{'relative':>12}"
          f"{'predicted noise':>18}{'truncation':>14}")
    for h in h_list:
        rms = math.sqrt(sum(errs[h]) / len(errs[h]))
        pred_noise = sigma / (h * math.sqrt(2.0))
        # leading truncation for this profile, from a Richardson-free estimate
        trunc = abs(centred(gz, x0, h / 2.0) - 4.0 / 3.0 * centred(gz, x0, h)
                    + 1.0 / 3.0 * centred(gz, x0, 2.0 * h))
        print(f"  {h:>10.1f}{rms:>14.3e}"
              f"{rms / abs(dgz_dx_exact(x0)):>12.3e}"
              f"{pred_noise:>18.3e}{trunc:>14.3e}")
    print("  A centred difference of two values each with error s.d. sigma has")
    print("  error s.d. sigma/(h*sqrt(2)); at h = 5 m and sigma = 0.01 mGal")
    print(f"  that is {sigma / (5 * math.sqrt(2)):.2e} mGal/m, and the measured RMS")
    print("  error there is of the same size, so the model is adequate.")
    print("  The RMS error first falls as h grows (noise term shrinking) and")
    print("  then rises (truncation term growing): the minimum near h = 25-50 m")
    print("  is where the two contributions cross. The minimum is not at the")
    print("  same h as in the noise-free experiment, and the floor cannot be")
    print("  lowered by changing the arithmetic.")
    print("  The three error sources are therefore distinct:")
    print("    round-off   ~ u |f| / h        -- grows as h shrinks")
    print("    noise       ~ sigma / (h sqrt2) -- grows as h shrinks")
    print("    truncation  ~ |f'''| h^2 / 6    -- falls as h shrinks")
    print("  Only the last responds to the stencil; the first two set the floor.")
    print("  The remedy for the noise floor is smoothing or model fitting,")
    print("  which is a statement about regularisation, not about differences.")


def main() -> None:
    report_polynomial_exactness()
    report_error_curve()
    report_optimal_scaling()
    report_richardson()
    report_gravity_gradient()
    section("Summary")
    print("forward   d/dx : order 1, exact on linear polynomials, h* ~ u^(1/2)")
    print("centred   d/dx : order 2, exact on quadratics,      h* ~ u^(1/3)")
    print("centred   d2/dx2: order 2, exact on cubics")
    print("Richardson     : one order cheaper than redesigning the stencil")
    print("the optimal h is a property of the stencil, not a universal number")


if __name__ == "__main__":
    main()
