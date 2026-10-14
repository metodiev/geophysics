"""Check the mathematics formula sheet with a few explicit numbers.

Print-only, seeded, no plots, no file I/O. Every number quoted in
26-03-01-formulas-mathematics.md comes from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_mathematics_demo.py
"""

from __future__ import annotations

import math

import numpy as np

SEED = 20261014


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Mathematics formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print("PROVENANCE: SYNTHETIC -- all numbers are computed here, none are measured.")

    # 1. Quadrature: trapezoid and Simpson against the analytic value.
    banner(1, "Quadrature of exp(x) on [0, 1]")
    exact = math.e - 1.0
    xs = np.linspace(0.0, 1.0, 5)
    ys = np.exp(xs)
    trap = np.trapezoid(ys, xs)
    simpson = (xs[1] - xs[0]) / 3.0 * (ys[0] + 4 * ys[1] + 2 * ys[2] + 4 * ys[3] + ys[4])
    print(f"  exact            = {exact:.9f}")
    print(f"  trapezoid, h=0.25= {trap:.9f}   error = {trap - exact:+.3e}")
    print(f"  Simpson,   h=0.25= {simpson:.9f}   error = {simpson - exact:+.3e}")

    # 2. Finite differences for d/dx sin(x) at x = 1 rad: exact value cos(1).
    banner(2, "Finite-difference derivative of sin(x) at x = 1 rad")
    h = 1.0e-4
    exact_d = math.cos(1.0)
    forward = (math.sin(1.0 + h) - math.sin(1.0)) / h
    central = (math.sin(1.0 + h) - math.sin(1.0 - h)) / (2 * h)
    second = (math.sin(1.0 + h) - 2 * math.sin(1.0) + math.sin(1.0 - h)) / h**2
    print(f"  exact  cos(1)          = {exact_d:+.10f}")
    print(f"  forward difference h=1e-4 = {forward:+.10f}  error = {forward - exact_d:+.3e}")
    print(f"  central difference h=1e-4 = {central:+.10f}  error = {central - exact_d:+.3e}")
    print(f"  second difference  h=1e-4 = {second:+.10f}  (exact = {-math.sin(1.0):+.10f})")

    # 3. Taylor series of exp(1) truncated at N terms.
    banner(3, "Truncated Taylor series for exp(1)")
    for n_terms in (5, 10, 20):
        partial = sum(1.0 / math.factorial(k) for k in range(n_terms))
        print(f"  N = {n_terms:2d} terms: {partial:.10f}   error = {partial - math.e:+.3e}")

    # 4. Laplacian check: lap(1/r) = 0 away from the origin, in spherical coordinates.
    banner(4, "Laplacian of 1/r in spherical coordinates (away from origin)")
    for r in (1.0, 2.5):
        dd = 2.0 / r**3  # d2/dr2 (1/r); the radial Laplacian term is (1/r^2) d(r^2 f')/dr
        lap = dd + (2.0 / r) * (-1.0 / r**2)
        print(f"  r = {r:.2f} m -> Laplacian(1/r) = {lap:+.3e} m^-1 (analytic value 0)")

    # 5. Complex-exponential identity: |exp(i theta)| = 1.
    banner(5, "Complex exponential identity")
    theta = rng.uniform(0.0, 2 * math.pi)
    z = np.exp(1j * theta)
    print(f"  theta = {theta:.6f} rad")
    print(f"  |exp(i theta)| = {abs(z):.10f}  (exact 1), phase = {np.angle(z):+.10f} rad")

    print("\nAll five checks completed; exit status 0.")


if __name__ == "__main__":
    main()
