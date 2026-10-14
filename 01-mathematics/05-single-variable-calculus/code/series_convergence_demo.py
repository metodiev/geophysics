"""Sequences, series and convergence, with the error printed at each step.

Run:  python3 series_convergence_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-07. Two ideas run through the whole file. First,
convergence is a statement about the *tail*, so a series is judged by how its
terms eventually behave, never by its first terms. Second, the useful question
is not 'does it converge' but 'how many terms do I need' - which is why every
section prints an error rather than a verdict.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def main() -> None:
    section("1. Geometric series: convergence rate is just the ratio")
    r = 0.8
    exact = 1.0 / (1.0 - r)
    print(f"  r = {r}, exact sum = 1/(1-r) = {exact!r}")
    print(f"{'terms n':>8}  {'partial sum':>22}  {'error':>12}"
          f"  {'prev err / err':>16}")
    previous = None
    for n in (1, 2, 5, 10, 20, 50, 100):
        partial = sum(r ** k for k in range(n))
        error = exact - partial
        ratio = previous / error if previous else float("nan")
        print(f"{n:>8}  {partial:>22.17f}  {error:>12.3e}  {ratio:>16.4f}")
        previous = error
    print("  Reading: the ratio of successive errors is (1/r) raised to the")
    print("  number of terms added - 1.25 for one step, 1.25^30 = 808 for the")
    print("  thirty steps between n = 20 and n = 50, and 1.25^50 = 70065 for")
    print("  the fifty steps between n = 50 and n = 100. In other words the")
    print("  error itself falls by exactly the factor r = 0.8 per term. A")
    print("  geometric series is the reference against which every other series")
    print("  is judged: if you can bound a remainder by a geometric series with")
    print("  ratio r < 1, the question is answered.")

    section("2. Harmonic series: divergence you cannot see")
    total = 0.0
    gamma = 0.5772156649015329
    print(f"{'n':>10}  {'H_n':>20}  {'ln n + gamma':>16}")
    n_previous = 0
    for n in (10, 100, 1000, 10000, 1000000, 10000000):
        for k in range(n_previous + 1, n + 1):
            total += 1.0 / k
        n_previous = n
        print(f"{n:>10}  {total:>20.10f}  {math.log(n) + gamma:>16.10f}")
    print("  Reading: H_n = ln n + gamma + O(1/n), with gamma the")
    print("  Euler-Mascheroni constant 0.5772156649. Even at ten million terms")
    print("  the sum has reached only about 16.7. Divergence is a fact about")
    print("  the limit; on any finite computation it is indistinguishable from")
    print("  very slow convergence, which is exactly why an iterative solver")
    print("  that 'has not converged yet' must be diagnosed from its rate of")
    print("  change rather than from patience.")

    section("3. p-series: the borderline case p = 1")
    print(f"{'p':>6}  {'n':>10}  {'partial sum':>20}  {'pi^2/6 or (diverges)':>22}")
    for p in (2.0, 1.5, 1.0):
        for n in (100, 10000, 1000000):
            partial = sum(k ** -p for k in range(1, n + 1))
            label = f"{math.pi ** 2 / 6.0:.12f}" if p == 2.0 else "(diverges)"
            print(f"{p:>6.1f}  {n:>10}  {partial:>20.12f}  {label:>22}")
    print("  Reading: sum 1/n^2 converges to pi^2/6 = 1.644934066848; sum")
    print("  1/n^1.5 converges more slowly; sum 1/n diverges. The exponent 1 is")
    print("  the exact boundary, and the boundary is logarithmic: no power of n")
    print("  describes the growth of the harmonic sum.")

    section("4. The ratio test: decisive, inconclusive, and misused")
    print("  Series A: sum 10^n / n!   (terms a_n = 10^n/n!)")
    a = 1.0
    for n in (1, 5, 10, 20, 50, 100):
        a = 10.0 ** n / math.factorial(n)
        next_a = 10.0 ** (n + 1) / math.factorial(n + 1)
        print(f"    n={n:>4}: a_n = {a:.6e}   a_(n+1)/a_n = {next_a / a:.6f}")
    print("    ratio -> 0, so the series converges (to exp(10), in fact).")
    print("  Series B: sum 1/n^2   (terms a_n = n^-2)")
    for n in (10, 100, 1000, 10000):
        print(f"    n={n:>6}: a_(n+1)/a_n = {((n + 1.0) / n) ** 2:.8f}")
    print("    ratio -> 1 for every p, so the ratio test proves nothing about")
    print("    any p-series. When the ratio test is inconclusive you need a")
    print("    comparison test, an integral test, or a logarithm.")

    section("5. Alternating series: a convergence rate you can quote")
    print(f"{'n':>10}  {'partial sum':>20}  {'|error|':>12}"
          f"  {'next term 1/(n+1)':>18}  {'ratio':>8}")
    for n in (10, 100, 1000, 10000, 1000000):
        partial = sum(((-1) ** (k + 1)) / k for k in range(1, n + 1))
        error = abs(partial - math.log(2.0))
        bound = 1.0 / (n + 1.0)
        print(f"{n:>10}  {partial:>20.16f}  {error:>12.3e}"
              f"  {bound:>18.3e}  {error / bound:>8.4f}")
    print("  Reading: for an alternating series with decreasing terms the error")
    print("  is bounded by the first omitted term, and here the error is")
    print("  consistently half the bound. That factor of 2 is the difference")
    print("  between a bound and an estimate; a bound is safe, an estimate is")
    print("  useful, and only an analysis gives you the estimate.")

    section("6. Fixed-point iteration: linear convergence with a known rate")
    print("  Solving x = cos(x) by x_(n+1) = cos(x_n) from x_0 = 0.5")
    print(f"{'n':>4}  {'x_n':>20}  {'|error|':>12}"
          f"  {'err_n / err_(n-1)':>18}")
    x = 0.5
    root = 0.7390851332151607
    previous = None
    for n in range(1, 41):
        x = math.cos(x)
        error = abs(x - root)
        if n <= 6 or n in (10, 20, 40):
            ratio = error / previous if previous else float("nan")
            print(f"{n:>4}  {x:>20.16f}  {error:>12.3e}  {ratio:>18.4f}")
        previous = error
    print(f"  |g'(root)| = |sin(root)| = {abs(math.sin(root)):.6f}")
    print("  Reading: the ratio of successive errors settles on 0.6736, which")
    print("  is exactly |g'(root)|, the derivative of the iteration map at the")
    print("  fixed point. The error shrinks by a constant factor per iteration -")
    print("  linear convergence with rate |g'(root)| < 1 - and that factor is")
    print("  computable before you iterate, so you can predict in advance how")
    print("  many iterations a tolerance will cost. Fixed-point iterations")
    print("  converge when the map is a contraction; |g'| > 1 makes them")
    print("  diverge, and |g'| = 1 makes them crawl.")

    section("7. Newton's method: quadratic convergence, and its price")
    print("  Solving x^2 - 2 = 0 by x_(n+1) = (x_n + 2/x_n)/2")
    print(f"{'n':>4}  {'x_n':>24}  {'|error|':>12}"
          f"  {'err_n / err_(n-1)^2':>22}")
    x = 1.0
    target = math.sqrt(2.0)
    previous = None
    for n in range(0, 6):
        error = abs(x - target)
        ratio = error / previous ** 2 if previous else float("nan")
        print(f"{n:>4}  {x:>24.17f}  {error:>12.3e}  {ratio:>22.6f}")
        previous = error
        x = 0.5 * (x + 2.0 / x)
    print("  Reading: the errors are 4.1e-1, 8.6e-2, 2.5e-3, 2.1e-6, 1.6e-12")
    print("  - each roughly the square of the previous one, so the number of")
    print("  correct digits doubles per iteration. The last column, error")
    print("  divided by the square of the previous error, settles near 0.354 =")
    print("  1/(2 sqrt 2): the constant in the quadratic error law. The price of")
    print("  this speed is that Newton's method needs a derivative and can fail")
    print("  when that derivative vanishes or the initial guess is far away.")

    section("8. Series in floating point: accuracy has a floor too")
    # Sum 1/k^2 forwards and backwards; the true limit is pi^2/6.
    exact = math.pi ** 2 / 6.0
    n = 1000000
    forward = 0.0
    for k in range(1, n + 1):
        forward += 1.0 / k ** 2
    backward = 0.0
    for k in range(n, 0, -1):
        backward += 1.0 / k ** 2
    tail = 1.0 / n
    print(f"  sum_1^{n} 1/k^2, added forwards  = {forward!r}")
    print(f"  sum_1^{n} 1/k^2, added backwards = {backward!r}")
    print(f"  difference between the two orders = {abs(forward - backward):.3e}")
    print(f"  true limit pi^2/6 = {exact!r}")
    print(f"  truncation tail ~ 1/n = {tail:.3e}")
    print("  Reading: two mathematically identical summations differ by")
    print("  4.374e-14 - about three parts in 10^14. Which one is closer to the")
    print("  truth depends on the order of the terms, which is a fact about the")
    print("  machine rather than about the series. Note also the scale: the")
    print("  truncation tail 1/n = 1e-6 is ten million times larger than the")
    print("  order-of-summation effect, so here the *mathematics* of convergence")
    print("  matters far more than the arithmetic. Sum small terms first when you")
    print("  can, but bound the tail first of all.")

    section("9. A divergent series that is still useful: the asymptotic E1")
    # E1(x) = int_x^inf exp(-t)/t dt ~ (e^-x / x) * sum_k (-1)^k k!/x^k.
    # The series diverges for every x, yet its smallest term is tiny.

    def simpson(f, a: float, b: float, n: int) -> float:
        if n % 2:
            n += 1
        h = (b - a) / n
        total = f(a) + f(b)
        for i in range(1, n):
            total += (4.0 if i % 2 else 2.0) * f(a + i * h)
        return total * h / 3.0

    x = 20.0
    exact = simpson(lambda t: math.exp(-t) / t, x, x + 60.0, 200000)
    print(f"  x = {x:.0f}, E1(x) computed by quadrature = {exact!r}")
    print(f"{'terms k':>8}  {'partial asymptotic sum':>24}  {'relative error':>16}")
    prefactor = math.exp(-x) / x
    total = 0.0
    for k in range(0, 9):
        total += (-1.0) ** k * math.factorial(k) / x ** k
        approximate = prefactor * total
        print(f"{k:>8}  {approximate:>24.12e}"
              f"  {abs(approximate - exact) / exact:>16.3e}")
    print("  Reading: the terms k!/x^k shrink while k < x and grow once k > x,")
    print("  so the series diverges - yet at k = 8, near the smallest term, the")
    print("  answer is right to five parts in ten million. That is how")
    print("  asymptotic series are used: truncated at the smallest term, never")
    print("  summed to infinity. Every multipole expansion in potential theory")
    print("  behaves this way.")


if __name__ == "__main__":
    main()
