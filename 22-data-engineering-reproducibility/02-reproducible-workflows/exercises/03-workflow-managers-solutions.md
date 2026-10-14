# Solutions — 22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [03 Workflow Managers](../03-workflow-managers.md).

---

## ★1 — The rule model in one sentence each

- **Rule**: a named transformation with declared inputs, declared outputs and a
  command, plus optional resources.
- **Target**: an output the user asks for; the engine resolves it backwards to the
  rules that produce it.
- **Input / output**: the files (or objects) a rule consumes and produces; they are
  what the engine compares to decide staleness.
- **Partial execution**: running only the rules on the paths between a changed
  input and the requested target.
- **Invalidation**: deciding that an output is stale because an input changed, the
  rule changed, or the output is missing.

## ★2 — Ceiling of the demonstration's graph

(a) $S_{\max} = 383.4/137.4 = 2.790$.

(b) The shortest possible wall time is **137.4 min**, the critical path, on any
number of workers: the tasks on that chain depend on one another, so they cannot
overlap. The demonstration confirms it — the 8-worker makespan is exactly
137.4 min.

(c) Structural changes that raise the ceiling: break a long sequential chain into
independent branches that run concurrently and merge at the end (for example, run
the regional subsets as separate rules instead of looping inside one rule), or
shorten the longest task on the critical path. Adding workers does not change
$S_{\max}$.

## ★3 — Reading the scheduling table

| Workers | Makespan (min) | Speedup | Efficiency |
|---|---|---|---|
| 2 | 203.8 | 1.88 | 0.94 |
| 8 | 137.4 | 2.79 | 0.35 |

Efficiency falls as workers rise because the critical path bounds the makespan: at
8 workers the run finishes in exactly 137.4 min regardless of the extra capacity,
so five or six of the eight workers are idle for much of the run. Speedup rises
towards the ceiling $S_{\max} = 2.79$ and then stops.

## ★★4 — A hand-scheduled pipeline

$A \to B \to C$ with durations 10, 20, 30 min; $D$ 15 min; $E$ 40 min,
independent.

(a) Serial cost $= 10 + 20 + 30 + 15 + 40 = 115$ min. Critical path: the chain
$A \to B \to C = 60$ min, against $E = 40$ and $D = 15$; so $C_{\text{crit}} =
60$ min and $S_{\max} = 115/60 = 1.92$.

(b) Largest-ready-first schedule:

- **1 worker**: everything serial: $115$ min.
- **2 workers**: at $t=0$ the ready set is $\{A, D, E\}$; largest first is $E$ (40)
  → worker 1; next $D$ (15) → worker 2. Worker 2 then takes $A$ (10) at $t=15$
  (free because 15 > 0), finishing at 25; $B$ needs $A$ finished (25) and a worker
  (worker 2 free at 25) → $B$ runs 25→45; $C$ needs $B$ (45) and a worker (worker 1
  free at 40, worker 2 at 45) → starts at 45 on worker 1, running to 75. Makespan
  $= \mathbf{75}$ min.
- **3 workers**: $E$ (40) → w1 at 0; $D$ (15) → w2 at 0; $A$ (10) → w3 at 0,
  finishing at 10; $B$ (20) needs $A$ (10) and a worker (w3 free at 10) → 10→30;
  $C$ (30) needs $B$ (30), w3 free at 30 → 30→60. Makespan $= \mathbf{60}$ min,
  equal to the critical path.

(c) Efficiency $= S_{\text{serial}}/(W \times \text{makespan})$:

- 2 workers: $115/(2 \times 75) = 0.767$;
- 3 workers: $115/(3 \times 60) = 0.639$.

Request **2 workers**: three workers buy 15 min of wall time (75 → 60) at the cost
of 25 % more allocation, and the run is not wall-time constrained here. If the wall
time mattered, three workers is the smallest count reaching the ceiling of 60 min.

## ★★5 — Why one changed input re-runs 15 of 24 tasks

(a) The mechanism is **input fan-out plus downstream propagation**. Each task reads
one to three of the six inputs, so a change to one input directly invalidates
several tasks; each of those then invalidates all its descendants. In the generated
graph 40 dependency edges spread over 24 tasks produce an average of 2.8
descendants (measured in
[22-02-04](../04-notebooks-vs-pipelines.md) §3 for a
similar graph), and the tasks that read an input are early in the graph, so their
cones cover most of it.

(b) **Restructure by input partition.** Split the workflow so that each branch
reads one input end to end and produces one output, with a thin aggregation rule on
top. Then a change invalidates one branch instead of most of the graph; the price
is duplicated work across branches (the shared early steps are computed once per
branch) and more rules to maintain.

(c) The failure mode is an **undeclared input**: if a rule reads a file it does not
declare, the engine will not invalidate it, so the measured re-run fraction is
*smaller* than the true one and the workflow silently serves a stale output. This is
the single most dangerous workflow failure, because it produces a plausible result
rather than an error.

## ★★6 — An undeclared configuration file

(a) The engine sees no dependency between the rule and `cfg["path"]`; when the
configuration changes, the rule's declared inputs are unchanged, so the output is
considered up to date and **the rule is not re-run**.

(b) The observable symptom is a figure that does not change when a parameter is
edited — sometimes mistaken for "the result is insensitive to that parameter".
Nothing in the log indicates a skipped rule unless the engine reports its
invalidation decisions.

