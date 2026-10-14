#!/usr/bin/env python3
"""How much review is enough? A SYNTHETIC inspection model with numbers.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code_review_demo.py

Everything here is SYNTHETIC.  The defect density, the inspection rate and the
detection law are chosen teaching values; no defect database is read and no
published review study is quoted.

Sections
--------
1. Detection probability and inspection time versus change size.
2. Escaped defects per KLOC versus change size.
3. One reviewer versus two, as a function of review size.
4. Monte Carlo scatter: the escape rate is itself uncertain.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC inspection model (chosen, not measured) ----------------------
DEFECT_DENSITY = 8.0     # defects per KLOC before review
INSPECT_RATE = 200.0     # lines inspected per person-hour
K_DETECT = 0.90          # detection rate law p = 1 - exp(-k t), 1/hour
SIZES = np.array([25, 50, 100, 200, 400, 800])


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def detection(size, rate=INSPECT_RATE, k=K_DETECT):
    """Detection probability for a change of `size` lines."""
    hours = size / rate
    return 1.0 - np.exp(-k * hours)


def escapes_per_kloc(size, p_two=False):
    """Escaped defects per KLOC after review."""
    p = detection(size)
    if p_two:
        p = 1.0 - (1.0 - p) ** 2
    return DEFECT_DENSITY * (1.0 - p)


def main():
    section("1. Detection probability and inspection time versus change size")
    print(f"SYNTHETIC model: density {DEFECT_DENSITY:.1f} defects/KLOC, "
          f"inspection rate {INSPECT_RATE:.0f} lines/h, "
          f"p = 1 - exp(-{K_DETECT:.2f} t) (chosen)")
    print("  size (lines) | person-hours | p(detect) | defects in review")
    for size in SIZES:
        t = size / INSPECT_RATE
        p = detection(size)
        print(f"  {size:>12d} | {t:>12.2f} | {p:>9.3f} | "
              f"{p * DEFECT_DENSITY * size / 1000.0:>10.2f}")
    print("  -> doubling a review does not double detection; the law saturates "
          "and the marginal value of extra lines falls")

    section("2. Escaped defects per KLOC versus change size")
    print("  size (lines) | escaped defects per KLOC")
    for size in SIZES:
        print(f"  {size:>12d} | {escapes_per_kloc(size):>9.2f}")
    target = 1.0
    sizes = np.linspace(5.0, 1200.0, 12000)
    esc = escapes_per_kloc(sizes)
    crossing = float(sizes[np.argmax(esc < target)])
    print(f"  size at which escapes fall below {target:.1f} per KLOC = "
          f"{crossing:.0f} lines")
    print("  -> review time is linear in size, but the escape rate is not: "
          "large reviews are the expensive place to hide defects")

    section("3. One reviewer versus two")
    print("  size (lines) | escapes, one | escapes, two | reduction")
    for size in SIZES:
        one = escapes_per_kloc(size)
        two = escapes_per_kloc(size, p_two=True)
        print(f"  {size:>12d} | {one:>13.2f} | {two:>13.2f} | "
              f"{100.0 * (1.0 - two / one):>8.1f} %")
    print("  -> a second independent reviewer multiplies the odds, but it also "
          "multiplies the cost: 2x person-hours for the same change")

    section("4. Monte Carlo scatter on the escape rate")
    size = 200
    p = detection(size)
    defects = DEFECT_DENSITY * size / 1000.0          # expected defects in change
    draws = RNG.binomial(int(round(defects * 1000)), p, size=2000) / 1000.0
    print(f"  change size {size} lines: expected defects = {defects:.2f}, "
          f"p(detect) = {p:.3f}")
    print(f"  escaped defects per change: mean = {1.0 - draws.mean():.3f}, "
          f"s.d. = {draws.std():.3f} over 2000 simulated reviews")
    print(f"  5th-95th percentile of escapes = "
          f"{np.percentile(1.0 - draws, 5):.2f} to {np.percentile(1.0 - draws, 95):.2f}")
    print("  -> the escape rate is a distribution; a review process cannot be "
          "certified by a single observed outcome")


if __name__ == "__main__":
    main()
