#!/usr/bin/env python3
"""Data pipeline reliability: retries, idempotency and duplicates, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_pipelines_demo.py

Everything here is SYNTHETIC.  Failure probabilities, retry limits and stage costs
are chosen teaching values; no pipeline was run and no service was called.

Sections
--------
1. End-to-end success for a chain of stages, with and without retries.
2. Expected attempts and wasted work per run.
3. At-least-once delivery: duplicate and loss rates for a retry policy.
4. Partial failure: which stages must be idempotent, and what it costs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC pipeline model (chosen, not measured) ------------------------
N_STAGES = 8
P_FAIL = 0.02          # per-attempt failure probability of each stage
MAX_RETRIES = 3
N_RUNS = 100_000       # simulated pipeline runs
P_DELIVER = 0.99       # probability a message reaches the consumer at all


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. End-to-end success for a chain of stages")
    p_no_retry = (1.0 - P_FAIL) ** N_STAGES
    p_stage_retry = 1.0 - P_FAIL ** (MAX_RETRIES + 1)
    p_with_retry = p_stage_retry ** N_STAGES
    print(f"SYNTHETIC pipeline: {N_STAGES} stages, per-attempt failure "
          f"{P_FAIL:.2f}, retries {MAX_RETRIES} (chosen)")
    print(f"  no retries: stage success {1 - P_FAIL:.4f}, end-to-end "
          f"{p_no_retry:.4f} ({100 * p_no_retry:.1f} %)")
    print(f"  with retries: stage success {p_stage_retry:.6f}, end-to-end "
          f"{p_with_retry:.6f} ({100 * p_with_retry:.4f} %)")
    print(f"  failures per 10 000 runs: no retries "
          f"{10000 * (1 - p_no_retry):.0f}, with retries "
          f"{10000 * (1 - p_with_retry):.1f}")
    print("  -> retries turn a per-stage flake into a rare event, but they do not")
    print("     make the pipeline correct: the failure probability is multiplied,")
    print("     not removed, and each retry must be safe to repeat")

    section("2. Expected attempts and wasted work")
    expected_attempts = sum(P_FAIL ** k for k in range(MAX_RETRIES + 1))
    print(f"  expected attempts per stage = sum p^k, k = 0..{MAX_RETRIES} = "
          f"{expected_attempts:.6f}")
    print(f"  total stage attempts per run = "
          f"{N_STAGES * expected_attempts:.4f} (against {N_STAGES} ideal)")
    print(f"  wasted fraction = "
          f"{100 * (N_STAGES * expected_attempts - N_STAGES) / N_STAGES:.3f} %")
    print("  -> the cost of retries is equal to the failure rate that triggers")
    print("     them: a 2 % flake rate costs 2 % more work, which is trivial")
    print("     next to the value of not failing 15 % of the time")

    section("3. At-least-once delivery: duplicates and losses")
    runs = RNG.random((N_RUNS, N_STAGES)) < P_FAIL
    delivered = RNG.random((N_RUNS, N_STAGES)) < P_DELIVER
    retries = runs            # any stage that failed is retried
    dup = retries & delivered & (RNG.random((N_RUNS, N_STAGES)) < 0.5)
    lost = (~runs) & (~delivered)
    print(f"  {N_RUNS} simulated runs, delivery probability {P_DELIVER:.2f}")
    print(f"  stage-attempts that were delivered twice  = {dup.sum()}")
    print(f"  stage-attempts lost without an error      = {lost.sum()}")
    print(f"  duplicate rate = {dup.sum() / (N_RUNS * N_STAGES):.5f}, "
          f"silent loss rate = {lost.sum() / (N_RUNS * N_STAGES):.5f}")
    n_runs_with_dup = int(dup.any(axis=1).sum())
    n_runs_lost = int(lost.any(axis=1).sum())
    print(f"  runs containing at least one duplicate    = {n_runs_with_dup} "
          f"({100 * n_runs_with_dup / N_RUNS:.2f} %)")
    print(f"  runs containing at least one silent loss  = {n_runs_lost} "
          f"({100 * n_runs_lost / N_RUNS:.2f} %)")
    print("  -> a retry policy converts failures into duplicates; an idempotent")
    print("     stage must produce the same state for the same input, or the")
    print("     duplicate becomes double counting")

    section("4. Which stages must be idempotent")
    print("  stage kind            | idempotent by construction? | if retried, harm")
    rows = [
        ("download to a file", "yes, same bytes overwritten", "none"),
        ("append to a table", "no", "duplicated rows"),
        ("increment a counter", "no", "inflated totals"),
        ("write a whole output", "yes, replaced", "none"),
        ("emit a message", "no", "duplicate downstream work"),
        ("delete then write", "yes if keyed by id", "none"),
    ]
    for kind, idem, harm in rows:
        print(f"  {kind:<21} | {idem:<27} | {harm}")
    print("  -> retries assume idempotence; where a stage cannot be made")
    print("     idempotent, the pipeline needs a deduplication key instead")


if __name__ == "__main__":
    main()
