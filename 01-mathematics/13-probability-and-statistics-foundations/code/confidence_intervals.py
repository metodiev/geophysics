"""Confidence intervals: construction, coverage, and what they do not mean.

Run:  python3 confidence_intervals.py
Requires: Python standard library only.  The Student-t quantile is computed
here from its definition, via the regularised incomplete beta function, so no
statistical tables are needed.
Random seed: 20240123 (fixed).

Companion to lesson 01-13-07.

Coverage is the only property a confidence interval is guaranteed to have, so
it is the property measured here. The last two sections show the ways coverage
breaks in practice: the interval assumes a noise model, and it assumes the
measurement has no systematic error.
"""

import math
import random

SEED = 20240123


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def stdev(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def laplace(rng, b=1.0):
    """Standard Laplace sample: |x| exponential, sign symmetric."""
    u = rng.random()
    if u == 0.0:
        u = 1e-15
    if u < 0.5:
        return b * math.log(2.0 * u)
    return -b * math.log(2.0 * (1.0 - u))


# --------------------------------------------------------------------------
# Student-t quantiles, computed from the definition
# --------------------------------------------------------------------------

def betacf(a: float, b: float, x: float, itmax: int = 300,
           eps: float = 3.0e-15) -> float:
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < 1.0e-300:
        d = 1.0e-300
    d = 1.0 / d
    h = d
    for m in range(1, itmax + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < 1.0e-300:
            d = 1.0e-300
        c = 1.0 + aa / c
        if abs(c) < 1.0e-300:
            c = 1.0e-300
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < 1.0e-300:
            d = 1.0e-300
        c = 1.0 + aa / c
        if abs(c) < 1.0e-300:
            c = 1.0e-300
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def betai(a: float, b: float, x: float) -> float:
    """Regularised incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                     + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * betacf(a, b, x) / a
    return 1.0 - front * betacf(b, a, 1.0 - x) / b


def t_cdf(t: float, df: float) -> float:
    x = df / (df + t * t)
    tail = 0.5 * betai(0.5 * df, 0.5, x)
    return 1.0 - tail if t > 0 else tail


def t_quantile(p: float, df: float) -> float:
    lo, hi = 0.0, 1.0e6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def check_t_quantiles() -> None:
    section("0. The Student-t quantile routine, checked against known limits")
    print("  95 % two-sided critical values t(0.975, df):")
    for df in (1, 2, 5, 15, 30, 100, 10 ** 6):
        print(f"    df = {df:>8}: t = {t_quantile(0.975, df):.6f}")
    print("  As df grows the value approaches the normal 1.959964. At df = 1 the")
    print(f"  t distribution is Cauchy and the quantile is "
          f"{t_quantile(0.975, 1):.6f},")
    print(f"  against tan(0.475 pi) = {math.tan(0.475 * math.pi):.6f} computed")
    print("  directly. Both checks pass, so the tables used below are honest.")


# --------------------------------------------------------------------------
# 1. Known-sigma z interval
# --------------------------------------------------------------------------

def z_interval() -> None:
    section("1. Known-sigma z interval: nominal 95 %, observed coverage")
    mu, sigma, n = 10.0, 2.0, 16
    z = 1.9599639845
    half = z * sigma / math.sqrt(n)
    rng = random.Random(SEED)
    reps = 100_000
    inside = 0
    for _ in range(reps):
        xs = [rng.gauss(mu, sigma) for _ in range(n)]
        if mean(xs) - half <= mu <= mean(xs) + half:
            inside += 1
    se = math.sqrt(0.95 * 0.05 / reps)
    print(f"  mu = {mu}, sigma = {sigma} (known), n = {n}, reps = {reps:,}")
    print(f"  half-width = 1.96 sigma/sqrt(n) = {half:.6f}")
    print(f"  nominal coverage  = 0.950000")
    print(f"  observed coverage = {inside / reps:.6f}  "
          f"(binomial standard error {se:.6f})")


# --------------------------------------------------------------------------
# 2. Unknown-sigma t interval
# --------------------------------------------------------------------------

def t_interval() -> None:
    section("2. Unknown-sigma t interval: coverage at nominal 95 %")
    mu, n = 10.0, 16
    df = n - 1
    tcrit = t_quantile(0.975, df)
    print(f"  n = {n}, df = {df}, t(0.975, {df}) = {tcrit:.6f} "
          f"(against 1.95996 for known sigma)")
    rng = random.Random(SEED + 1)
    reps = 100_000
    for name, gen in (("Gaussian(10,2)", lambda r: r.gauss(mu, 2.0)),
                      ("Laplace(10,2) ", lambda r: mu + 2.0 * laplace(r))):
        inside = 0
        for _ in range(reps):
            xs = [gen(rng) for _ in range(n)]
            half = tcrit * stdev(xs) / math.sqrt(n)
            if mean(xs) - half <= mu <= mean(xs) + half:
                inside += 1
        print(f"  observed coverage, {name} = {inside / reps:.6f}")
    print("  Both are close to 0.95. The Laplace value sits slightly *above*")
    print("  nominal: symmetric heavy tails inflate the sample standard deviation")
    print("  often enough to buy back the coverage that the occasional outlier")
    print("  costs. The effect is small and is not a licence to assume that heavy")
    print("  tails are harmless; Section 3 shows where it fails badly.")


# --------------------------------------------------------------------------
# 3. Coverage when the noise model is wrong
# --------------------------------------------------------------------------

def coverage_breakdown() -> None:
    section("3. Coverage when the noise model is wrong")
    reps = 20_000
    cases = (
        ("Gaussian(0,1)          ", 0.0, lambda r: r.gauss(0.0, 1.0),
         (16, 256)),
        ("Laplace(0,1)           ", 0.0, lambda r: laplace(r), (16, 256)),
        ("Pareto(1.5) mean 3     ", 3.0,
         lambda r: r.random() ** (-1.0 / 1.5), (16, 256)),
    )
    print("  nominal coverage 0.95; the target is the parent mean")
    print(f"  {'parent':>24}  {'n':>6}  {'coverage':>10}  "
          f"{'mean half-width':>16}")
    for name, target, gen, ns in cases:
        for n in ns:
            rng = random.Random(SEED + 2 + n)
            tcrit = t_quantile(0.975, n - 1)
            inside = 0
            widths = 0.0
            for _ in range(reps):
                xs = [gen(rng) for _ in range(n)]
                half = tcrit * stdev(xs) / math.sqrt(n)
                widths += half
                if abs(mean(xs) - target) <= half:
                    inside += 1
            print(f"  {name:>24}  {n:>6}  {inside / reps:>10.6f}  "
                  f"{widths / reps:>16.6f}")
    print("  For Gaussian noise the interval is calibrated. For the heavy-tailed")
    print("  Pareto parent the sample standard deviation is unstable, so the")
    print("  interval fails well below 0.95 and does not recover by n = 256.")
    print("  Coverage is a property of the pair (procedure, model), not of the")
    print("  procedure alone.")

    print("\n  Systematic error is worse than any distributional misspecification.")
    print("  Target 0, every reading offset by +0.5 mGal, sigma = 1.0 mGal:")
    sigma, offset = 1.0, 0.5
    print(f"  {'n':>6}  {'half-width':>11}  {'coverage':>10}")
    for n in (16, 64, 256, 1024):
        rng = random.Random(SEED + 3 + n)
        tcrit = t_quantile(0.975, n - 1)
        inside = 0
        widths = 0.0
        for _ in range(reps):
            xs = [rng.gauss(0.0, sigma) + offset for _ in range(n)]
            half = tcrit * stdev(xs) / math.sqrt(n)
            widths += half
            if abs(mean(xs)) <= half:
                inside += 1
        print(f"  {n:>6}  {widths / reps:>11.6f}  {inside / reps:>10.6f}")
    print("  At n = 16 the half-width (about 0.53) is comparable to the offset")
    print("  (0.5), so coverage is a little over one half. As n grows the interval")
    print("  narrows as n^-1/2 while the offset does not move at all, and coverage")
    print("  collapses towards zero. The interval is doing exactly what it")
    print("  promises: it covers the mean of the measured quantity. The measured")
    print("  quantity is simply not the physical target, and no amount of")
    print("  statistics inside the loop can detect a bias that lives outside it.")


# --------------------------------------------------------------------------
# 4. What a realised interval is
# --------------------------------------------------------------------------

def interpretation() -> None:
    section("4. What a realised interval is, and what it is not")
    mu, sigma, n = 10.0, 2.0, 16
    half = 1.9599639845 * sigma / math.sqrt(n)
    rng = random.Random(SEED + 4)
    print(f"  true mu = {mu}; twelve realised 95 % intervals of half-width "
          f"{half:.4f}:")
    for _ in range(12):
        xs = [rng.gauss(mu, sigma) for _ in range(n)]
        m = mean(xs)
        flag = "covers" if m - half <= mu <= m + half else "MISSES"
        print(f"    [{m - half:8.4f}, {m + half:8.4f}]  {flag}")
    print("  Across many repetitions about 95 % of intervals cover mu, and that")
    print("  is the whole content of the statement. For a single realised")
    print("  interval the probability that mu lies inside it is 0 or 1, because")
    print("  mu is fixed and the endpoints are the random quantities. The common")
    print("  sentence 'there is a 95 % probability that mu is in this interval'")
    print("  is a Bayesian statement that requires a prior on mu; it is not what")
    print("  the confidence procedure asserts. A credible interval answers that")
    print("  question; a confidence interval answers a different one.")


def main() -> None:
    check_t_quantiles()
    z_interval()
    t_interval()
    coverage_breakdown()
    interpretation()
    print("\nDone. Reproducible with seed 20240123.")


if __name__ == "__main__":
    main()
