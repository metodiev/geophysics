# 22 — Data Engineering, Reproducibility and Scientific Software

**Stages:** intermediate → research

This folder is about the machinery that surrounds a geophysical result: the code that
computes it, the environment that runs it, the format that stores it, the database that finds
it, the workflow that regenerates it, the team that reviews it, the machine that executes it
and the tests that decide whether any of it still works. The organising idea is that **every
engineering choice has a measurable consequence** — a parse time, a false-positive rate, a
queue wait, a bill, an invalidation set, a noise floor — and that the consequence, not the
convention, is what decides the choice.

The first honest difficulty is that reproducibility is not a property of a paper; it is a
property of an artefact chain. A result is reproducible when the data, the code, the
environment and the workflow are all identified and all available, and when the intermediate
steps can be re-executed without a human reconstructing them from memory. Every module here
works on one link of that chain: 22-01 on the code and its review, 22-02 on environments and
workflows, 22-03 on formats, schemas, QC and metadata, 22-04 on databases and layouts,
22-05 on the practices that keep the chain intact across people and years, 22-06 on where the
computation runs and what it costs, and 22-07 on the tests and goldens that tell you whether
the chain still produces what it produced last month.

The second difficulty is that **scale changes the failure mode, not only the numbers**. A
partition key holding 1.9 % of the rows becomes a task 22.9× the mean; a 64-instance fleet
running for two hours is interrupted with probability 0.864; a 600-test suite with a 1 %
per-test flake rate is red on 99.76 % of pushes, and a red build then implies a real defect
with probability 0.100. None of these is a bug in someone's code; each is a structural
consequence of size that a small test never reveals. The lessons pair each with the
arithmetic that exposes it and the practice that prevents it.

The third difficulty is that **most of the cost of data work is not compute**. A 12-hour
64-core run producing two terabytes costs 698.4 units in module 22-06's teaching model, of
which 38.4 is compute: storage and egress are 95 % of it, and in a project-level view 65 % of
the bill can be storage, movement and recomputation. The same shape appears throughout the
folder — in format choice, in chunk sizes, in retention policy and in cache invalidation —
and the lessons measure it rather than asserting it.

Three distinctions recur often enough to state once:

- **Measured, modelled and chosen.** A file size or a runtime is measured; a queue wait, a
  partition skew and a cache invalidation set are modelled from statistics; a compression
  level, a chunk size, a tolerance and a retention period are chosen. Lessons quote each in
  its own terms, and the exercises ask for the label.
- **Sufficient versus necessary.** A checksum is sufficient to detect a change in bytes but
  not in meaning; a reference system in the metadata is necessary but not sufficient for a
  correct distance; a passing suite is necessary but not sufficient for correct science. The
  lessons state which of the two each practice provides.
- **Cost of the practice versus the cost of the failure.** Every recommendation here is priced
  on both sides: a goldens' tolerance against a platform change, a checkpoint interval
  against an interruption, a retry policy against a masked race, an egress redesign against a
  bill.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Design** scientific software as testable, documented, reviewable modules, and
   **release** them with a licence and a citation file that make them citable.
2. **Build** a reproducible workflow: pinned environments, a workflow manager with
   content-addressed invalidation, versioned data, and containers with recorded digests.
3. **Choose** a data format, layout and compression from a measured access pattern, and
   **state** the cost of the alternative.
4. **Design** a queryable archive — relational, spatial, time-series or object-store —
   from statistics about the queries it will serve, and **compute** the cost of a scan, an
   index lookup, a join and a request.
5. **Run** a project so that it can be handed over: a structure, an issue tracker, a
   writing process, a data management plan and an open-science practice.
6. **Request**, size and cost computation on a cluster or in the cloud, and **diagnose** the
   failures specific to each: an oversized request, a serial stage, a checkpoint interval
   longer than the interruption interval, an egress bill.
