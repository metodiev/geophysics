# Exercises — 22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect

Attempt these before reading the
[solutions](./03-workflow-managers-solutions.md). The lesson is
[03 Workflow Managers](../03-workflow-managers.md). All workflow numbers refer to
the **SYNTHETIC** graph of `code/workflow_managers_demo.py`: 24 tasks, 40
dependencies, durations in $[2,25]$ min, serial cost 383.4 min, critical path
137.4 min.

## ★ Foundational

**★1.** Define each of the following in one sentence, using the rule model of the
lesson: rule, target, input, output, partial execution, invalidation.

**★2.** For the demonstration's graph, the serial cost is 383.4 min and the
critical path is 137.4 min. (a) Compute the maximum available speedup. (b) State
the shortest possible wall time on 100 workers and why it cannot be improved.
(c) Name one structural change to an analysis that would raise the speedup.

**★3.** Read the demonstration's scheduling table. State the makespan, speedup and
efficiency at 2 and at 8 workers, and explain in one sentence why the efficiency
falls while the speedup rises.

## ★★ Applied

**★★4.** A pipeline has rules with these durations and dependencies:
$A$ (10 min) $\to B$ (20 min) $\to C$ (30 min), plus $D$ (15 min) and $E$ (40 min),
both independent of the chain and of each other.

(a) Compute the serial cost, the critical path and $S_{\max}$. (b) Compute the
makespan on 1, 2 and 3 workers with a largest-ready-first schedule, showing the
assignment. (c) Compute the efficiency at 2 and 3 workers and state which count
you would request.

**★★5.** The demonstration measures the fraction of the workflow re-run when an
input changes: 62 % for one changed input of six, 91 % for three. (a) Explain the
mechanism that makes one changed input invalidate 15 of 24 tasks. (b) Propose a
restructuring that would reduce the fraction, and state what it costs.
(c) State the failure mode that would make the measured fraction *smaller* than
the true one on a real system.

**★★6.** A rule reads a configuration file with `open(cfg["path"])` inside a
function, without declaring the file. State (a) what the engine will do when the
configuration changes, (b) the observable symptom of the bug, and (c) the
two-line change that removes it.

## ★★★ Research-oriented

**★★★7.** Design a workflow for an ensemble inversion of 200 realisations, each
needing a forward model (30 min) and a local optimiser (45 min) whose result is
aggregated into one figure. State the rule set, the DAG's critical path, the
maximum speedup, the worker count you would request, and the caching behaviour
when one realisation's input changes. A specification that could not be executed
is a failed answer.

**★★★8.** The demonstration's invalidation rule re-runs a task when any declared
input changes. Compare it with a content-hash-key rule (re-run only if the
*combination* of inputs is new) on the same graph: state the metric, predict the
direction of the difference, and describe the failure each rule can produce that
the other cannot.

**★★★9.** Your group's workflow takes 9 h of serial work with a 7 h critical path
and consumes 400 GB of intermediate files. Propose and justify three changes —
one to the graph, one to the storage, one to the scheduling — and state for each
the measurement you would use to show it worked.
