# Module 22-02 — Reproducible Research Workflows

**Stages:** intermediate → research · **Prerequisites:** module 22-01 (or equivalent
familiarity with Git and code review), and comfort with a Python analysis loop.

This module is about the machinery that makes a computational result repeatable and
auditable: the environment it ran in, the order in which its steps ran, the identity
of the data it consumed, and the statistics that decide whether the result means what
it appears to mean. Where module 22-01 addressed the code as an artefact, this module
addresses the **run** as an event: something that happened once, in a particular
environment, over a particular version of the data, and which must be capable of
happening again.

The organising idea is the **failure taxonomy**. Every lesson begins from a way a
result fails to reproduce — ambiguous data, unpinned environment, manual steps,
unrecorded randomness, unordered session — and then measures the remedy. The module
is deliberately quantitative about remedies, because the honest answer to "should we
use a container / a workflow manager / a data version store?" is a number: an
unpinned install admits $10^{30.9}$ combinations; a 14-cell notebook has
$913\,584$ valid execution orders of which the saved outputs record exactly one; a
container built without digests agrees bitwise with its sibling build 60.6 % of the
time; 50 versions of a 320 kB grid cost 2.57 MB when chunk-deduplicated against
16.00 MB naive.

The third thread is the limits of engineering. The last part of lesson 01 is
statistical: a significant result replicates with probability equal to the study's
power, a significance filter inflates the reported effect by 39 % at low power, and
20 uncorrected tests give a mean false discovery proportion of 0.899 when the effects
are null. No container fixes any of that, and a module that stopped at environments
would leave the most common cause of irreproducible results untouched.

All measurements in this module are **SYNTHETIC** or **exact for a generated model**:
the studies, dependency sets, workflows, cell graphs, version series and images are
produced by the demonstrations with chosen parameters, and the statistics of the
statistical lesson are Monte Carlo properties of a stated z-test model. No repository
was parsed, no registry or catalogue was queried, and no published replication rate,
benchmark or effect size is quoted.

## Learning objectives

By the end of this module you will be able to:

1. Classify a reproducibility failure into its category and choose the remedy that
   actually removes it, stating what the remedy leaves behind.
2. Reason about statistical reproducibility: compute power, predict conditional
   replication, quantify the winner's curse, and compute a false discovery
   proportion.
3. Pin an environment to the level the failure requires, and compute the size of the
   space an unpinned install leaves open.
4. Express an analysis as a rule graph, compute its critical path and cache behaviour,
   and report both wall time and core-hours.
5. Choose between a notebook and a pipeline for a stated task, and produce a
   published artefact from an exploratory session without losing the exploration.
6. Version data and record provenance such that a figure can name exactly the bytes
   and steps that produced it.
7. Decide whether a container is warranted, pin it so that two builds agree, and say
   what it does not freeze.
8. Recognise the failure modes that survive every tool in this module and report the
   uncertainty they leave.

## Prerequisites

- [22-01-03 Code Review and Collaborative Development](../01-research-software-engineering/03-code-review.md) —
  the practice that catches undeclared inputs before they become stale outputs.
- [22-01-04 Documentation, Docstrings and READMEs That Work](../01-research-software-engineering/04-documentation.md) —
  where environment, seed and data facts are recorded.
