#!/usr/bin/env python3
"""Programmatic access to Earth data: planning a windowed fetch, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python getting_earth_data_demo.py

Everything here is SYNTHETIC.  The service model (per-request latency, window cap,
transfer rate, rate limit and retry probability) uses chosen teaching values; no
service was called and no published performance figure is quoted.

Sections
--------
1. A fetch plan: requests, overhead and transfer time versus window length.
2. The window cap and the rate limit: which constraint binds.
3. Retries: the cost of a flaky service, and the plan that absorbs it.
4. What a fetch plan must record for the result to be reproducible.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC service model (chosen, not measured) -------------------------
TOTAL_DAYS = 365.0
LATENCY_S = 1.0             # fixed cost per request, s
WINDOW_CAP_DAYS = 30.0      # maximum span a single request may ask for
DATA_RATE_MB_S = 5.0        # transfer rate, MB/s
BYTES_PER_DAY_MB = 40.0     # data volume per day of record, MB
RATE_LIMIT_PER_MIN = 60.0   # service rate limit, requests per minute
P_REQUEST_FAIL = 0.05       # probability a request fails and must be retried
MAX_RETRIES = 2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def plan(days, window_days):
    """Fetch plan for `days` of record with the given window length."""
    n_requests = int(np.ceil(days / window_days))
    overhead = n_requests * LATENCY_S
    bytes_mb = days * BYTES_PER_DAY_MB
    transfer = bytes_mb / DATA_RATE_MB_S
    return n_requests, bytes_mb, overhead, transfer


def main():
    section("1. A fetch plan: requests, overhead and transfer")
    print(f"SYNTHETIC service: {LATENCY_S:.1f} s per request, window cap "
          f"{WINDOW_CAP_DAYS:.0f} days, {DATA_RATE_MB_S:.0f} MB/s, "
          f"{BYTES_PER_DAY_MB:.0f} MB per day of record (chosen)")
    print(f"  fetching {TOTAL_DAYS:.0f} days of record")
    print("  window (days) | requests | overhead (s) | transfer (s) | total (s)")
    for window in (1.0, 7.0, 30.0):
        n, mb, overhead, transfer = plan(TOTAL_DAYS, window)
        print(f"  {window:>13.0f} | {n:>8d} | {overhead:>12.1f} | "
              f"{transfer:>12.1f} | {overhead + transfer:>9.1f}")
    print("  -> with a fixed per-request cost, fewer and larger requests always")
    print("     win; the window cap is therefore the plan's most valuable number")

    section("2. The window cap and the rate limit")
    n, mb, overhead, transfer = plan(TOTAL_DAYS, WINDOW_CAP_DAYS)
    rate_limited = n / RATE_LIMIT_PER_MIN * 60.0
    print(f"  at the cap ({WINDOW_CAP_DAYS:.0f} days): {n} requests, "
          f"{overhead:.0f} s of latency, {transfer:.0f} s of transfer")
    print(f"  the rate limit allows {RATE_LIMIT_PER_MIN:.0f} requests/min, so the "
          f"floor from the limit is {rate_limited:.1f} s")
    print(f"  binding constraint: "
          f"{'the rate limit' if rate_limited > overhead + transfer else 'latency plus transfer'}")
    print("  -> the plan's total is max(sum of stages, rate-limit floor); quoting")
    print("     one number without the other hides which limit you will hit")

    section("3. Retries: the cost of a flaky service")
    p_fail_any = 1.0 - (1.0 - P_REQUEST_FAIL) ** n
    attempts = sum(P_REQUEST_FAIL ** k for k in range(MAX_RETRIES + 1))
    print(f"  per-request failure probability {P_REQUEST_FAIL:.2f}, "
          f"retries {MAX_RETRIES} (chosen)")
    print(f"  probability at least one of {n} requests fails = "
          f"{p_fail_any:.3f} without retries")
    print(f"  expected attempts per request = {attempts:.4f}, so "
          f"{n * (attempts - 1):.1f} extra requests per fetch")
    print(f"  extra latency from retries = {n * (attempts - 1) * LATENCY_S:.1f} s "
          f"({100 * (attempts - 1):.2f} % more time)")
    base = overhead + transfer
    print(f"  plan total grows from {base:.0f} s to "
          f"{base + n * (attempts - 1) * LATENCY_S:.0f} s")
    print("  -> retries cost a few per cent and remove a "
          f"{100 * p_fail_any:.0f} % chance of an incomplete archive")

    section("4. What a fetch plan must record")
    items = [
        "service and version of the query interface",
        "the request window list (start, end, channels, level)",
        "the retrieved file count and a checksum per file",
        "the retrieval date and the service's own version identifiers",
        "the failure and retry log, including any window that never arrived",
    ]
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item}")
    print("  -> the plan is the provenance of the data set: without it a later")
    print("     reader cannot distinguish 'the archive was this' from 'we got")
    print("     what the service returned that day'")


if __name__ == "__main__":
    main()
