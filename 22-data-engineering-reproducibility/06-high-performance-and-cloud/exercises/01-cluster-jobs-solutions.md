# Solutions — 22-06-01 Running Jobs on HPC Clusters and Schedulers

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [01 Running Jobs on HPC Clusters and Schedulers](../01-cluster-jobs.md).

---

## ★1 — A request's declarations

**Declared**: nodes (or cores), walltime, memory, and the queue or partition. The first
two determine the **wait** under the product rule (the request's fraction of the
machine), and the first two plus memory determine the **resource use** while the job
runs.

## ★2 — Request fractions and waits

(a) 16 nodes × 8 h: $f = 128/6144 = 0.0208$. 1 node × 24 h:
$f = 24/6144 = 0.0039$.

(b) Waits: $0.5 + 40 \times 0.0208^{0.8} = 0.5 + 40 \times 0.0450 = 2.31$ h;
$0.5 + 40 \times 0.0039^{0.8} = 0.5 + 40 \times 0.0124 = 0.97$ h. Both match the printed
table.

(c) They differ because the *product* sets the wait: 128 node-hours arranged as 16 nodes
for 8 hours is a bigger simultaneous claim than 1 node for 24 hours, and the scheduler
must find a wider gap. Node-hours alone do not determine the queueing.

## ★3 — A small request

$8 \times 5 = 40$ node-hours; over a day the partition offers
$256 \times 24 = 6144$ node-hours, so the job claims $40/6144 = 0.65\ \%$ at most (less,
because it occupies the machine for 5 hours rather than a day).

## ★★4 — Two jobs on a 512-node partition

(a) 64 nodes × 12 h: $f = 768/(512 \times 24) = 768/12\,288 = 0.0625$. 4 nodes × 24 h:
$f = 96/12\,288 = 0.0078$.

(b) The **64-node, 12-hour job waits longer** — its request fraction is eight times
larger, and the scheduler needs a coordinated block of 64 nodes for half a day, which is
rarer than four nodes for a day.

(c) Split it into four 16-node, 12-hour jobs (or twelve 64-node, 1-hour jobs) so that the
scheduler can backfill pieces into smaller gaps; the total work is unchanged, the
request fractions are smaller, and the waiting falls. The cost is a merge step and more
job-management overhead.

## ★★5 — A single-thread request

(a) Node-hours claimed: $1 \times 12 = 12$; core-hours claimed:
$12 \times 32 = 384$; core-hours used: $12 \times 1 = 12$ (if the code uses one core).

(b) Idle fraction $= (384 - 12)/384 = 96.9\ \%$ — 31 of 32 cores idle for the job's
duration.

(c) The correction is to request **cores** (one, plus one for the runtime overhead) rather
than a whole node, if the site's scheduler supports it; the user's cost is potential
memory or interconnect limits per core and the possibility that the job is packed onto a
node shared with others, which changes the timing slightly. Both are usually acceptable
next to a factor of 32 in resource use.

## ★★6 — Busy but flat

(a) The three checks: (i) **request shape** — cores requested against cores used, which
reveals whole-node requests for threaded code; (ii) **walltime accuracy** — runtime
against requested walltime, which reveals claims several times larger than the work;
(iii) **re-runs** — the fraction of node-hours spent on tasks that were re-run after a
bug, which reveals wasted work rather than wasted resources.

(b) Report: nodes requested against cores used, walltime requested against runtime, and
completed tasks per node-hour.

(c) The measurement that separates busy from productive: **completed tasks (or
analyses) per node-hour**, ideally with the count of tasks that had to be re-run. A
partition can be 92 % occupied and produce one completed analysis per thousand
node-hours, and only a work-attached number shows it.

## ★★★7 — A 1 000-realisations inversion

**Per realism**: 40 core-hours, 8 GB. On 32-core nodes, 40 core-hours is 1.25 node-hours;
use a **1-node job with 8 cores for 5 hours** (40 core-hours) — comfortably inside the
24-hour limit and inside the memory budget.

