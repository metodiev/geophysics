# Exercises — 22-03-03 Designing Robust Data Pipelines for Earth Data

Attempt these before reading the
[solutions](./03-data-pipelines-solutions.md). The lesson is
[03 Designing Robust Data Pipelines](../03-data-pipelines.md). Numbers refer to the
**SYNTHETIC** model of `code/data_pipelines_demo.py`: 8 stages, 0.02 per-attempt
failure probability, 3 retries, 100 000 simulated runs, 0.99 delivery probability.

## ★ Foundational

**★1.** Write the formula for end-to-end success of $N$ independent stages with
per-attempt failure probability $p$ and $R$ retries, and state in words what
"independent" assumes.

**★2.** For $N = 8$, $p = 0.02$, $R = 3$: (a) compute the end-to-end success without
retries; (b) compute the stage success with retries and the end-to-end success;
(c) explain in one sentence why the retried value is not exactly 1.

**★3.** State which of these stages are idempotent and why: a file download that
overwrites its target, a counter increment, a table append, a file overwrite, a
message emission.

## ★★ Applied

**★★4.** For $p = 0.02$ and $R = 3$: (a) compute the expected attempts per stage;
(b) compute the expected attempts per run for 8 stages; (c) express the waste as a
percentage and state the general rule the number illustrates.

**★★5.** A pipeline appends a row per station-day to a table and is retried on
failure.

(a) Compute the expected number of duplicate rows per 10 000 station-days if the
per-attempt delivery is 99 % and every failure is retried once with a 50 % chance of
the duplicate being delivered. (b) State the schema change that would make the
append safe. (c) State what a reader of the table would see if the change were not
made.

**★★6.** A pipeline's nightly ingest is short of the source by a few rows about once
a week, with no errors in the log.

(a) Name the failure from §6, and state why retries do not fix it. (b) Design the
validation gate that catches it, including the numbers it compares. (c) State how the
gate's firing rate relates to the modelled 7.71 % of runs with at least one silent
loss.

## ★★★ Research-oriented

**★★★7.** A pipeline ingests 200 stations from three different services, one of which
is frequently unavailable. Design the reliability architecture: state the stage
decomposition, where idempotence or deduplication is required, the retry and backoff
policy, the validation gates, and the failure semantics you promise the users of the
resulting archive. State the one failure your design cannot prevent.

**★★★8.** The model assumes independent stage failures and a constant failure
probability. Propose a measurement of real dependence in a pipeline's failures —
state the data, the statistic, and the pattern that would show that a single service
outage, not independent flakiness, dominates. State how the retry policy should change
if dependence is confirmed.

**★★★9.** Design a rehearsal test for a pipeline's failure handling: state what is
injected, at which stages, the observable that means the handling worked, and the
false conclusion the test could give if the injection point is not realistic. State
what the rehearsal cannot establish about the pipeline in production.
