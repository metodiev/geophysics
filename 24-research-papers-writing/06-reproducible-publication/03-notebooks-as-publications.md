---
id: 24-06-03
title: "Interactive Publications and Notebooks as Articles"
level: research
prereqs: ["24-06-01", "22-02-04"]
estimated_minutes: 50
tags: [notebooks, reproducibility, publishing, executable-papers, hidden-state]
---

# Interactive Publications and Notebooks as Articles

A notebook is the most convenient container for a computation and the easiest one to
publish in a state that does not run. The difference is not the tool but the
**execution order**: a notebook is a chain of cells, and it reproduces only if every
link in the chain does. This lesson models that chain, measures how quickly it breaks
as notebooks grow, and separates the two failure causes — hidden state and
environment — because they have different remedies.

The organising idea is that **reproduction is a property of the whole chain**. With a
$0.9\%$ per-cell chance that an out-of-order execution leaves a hidden dependency, a
ten-cell notebook reproduces about $90\%$ of the time and a $160$-cell notebook about
$19\%$ of the time. The length is under the author's control, and so is the discipline
that removes the term entirely.

> **Data provenance.** All numbers are **SYNTHETIC**. Notebooks are simulated as
> chains of cells with chosen probabilities; no notebook was executed, inspected or
> archived. The per-cell probability is a teaching value chosen to make the
> compounding visible.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** hidden state and **state** why a notebook with hidden state reproduces
   in the author's session and fails on a fresh kernel.
2. **Compute** the probability that a notebook of a given length contains at least one
   hidden dependency.
3. **Separate** the hidden-state failure from the environment failure and **state**
   the different remedy for each.
4. **Measure** the reproducibility decline with notebook length and **state** the
   design implication.
5. **Prepare** a notebook for publication: restart, run in order, pin the environment,
   and check the outputs.
6. **Choose** between a notebook and a script-and-report pipeline and **state** the
   criteria.

## Prerequisites

- [24-06-01 Publishing Data and Code Alongside Papers](01-data-publication.md) — the
  deposit the notebook belongs to.
- [22-02-04 Notebooks versus Pipelines](../../22-data-engineering-reproducibility/02-reproducible-workflows/04-notebooks-vs-pipelines.md) —
  the tooling comparison this lesson quantifies.

## 1. Hidden state

A notebook's cells share one kernel state. If a cell is executed out of source order —
a normal event while exploring — it can use a value that only exists because an
earlier cell had been run later in the session. The saved file then contains outputs
that the source, read top to bottom, cannot produce.

Three observable symptoms, all offline-checkable:

- **Missing execution counts.** A cell with output but no stored execution count was
  executed in import or by hand; the demonstration's model gives a mean of $3.9$
  such cells in a $10$-cell notebook and $65.0$ in a $160$-cell notebook.
- **Non-monotonic execution counts.** Counts that go $1,2,3,11,5,\dots$ record a
  session that was re-run; the file no longer describes a linear script.
- **Variables defined after use.** The clearest symptom, and the one a reader cannot
  see without running the notebook.

## 2. The chain, and how it breaks

Model a notebook with $n$ cells, each executed out of source order with probability
$0.30$, and each such execution creating a real hidden dependency with probability
$0.03$. The per-cell hazard is

$$h = 0.30 \times 0.03 = 0.009,$$

so the probability that a notebook of $n$ cells contains at least one hidden
dependency is

$$\mathbb{P}(\text{at least one}) = 1 - (1 - h)^{n}.$$

The demonstration's simulation:

| Cells | Mean out-of-order cells | Notebooks with at least one hidden dependency |
|---|---|---|
| $10$ | $3.1$ | $11.5\%$ |
| $20$ | $5.9$ | $18.0\%$ |
| $40$ | $11.7$ | $36.5\%$ |
| $80$ | $23.9$ | $51.5\%$ |
| $160$ | $48.5$ | $77.0\%$ |