- [21-01-01 Descriptive Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  the vocabulary of the statistical part of lesson 01.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [The Reproducibility Problem in the Computational Sciences](01-reproducibility-crisis.md) | intermediate | A significant result replicates with probability equal to the power (0.374 at 37.6 % power); a significance filter inflates the effect by 39 % |
| 02 | [Pinning Environments and Managing Dependencies](02-environment-pinning.md) | advanced | An unpinned install admits $10^{30.9}$ combinations; hash-based locks detect a silent re-upload in proportion to their coverage (0.500 at 30 of 60) |
| 03 | [Workflow Managers: Snakemake, Make, Dask, Prefect](03-workflow-managers.md) | research | A 383.4-minute workflow with a 137.4-minute critical path caps at 2.79×; one changed input re-runs 62 % of the graph |
| 04 | [Notebooks vs Pipelines: Choosing the Right Tool](04-notebooks-vs-pipelines.md) | advanced | 913 584 of 87 178 291 200 cell orders are valid; editing one cell leaves 2.8 cells (worst 7) silently stale |
| 05 | [Data Versioning and Provenance Tracking](05-data-versioning.md) | research | 50 versions cost 2.57 MB deduplicated against 16.00 MB naive; reprocessings, not versions, drive storage |
| 06 | [Containers for Computational Reproducibility](06-containers-reproducibility.md) | research | Code is 0.7 % of a 1.78 GB image; unpinned builds agree bitwise 0.606 of the time, and $10^{-7}$ arithmetic differences survive pinning |

## Suggested path

**If you have just lost a result:** read 01 §2 (the taxonomy) and follow the pointer
for the category your failure belongs to — 02 for environments, 03 for manual steps,
05 for data, 04 for sessions. Then read 01 §4, because the remaining category is the
one no tool fixes.

**If you are preparing a paper's artefact:** read 02, 03 and 06 in that order, then
05 §7 as the checklist. That sequence is exactly the set of decisions an artefact
needs to be runnable by a stranger.

**If you run a group's infrastructure:** read 02 §7, 03 §7, 05 §7 and 06 §7 — the
four practice sections — and write down the four conventions you will enforce. Each
is justified by arithmetic in the preceding sections.

**If you are here for the statistics:** read 01 in full, then 04 §3–4 for the
execution-order counts, and use the ★★★ exercises, which ask for designs rather than
calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-reproducibility-crisis.md`](01-reproducibility-crisis.md) | Lesson 01 |
| [`02-environment-pinning.md`](02-environment-pinning.md) | Lesson 02 |
| [`03-workflow-managers.md`](03-workflow-managers.md) | Lesson 03 |
| [`04-notebooks-vs-pipelines.md`](04-notebooks-vs-pipelines.md) | Lesson 04 |
| [`05-data-versioning.md`](05-data-versioning.md) | Lesson 05 |
| [`06-containers-reproducibility.md`](06-containers-reproducibility.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/reproducibility_crisis_demo.py`](code/reproducibility_crisis_demo.py) | Power, sample size for 80 % power, conditional replication, winner's curse, false discovery proportion |
| [`code/environment_pinning_demo.py`](code/environment_pinning_demo.py) | Admissible version space, pinning levels, hash coverage, closure growth |
| [`code/workflow_managers_demo.py`](code/workflow_managers_demo.py) | Critical path, makespan and efficiency on $W$ workers, cache invalidation fractions, core-hours |
| [`code/notebooks_vs_pipelines_demo.py`](code/notebooks_vs_pipelines_demo.py) | Exact counts of valid cell orders, stale-output exposure, pipeline comparison |
| [`code/data_versioning_demo.py`](code/data_versioning_demo.py) | Naive versus deduplicated storage, new chunks per version, ancestry, ambiguity |
| [`code/containers_reproducibility_demo.py`](code/containers_reproducibility_demo.py) | Layer recipe, rebuild cascade, bitwise agreement, surviving arithmetic differences |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_crisis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python environment_pinning_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python workflow_managers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python notebooks_vs_pipelines_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_versioning_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python containers_reproducibility_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits
0. Each runs in well under two seconds.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group publishes a paper whose main result is a correlation of 0.34, significant
> at $p = 0.02$ from 30 records, with 12 further relationships examined. Their
> repository has a requirements file with no versions, one 300-line script run by
> hand, a data path into a shared directory, and no figures metadata.
> **(a)** State the power for an effect of 0.5 at $n = 30$ and the expected
> replication rate. **(b)** Compute the mean false discovery proportion for 12 tests
> with a 10 % prior, and state the two inputs it depends on. **(c)** Classify each of
> the four repository problems into the lesson's taxonomy and name the lesson that
> treats it. **(d)** State the sample size for 80 % power at an effect of 0.3, and the
> data identifier you would ask for before anything else. **(e)** Write the five
> provenance fields for the analysis, and say which cannot be recovered three years
> later.

Worked versions of (a)–(e) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **Fixing the wrong category.** A pinned environment does not repair an unresolved
   data identifier, and a workflow manager does not repair a winner's-curse estimate.
2. **Quoting a model number as a measurement.** Every figure in this module is a
   property of a stated model; the lessons say which parameter it depends on.
3. **Engineering without inference.** The most reproducible pipeline in the world can
   compute a post-selection estimate; lesson 01 measures the size of that effect.
4. **Versioning code and not data.** Code without data versions is a script; data
   without code versions is a file.
5. **Assuming a container is a guarantee.** It freezes the software environment and
   leaves the arithmetic, the scheduler, the clock and the services.
6. **Recording provenance where nobody looks.** The identifier belongs in the figure,
   the README and the availability statement, not only in a log file.

## Related modules

- [22-01 Research Software Engineering](../01-research-software-engineering/README.md) —
  the code-level practices this module's runs depend on.
- [22-07 Testing and Quality Assurance for Scientific Code](../07-software-testing-quality/README.md) —
  the automated checks that make a pipeline trustworthy.
- [22-04 Databases and Large Data Collections](../04-databases-and-large-data/README.md) —
  where versioned data live at scale.
- [22-06 High-Performance and Cloud Computing for Research](../06-high-performance-and-cloud/README.md) —
  where workflows and containers meet schedulers and budgets.
- [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md) —
  where the environment, data and licence statements meet the paper.
