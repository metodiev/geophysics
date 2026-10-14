#!/usr/bin/env python3
"""Reproducible research practice: digests, determinism and parameter dependence.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_research_practice_demo.py

Everything here is SYNTHETIC.  The pipeline is a small arithmetic surrogate; no
files are written, nothing is downloaded and no external data are read.

Sections
--------
1. A results table and its content digest.
2. Determinism: same inputs, same digest, run twice.
3. Parameter dependence: what one changed number does to the table.
4. Unpinned environments and what they cost the reported digits.
"""

import hashlib

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC pipeline (chosen teaching values) ----------------------------
N_RESULTS = 6
BASE_PARAMS = np.array([0.30, 0.45, 0.20, 0.35, 0.10, 0.60])
PARAM_NAMES = ("high-cut corner", "taper length", "window length",
               "velocity step", "damping factor", "elevation correction")
ENV_PERTURBATION = 1e-4      # relative size of one environment-induced shift
SIGNIFICANT_DIGITS = 4
# Fixed sensitivity matrix: every parameter influences every result.  The
# entries are drawn once from a seeded generator so the demo is reproducible.
_WEIGHTS = np.random.default_rng(99).normal(1.0, 0.35, (len(BASE_PARAMS), N_RESULTS))


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def digest(array):
    return hashlib.sha256(np.ascontiguousarray(array, dtype=np.float64).tobytes()).hexdigest()


def sig_round(x, digits):
    """Round to a number of significant digits (not decimal places)."""
    x = np.asarray(x, dtype=float)
    scale = 10.0 ** (digits - 1 - np.floor(np.log10(np.abs(x))))
    return np.round(x * scale) / scale


def pipeline(params, seed, n_results=N_RESULTS, env_shift=0.0, env_count=0):
    """Deterministic synthetic result vector."""
    rng = np.random.default_rng(seed)
    weights = _WEIGHTS[:, :n_results]
    value = 100.0 * (1.0 + weights.T @ params) / weights.shape[0] * len(BASE_PARAMS)
    noise = rng.normal(0.0, 0.5, n_results)   # measurement noise on the result
    if env_count:
        value = value * (1.0 + env_shift * rng.normal(0.0, 1.0, n_results)
                         * np.sqrt(env_count))
    return value + noise


def main():
    section("1. A results table and its content digest")
    results = pipeline(BASE_PARAMS, 20261014)
    rt = tuple(sig_round(results, SIGNIFICANT_DIGITS))
    d = digest(np.asarray(rt))
    print(f"SYNTHETIC pipeline: {N_RESULTS} reported quantities, "
          f"{SIGNIFICANT_DIGITS} significant digits")
    for name, value in zip(PARAM_NAMES, BASE_PARAMS):
        print(f"  parameter {name:<22s} = {value:.2f}")
    for k, value in enumerate(rt):
        print(f"  result {k + 1}: {value:12.4f}")
    print(f"  SHA-256 of the rounded result vector = {d[:16]}... "
          f"({len(d)} hex characters)")
    print("  -> the digest is a 256-bit summary of the published numbers; two")
    print("     digests either match or they do not.")

    section("2. Determinism: same inputs, same digest, run twice")
    d2 = digest(np.asarray(tuple(sig_round(pipeline(BASE_PARAMS, 20261014),
                                              SIGNIFICANT_DIGITS))))
    d3 = digest(np.asarray(tuple(sig_round(pipeline(BASE_PARAMS, 20261014),
                                              SIGNIFICANT_DIGITS))))
    print(f"  run A digest = {d2[:16]}...")
    print(f"  run B digest = {d3[:16]}...")
    print(f"  identical: {d2 == d3}")
    d4 = digest(np.asarray(tuple(sig_round(pipeline(BASE_PARAMS, 20261015),
                                              SIGNIFICANT_DIGITS))))
    print(f"  same parameters, different RNG seed -> digest {d4[:16]}... "
          f"identical to run A: {d4 == d2}")
    print("  -> determinism is a property of (code, parameters, seed, environment).")
    print("     Change any one and the digest changes; that is the point.")

    section("3. Parameter dependence: what one changed number does to the table")
    for i, name in enumerate(PARAM_NAMES):
        perturbed = BASE_PARAMS.copy()
        perturbed[i] *= 1.01                     # a 1 % change
        new = sig_round(pipeline(perturbed, 20261014), SIGNIFICANT_DIGITS)
        changed = int(np.sum(new != rt))
        rel = np.max(np.abs(new - np.asarray(rt)) / np.abs(rt)) * 100.0
        print(f"  {name:<22s} +1 % -> {changed} of {N_RESULTS} results change digits, "
              f"largest relative change {rel:.4f} %")
    print("  -> every parameter influences every result, so 'the same to four")
    print("     significant digits' is a testable reproducibility claim rather than a")
    print("     phrase: a 1 % change in any one parameter breaks it.")

    section("4. Unpinned environments and what they cost the reported digits")
    print(f"  one environment-induced difference has relative size "
          f"{ENV_PERTURBATION:.0e}; several accumulate as the square root of their number")
    print(f"  accumulated differences: results still identical at "
          f"{SIGNIFICANT_DIGITS} digits, of {N_RESULTS}")
    for k in (0, 1, 4, 9, 16, 25, 36, 49, 100):
        perturbed = sig_round(pipeline(BASE_PARAMS, 20261014, env_shift=ENV_PERTURBATION,
                                      env_count=k), SIGNIFICANT_DIGITS)
        same = int(np.sum(perturbed == rt))
        print(f"  {k:3d}: {same} of {N_RESULTS}")
    print(f"  even one environment difference of relative size {ENV_PERTURBATION:.0e}")
    print("  changes the fourth significant digit of some results.  More differences do")
    print("  not monotonically change more of them: whether a digit flips depends on")
    print("  where the value sits relative to a rounding boundary, not on the size of")
    print("  the perturbation alone.")
    print("  -> pin the environment or report to fewer digits: those are the two")
    print("     honest options, and both should be stated in the Methods.")


if __name__ == "__main__":
    main()
