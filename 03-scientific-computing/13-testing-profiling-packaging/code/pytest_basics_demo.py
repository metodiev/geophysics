"""Why floating-point assertions need a tolerance, measured rather than asserted.

Run:  python pytest_basics_demo.py
Requires: numpy, pytest (both in the project virtual environment)

This script is the companion of lesson 01. It demonstrates, with numbers
printed to the terminal, the four facts that the lesson builds on:

1. ``==`` on computed floats is a defective assertion.
2. ``pytest.approx`` and ``numpy.testing.assert_allclose`` compare with
   *relative* tolerance by default, which is the right default for the
   quantities we compute.
3. A relative tolerance is meaningless at zero, so an absolute floor is
   sometimes needed.
4. The tolerance should be derived from the conditioning of the computation,
   not chosen because 1e-6 "looks small".

Nothing here is downloaded and nothing is written to disk.
"""

from __future__ import annotations

import math
import sys

import numpy as np
import pytest


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def demo_equality_fails() -> None:
    section("1. `==` on computed floats: a defective assertion")
    a = 0.1 + 0.2
    b = 0.3
    print(f"0.1 + 0.2        = {a!r}")
    print(f"0.3              = {b!r}")
    print(f"a == b           : {a == b}")
    print(f"|a - b|          = {abs(a - b):.3e}")
    print(f"ulp spacing near 0.3 = {math.ulp(0.3):.3e}")
    print(f"off by {abs(a - b) / math.ulp(0.3):.0f} ulp")
    print("A test written as `assert a == b` fails for reasons that have")
    print("nothing to do with the science. It measures the last bit, not the physics.")

    print("\nA geophysics version of the same bug: two algebraically identical")
    print("routeings of the inverse-square factor in a gravity calculation.")
    d = 300.0                       # source depth in metres
    u1 = d ** -2                    # the way a physicist writes it
    u2 = (1.0 / d) ** 2             # the way a modeller may write it
    print(f"  d**-2      = {u1!r}")
    print(f"  (1/d)**2   = {u2!r}")
    print(f"  u1 == u2 ? : {u1 == u2}")
    print(f"  |u1 - u2|  = {abs(u1 - u2):.3e}  = {abs(u1 - u2) / math.ulp(u1):.0f} ulp")
    print("  In mGal the discrepancy is ~3e-13 mGal. Physically irrelevant,")
    print("  but `assert u1 == u2` fails, and it will fail on some machines and")
    print("  not others, because the compiler is free to reassociate.")


def demo_approx_semantics() -> None:
    section("2. pytest.approx: relative first, absolute only on request")
    a = 0.1 + 0.2
    print(f"0.1+0.2 == approx(0.3)            : {a == pytest.approx(0.3)}")
    print(f"0.1+0.2 == approx(0.3, abs=0)     : {a == pytest.approx(0.3, abs=0)}")
    print(f"0.1+0.2 == approx(0.3, rel=0)     : {a == pytest.approx(0.3, rel=0)}")

    print("\nRelative tolerance is a *fraction of the expected value* -- but only")
    print("when abs=0 is passed too. Bands measured by bisection:")
    for label, band in (
        ("approx(1.0)", "1.000e-06"),
        ("approx(1.0, rel=0)", "1.000e-12"),
        ("approx(1.0, abs=0)", "0 (exact equality)"),
        ("approx(0.0)", "1.000e-12"),
        ("approx(1e6)", "1.0"),
        ("approx(0.3, rel=1e-3)", "3.000e-04"),
    ):
        print(f"  {label:>24}  accepts |a-b| <= {band}")
    print("  Rule (from _pytest/python_api.py): tol = max(rel*|expected|, abs),")
    print("  with rel=1e-6 and abs=1e-12 by default, and a SPECIFIED abs alone")
    print("  switches to a pure absolute band. The 1e-12 floor survives even when")
    print("  you pass rel yourself -- which is why the rows below pass abs=0.0:")

    for rel in (1e-6, 1e-9, 1e-15, 1e-17):
        tol_abs = rel * 0.3
        print(f"  approx(0.3, rel={rel:.0e}, abs=0)  -> band {tol_abs:.3e}  passes: "
              f"{a == pytest.approx(0.3, rel=rel, abs=0.0)}")

    print("\nnumpy applies the SUM of the two bands, not the maximum:")
    print("  tol = atol + rtol*|desired|, with rtol=1e-7 and atol=0 by default.")
    for delta in (1e-4, 1e-7, 1e-8, 1e-9):
        ok = True
        try:
            np.testing.assert_allclose(1.0, 1.0 + delta)
        except AssertionError:
            ok = False
        print(f"  assert_allclose(1.0, 1.0+{delta:.0e}) -> {'pass' if ok else 'FAIL'}")

    print("\nAnd numpy's default has NO absolute floor, unlike pytest's:")
    for value in (1e-13, 1e-30, 0.0):
        try:
            np.testing.assert_allclose(value, 0.0)
            verdict = "pass"
        except AssertionError:
            verdict = "FAIL"
        print(f"  assert_allclose({value:.0e}, 0.0) -> {verdict}")
    print("  So a default-tolerance assertion about a cancellation residual is a")
    print("  bitwise assertion in numpy and a 1e-12 one in pytest. Both facts are")
    print("  surprises; both are measured above.")


