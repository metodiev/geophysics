# Exercises — 22-07-02 Continuous Integration for Research Software

Attempt these before reading the
[solutions](./02-continuous-integration-solutions.md). The lesson is
[02 Continuous Integration for Research Software](../02-continuous-integration.md).
Numbers refer to the **SYNTHETIC** model of `code/continuous_integration_demo.py`.

## ★ Foundational

**★1.** Write the expression for the probability that a suite of $N$ independent tests is
red, given a per-test flake rate $p$, and state the two assumptions it makes.

**★2.** A matrix has 2 systems × 5 interpreter versions × 3 dependency sets. Each job takes
1 min of setup, 1.5 min of install and 5 min of tests.

(a) Compute the number of jobs, the per-job duration and the machine-minutes.
(b) Compute the wall time with 4, 10 and 30 runners, and state the floor.
(c) State the change that shortens the wall time when the runner count is already large.

**★3.** State three things a developer's laptop cannot check that a CI service can, and one
thing neither can check.

## ★★ Applied

**★★4.** A suite has 300 tests; one test has a per-run flake rate of 0.004 and the others
never flake.

(a) Compute the probability that a push is red. (b) Compute the posterior probability that
the push is broken, given a prior of 0.15, and interpret it. (c) Compute the expected number
of red builds per year at 15 pushes a day for 220 working days.

**★★5.** A group retries each failed test up to three attempts and does not record retries.

(a) Compute the probability that a push is red for $N = 300$, $p = 0.004$ with 3 attempts.
(b) A real, intermittent bug fails one test in 8 runs. Compute the probability that a push
containing it looks green. (c) State the policy that keeps the noise reduction without the
masking, and the measurement that distinguishes the two cases.

**★★6.** A suite of ten files takes 3 000 s in total, with file durations of 600, 500, 450,
400, 350, 300, 200, 100, 60 and 40 s, in that order in the repository listing.

(a) Compute the shard times and the wall time for 5 shards split contiguously (two files
each, in listing order). (b) Compute the shard times and the wall time for 5 shards assigned
longest-file-first to the least loaded shard. (c) State the floor for any 5-shard split, and
what you would do about it.

## ★★★ Research-oriented

**★★★7.** Design the CI pipeline for a research code that ships a Python library, a
Fortran kernel built with a compiler wrapper, a Snakemake workflow and a paper repository.

State the jobs, their triggers (push, nightly, tag), their durations and the checks each
performs; the fast-lane selection; the artifact and cache policy; the golden-value strategy;
the policy for network-dependent tests; and the two failure modes you expect to dominate and
how you would measure them.

**★★★8.** A group's CI is green but their published results were produced by a pipeline
that no longer builds.

Design the investigation: state the evidence you would collect (build logs, lock files, tag
history, environment snapshots, data versions), the four candidate causes and the check that
distinguishes each, and the pipeline change that would have prevented it. State what you
would publish if the original environment cannot be rebuilt.

**★★★9.** A PI proposes to remove the multi-system matrix and run only one system, arguing
the science group all use one machine, and to drop retries because "flaky tests should just
be fixed".

Analyse both proposals: state the defect class the matrix protects against, the cost of
keeping it as a nightly job, the evidence for whether flakiness is a test problem or a
scheduling problem, and the combined policy you would recommend. State the measurement that
decides the argument, and the one proposal you would accept.
