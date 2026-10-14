#!/usr/bin/env python3
"""Notebooks as publications: execution order, hidden state and reproduction.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python notebooks_as_publications_demo.py

Everything here is SYNTHETIC.  Notebooks are simulated as dependency graphs over
cells with chosen probabilities; no notebook was executed or inspected.

Sections
--------
1. Execution order and the dependency inversion.
2. What a clean re-run does: the reproduction failure rate.
3. Length: why long notebooks fail more often.
4. What pinning and testing reduce, and what they do not.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_NOTEBOOKS = 200
CELLS = (10, 20, 40, 80, 160)
P_OUT_OF_ORDER = 0.30       # P(a cell is executed out of source order)
P_INVERSION = 0.03          # P(out-of-order execution creates a hidden dependency)
P_ENV_NUMERICAL = 0.05      # P(a clean re-run differs numerically, unpinned)
P_ENV_PINNED = 0.01         # P(a clean re-run differs numerically, pinned)
P_PARTIAL_OUTPUT = 0.40     # P(a cell has output but no stored execution count)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. Execution order and the dependency inversion")
    print(f"SYNTHETIC notebooks: {N_NOTEBOOKS} with {CELLS[0]}-{CELLS[-1]} cells")
    print(f"  P(cell executed out of source order) = {P_OUT_OF_ORDER:.2f}")
    print(f"  P(that execution creates a hidden dependency) = {P_INVERSION:.2f}")
    print("  a hidden dependency means a cell used a value that only existed because an")
    print("  earlier cell had been re-run later in the session; the notebook then works")
    print("  in the saved session and fails from the top")
    for n_cells in CELLS:
        out_of_order = RNG.random((N_NOTEBOOKS, n_cells)) < P_OUT_OF_ORDER
        inversions = (RNG.random((N_NOTEBOOKS, n_cells)) < P_INVERSION) & out_of_order
        any_inversion = inversions.any(axis=1)
        print(f"  {n_cells:3d} cells: mean out-of-order cells "
              f"{out_of_order.sum(axis=1).mean():5.1f}, "
              f"notebooks with at least one inversion "
              f"{any_inversion.mean() * 100:5.1f} %")
    print("  -> most out-of-order executions are harmless re-runs; the dangerous minority")
    print("     create a hidden dependency.  Even a 1 % per-cell chance compounds: the")
    print("     failure is invisible in the saved file and complete on a fresh kernel.")

    section("2. What a clean re-run does: the reproduction failure rate")
    n_cells = 40
    out_of_order = RNG.random((N_NOTEBOOKS, n_cells)) < P_OUT_OF_ORDER
    inversions = (RNG.random((N_NOTEBOOKS, n_cells)) < P_INVERSION) & out_of_order
    hidden_state = inversions.any(axis=1)
    numerical = RNG.random(N_NOTEBOOKS) < P_ENV_NUMERICAL
    fails = hidden_state | numerical
    print(f"  {N_NOTEBOOKS} notebooks of {n_cells} cells, clean re-run from the top")
    print(f"  fail because of hidden state  = {int(hidden_state.sum())} "
          f"({hidden_state.mean() * 100:.1f} %)")
    print(f"  fail because of environment or numerical differences = "
          f"{int(numerical.sum())} ({numerical.mean() * 100:.1f} %)")
    print(f"  fail for at least one reason  = {int(fails.sum())} "
          f"({fails.mean() * 100:.1f} %)")
    print(f"  reproduce without intervention = {int((~fails).sum())} "
          f"({(~fails).mean() * 100:.1f} %)")
    print("  -> the dominant failure is hidden state, which is a property of how the")
    print("     notebook was used, not of the environment.")

    section("3. Length: why long notebooks fail more often")
    print("  cells   P(no hidden state)   reproducibility   reproducibility   cells with")
    print("                              unpinned          pinned            partial output")
    for n in CELLS:
        oo = RNG.random((N_NOTEBOOKS, n)) < P_OUT_OF_ORDER
        inv = (RNG.random((N_NOTEBOOKS, n)) < P_INVERSION) & oo
        ok = ~inv.any(axis=1)
        partial = (RNG.random((N_NOTEBOOKS, n)) < P_PARTIAL_OUTPUT)
        env = RNG.random(N_NOTEBOOKS)
        print(f"  {n:5d}   {ok.mean() * 100:18.1f} %   "
              f"{np.mean(ok & (env >= P_ENV_NUMERICAL)) * 100:16.1f} %   "
              f"{np.mean(ok & (env >= P_ENV_PINNED)) * 100:16.1f} %   "
              f"{partial.sum(axis=1).mean():17.1f}")
    print("  -> reproduction probability falls steeply with length: a notebook is a")
    print("     chain of cells, and the chain survives only if every link does.")

    section("4. What pinning and testing reduce")
    oo = RNG.random((N_NOTEBOOKS, 40)) < P_OUT_OF_ORDER
    inv = (RNG.random((N_NOTEBOOKS, 40)) < P_INVERSION) & oo
    hidden = inv.any(axis=1)
    for label, p_env in (("unpinned", P_ENV_NUMERICAL), ("pinned", P_ENV_PINNED)):
        env = RNG.random(N_NOTEBOOKS) < p_env
        print(f"  {label:<10s} environment failure {env.mean() * 100:5.1f} %, "
              f"total failure {np.mean(hidden | env) * 100:5.1f} %")
    print(f"  if hidden state is removed by running cells in order and restarting")
    print(f"  before saving (a discipline, not a tool), the failure rate becomes:")
    for label, p_env in (("unpinned", P_ENV_NUMERICAL), ("pinned", P_ENV_PINNED)):
        env = RNG.random(N_NOTEBOOKS) < p_env
        print(f"  {label:<10s} total failure {env.mean() * 100:5.1f} %")
    print("  -> pinning removes the environment term; only the discipline removes the")
    print("     hidden-state term.  Execution-order testing catches both, and is the")
    print("     single practice that makes a notebook a publication.")


if __name__ == "__main__":
    main()