Most out-of-order executions are harmless re-runs; the dangerous minority compounds
with length. A $1\%$ per-cell chance is enough to make a long notebook more likely
than not to contain hidden state.

## 3. Two failure causes, two remedies

For $200$ notebooks of $40$ cells:

| Cause | Notebooks failing |
|---|---|
| Hidden state | $59$ ($29.5\%$) |
| Environment or numerical difference | $7$ ($3.5\%$) |
| At least one cause | $66$ ($33.0\%$) |
| Reproduces without intervention | $134$ ($67.0\%$) |

Hidden state is the dominant cause, and the remedies are different:

- **Hidden state** is removed by *discipline*: restart the kernel, run all cells in
  order, re-run, and save only after a clean pass. No tool prevents out-of-order
  execution; the tool only makes the check possible.
- **Environment** is removed by *pinning*: a locked environment specification. The
  demonstration's effect of pinning alone, with hidden state present, is to move total
  failure from $32.5\%$ to $31.0\%$; with hidden state removed it moves failure from
  $6.0\%$ to $0.5\%$. Pinning is necessary and is not sufficient.

**The single practice that catches both** is execution-order testing: run the notebook
from a fresh kernel on a machine that is not the author's, before depositing it. It
catches hidden state directly and environment differences as a by-product.

## 4. Length and reproduction

| Cells | No hidden state | Reproducible, unpinned | Reproducible, pinned |
|---|---|---|---|
| $10$ | $90.5\%$ | $85.5\%$ | $90.0\%$ |
| $20$ | $87.5\%$ | $79.5\%$ | $86.0\%$ |
| $40$ | $70.0\%$ | $65.5\%$ | $68.5\%$ |
| $80$ | $48.5\%$ | $48.0\%$ | $48.5\%$ |
| $160$ | $19.0\%$ | $18.0\%$ | $19.0\%$ |

Reproducibility falls steeply with length, and above about $80$ cells the environment
term is irrelevant because hidden state has already dominated. The design implication
is straightforward: **split the notebook**. A deposit of five $20$-cell notebooks,
each reproducing about $80\%$ of the time, is more useful than one $100$-cell
notebook reproducing about $40\%$ of the time — and each of the five can be fixed
independently.

## 5. Preparing a notebook for publication

The checklist, in order:

1. **Restart the kernel and run all.** Do it three times; a notebook that reproduces
   twice and fails once has hidden state.
2. **Move the setup to the top.** Imports, parameters, paths, seeds — one cell, first.
3. **Delete dead cells.** Exploration scaffolding is not part of the publication.
4. **Number the sections** so the narrative is visible in the outlines.
5. **Pin the environment**, and record the versions in the notebook's first cell
   output.
6. **Check every output against the paper.** A number that drifted is the commonest
   silent inconsistency in an executable paper.
7. **Add a "run this to check" cell** that recomputes the paper's main table.
8. **Export the narrative** to a static form (HTML or PDF) alongside the notebook, so
   the record survives a format change.

## 6. When a script and a report are better

A notebook is the right container when the value is in the narrative and the
exploration. It is the wrong container when:

- **the computation is a pipeline** that runs unattended, where a notebook's kernel
  state and cell order add risk without adding explanation; use a script and a build
  step (see
  [22-02-03 Workflow Managers](../../22-data-engineering-reproducibility/02-reproducible-workflows/03-workflow-managers.md));
- **the artefact must be tested**, since tests run against functions and scripts, not
  against cells;
- **the output is large**, because notebook files embed outputs and grow unmanageably.

The common arrangement in practice is both: scripts hold the computation, and a
notebook holds the narrative that imports them and produces the figures. The notebook
then has no hidden state because every step is a function call with explicit inputs.

## Assumptions and regime of validity

1. **The probabilities are chosen.** Real notebooks vary in how much exploration they
   contain; the per-cell hazard is a teaching value chosen to make compounding
   visible, not a measurement.
2. **Independence between cells is assumed.** In practice hidden dependencies cluster
   (the same variable is reused throughout), which makes failures more likely to be
   fatal when they occur.
