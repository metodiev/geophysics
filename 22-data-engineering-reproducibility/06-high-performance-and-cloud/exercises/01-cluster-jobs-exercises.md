# Exercises — 22-06-01 Running Jobs on HPC Clusters and Schedulers

Attempt these before reading the
[solutions](./01-cluster-jobs-solutions.md). The lesson is
[01 Running Jobs on HPC Clusters and Schedulers](../01-cluster-jobs.md). Numbers refer
to the **SYNTHETIC** model of `code/cluster_jobs_demo.py`: 256 nodes × 32 cores, 4 000
jobs at 400/day, median walltime 3 h, wait $\approx 0.5 + 40\,f^{0.8}$ with
$f = \text{nodes} \times \text{hours}/(256 \times 24)$.

## ★ Foundational

**★1.** State the four quantities a job request declares, and the two that determine the
wait under the product rule.

**★2.** For the demonstration's partition: (a) compute the request fraction of a 16-node,
8-hour job and of a 1-node, 24-hour job; (b) state the modelled wait for each; (c) explain
in one sentence why the two differ despite similar node-hours.

**★3.** Compute the kernel-hours of a job requesting 8 nodes for 5 hours, and the fraction
of the partition it claims over a day.

## ★★ Applied

**★★4.** A 512-node partition receives jobs with a median request of 4 nodes for 6 hours.

(a) Compute the request fraction of a 64-node, 12-hour job and of a 4-node, 24-hour job
using $f = \text{nodes} \times \text{hours}/(512 \times 24)$. (b) State which waits longer
under the product rule and why. (c) State the change to the first job that would reduce
its wait without changing its total work.

**★★5.** A job uses one thread but requests a whole 32-core node for 12 hours.

(a) Compute the node-hours and core-hours the request claims and the core-hours actually
used. (b) Compute the fraction of the claimed resource that is idle. (c) State the
correction and what it costs the user.

**★★6.** A group reports 92 % node utilization with flat scientific output.

(a) State the three checks of the lesson's diagnosis and what each would reveal.
(b) State the three numbers to report. (c) State the one measurement that distinguishes
"busy" from "productive".

## ★★★ Research-oriented

**★★★7.** Design a job strategy for an inversion experiment of 1 000 realisations, each
needing 40 core-hours and 8 GB of memory, on a partition with a 24-hour walltime limit
and 128 nodes of 32 cores. State the job decomposition, the request per job, the array or
workflow mechanism, the checkpointing, the completion tracking, and the expected
allocation consumption. State the one failure your strategy cannot survive.

**★★★8.** Design a measurement of a real allocation's *request accuracy*: state the data
from the scheduler's accounting, the statistics (runtime/walltime distribution,
cores used/cores requested, tasks completed per node-hour), and the confounder (jobs that
are killed at the limit look maximally accurate). State what the measurement cannot tell
you about the science produced.

**★★★9.** A site proposes raising the walltime limit from 24 to 72 hours. Analyse the
proposal: state the jobs it enables, the queue effect on other jobs, the utilization
effect, and the measurement that would settle the question with the site's own data.
State the assumption in the lesson's model that makes your prediction uncertain.
