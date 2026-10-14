---
id: 22-02-04
title: "Notebooks vs Pipelines: Choosing the Right Tool"
level: advanced
prereqs: ["22-02-03", "22-02-01"]
estimated_minutes: 45
tags: [notebooks, pipelines, reproducibility, exploration, scientific-workflow]
---

# Notebooks vs Pipelines: Choosing the Right Tool

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a notebook's result depends on the order in which its cells ran,
   and **state** what "restart and run all" therefore tests.
2. **Count** the valid execution orders of a cell graph exactly, and **compute** the
   probability that a random order is valid.
3. **Measure** how many cells hold stale output after editing one cell, and **state**
   why a notebook gives no warning.
4. **Explain** what a pipeline removes from the problem and what it costs, and
   **choose** a tool for a stated task rather than on preference.
5. **Convert** an exploratory notebook into a pipeline without losing the record of
   the exploration.
6. **Design** a hybrid workflow in which exploration is free and the published
   artefact is ordered.

Every number in this lesson is **SYNTHETIC** and exact for the generated graph: the
cell graph is built with chosen parameters and the counts of execution orders are
computed by dynamic programming, not estimated from notebooks. No notebook file was
parsed and no survey of notebook usage is quoted.

## Prerequisites

- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](./03-workflow-managers.md) —
  the rule model and the invalidation rules this lesson contrasts with a session.
- [22-02-01 The Reproducibility Problem in the Computational Sciences](./01-reproducibility-crisis.md) —
  the failure taxonomy, of which manual steps are one category.

## 1. Intuition: two tools for two different jobs

A notebook is a **session** with a persistent interpreter: cells share variables and
can be run, re-run, skipped and reordered. That mutability is exactly what makes
exploration efficient, and exactly what makes the session's final state
unrepeatable. A pipeline is a **schedule**: it declares what depends on what and
executes the graph, with no session and no way for the result to depend on what the
analyst did last Tuesday.

The two are not competing answers to one question. Exploration wants a mutable
environment and cheap iteration; a published result wants a fixed order and
reproducible inputs. The mistake this lesson measures is using the exploration tool
as the production artefact — that is, treating "the notebook as it stands" as the
record of how the figure was made.

## 2. The model: cells, dependencies and execution orders

Model a notebook as a set of cells with **definition-use dependencies**: cell $j$
depends on cell $i$ when it uses a name that $i$ defines. A session that produced a
coherent result must have run each cell after its dependencies, so the **valid**
orders are the **linear extensions** of the cell graph — the permutations in which
every cell follows all of its dependencies.

The count of linear extensions is computable exactly, even for a moderate number of
cells, by dynamic programming over subsets:

$$L(S) = \sum_{j \notin S,\ \text{preds}(j) \subseteq S} L(S \cup \{j\}),
\qquad L(\text{all}) = 1,$$

where $S$ is the set of cells already executed. The total number of orders is
$n!$, and the probability that a **random** order is valid is $L/n!$.

## 3. Counting: how much freedom a session has

The demonstration builds a **SYNTHETIC** graph of $n = 14$ cells with 20
dependencies and computes:

$$n! = 87178291200, \qquad L = 913584, \qquad
\frac{L}{n!} = 1.048 \times 10^{-5}.$$

So one ordering in roughly $95\,000$ is valid, and the notebook's saved outputs
correspond to one of the $913\,584$ valid orders. As the notebook grows, the
fraction collapses:

| Cells | Dependencies | Valid orders | $P(\text{a given order is valid})$ |
|---|---|---|---|
| 6 | 4 | 72 | $1.000 \times 10^{-1}$ |
| 8 | 8 | 392 | $9.722 \times 10^{-3}$ |
| 10 | 12 | 1260 | $3.472 \times 10^{-4}$ |
| 12 | 16 | 147840 | $3.086 \times 10^{-4}$ |
| 14 | 20 | 913584 | $1.048 \times 10^{-5}$ |

The table is not monotone in the fraction: it is driven by the ratio of dependencies
to cells, so a 12-cell notebook with 16 dependencies can have a *larger* fraction of
valid orders than a 10-cell notebook with 12 (the counts happen to be close here,
and the 10-cell case has proportionally more edges). What is universal is the
conclusion: for a dozen interacting cells the valid orders are a tiny island in the
space of permutations, and the session's state is only reachable from one of them.

The practical consequence is the answer to a common argument: "I always run the
cells in order, so the order does not matter." Right — but *which* order is not
recorded anywhere, and among the many valid ones they differ in what variables hold
at the end of the run.

## 4. Stale output: the failure that is invisible

Editing a cell invalidates everything downstream, because those cells used values
computed from it. The demonstration measures, for the 14-cell graph:

- mean number of downstream cells with stale output after editing one cell:
  **2.8**;
- worst case: **7 of 14** cells;
- cells with no downstream dependents (safe to edit with no consequence): **3**.