3. **Environment failure is a single probability.** Real numerical differences depend
   on the algorithm, the linear-algebra backend and the hardware.
4. **Reproduction is defined as running from the top.** A notebook may be reproducible
   in other senses, such as producing the same figure under interactive use.
5. **The checklist is not a guarantee.** A cleanly run notebook can still depend on
   data that were not deposited; the deposit is the other half of the claim.

## The honest summary

Hidden state dominates: $29.5\%$ of $40$-cell notebooks contain it, rising to $77.0\%$
at $160$ cells, and pinning alone moves total failure by $1.5$ percentage points while
the discipline of a clean run moves it by $26$. Reproducibility falls with length, so
split the notebook, run it clean, and export the narrative.

## Python demonstration

[`code/notebooks_as_publications_demo.py`](./code/notebooks_as_publications_demo.py)
prints four labelled sections: out-of-order execution and hidden dependencies; the
clean-re-run failure rate with its two causes; the decline of reproducibility with
length; and the separate effects of pinning and of removing hidden state.

```bash
cd 24-research-papers-writing/06-reproducible-publication/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python notebooks_as_publications_demo.py
```

## Exercises

Problems are in
[`exercises/03-notebooks-as-publications-exercises.md`](./exercises/03-notebooks-as-publications-exercises.md),
worked answers in
[`exercises/03-notebooks-as-publications-solutions.md`](./exercises/03-notebooks-as-publications-solutions.md).

## Mastery checkpoint

1. Take a notebook you have written and record its execution counts: are they
   monotonic?
2. Restart the kernel and run all cells; note anything that fails or changes.
3. Count the cells with output but no execution count.
4. Compute your notebook's implicit cell hazard: how many cells could depend on a
   later cell?
5. Deposit a version that passes the checklist of §5, and state the command a reader
   should run.

## Common pitfalls

1. **Saving the session, not the script.** The outputs are not the computation.
2. **Re-running one cell and re-saving.** This is how hidden state is created.
3. **Assuming a pinned environment is sufficient.** It removes one term of two.
4. **Long notebooks.** Reproduction probability falls steeply with length.
5. **Outputs that drift from the paper.** Check every number, not only the figures.
6. **Not exporting a static form.** The notebook format changes; the narrative should
   survive it.

## Where this is used

- **Executable papers and supplementary notebooks:** the checklist is the submission
  step.
- **Teaching:** notebooks are the standard delivery format, and the same discipline
  makes them reusable next year; see
  [24-06-01 Publishing Data and Code Alongside Papers](01-data-publication.md).
- **Group practice:** a "run all before sharing" rule is cheap and catches the dominant
  failure.
- **Reproducibility claims:** the notebook's clean run is evidence; the digest of its
  outputs is the test; see
  [24-03-04 Reproducible Research Practice End to End](../03-research-methods-and-rigour/04-reproducible-research-practice.md).

## Related lessons

- [24-06-01 Publishing Data and Code Alongside Papers](01-data-publication.md) —
  the deposit the notebook accompanies.
- [24-06-02 DOIs, ORCID, Persistent Identifiers and Data Repositories](02-persistent-identifiers.md) —
  how the release is addressed and versioned.
- [22-02-04 Notebooks versus Pipelines](../../22-data-engineering-reproducibility/02-reproducible-workflows/04-notebooks-vs-pipelines.md) —
  the tooling trade-off.
- [22-07-03 Regression Testing Data](../../22-data-engineering-reproducibility/07-software-testing-quality/03-regression-testing-data.md) —
  the tests that catch silent output drift.

## Self-assessment checklist

- [ ] I can define hidden state and recognise its three symptoms.
- [ ] I can compute the chain probability for a notebook of a given length.
- [ ] I can separate hidden-state and environment failures and their remedies.
- [ ] I can state why splitting a notebook raises reproducibility.
- [ ] I can run the eight-step publication checklist.
- [ ] I can choose between a notebook and a script-and-report arrangement.
