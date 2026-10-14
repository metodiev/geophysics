#!/usr/bin/env python3
"""Continuous integration for research software, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python continuous_integration_demo.py

Everything here is SYNTHETIC.  Job counts, per-job durations, flake rates and
runner counts are chosen teaching values; no CI service is contacted and no
provider limit or quota is quoted.

Sections
--------
1. The matrix: jobs, machine-minutes and the wall-time floor.
2. Flakiness destroys the signal: suite-level red rates and the posterior.
3. Retries: what they buy and what they hide.
4. Sharding: the same machine-minutes, a different wall clock.
"""

import math

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def red_rate(p_test, n_tests):
    return 1.0 - (1.0 - p_test) ** n_tests


def main():
    print("SYNTHETIC teaching values; the arithmetic is this machine's IEEE-754 float64.")
    print("No real suite, benchmark or CI service was measured.")
    section("1. The matrix: jobs, machine-minutes and the wall-time floor")
    systems = 3
    pythons = 4
    deps = 2
    jobs = systems * pythons * deps
    setup = 0.5
    install = 2.0
    cached_install = 0.2
    tests = 6.0
    per_job = setup + install + tests
    per_job_cached = setup + cached_install + tests
    print(f"  matrix: {systems} systems x {pythons} Python versions x {deps} "
          f"dependency sets = {jobs} jobs (chosen)")
    print(f"  per job: {setup:.1f} setup + {install:.1f} install + {tests:.1f} tests "
          f"= {per_job:.1f} min, or {per_job_cached:.1f} min with a warm cache")
    print(f"  machine-minutes: {jobs * per_job:.0f} cold, {jobs * per_job_cached:.0f} "
          f"warm -> caching saves {jobs * (per_job - per_job_cached):.0f} machine-minutes")
    print("  runners | wall time (min) | machine-minutes | runner utilization")
    for runners in (1, 2, 3, 5, 8, 12, 24, 48):
        waves = math.ceil(jobs / runners)
        wall = waves * per_job
        used = jobs * per_job
        util = used / (wall * min(runners, jobs))
        print(f"  {runners:>7d} | {wall:>15.2f} | {used:>15.0f} | "
              f"{100 * util:>17.1f} %")
    print(f"  -> beyond {jobs} runners the wall time cannot fall below one job "
          f"({per_job:.1f} min): the duration is the parallelism limit, not the fleet")
    fast_lane_minutes = per_job_cached
    print(f"  -> a fast lane (one system, newest version) finishes in "
          f"{fast_lane_minutes:.1f} min; the full matrix is a nightly job")

    section("2. Flakiness destroys the signal: suite-level red rates")
    n_tests = 600
    prior_broken = 0.10
    print(f"  suite of {n_tests} tests, prior probability that a push is broken "
          f"= {prior_broken:.2f} (chosen)")
    print("  flake rate per test | P(suite red) | P(the push is broken | red)")
    for p in (0.0001, 0.001, 0.005, 0.01, 0.02):
        red = red_rate(p, n_tests)
        posterior = prior_broken / (prior_broken + (1 - prior_broken) * red)
        print(f"  {p:>19.4f} | {red:>12.4f} | {posterior:>28.4f}")
    p = 0.01
    red = red_rate(p, n_tests)
    posterior = prior_broken / (prior_broken + (1 - prior_broken) * red)
    print(f"  -> at a {100 * p:.1f} % per-test flake rate a red build means the code "
          f"is broken with probability {posterior:.3f}")
    print(f"  -> {100 * (1 - posterior):.1f} % of red builds are noise, so a red build "
          f"stops being a signal and becomes a rerun")
    pushes = 20 * 250
    print(f"  -> {pushes} pushes a year produce about {pushes * red:.0f} red builds "
          f"and {pushes * (1 - prior_broken) * red:.0f} of them spurious")

    section("3. Retries: what they buy and what they hide")
    print("  attempts | spurious red per push | spurious reds per year")
    for attempts in (1, 2, 3):
        per_test = p ** attempts
        rate = red_rate(per_test, n_tests)
        print(f"  {attempts:>8d} | {rate:>23.6f} | {pushes * rate:>24.1f}")
    print("  -> two attempts cut spurious reds by a factor of "
          f"{red_rate(p, n_tests) / red_rate(p ** 2, n_tests):.0f}; a third cuts them "
          f"again")
    real = 0.05
    masked = (1 - red_rate(real ** 3, n_tests))
    print(f"  -> a genuinely intermittent failure affecting {100 * real:.0f} % of runs "
          f"is caught with certainty by one attempt")
    print(f"  -> with three attempts the same bug looks green in {100 * masked:.1f} % "
          f"of pushes: retries hide real races as effectively as they hide noise")
    print("  -> a retried failure must always open a record: run the test in a loop, "
          "measure the failure rate, and fix it or quarantine it with a deadline")

    section("4. Sharding: the same machine-minutes, a different wall clock")
    n_files = 60
    file_means = RNG.lognormal(mean=math.log(0.6), sigma=0.9, size=n_files)
    counts = RNG.integers(20, 60, size=n_files)
    file_totals = np.empty(n_files)
    for k in range(n_files):
        file_totals[k] = RNG.lognormal(
            mean=math.log(file_means[k]), sigma=0.5, size=counts[k]).sum()
    total = file_totals.sum()
    print(f"  {n_files} test files, {counts.sum()} tests, {total:.0f} s of test work on "
          f"one runner (chosen lognormal file costs)")
    print(f"  slowest file {file_totals.max():.1f} s, median file {np.median(file_totals):.1f} s")
    shards = 4
    naive = np.array_split(file_totals, shards)
    naive_wall = max(part.sum() for part in naive)
    print(f"  contiguous split of the file list : wall {naive_wall:.1f} s, shard times "
          f"{np.round([part.sum() for part in naive], 1).tolist()}")
    order = np.argsort(-file_totals)
    bins = np.zeros(shards)
    for k in order:
        bins[int(np.argmin(bins))] += file_totals[k]
    print(f"  longest-file-first assignment    : wall {bins.max():.1f} s, shard times "
          f"{np.round(bins, 1).tolist()}")
    print(f"  -> ordering by the largest file first cuts the wall time from "
          f"{naive_wall:.1f} s to {bins.max():.1f} s "
          f"({100 * (1 - bins.max() / naive_wall):.1f} % shorter) at identical "
          f"machine-minutes")
    print(f"  -> the residual floor is the largest single file "
          f"({file_totals.max():.1f} s): sharding cannot fix one slow file, only "
          f"splitting it can")


if __name__ == "__main__":
    main()