A notebook displays no marker for a stale cell. Its output is the previous run's
value, formatted identically to a fresh one, and the analyst reads it as current.
This is the notebook's version of the workflow manager's undeclared input
([22-02-03](03-workflow-managers.md) §8): a plausible number with no error, from a
tool that had no way to know the state was inconsistent.

## 5. What a pipeline removes, and what it costs

For the same graph, a pipeline has **one** state: the scheduler computes the
dependency order, re-runs the invalidated subgraph, and there is no other ordering
to produce. The demonstration's ratio is $913\,584$ notebook states to $1$ pipeline
state.

| Property | Notebook | Pipeline |
|---|---|---|
| Iteration cost while exploring | very low (state persists) | high (re-run the graph) |
| Ordering ambiguity | hundreds of thousands of valid states | none |
| Stale output | silent | impossible (the output is regenerated or reported as skipped) |
| Parameter sweeps | loop in a cell, or copy the notebook | one rule per parameter |
| Partial failure | the session continues in a half-updated state | the rule fails and its output is absent |
| Review of a change | diff of a JSON file | diff of code and rules |

Nothing in that table says a pipeline is better; it says the two tools trade
iteration speed for order. The design rule that follows is: **explore in a
notebook, publish a pipeline**. The pipeline does not make the analysis correct
(this is the lesson's honest core), but it removes the order as a variable, which
is what makes a wrong result visible.

## 6. Converting exploration into a published artefact

The conversion has four steps, and none of them is "delete the notebook":

1. **Extract the computation into functions.** Each cell whose logic matters becomes
   a function with a narrow signature (see
   [22-01-01](../01-research-software-engineering/01-software-design-science.md) §6).
   The notebook then calls the functions, so the notebook and the pipeline share one
   implementation.
2. **Write the pipeline as rules over those functions**, one rule per artefact, with
   declared inputs and outputs and pinned environments
   ([22-02-02](02-environment-pinning.md)).
3. **Keep the notebook as the exploration record**, with a note saying which
   pipeline now produces the published figures. Its outputs are history, not
   evidence.
4. **Adopt the restart-and-run-all test.** Before release, restart the kernel and
   run the whole notebook top to bottom. If the figures change, the notebook was
   relying on state; that state is now a bug to fix in the pipeline.

Two further practices make the record useful rather than decorative: run notebooks
in CI with a reduced input so that the "run all" test is automated, and never commit
executed outputs as if they were evidence — an executed notebook's outputs are
convenient but they cannot be reproduced from the file alone.

## 7. Worked example: which tool for which job

| Task | Tool | Why |
|---|---|---|
| Exploring a new dataset for the first time | Notebook | iteration cost dominates; no artefact yet |
| Testing three filter designs against one record | Notebook | the value is in comparing intermediates, not in the order |
| Producing figure 3 of the paper | Pipeline | the order and inputs must be fixed and recorded |
| Sweeping a parameter over 50 values | Pipeline | one rule per value; the notebook's loop is not resumable |
| A 9-hour inversion to run overnight | Pipeline | resumability and failure attribution |
| Teaching or a demonstration to a reviewer | Notebook | the narrative order *is* the content |

Notice that the same project uses both, and that the transition point is not
"the project got big" but "the value now lies in the artefact rather than in the
exploration".

## 8. Worked example: a stale figure

A group discovers that a conference figure was produced from a stale cell: they had
edited the velocity model in an early cell, run the cells below it, but not the QC
cell that produced the figure's colour scale. Work through it:

1. **Was the output stale?** Yes — the edited model was one of the changed cell's 7
   downstream cells, which in the demonstration's model would be 3 of the 14 cells
   on average and up to 7.
2. **Would a pipeline have prevented it?** Yes: the colour-scale artefact declared
   the velocity model as an input, so the edit would have invalidated it and the
   scheduler would have regenerated it before the figure rule ran.
3. **Would a pipeline have caught the error in the *analysis*?** No. If the velocity
   model itself was wrong, the pipeline would have produced a wrong figure
   consistently and reproducibly.
4. **What is the fix?** Move the model preparation into a rule with the model file
   declared as an input, add the restart-and-run-all test to CI, and state in the
   paper's artefact which pipeline produced the figure.

## Assumptions and regime of validity

1. **Definition-use dependencies are the only ones modelled.** A cell can also
   depend on the filesystem, on a mutable object mutated in place, on a random
   seed's position or on network state; those dependencies are invisible to the
   count, so the real number of valid orders is *smaller* and the hazard *larger*.
2. **Exact counts for a small graph.** $L$ is exact for the generated graph;
   the numbers describe this graph, not a distribution over notebooks.
3. **A cell's dependency set is a static approximation.** In a real notebook a name
   can be rebound later, so the "graph" changes as the session runs — another way
   the count is optimistic.
4. **Random order as the null.** The $L/n!$ fraction answers "what if the order were
   chosen at random"; a real analyst runs sensible orders, so the practical risk is
   not random order but *undo*cumented differences between two sensible orders.
5. **The pipeline comparison assumes a correct invalidation rule.** A pipeline with
   an undeclared input has the notebook's failure mode with a scheduler's
   confidence.

## The honest summary

A notebook is a session: it keeps state, which is what makes exploration cheap and
what makes its final state underdetermined. For a 14-cell graph with 20
dependencies, $913\,584$ of $87\,178\,291\,200$ cell orders are valid
($1.048 \times 10^{-5}$), the saved outputs correspond to one of them, and editing a
single cell leaves a mean of 2.8 cells (worst case 7) holding stale output with no
visible warning. A pipeline removes the order as a variable — one state instead of
$913\,584$ — at the cost of iteration speed, and it does not make the analysis
correct. The workable practice is hybrid: explore in the notebook, extract the
computation into functions, publish a pipeline, keep the notebook as the record,
and adopt the restart-and-run-all test as the check that the notebook never
contributed more than exploration.

## Python demonstration

[`code/notebooks_vs_pipelines_demo.py`](./code/notebooks_vs_pipelines_demo.py)
builds the cell graph with `np.random.default_rng(20261014)` and prints, under four
numbered banners:

1. $14!$, the exact count of valid orders ($913\,584$) and the fraction
   $1.048 \times 10^{-5}$;
2. the valid-order table for 6, 8, 10, 12 and 14 cells;
3. the stale-output statistics after a one-cell edit (mean 2.8, worst 7, three
   cells with no dependents);
4. the pipeline comparison: $913\,584$ states against one.

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python notebooks_vs_pipelines_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-notebooks-vs-pipelines-exercises.md`](./exercises/04-notebooks-vs-pipelines-exercises.md)
and
[`exercises/04-notebooks-vs-pipelines-solutions.md`](./exercises/04-notebooks-vs-pipelines-solutions.md).

## Mastery checkpoint

Without notes: a notebook has eight cells. Cell 1 loads data; cells 2 and 3 define
two parameters; cell 4 filters; cell 5 plots the filter response; cell 6 inverts;
cell 7 plots the model; cell 8 prints a summary.

1. Draw the dependency graph under the reasonable assumption that 4 uses 1, 2 and
   3, that 5 uses 2 and 4, that 6 uses 2 and 4, that 7 uses 6, and that 8 uses 7.
2. Count the valid execution orders by hand (or explain the structure that makes the
   count straightforward).
3. State which cells become stale if cell 2 is edited.
4. State the two properties a pipeline would give you here, and the one thing it
   would not.

## Common pitfalls

1. **Trusting "I always run the cells in order".** The order is not recorded; among
   the $913\,584$ valid orders of the demonstration's graph, different ones leave
   different values in scope.
2. **Reading a stale output as a fresh one.** There is no marker, and the mean
   number of stale cells after a single edit is 2.8.
3. **Committing executed notebooks as evidence.** The outputs cannot be regenerated
   from the file alone; the pipeline is the evidence.
4. **Replacing exploration with pipeline authoring.** Writing rules before the
   analysis is understood wastes both tools; extract functions first.
5. **Assuming a pipeline fixes the science.** A pipeline removes ordering ambiguity;
   it does not check that the model is right.
6. **Skipping the restart-and-run-all test.** It is the cheapest test that the
   notebook's figures are reproducible from the notebook.

## Where this is used

- **Paper artefacts** — the published figure should come from a pipeline or from a
  notebook that passes the restart test: see
  [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Group practice** — a shared convention of "notebooks are drafts, pipelines are
  artefacts" resolves most reproducibility arguments before they happen.
- **Teaching** — the notebook's narrative order is the content, which is a
  legitimate use of the format.
- **Long analyses** — overnight inversions need resumability and failure
  attribution, which is the pipeline's strength: see
  [22-06-01 Running Jobs on HPC Clusters and Schedulers](../06-high-performance-and-cloud/01-cluster-jobs.md).

## Related lessons

- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](./03-workflow-managers.md) —
  the tool the pipeline is written in.
- [22-02-05 Data Versioning and Provenance Tracking](./05-data-versioning.md) —
  what the cells and rules consume, and how it is identified.
- [03-06-03 Reproducible Notebooks](../../03-scientific-computing/06-jupyter-and-notebooks/03-reproducible-notebooks.md) —
  the mechanics of notebook metadata, execution counts and conversion.
- [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md) —
  where the restart-and-run-all test is automated.

## Self-assessment checklist

- [ ] I can explain why a notebook's result depends on the execution order.
- [ ] I can compute the number of valid execution orders for a small cell graph.
- [ ] I can measure the stale-output exposure of a cell.
- [ ] I can state what a pipeline removes and what it does not fix.
- [ ] I can convert a notebook into a pipeline in four steps.
- [ ] I can choose the right tool for exploration, production and teaching.
