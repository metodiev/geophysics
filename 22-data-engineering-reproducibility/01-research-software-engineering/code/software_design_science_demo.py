#!/usr/bin/env python3
"""Design metrics for scientific software, measured on a SYNTHETIC module graph.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python software_design_science_demo.py

Everything here is SYNTHETIC.  The module graph is generated below; no real
project, repository or defect database is read.  Printed numbers are model
outputs of this script, not measurements of any published system.

Sections
--------
1. Shape of the dependency graph: size, edges, coupling and layering.
2. Change propagation: direct versus transitive blast radius.
3. Instability and its correlation with blast radius.
4. A defect-density model driven by fan-out.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC graph and model parameters (chosen, not measured) ------------
N_MODULES = 60        # modules in the synthetic package
EDGE_PROB = 0.06      # probability of a dependency between an ordered pair
DEFECT_BASE = 0.5     # defects per KLOC at minimal complexity
DEFECT_SLOPE = 0.30   # extra defects per KLOC per effective decision


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build_dependency_dag(n, p, rng):
    """Acyclic module graph: an edge i -> j means module i imports j."""
    upper = (rng.random((n, n)) < p).astype(np.int8)
    np.fill_diagonal(upper, 0)
    return np.triu(upper, 1)


def reachability(adj):
    """Transitive closure by boolean squaring."""
    reach = adj.copy()
    while True:
        nxt = (((reach @ reach) > 0).astype(np.int8)) | reach
        if np.array_equal(nxt, reach):
            return reach
        reach = nxt


def main():
    section("1. Shape of the dependency graph")
    adj = build_dependency_dag(N_MODULES, EDGE_PROB, RNG)
    out_deg = adj.sum(axis=1)          # fan-out: what a module depends on
    in_deg = adj.sum(axis=0)           # fan-in: what depends on a module
    edges = int(adj.sum())
    print(f"SYNTHETIC module graph: {N_MODULES} modules, {edges} dependency edges, "
          f"p_edge = {EDGE_PROB:.2f} (chosen)")
    print(f"  mean fan-out (dependencies per module)   = {out_deg.mean():.2f}")
    print(f"  mean fan-in (dependents per module)      = {in_deg.mean():.2f}")
    print(f"  max fan-in                               = {int(in_deg.max())}")
    print(f"  modules with fan-out 0 (leaves)          = {int((out_deg == 0).sum())}")

    section("2. Change propagation: direct versus transitive blast radius")
    reach = reachability(adj)
    direct = out_deg.astype(float)
    transitive = reach.sum(axis=1).astype(float)
    # Blast radius: how many modules are affected when THIS module changes.
    blast = reach.sum(axis=0).astype(float)
    print(f"  mean direct dependencies per module      = {direct.mean():.2f}")
    print(f"  mean transitive dependencies per module  = {transitive.mean():.2f}")
    print(f"  amplification (transitive / direct)      = "
          f"{transitive.mean() / direct.mean():.2f}x")
    print(f"  mean blast radius (dependents affected)  = {blast.mean():.2f} modules")
    print(f"  largest blast radius                     = {int(blast.max())} modules")
    print(f"  modules with blast radius > 20           = {int((blast > 20).sum())} "
          f"({100.0 * (blast > 20).mean():.1f} % of the package)")
    print("  -> a change is never local: the median module reaches "
          f"{np.median(blast):.0f} others transitively")

    section("3. Instability and its correlation with blast radius")
    instability = np.where((in_deg + out_deg) > 0,
                           out_deg / np.maximum(in_deg + out_deg, 1), 0.0)
    print(f"  mean instability I = fan-out/(fan-in+fan-out) = {instability.mean():.3f}")
    print(f"  modules with I > 0.80 (unstable)              = "
          f"{int((instability > 0.80).sum())} "
          f"({100.0 * (instability > 0.80).mean():.1f} %)")
    corr = np.corrcoef(in_deg.astype(float), blast)[0, 1]
    print(f"  Pearson correlation(fan-in, blast radius)     = {corr:.3f}")
    print("  -> fan-in predicts blast radius; keep fan-in low on the modules "
          "you expect to change")

    section("4. Defect-density model driven by fan-out")
    decisions = 1.0 + out_deg + in_deg
    density = DEFECT_BASE + DEFECT_SLOPE * decisions
    loc = 120.0 * (1.0 + out_deg)      # bigger modules couple more
    total_defects = float((density * loc / 1000.0).sum())
    print(f"  model: density = {DEFECT_BASE:.2f} + {DEFECT_SLOPE:.2f} x decisions "
          f"per KLOC, decisions = 1 + fan-out + fan-in (chosen)")
    print(f"  mean defects per KLOC                    = {density.mean():.2f} "
          f"+/- {density.std():.2f} (s.d. over modules)")
    print(f"  total synthetic size                     = {loc.sum() / 1000.0:.2f} KLOC")
    print(f"  predicted total defects                  = {total_defects:.1f} "
          f"(model output, not a measurement)")
    hi = density[blast > 20].mean()
    lo = density[blast <= 20].mean()
    print(f"  mean density on high-blast modules       = {hi:.2f} per KLOC")
    print(f"  mean density on low-blast modules        = {lo:.2f} per KLOC")
    print(f"  ratio                                    = {hi / lo:.2f}x")


if __name__ == "__main__":
    main()