**Decomposition.** An array job (or a workflow's rule per realism) with 1 000 tasks, each
requesting 8 cores, 8 GB and a 6-hour walltime (5 hours plus margin). Submitting in
blocks (say 100 at a time) keeps the queue tractable and lets the group stop early if the
first block reveals a bug.

**Mechanism.** The scheduler's array mechanism if the site supports it (one submission,
1 000 tasks, per-task logs named by index), otherwise a workflow manager that submits and
tracks the tasks
([22-02-03](../../02-reproducible-workflows/03-workflow-managers.md)).

**Checkpointing.** Each task writes its output and a completion marker at the end; the
task is idempotent (re-running overwrites), and the completion marker is what a
resubmission checks. For a 5-hour task, intra-task checkpointing is unnecessary; for a
20-hour task it would be mandatory.

**Completion tracking.** A manifest listing the 1 000 task identifiers and their states,
updated by the task itself (a write at completion), so the group's progress is a query
and a resubmission skips finished tasks.

**Expected consumption.** $1\,000 \times 8 \times 5 = 40\,000$ core-hours, i.e.
1 250 node-hours — about 5 % of a 128-node partition for a day. With queueing, expect the
sweep to take several days of wall time, and plan the deadline accordingly.

**The failure it cannot survive.** A bug that invalidates the *results* after they are
computed (a wrong parameter, a units error): the strategy is resilient to node failures
and limit expiries, but it cannot detect a systematic error — which is why the test job at
small scale (10 realisations with known answers) comes first.

## ★★★8 — Measuring request accuracy

**Data.** The scheduler's accounting records: per job, the resources requested (cores,
walltime, memory), the resources used or charged (core-hours, maximum memory,
runtime), the exit state, and the time to start.

**Statistics.** (i) The distribution of **runtime / requested walltime**, which shows
over-claiming (a mode near 0.2 means requests are five times too large); (ii)
**cores used / cores requested**, which shows whole-node requests for threaded code;
(iii) **tasks completed per node-hour**, the work-attached measure; (iv) the fraction of
jobs that exit with a non-zero state or are killed, which separates waste from accuracy.

**Confounder.** Jobs **killed at the limit** look maximally accurate (runtime = walltime)
while actually indicating an under-estimate; exclude killed jobs from the accuracy
statistics and report them separately, or the distribution shows a spurious mode at 1.0
that flatters the group's requests.

**What it cannot tell you.** Whether the science was worth the node-hours: a perfectly
accurate request can compute something wrong, and a wasteful request can produce a
result of great value. Request accuracy is an efficiency measure, complementary to the
project's scientific assessment.

## ★★★9 — Raising the walltime limit from 24 to 72 hours

**Jobs it enables.** Jobs that genuinely need more than 24 hours: long simulations,
coupled runs, and codes that cannot checkpoint cheaply. Their number can be estimated from
the accounting: the fraction of jobs that hit the 24-hour limit (with a non-zero state)
is the pool the change would serve — and if that fraction is a few per cent of jobs but a
large share of node-hours, the change is justified on those grounds.

**Queue effect on other jobs.** Longer limits make the largest claims possible, which
raises the *maximum* request fraction and lengthens the tail of the wait distribution;
the size of the effect depends on whether the scheduler **backfills** (which it can only
do when it knows the true duration) and on whether the site reserves capacity for
long jobs. The demonstration's model predicts a disproportionate effect: waits are a
function of the product, so a job escalating from 24 to 72 hours at the same node count
triples its request fraction and moves far up the queueing curve.

**Utilization effect.** Longer limits tend to *lower* effective utilization if people
request the new maximum by default, because finished jobs idle their nodes until the
claim expires; they can *raise* it if the enabled long jobs fill otherwise unusable gaps
(a weekend, a maintenance window).

**The measurement that settles it.** From the site's own data: the distribution of
runtime/walltime for existing jobs (over-claiming), the count and node-hours of jobs
killed at the limit (genuine demand), the wait distribution before and after a trial
change, and the utilization. Run it as a **trial on one partition** for a quarter, with
the four series published to users, rather than as a permanent policy change.

**The assumption that makes the prediction uncertain.** The lesson's wait model is a
smooth function of the request fraction, whereas real schedulers use queues, priorities,
reservations and backfilling — policies that can make a limit increase almost free (if
long jobs are confined to a reserved partition) or very expensive (if everyone raises
their requests by default). The structure — longer claims, longer waits — transfers; the
magnitude does not.