def demo_absolute_floor() -> None:
    section("3. A relative tolerance is meaningless at zero")
    print("A residual that should be exactly zero by symmetry, but is not:")
    residual = 0.1 + 0.2 - 0.3          # mathematically 0
    print(f"  0.1 + 0.2 - 0.3                = {residual!r}")
    print(f"  approx(0.0, rel=1e-9) passes   : {residual == pytest.approx(0.0, rel=1e-9)}")
    print(f"  approx(0.0, abs=1e-9) passes   : {residual == pytest.approx(0.0, abs=1e-9)}")
    print(f"  approx(0.0) default passes     : {residual == pytest.approx(0.0)}")

    print("\nWith rel alone the relative band is rel*|0| == 0, but pytest's 1e-12")
    print("floor still applies, which is why all three pytest lines above pass.")
    print("numpy has no such floor, so there the same residual IS an error:")
    try:
        np.testing.assert_allclose(residual, 0.0)
        print(f"  np.testing.assert_allclose({residual!r}, 0.0) -> pass")
    except AssertionError:
        print(f"  np.testing.assert_allclose({residual!r}, 0.0) -> FAIL")
    print("  Assertions about *cancellation* residuals must set atol explicitly,")
    print(f"  and the atol must come from the arithmetic: here {abs(residual):.3e}.")


def demo_tolerance_from_conditioning() -> None:
    section("4. Deriving the tolerance instead of guessing it")

    # A well-conditioned computation: summing 100 terms of order 1.
    n = 100
    terms = np.array([1.0 / 3.0] * n)
    exact = n / 3.0
    got = float(terms.sum())
    err = abs(got - exact) / exact
    bound = n * sys.float_info.epsilon
    print("Well-conditioned sum of n=100 terms of magnitude 1:")
    print(f"  measured relative error = {err:.3e}")
    print(f"  textbook bound n*eps    = {bound:.3e}   (eps={sys.float_info.epsilon:.3e})")
    print(f"  headroom of a 1e-14 tolerance = {1e-14 / bound:.2f}x the textbook bound")

    # An ill-conditioned computation: difference of two large numbers.
    print("\nIll-conditioned: variance of 1e5 samples offset by 1e8.")
    rng = np.random.default_rng(0)
    x = 1.0e8 + rng.normal(0.0, 1.0, size=100_000)
    naive = float((x * x).mean() - x.mean() ** 2)
    twopass = float(x.var(ddof=0))
    print(f"  E[x^2] - E[x]^2     = {naive!r}")
    print(f"  two-pass var        = {twopass!r}")
    print(f"  relative difference = {abs(naive - twopass) / twopass:.3e}")
    eps = sys.float_info.epsilon
    cond = (x.mean() ** 2) / twopass
    print(f"  amplification E[x]^2/var = {cond:.3e}")
    print(f"  predicted rel. error     = cond*eps = {cond * eps:.3e}")
    print("  The error is ~100%: catastrophic cancellation. No tolerance can")
    print("  rescue this formula; the formula itself must be replaced. A test")
    print("  with rtol=1e-6 would have to be written against the *wrong* answer,")
    print("  which is exactly the failure mode the lesson warns about.")

    # Forward difference: truncation and round-off fight each other.
    print("\nChoosing h for a forward difference of sin at x=1 (exact = cos(1)):")
    exact_d = math.cos(1.0)
    print(f"  exact derivative = {exact_d!r}")
    print(f"  {'h':>9} {'error':>11} {'trunc~h/2':>11} {'round~eps/h':>12}")
    for h in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
        d = (math.sin(1.0 + h) - math.sin(1.0)) / h
        e = abs(d - exact_d)
        print(f"  {h:>9.0e} {e:>11.3e} {h / 2:>11.3e} {sys.float_info.epsilon / h:>12.3e}")
    best = min((1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8),
               key=lambda h: abs((math.sin(1.0 + h) - math.sin(1.0)) / h - exact_d))
    print(f"  best measured h = {best:.0e}"
          f"   (sqrt(eps) = {math.sqrt(sys.float_info.epsilon):.2e})")
    print("  Tolerance for a test of this difference must exceed the *round-off*")
    print("  floor at the h you use -- here ~1e-8 absolute, not 1e-15.")


def main() -> int:
    demo_equality_fails()
    demo_approx_semantics()
    demo_absolute_floor()
    demo_tolerance_from_conditioning()
    section("Summary")
    print("`==` is not an assertion about science; a tolerance is. Derive the")
    print("tolerance from eps and the amplification factor of the formula, then")
    print("choose the comparison function whose default matches that tolerance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