(c) Declare the file as an input and read it in one place:

```python
rule invert:
    input:
        data="data/catalogue.csv",
        cfg="config/inversion.yml"      # declared: now part of the cache key
    output:
        "results/model.npz"
```

Reading the configuration in the rule header (or a params block sourced from a
declared input) makes it part of the invalidation decision.

## ★★★7 — Ensemble inversion workflow

**Rule set.**

| Rule | Inputs | Output | Cost |
|---|---|---|---|
| `prepare` | catalogue, config | `data/realisation_{i}.npz` $\times 200$ | 5 min each |
| `forward` | `realisation_{i}.npz` | `fwd/realisation_{i}.npz` | 30 min each |
| `invert` | `fwd/realisation_{i}.npz` | `inv/realisation_{i}.npz` | 45 min each |
| `aggregate` | all `inv/*.npz` | `figures/ensemble.png` | 10 min |

Each of the 200 realisations is its own rule invocation (Snakemake-style wildcards),
so the DAG is 200 independent `prepare → forward → invert` chains joining at
`aggregate`.

**Critical path.** One realisation's chain is $5 + 30 + 45 = 80$ min, plus the
10-minute aggregation: $C_{\text{crit}} = 90$ min.

**Maximum speedup.** Serial cost $= 200 \times 80 + 10 = 16\,010$ min
(266.8 h). $S_{\max} = 16\,010/90 = 177.9$ — this is an embarrassingly parallel
workflow, and its ceiling is set by the per-realisations chain, not by the number
of realisations.

**Worker count.** With $W$ workers, a list schedule has each worker run whole
chains; if $W \ge 200$ all chains start together and the makespan is the chain
time plus aggregation, 90 min. Below 200, the makespan is roughly
$\lceil 200/W \rceil \times 80 + 10$ for large $W$ (with packing inefficiency), so
$W = 200$ is the smallest count reaching the 90-minute floor. Request
**$W = 50$** if a wall time of about 5.3 h is acceptable: $4 \times 80 + 10 = 330$
min, with each worker fully busy. The request should be phrased as a wall-time
constraint (e.g. "finish within 6 h"), which 50 workers satisfy.

**Caching on a per-realisations change.** If one realisation's input changes, only
that realisation's `prepare`, `forward` and `invert` re-run (3 rules, 80 min of
work), plus the `aggregate` rule because its input set changed. Everything else is
untouched — provided the aggregate rule declares all 200 inputs, which is exactly
the declaration discipline of §7 of the lesson.

## ★★★8 — Change detection versus hash-key caching

**Metric.** The **re-run ratio**: the number of tasks executed divided by the
number of tasks in the workflow, averaged over a set of realistic edits (parameter
tweaks, data corrections, code edits). Report it alongside the *false-skip rate* —
the number of tasks whose output should have changed but was not re-run — because
a caching scheme that skips too much is fast and wrong.

**Predicted direction.** Hash-key caching never re-runs *more* than
change-detection caching on the same graph: a task whose declared input files
changed but whose content hash is unchanged (a rewritten file with identical
content — a re-export, a re-serialised CSV, a touched timestamp) is re-run by
change detection and skipped by hashing. So the re-run ratio for hash keys is
**lower or equal**, and the difference is the fraction of edits that are
content-preserving. In dirty-workflow benchmarks this fraction is often substantial
because of re-exported intermediates.

**Failures.** Change detection can re-run needlessly (expensive, safe). Hash-key
caching can **skip a task whose inputs are content-identical but whose *behaviour*
depends on something not in the key** — the environment, a global parameter, a
clock, or an undeclared file. The failure is a stale output, so the hash key must
include everything behaviour-depends on (environment hash, parameter values, code
revision), which is exactly what a content-addressed workflow does when it hashes
the command and the environment as well as the data.

## ★★★9 — Three changes to a slow, storage-heavy workflow

Setup: 9 h serial, 7 h critical path, 400 GB of intermediates.

1. **Graph change — break the critical path.** 9 h serial with a 7 h critical path
   gives $S_{\max} = 1.29$: parallelism cannot help. Identify the longest chain and
   find a stage inside it that can be split into independent parts (by region, by
   frequency band, by realisation), then merge them with an aggregation rule.
   *Measurement*: report $C_{\text{serial}}$, $C_{\text{crit}}$ and $S_{\max}$ before
   and after; the change worked if $S_{\max}$ rose, even if the serial cost grew
   slightly through duplicated work.

2. **Storage change — chunk and deduplicate the intermediates.** 400 GB of
   intermediates is usually mostly unchanged between runs. Store intermediates in a
   chunked, content-addressed form and delete the whole-file copies; the
   demonstration of
   [22-02-05](../05-data-versioning.md) measures a 6.2×
   storage reduction for a 50-version time series by chunk-level deduplication.
   *Measurement*: total bytes stored per full run, before and after, with the number
   of unique chunks; the change worked if the bytes fall by the predicted factor and
   the run's results are bitwise identical.

3. **Scheduling change — request resources per rule.** Instead of asking for one
   large job, declare threads and memory per rule and let the scheduler pack them,
   keeping the worker count at the $S_{\max}$ point rather than the cluster maximum.
   *Measurement*: wall time, core-hours consumed and efficiency per run.
   The change worked if wall time is maintained or improved *and* core-hours per
   run fall; reporting wall time alone is how a queue fills with idle allocations.