7. **Test** numerical and data code at a stated tolerance, **run** the tests in CI without
   drowning in flakes, **record** goldens that a future maintainer can interpret, and
   **benchmark** against a measured noise floor.
8. **State** honestly what each artefact in the chain does not guarantee: a format does not
   guarantee a meaning, a test does not guarantee correctness, a cost model does not
   guarantee a price, and a container does not guarantee a result.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Level |
|---|---|---|---|
| 01 | [Research Software Engineering](./01-research-software-engineering/README.md) | Software design for research; version control; code review; documentation; licensing, citation and credit | intermediate → graduate |
| 02 | [Reproducible Research Workflows](./02-reproducible-workflows/README.md) | The reproducibility problem; pinned environments; workflow managers; notebooks versus pipelines; data versioning; containers | intermediate → research |
| 03 | [Data Formats and Engineering](./03-data-formats-and-engineering/README.md) | Scientific file formats; format design trade-offs; pipeline design and provenance; finding and fetching earth data; quality control and flagging; metadata standards | intermediate → research |
| 04 | [Databases and Large Data Collections](./04-databases-and-large-data/README.md) | Relational databases and SQL; spatial databases; time-series databases; partitioning, chunking and out-of-core; cloud-native access | advanced → research |
| 05 | [Collaboration and Project Management](./05-collaboration-and-project-management/README.md) | Project structure; issue tracking; collaborative writing; data management plans; open-science practice | intermediate → graduate |
| 06 | [High-Performance and Cloud Computing for Research](./06-high-performance-and-cloud/README.md) | Cluster jobs and schedulers; cloud computation; cost, scaling and practical efficiency | research |
| 07 | [Testing and Quality Assurance for Scientific Code](./07-software-testing-quality/README.md) | Test strategy for numerical and data code; continuous integration; regression testing against known results; benchmarking and documentation tests | research |

## The dependency spine

- **22-01 is the entry point** for anyone who writes code and has not worked in a team:
  design, version control, review, documentation, licence.
- **22-02 depends on 22-01** and is the technical core of the folder: the lock file, the
  workflow manager, the data version and the container are the four artefacts that make a
  result re-runnable.
- **22-03 depends on 22-02** and turns storage into a decision: formats, layouts, pipelines,
  QC and metadata.
- **22-04 depends on 22-03** and turns access into a decision: which store answers which
  query at what cost.
- **22-05 runs alongside 22-01 to 22-04**: it is the human side of the same chain, and the
  only module that is useful before any of the technical ones.
- **22-06 depends on 22-02 and 22-04**: where the jobs run, and what they cost.
- **22-07 depends on 22-01 and 22-02**: what the code must prove about itself before it is
  trusted with a result.

## Suggested paths

**If you are a researcher writing your own analysis code:** 01 (design, version control,
documentation), then 02 (§1–3 reproducibility and environments), then 07 (§1–3 testing and
goldens). That path alone prevents most of the reproducibility failures described in 02 §1.

**If you are building a data service:** 03 (formats, pipelines, metadata), then 04 in full,
then 02 §5–6 (data versioning and containers) and 06 §1 (where the jobs run).

**If you are preparing a large simulation campaign:** 02 §3 (workflow managers), 04 §4
(partitioning and out-of-core), 06 in full (requests, cloud, cost), 07 §4 (benchmarking).

**If you are preparing a paper or a dataset release:** 01 §5 (licence and citation), 03 §6
(metadata), 05 §3–5 (writing, data management plan, open science), 07 §1 and §3 (what the
tests and goldens prove).

**If you are here for the measurements:** every demo is self-contained, seeds its random
numbers, prints labelled values with units, writes nothing and exits 0; the ★★★ exercises ask
you to design measurements on systems you choose.

## Mastery checkpoint for the folder

Answer without notes; the demonstrations in the modules are there to check arithmetic:

> A group is preparing a four-year project that will acquire a 150-station seismic network,
> build an event catalogue, run a 5 000-realisations inversion ensemble and publish three
> papers with open data and code.
> **(a)** State the four artefacts that make a published result re-runnable, and where each
> is recorded. **(b)** They store the continuous waveform archive as one file per channel-day
> and expect to query windows of minutes; compute the amplification of the read pattern and
> name the layout change. **(c)** The ensemble's serial fraction is 5 % and each realisation
> takes 2 core-hours at 4 cores; state the smallest job shape that finishes 5 000
> realisations in a week, and the completion-tracking mechanism. **(d)** Their suite has 400
> tests with a 0.5 % per-test flake rate; compute whether a red build is likely to be real.
> **(e)** Their event catalogue query returns 3 000 of 50 million rows; state the access path
> and the reason. **(f)** State the three engineering decisions in this project that you would
> document first for a reader in ten years, and why those three.

Worked versions of (a)–(f) appear across the folder's lesson solutions at ★★ and ★★★ level.

## Conventions used throughout

- **Units are always stated**, and physical quantities carry them: seconds, metres of
  storage, bytes, core-hours, arbitrary cost units.
- **Numbers that are modelled are labelled** as SYNTHETIC or as a model, with the parameters
  that produced them. Numbers that are measured say on what.
- **Tolerances and thresholds are measurements**, not conventions: each lesson that uses one
  states the floor it was placed above.
- **Relative links are repository-relative** and resolve on GitHub; external URLs are avoided
  except where a specific tool's documentation is genuinely authoritative, and those are
  registered in `tools/verified_links.tsv`.
- **Demos print, and then exit.** No file writes, no network, no plots, no exceptions: a
  demonstration that fails on a reader's machine teaches nothing.

## A caution about numbers in this folder

Every page count, parse time, queue wait, price, flake rate, coverage figure, tolerance and
cost in this folder is either **measured on a stated platform** or **computed from a stated
model with chosen parameters**. File sizes depend on the data, latencies depend on the store,
prices depend on the provider and the day, flake rates depend on the machine, and
floating-point arithmetic depends on the platform. Treat the *shape* of each result — which
term dominates, how the cost scales, what the false-alarm rate is — as the transferable
content, and re-measure the constants on your own system before using them in a decision.
That instruction is itself one of the folder's lessons: 22-07 §2 explains why a benchmark
without a measured noise floor cannot support a claim, and the same discipline applies to
every number here.

## How to use the code

Each module has a `code/` directory of demonstrations and an `exercises/` directory with
graded problems (★ foundational, ★★ applied, ★★★ research-oriented) and worked solutions.
The demonstrations are plain scripts with no dependencies beyond the project environment:

```bash
cd 22-data-engineering-reproducibility/<module>/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python <demo>.py
```

Each script prints its results as labelled tables, seeds its random numbers with
`np.random.default_rng(20261014)` so a reader sees the same values, runs in well under a
second, and exits 0. The numbers printed are the numbers quoted in the lessons — if they
disagree, the lesson is wrong, and that is worth an issue.

## Where this folder sits

- **Before it:** [03 Scientific Computing](../03-scientific-computing/README.md) for the
  Python and numerical tooling, and
  [19 Numerical Modeling and HPC](../19-numerical-modeling-hpc/README.md) for the algorithms
  whose cost this folder measures.
- **Alongside it:** [21 Statistics and Bayesian Methods](../21-statistics-bayesian-ml/README.md),
  whose results have to be computed reproducibly, and
  [20 Signal Processing](../20-signal-processing/README.md), whose pipelines are the
  consumers of the formats and stores described here.
- **After it:** [23 Field Methods and Instruments](../23-field-methods-instruments/README.md),
  where the data originates, and
  [24 Research Papers and Writing](../24-research-papers-writing/README.md), where the
  citation, licensing and metadata practices of 22-01 and 22-03 become a publication.
