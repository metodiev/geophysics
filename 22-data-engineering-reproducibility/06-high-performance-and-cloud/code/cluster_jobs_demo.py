#!/usr/bin/env python3
"""HPC clusters and schedulers: queueing, limits and backfill, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cluster_jobs_demo.py

Everything here is SYNTHETIC.  The job mix, node count, walltime limits and the
scheduler's rules are chosen teaching values; no cluster was used and no
scheduler's policy is described.

Sections
--------
1. A job mix and the resources it requests.
2. Queueing: wait time against walltime limit and node count.
3. Utilization: how much of the machine a typical mix actually uses.
4. The two mistakes that waste an allocation.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC cluster model (chosen, not measured) -------------------------
N_NODES = 256               # nodes in the partition
CORES_PER_NODE = 32
JOB_ARRIVALS_PER_DAY = 400
N_JOBS = 4000
MEDIAN_WALL_HOURS = 3.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A job mix and the resources it requests")
    nodes_req = np.clip(RNG.lognormal(np.log(2.0), 0.9, N_JOBS).round(), 1,
                        N_NODES).astype(int)
    hours_req = np.clip(RNG.lognormal(np.log(MEDIAN_WALL_HOURS), 1.0, N_JOBS),
                        0.1, 48.0)
    core_hours = float((nodes_req * CORES_PER_NODE * hours_req).sum())
    print(f"SYNTHETIC cluster: {N_NODES} nodes x {CORES_PER_NODE} cores, "
          f"{N_JOBS} jobs (chosen)")
    print(f"  arrivals = {JOB_ARRIVALS_PER_DAY}/day, median walltime requested "
          f"{MEDIAN_WALL_HOURS:.1f} h")
    print(f"  median nodes requested = {np.median(nodes_req):.0f}, "
          f"mean = {nodes_req.mean():.1f}, max = {nodes_req.max()}")
    print(f"  total core-hours requested by the mix = {core_hours:,.0f}")
    print("  -> the mix is dominated by small jobs with a long tail; the tail's")
    print("     requests set the queue's behaviour, not the median job")

    section("2. Queueing: the product of nodes and hours")
    print("  job shape          | nodes x hours | request fraction | wait (h)")
    shapes = [("1 node, 1 h", 1, 1.0), ("1 node, 24 h", 1, 24.0),
              ("64 nodes, 1 h", 64, 1.0), ("16 nodes, 8 h", 16, 8.0),
              ("64 nodes, 12 h", 64, 12.0)]
    for name, nodes, hours in shapes:
        frac = nodes * hours / (N_NODES * 24.0)
        wait = 0.5 + 40.0 * frac ** 0.8
        print(f"  {name:<18} | {nodes * hours:>13.0f} | {frac:>16.3f} | "
              f"{wait:>8.2f}")
    print("  -> queueing delay rises with the *product* of nodes and hours: a long")
    print("     single-node job and a short wide job queue very differently even")
    print("     when they request the same node-hours")

    print("  and a walltime limit changes which jobs exist at all:")
    print("  limit (h) | jobs above the limit | their node-hours")
    for limit in (1, 4, 12, 24, 48):
        above = hours_req > limit
        print(f"  {limit:>9d} | {int(above.sum()):>20d} | "
              f"{float((nodes_req[above] * hours_req[above]).sum()):>15.0f}")

    section("3. Utilization of the machine")
    busy_node_hours = float((nodes_req * hours_req).sum())
    capacity_node_hours = N_NODES * 24.0 * (N_JOBS / JOB_ARRIVALS_PER_DAY)
    util = busy_node_hours / capacity_node_hours
    print(f"  node-hours requested = {busy_node_hours:,.0f}")
    print(f"  node-hours available over the same span = "
          f"{capacity_node_hours:,.0f}")
    print(f"  requested utilization = {100 * util:.1f} %")
    idle = 1.0 - util
    print(f"  the machine is asked for {100 * util:.1f} % of its time, so "
          f"{100 * idle:.1f} % is available")
    print("  -> a cluster that looks busy may be running small jobs across many")
    print("     nodes; utilization is a property of the mix, not of the users")

    section("4. The two mistakes that waste an allocation")
    print("  mistake                        | effect")
    rows = [
        ("requesting 48 h for a 3 h job", "the job holds nodes idle at the limit; "
                                          "backfill cannot schedule around it"),
        ("requesting whole nodes for a single-threaded job",
         "31 of 32 cores idle for the job's duration"),
        ("no output until the job ends", "a failure at hour 20 loses 20 hours"),
        ("one giant job instead of many small ones",
         "no resumability, and a longer queue wait"),
    ]
    for a, b in rows:
        print(f"  {a:<30} | {b}")
    print("  -> every item is a request-shape decision, and each is measurable in")
    print("     node-hours wasted before anyone changes the code")


if __name__ == "__main__":
    main()
