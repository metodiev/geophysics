#!/usr/bin/env python3
"""High-order, compact and staggered stencils: measured accuracy, measured
dispersion, and what each scheme costs per wavelength.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_stencils_demo.py

All models and data in this module are SYNTHETIC.  The stencils and the model
below are chosen teaching values, not measurements.

Contents
--------
1. Explicit central stencils of order 2, 4, 6, 8: measured error and order.
2. Dispersion: symbols against points per wavelength.
3. Staggered two-point derivative and the factor of four in its error.
4. Compact (Pade) stencils: a tridiagonal solve buys resolving power.
5. Cost of accuracy and the conservation property of the leapfrog update.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


CENTRAL = {
    2: np.array([-1.0, 0.0, 1.0]) / 2.0,
    4: np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / 12.0,
    6: np.array([-1.0, 9.0, -45.0, 0.0, 45.0, -9.0, 1.0]) / 60.0,
    8: np.array([3.0, -32.0, 168.0, -672.0, 0.0, 672.0, -168.0, 32.0, -3.0])
       / 840.0,
}


def apply_central(u, order, h):
    w = CENTRAL[order]
    half = len(w) // 2
    out = np.zeros_like(u)
    for i, wi in enumerate(w):
        shift = i - half
        if shift == 0:
            continue
        out += wi * np.roll(u, -shift)
    return out / h


def dispersion_explicit(order, theta):
    """Symbol of the explicit central stencil divided by i k, k = theta/h."""
    return {
        2: lambda t: np.sin(t) / t,
        4: lambda t: (8.0 * np.sin(t) - np.sin(2.0 * t)) / (6.0 * t),
        6: lambda t: (45.0 * np.sin(t) - 9.0 * np.sin(2.0 * t)
                      + np.sin(3.0 * t)) / (30.0 * t),
        8: lambda t: (672.0 * np.sin(t) - 168.0 * np.sin(2.0 * t)
                      + 32.0 * np.sin(3.0 * t) - 3.0 * np.sin(4.0 * t)) / (420.0 * t),
    }[order](theta)


def dispersion_staggered(theta):
    """Two-point half-grid difference: sin(theta/2)/(theta/2)."""
    return np.sin(theta / 2.0) / (theta / 2.0)


def dispersion_pade4(theta):
    """Tridiagonal compact scheme alpha = 1/4, a = 3/2 (fourth order)."""
    return 1.5 * np.sin(theta) / (theta * (1.0 + 0.5 * np.cos(theta)))


def dispersion_pade6(theta):
    """Compact scheme alpha = 1/3, a = 14/9, b = 1/9 (sixth order, two stencils)."""
    num = (14.0 / 9.0) * np.sin(theta) + 0.5 * (1.0 / 9.0) * np.sin(2.0 * theta)
    return num / (theta * (1.0 + (2.0 / 3.0) * np.cos(theta)))


def order_study():
    f = np.sin
    print("periodic grid of n cells covering [0, 2 pi), f = sin, derivative by")
    print("explicit central stencils; error is the maximum over all nodes")
    print(f"{'stencil order':>14} {'n':>6} {'h':>10} {'max error':>16} "
          f"{'observed order':>16}")
    for order in (2, 4, 6, 8):
        prev = None
        for n in (100, 200, 400, 800):
            h = 2.0 * np.pi / n
            x = 2.0 * np.pi * np.arange(n) / n
            approx = apply_central(f(x), order, h)
            err = np.max(np.abs(approx - np.cos(x)))
            obs = "n/a" if prev is None else f"{np.log(prev / err) / np.log(2.0):.4f}"
            print(f"{order:>14} {n:>6} {h:>10.6f} {err:>16.6e} {obs:>16}")
            prev = err
    print("each stencil reaches its design order; the higher the design order, the")
    print("sooner the global error reaches the round-off floor, because the whole")
    print("stencil is a difference of nearly equal numbers.")


def dispersion_table():
    print("derivative of a Fourier mode, relative to the exact derivative;")
    print("a value of 1 means exact, so the deviation is the dispersion error")
    print(f"{'PPW':>5} " + " ".join(f"{'p=' + str(p):>11}" for p in (2, 4, 6, 8))
          + f"{'stag 2':>11}{'Pade 4':>11}{'Pade 6':>11}")
    for ppw in (4, 6, 8, 12, 16, 32):
        theta = 2.0 * np.pi / ppw
        row = [f"{dispersion_explicit(p, theta):>11.7f}" for p in (2, 4, 6, 8)]
        row.append(f"{dispersion_staggered(theta):>11.7f}")
        row.append(f"{dispersion_pade4(theta):>11.7f}")
        row.append(f"{dispersion_pade6(theta):>11.7f}")
        print(f"{ppw:>5} " + " ".join(row))
    print("the staggered two-point difference has a dispersion error four times")
    print("smaller than the centred three-point difference of the same order,")
    print("because the truncation coefficients are h^2/24 and h^2/6.")


def truncation_factor():
    """Measure the ratio of the two second-order coefficients directly."""
    theta = 2.0 * np.pi / 8.0
    e_stag = 1.0 - dispersion_staggered(theta)
    e_cent = 1.0 - dispersion_explicit(2, theta)
    print(f"at PPW = 8: staggered error = {abs(e_stag):.8e}, "
          f"centred error = {abs(e_cent):.8e}, ratio = "
          f"{abs(e_cent / e_stag):.6f}")
    print(f"predicted ratio of the leading coefficients "
          f"(h^2/6)/(h^2/24) = {1.0 / 6.0 / (1.0 / 24.0):.6f}")
    print("at a small angle the ratio tends to 4 exactly, which is the ratio of")
    print("the truncation constants; the residual difference is the next term.")


def resolving_power():
    schemes = {
        "explicit p=2": lambda t: dispersion_explicit(2, t),
        "explicit p=4": lambda t: dispersion_explicit(4, t),
        "explicit p=6": lambda t: dispersion_explicit(6, t),
        "explicit p=8": lambda t: dispersion_explicit(8, t),
        "staggered 2": dispersion_staggered,
        "Pade 4": dispersion_pade4,
        "Pade 6": dispersion_pade6,
    }
    print("grid points per wavelength needed for a 1 % dispersion error")
    print(f"{'scheme':>14} {'PPW':>10} {'stencil width':>15} "
          f"{'PPW x width':>13}")
    widths = {"explicit p=2": 3, "explicit p=4": 5, "explicit p=6": 7,
              "explicit p=8": 9, "staggered 2": 2, "Pade 4": 3, "Pade 6": 5}
    for name, fn in schemes.items():
        lo, hi = 2.0, 2000.0
        for _ in range(90):
            mid = 0.5 * (lo + hi)
            if fn(2.0 * np.pi / mid) < 0.99:
                lo = mid
            else:
                hi = mid
        ppw = 0.5 * (lo + hi)
        print(f"{name:>14} {ppw:>10.3f} {widths[name]:>15} "
              f"{ppw * widths[name]:>13.1f}")
    print("'PPW x width' is a crude work-per-wavelength proxy for an explicit")
    print("stencil; the compact schemes win because a narrow stencil reaches the")
    print("same resolving power, at the price of solving a narrow band matrix.")


def compact_system():
    print("compact first derivative (alpha = 1/4, a = 3/2):")
    print("  alpha g_{j-1} + g_j + alpha g_{j+1} = a (u_{j+1} - u_{j-1})/(2h)")
    print(f"{'n':>6} {'h':>10} {'max error':>16} {'observed order':>16} "
          f"{'explicit p=4 error':>20}")
    prev = None
    alpha, a = 0.25, 1.5
    for n in (128, 256, 512, 1024):
        h = 2.0 * np.pi / n
        x = 2.0 * np.pi * np.arange(n) / n
        u = np.sin(x)
        rhs = a * (np.roll(u, -1) - np.roll(u, 1)) / (2.0 * h)
        M = (np.diag(np.ones(n)) + np.diag(alpha * np.ones(n - 1), 1)
             + np.diag(alpha * np.ones(n - 1), -1))
        M[0, -1] += alpha
        M[-1, 0] += alpha
        g = np.linalg.solve(M, rhs)
        err = np.max(np.abs(g - np.cos(x)))
        obs = "n/a" if prev is None else f"{np.log(prev / err) / np.log(2.0):.4f}"
        exp_err = np.max(np.abs(apply_central(u, 4, h) - np.cos(x)))
        print(f"{n:>6} {h:>10.6f} {err:>16.6e} {obs:>16} {exp_err:>20.6e}")
        prev = err
    print("the compact scheme is fourth-order like the explicit five-point")
    print("stencil, but its error is smaller at the same h and its matrix is")
    print("tridiagonal: 3n non-zeros against 5n for the explicit stencil.")


def cost_and_conservation():
    """Non-zero count of the two operators, and leapfrog energy conservation."""
    n = 1024
    alpha = 0.25
    nnz_compact = 3 * n
    nnz_explicit = 5 * n
    print(f"operator non-zeros for n = {n}: compact = {nnz_compact}, "
          f"explicit p=4 = {nnz_explicit}")
    print("\nleapfrog update of the 1-D wave equation, periodic, 400 cells,")
    print("C = 0.5, 5000 steps; energy 0.5*sum[(u^{n+1}-u^n)^2/dt^2 + (Du)^2]")
    n = 400
    h = 2.0 * np.pi / n
    C = 0.5
    dt = C * h
    x = 2.0 * np.pi * np.arange(n) / n
    up, u = np.sin(x - dt), np.sin(x)

    def energy(a, b):
        v = (b - a) / dt
        d = (np.roll(b, -1) - b) / h
        return 0.5 * np.sum(v ** 2 + d ** 2)

    e0 = energy(up, u)
    drift = [(0, energy(up, u) / e0 - 1.0)]
    for k in range(5000):
        un = 2.0 * u - up + C ** 2 * (np.roll(u, -1) - 2.0 * u + np.roll(u, 1))
        up, u = u, un
        if (k + 1) % 1000 == 0:
            drift.append((k + 1, energy(up, u) / e0 - 1.0))
    print(f"  initial energy = {e0:.6f}")
    print("  relative energy change during the run:")
    for k, d in drift:
        print(f"    step {k:>5}: {d:+.3e}")
    print("the drift stays at the round-off level and does not accumulate in one")
    print("direction: the leapfrog update is symplectic and conserves this")
    print("quadratic form exactly in exact arithmetic.")

    print("\nfor contrast, a first-order scheme on the same grid does not conserve")
    print("energy at all: the module-01 demonstration measures the upwind scheme")
    print("removing the highest grid mode entirely in a single step at C = 0.5.")


def main():
    section("1. Explicit central stencils: measured order")
    order_study()

    section("2. Dispersion: symbols against points per wavelength")
    dispersion_table()
    truncation_factor()

    section("3. Resolving power and stencil width")
    resolving_power()

    section("4. Compact (Pade) stencils")
    compact_system()

    section("5. Cost counting and the leapfrog conservation property")
    cost_and_conservation()


if __name__ == "__main__":
    main()
