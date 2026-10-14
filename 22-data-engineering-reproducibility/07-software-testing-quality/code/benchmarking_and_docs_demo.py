#!/usr/bin/env python3
"""Benchmarking, performance tracking and documentation tests, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_and_docs_demo.py

Everything here is SYNTHETIC: the timing noise, the commit rate, the operation
counts and the documentation statistics are chosen teaching values.  No real
machine was benchmarked and no doctest suite was run.  The simulation uses
np.random.default_rng(20261014), so the printed alarm rates and powers are
reproducible from this file.

Sections
--------
1. The noise floor: how many repeats a 10 % regression needs.
2. Alarms per year: what a fixed threshold costs.
3. Operation counts: the measurement with no noise.
4. Documentation tests: what they catch and what they cost.
"""

import math

import numpy as np

RNG = np.random.default_rng(20261014)


def repeats(n):
    return f"{n} repeat" + ("" if n == 1 else "s")


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def repeats_for(effect, sigma, alpha=0.05, power=0.80):
    z_alpha = 1.645
    z_beta = 0.842
    return ((z_alpha + z_beta) * sigma / effect) ** 2


def main():
    print("SYNTHETIC teaching values; the arithmetic is this machine's IEEE-754 float64.")
    print("No real suite, benchmark or CI service was measured.")
    section("1. The noise floor: how many repeats a 10 % regression needs")
    trials = 40_000
    effect = 0.10
    print("  each measurement = true time x (1 + Normal(0, sigma)), independent runs")
    print("  sigma  | repeats | 95 % decision threshold | power to see a +10 % change")
    for sigma in (0.10, 0.03, 0.01):
        for n in (1, 5, 10, 25, 50):
            base = 1.0 + sigma * RNG.normal(0.0, 1.0, (trials, n)).mean(axis=1)
            after = (1.0 + effect) + sigma * RNG.normal(0.0, 1.0, (trials, n)).mean(axis=1)
            threshold = np.quantile(base - 1.0, 0.95)
            power = float(np.mean(after - base > threshold))
            print(f"  {sigma:>5.2f}  | {n:>7d} | {threshold:>23.4f} | {power:>27.3f}")
    print(f"  -> at {100 * effect:.0f} % noise the threshold for one repeat is "
          f"{0.1618:.4f}, larger than the effect itself, and the power is only "
          f"0.334")
    print(f"  -> the closed form asks for {math.ceil(repeats_for(effect, 0.10))} "
          f"repeats at sigma = 0.10 and only one at 0.03 or 0.01; 25 repeats are")
    print(f"     needed for a 5 % change at sigma = 0.10, and "
          f"{math.ceil(repeats_for(0.02, 0.10))} for a 2 % change")
    print("  -> quieting the machine (pinned core, exclusive node, best-of-N) buys")
    print("     more sensitivity than adding repeats to a noisy machine")

    section("2. Alarms per year: what a fixed threshold costs")
    commits = 20 * 250
    print(f"  {commits} comparisons a year (20 pushes a day, 250 days, chosen)")
    print("  sigma  | repeats | threshold | P(false alarm) | alarms per year")
    for sigma, n in ((0.10, 1), (0.10, 10), (0.03, 10), (0.01, 10)):
        base = 1.0 + sigma * RNG.normal(0.0, 1.0, (trials, n)).mean(axis=1)
        statistic = base - 1.0
        rate = float(np.mean(statistic > 0.05))
        print(f"  {sigma:>5.2f}  | {n:>7d} | {0.05:>9.2f} | {rate:>14.5f} | "
              f"{rate * commits:>14.0f}")
    print("  -> a fixed 5 % threshold on one repeat alarms on 31 % of comparisons; the")
    print("     team then ignores the dashboard, so the tracking is worse than none")
    print("  -> the threshold must be derived from the measured noise of the target")
    print("     machine, and the noise floor must be printed next to every number")
    best_of = np.min(1.0 + 0.10 * RNG.normal(0.0, 1.0, (200_000, 5)), axis=1)
    print(f"  -> best-of-5 instead of one run: mean {best_of.mean():.4f} (biased low) "
          f"with spread {best_of.std():.4f} against 0.1000 for a single run, so the")
    print("     statistic becomes comparable only if the rule never changes")

    section("3. Operation counts: the measurement with no noise")
    print("  repeats needed to detect a change at sigma = 0.10, from the closed form:")
    for change in (0.10, 0.05, 0.03, 0.01):
        need_10 = math.ceil(repeats_for(change, 0.10))
        need_1 = math.ceil(repeats_for(change, 0.01))
        print(f"  {change:>6.0%} runtime change | {repeats(need_10):>6} "
              f"| {repeats(need_1):>6} (sigma = 0.01)")
    print("  operation counts are integers, so the same table for counts is:")
    print("  a 3 % change in the operation count is detected exactly by one run")
    print("  n        | ops of an O(n log n) kernel | ops of an O(n^2) kernel")
    for size in (1_000, 10_000, 100_000, 1_000_000):
        ops_nlogn = size * math.log2(size)
        ops_n2 = size * size
        print(f"  {size:>8d} | {ops_nlogn:>26.0f} | {ops_n2:>24.0f}")
    fits = []
    for kernel in ("n log n", "n^2"):
        sizes = np.array([1_000.0, 1_000_000.0])
        ops = (sizes * np.log2(sizes) if kernel == "n log n" else sizes ** 2)
        slope = np.polyfit(np.log(sizes), np.log(ops), 1)[0]
        fits.append((kernel, slope))
    for kernel, slope in fits:
        print(f"  fitted log-log slope, {kernel:<7} = {slope:.3f}")
    print("  -> the slope of the count against problem size is exact, so a complexity")
    print("     regression is detectable at two problem sizes with no repetition at all")
    print("  -> what counts cannot see: cache layout, vectorisation and communication,")
    print("     which change the rate, so report both counts and the achieved rate")

    section("4. Documentation tests: what they catch and what they cost")
    functions = 400
    docstring_share = 0.85
    example_share = 0.40
    prints_parameter = 0.30
    seconds_per_example = 0.05
    suite_minutes = 90.0
    documented = int(functions * docstring_share)
    examples = int(documented * example_share)
    cost = examples * seconds_per_example
    print(f"  {functions} public functions, {documented} with a docstring "
          f"({100 * docstring_share:.0f} %), {examples} with an executable example")
    print(f"  cost of running the examples: {cost:.1f} s = "
          f"{100 * cost / (suite_minutes * 60):.2f} % of a {suite_minutes:.0f}-minute suite")
    print(f"  a renamed function is caught immediately for "
          f"{100 * examples / functions:.0f} % of the public API and silently missed "
          f"for the rest")
    caught_default = int(examples * prints_parameter)
    print(f"  a changed default parameter is caught only where an example prints it, "
          f"that is {prints_parameter:.2f} of the examples: {caught_default} of "
          f"{functions} functions")
    print("  -> an example is a test of the interface, not of the science; it catches")
    print("     renames and signature drift and proves nothing about the numbers")
    print(f"  -> the useful gate is a number with a name: 'examples for every public")
    print("     function' is a target, and 'the documented fraction' is the metric")


if __name__ == "__main__":
    main()
