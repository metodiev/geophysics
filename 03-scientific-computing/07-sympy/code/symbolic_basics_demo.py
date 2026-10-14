"""Symbolic variables, exact arithmetic and assumptions.

Run:  .venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_basics_demo.py
Requires: sympy, mpmath (installed as a SymPy dependency).

Companion to lesson 03-07-01.

Part 1  assumptions decide the answer: sqrt(x**2) is not always x.
Part 2  exact rational arithmetic against binary floating point.
Part 3  recovering the rational a float was meant to be, and when not to.
Part 4  how many digits a 50-digit evaluation really delivers.
Part 5  a symbolic derivation of the Earth's mean density, end to end.
Part 6  what simplify() actually buys, measured in operations.
"""

from __future__ import annotations

import math

import mpmath
import sympy as sp


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    print(f"  sympy {sp.__version__}; mpmath default precision "
          f"mpmath.mp.dps = {mpmath.mp.dps} decimal digits")

    # ------------------------------------------------------------------
    section("1. Assumptions decide the answer")
    # ------------------------------------------------------------------
    symbols = {
        "Symbol('x')": sp.Symbol("x"),
        "Symbol('x', real=True)": sp.Symbol("x", real=True),
        "Symbol('x', positive=True)": sp.Symbol("x", positive=True),
        "Symbol('n', integer=True)": sp.Symbol("n", integer=True),
    }
    for construction, sym in symbols.items():
        keys = sorted(k for k, v in sym.assumptions0.items() if v)
        print(f"  {construction:<28} -> {len(keys):>2} assumptions: "
              f"{', '.join(keys)}")
    x_plain, x_real, x_pos, n_int = symbols.values()
    exprs = {
        "sqrt(x**2), x unconstrained": sp.sqrt(x_plain**2),
        "sqrt(x**2), x real": sp.sqrt(x_real**2),
        "sqrt(x**2), x positive": sp.sqrt(x_pos**2),
        "cos(n*pi), n integer": sp.cos(n_int * sp.pi),
        "Abs(x), x positive": sp.Abs(x_pos),
        "log(exp(x)), x real": sp.log(sp.exp(x_real)),
    }
    for label, expr in exprs.items():
        print(f"  {label:<28} -> {expr}")
    print("  Observation: three different answers to 'what is sqrt(x**2)',")
    print("  because the question is under-specified. SymPy keeps the branch")
    print("  it cannot rule out; a positive declaration removes it. Note that")
    print("  real=True alone is not enough -- sqrt(x**2) is |x|, still not x.")

    # ------------------------------------------------------------------
    section("2. Exact rational arithmetic against binary floating point")
    # ------------------------------------------------------------------
    third = sp.Rational(1, 3)
    print(f"  Rational(1, 3): {third}  (exact ratio of two Python ints)")
    print(f"  3 * Rational(1,3) == 1                 : {3 * third == 1}")
    print(f"  3 * (1/3) == 1 in binary64             : {3 * (1 / 3) == 1}")
    print("      ^ measured True: rounding hid the error here, which is why")
    print("      'it worked in my test' is not evidence that a float is exact.")
    print(f"  0.1 + 0.2 == 0.3 in binary64           : {0.1 + 0.2 == 0.3}")
    print(f"      0.1 + 0.2 - 0.3 = {(0.1 + 0.2) - 0.3:.3e}")
    exact_gap = sp.Rational(0.1) - sp.Rational(1, 10)
    print(f"  Rational(0.1) - Rational(1,10) exactly : {exact_gap}")
    print(f"      as a decimal: {float(exact_gap):.3e}, "
          f"relative {float(exact_gap) / 0.1:.3e}")
    big = 10**16
    print(f"  Rational(10)**16 + 1 - Rational(10)**16 : "
          f"{sp.Rational(big) + 1 - sp.Rational(big)}")
    print(f"  1e16 + 1.0 - 1e16 in binary64           : {(1e16 + 1.0) - 1e16}")
    print(f"  Rational(1,3) has denominator {sp.denom(third)} and "
          f"3 * Rational(1,3) is the integer {3 * third}")
    print(f"  Exact value of float 1/3 as a rational: {sp.Rational(1 / 3)}")
    print("  Observation: exact arithmetic is not a higher precision, it is a")
    print("  different arithmetic -- there is no rounding step to accumulate.")
    print("  The price is growth: numerator and denominator gain digits with")
    print("  every operation, so a long rational chain must be evaluated to")
    print("  a float before it is stored in an array.")

    # ------------------------------------------------------------------
    section("3. Recovering the rational a float was meant to be")
    # ------------------------------------------------------------------
    literal = sp.Rational(0.1)
    print(f"  Rational(0.1)  = {literal}")
    print(f"      denominator = {sp.denom(literal)} = 2**"
          f"{int(sp.log(sp.denom(literal), 2))}, the signature of a binary float")
    print(f"  nsimplify(0.1) = {sp.nsimplify(0.1)}")
    print(f"  nsimplify(0.1) - Rational(1,10) = "
          f"{sp.nsimplify(0.1) - sp.Rational(1, 10)}")
    ambiguous = 0.1000000000001
    print(f"  nsimplify({ambiguous!r}) = {sp.nsimplify(ambiguous)}")
    print(f"  nsimplify(0.1, rational=True) = "
          f"{sp.nsimplify(0.1, rational=True)}")
    print("  Observation: nsimplify guesses the simplest number consistent")
    print("  with the float, which is right for a hand-typed constant and")
    print("  wrong for a measurement. The second example shows the failure")
    print("  mode: a value that is genuinely not 1/10 is snapped to a ratio")
    print("  with a small denominator.")

    # ------------------------------------------------------------------
    section("4. What a 50-digit evaluation really delivers")
    # ------------------------------------------------------------------
    mpmath.mp.dps = 50
    high = sp.N(sp.pi, 50)
    text, reference = str(high), mpmath.nstr(mpmath.pi, 50)
    same = 0
    for a, b in zip(text, reference):
        if a != b:
            break
        same += 1
    print(f"  sympy N(pi, 50)          : {text}")
    print(f"  mpmath.nstr(mp.pi, 50)   : {reference}")
    print(f"  characters in agreement  : {same}")
    gap = float(abs(mpmath.mpf(math.pi) - mpmath.mpf(text)))
    print(f"  math.pi (binary64)       : {math.pi!r}")
    print(f"  measured |math.pi - pi|  = {gap:.3e}")
    print(f"  decimal places of agreement for the binary64 value: "
          f"{-math.log10(gap):.2f}")
    print("  Observation: 50 digits are available on demand and they are the")
    print("  right ones. Precision is still not accuracy: the 50th digit says")
    print("  nothing about whether the formula that consumed pi was correct.")

    # ------------------------------------------------------------------
    section("5. Earth's mean density, derived and evaluated")
    # ------------------------------------------------------------------
    G_sym, g_sym, R_sym, pi = sp.symbols("G g R pi", positive=True)
    density = sp.simplify(3 * g_sym / (4 * pi * G_sym * R_sym))
    print("  solving g = (4/3) pi G rho R for rho:")
    print(f"      rho = {sp.latex(density)}")
    g_meas, R_meas, G_meas = 9.80665, 6.371e6, 6.67430e-11
    rho = float(density.subs({g_sym: g_meas, R_sym: R_meas,
                              G_sym: G_meas, pi: sp.pi}))
    print(f"  g = {g_meas} m/s^2, R = {R_meas:.4e} m, "
          f"G = {G_meas:.5e} m^3 kg^-1 s^-2")
    print(f"      rho = {rho:.1f} kg m^-3")
    prem = 5514.0
    print(f"  PREM mean density (textbook reference value, not measured here): "
          f"{prem:.1f} kg m^-3")
    print(f"      difference = {rho - prem:+.1f} kg m^-3 "
          f"({abs(rho - prem) / prem * 100:.2f} %)")
    print("  Observation: three measured numbers reproduce the mean density")
    print("  of the Earth to 0.15 %. The residual has two contributions --")
    print("  the centripetal acceleration at the equator, which this formula")
    print("  ignores, and the fact that the Earth is not uniform. I have not")
    print("  separated them here, so I do not attribute the 0.15 % to either.")

    # ------------------------------------------------------------------
    section("6. What simplify() buys, counted in operations")
    # ------------------------------------------------------------------
    y = sp.Symbol("y")
    cases = [
        ((x_plain**2 - 1) / (x_plain - 1), "rational cancellation"),
        (sp.sin(x_plain) ** 2 + sp.cos(x_plain) ** 2, "Pythagorean identity"),
        (sp.exp(x_plain) * sp.exp(y) / sp.exp(x_plain + y), "exponential addition"),
        ((x_plain + 1) ** 4, "expansion of a fourth power"),
    ]
    for expr, label in cases:
        before = int(sp.count_ops(expr))
        simplified = sp.simplify(expr)
        after = int(sp.count_ops(simplified))
        print(f"  {label:<28} ops {before:>3} -> {after:>3}   "
              f"{expr}  ->  {simplified}")
    checked = sp.cancel((x_plain**2 - 1) / (x_plain - 1))
    print(f"  cancel() named explicitly      : {checked} "
          f"(ops {int(sp.count_ops(checked))})")
    resid = sp.simplify(checked - (x_plain + 1))
    print(f"  verification: cancel(...) - (x + 1) simplifies to {resid}")
    print("  Observation: simplify() is a search, not an algorithm with a")
    print("  guarantee -- it left (x + 1)**4 alone. When you know the identity")
    print("  you want, name the function, and verify the result by substitution.")


if __name__ == "__main__":
    main()
