---
id: 03-06-01
title: "Notebook Workflow, Cells, Kernels and Execution Order"
level: beginner
prereqs: ["03-01-04", "03-01-07"]
estimated_minutes: 90
tags: [jupyter, notebooks, kernels, reproducibility, tooling]
---

# Notebook Workflow, Cells, Kernels and Execution Order

A Jupyter notebook is the instrument most geophysicists actually think in. It
holds a computation, the figure that came out of it, and the sentence that
explains what the figure shows, in one file that can be emailed. That is
enormous leverage, and it comes with one structural flaw that has to be
understood rather than avoided: **the file and the computation are two different
objects, and the file can be saved in a state the computation never had.**

This lesson is about the mechanics of that split. It is not a list of
keyboard shortcuts. By the end you should be able to say, for any notebook you
are handed, what was computed in what order, and whether what you are looking at
is a record of a computation or a collection of outputs from several.

Every number and every quotation in this lesson was produced by running the
demonstration in this module's `code/` directory. Run it before reading on:

```bash
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebook_workflow_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the three objects a running notebook involves — the file, the
   kernel process and the browser view — and say which of them survives a save.
2. **Predict** the `execution_count` values a sequence of cell executions will
   produce, and **identify** a notebook whose stored outputs cannot have come
   from a single top-to-bottom run.
3. **Explain** why an out-of-order click can silently produce a wrong number and
   what a `NameError` tells you that a wrong number does not.
4. **State** what a kernel restart destroys and what it does not.
5. **Decide** when a notebook is the right tool and when a script is, on the
   basis of what each one can promise about its own state.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — the module and import model that a kernel implements.
- [03-01-07 Errors and Debugging](../01-python-fundamentals/07-errors-and-debugging.md)
  — reading a traceback, which is what a notebook cell stores when it fails.

You do not need a browser for this lesson. Everything below is done through
`nbformat` and `nbclient`, the two libraries that the Jupyter interface itself
uses, so the mechanism is visible rather than clicked.

## 1. Intuition: the three-object model

A notebook that looks like one thing is three:

| Object | Lives | Survives save? | Survives restart? |
|---|---|---|---|
| The `.ipynb` file | On disk | yes (it *is* the save) | yes |
| The kernel process | In memory | no | no |
| The browser view | In the front end | no | no |

The file is JSON. It contains the source of every cell, and — this is the part
that matters — the **outputs** of every cell as they were at the moment of the
last save, together with an `execution_count` for each code cell.

The kernel is a separate operating-system process running an IPython
interpreter. All the variables live there. When the demonstration saved a
notebook and read it back, the counts in the file were `[1, 2, 3, 4]`
and the file was 2623 bytes; the kernel that produced them was already gone.

So: **the file is a transcript, and the kernel is the computation.** A
transcript is only trustworthy if the computation happened in the order the
transcript implies. Nothing in the file format enforces that, which is the whole
subject of this lesson.

## 2. Definitions

**Cell.** A unit of content in the file. The two kinds that matter are *code*
cells (sent to the kernel) and *markdown* cells (rendered by the front end and
never sent to the kernel). A notebook is an ordered list of cells.

**Kernel.** A process that executes code cells and holds the resulting state. It
has a *name* — the kernelspec — which identifies a recipe for launching it. On
the machine used for these measurements the kernelspec named `python3` was:

```
argv = ['python', '-m', 'ipykernel_launcher', '-f', '{connection_file}']
resource_dir = .../geophysics/.venv/share/jupyter/kernels/python3
```

Note what the recipe is: `python -m ipykernel_launcher`. A kernel is not a
special kind of interpreter; it is an ordinary interpreter started with a
launcher that speaks the Jupyter messaging protocol over a socket.

**Execution count.** An integer the kernel assigns to each *code* cell it
executes, incrementing once per execution. It is stored in the file. Markdown
cells never receive one, which the demonstration confirms: re-executing the
markdown cell left the counts at `[1, 2, 3, 4]`.

**State.** The set of names bound in the kernel, plus the state of any library
that holds global data. This is not in the file at all.

**Session.** The lifetime of a kernel between launches. Two notebooks open at
once are two sessions even when they run the same kernelspec.

## 3. Execution order and the count

A linear run of a five-cell notebook (one markdown cell, four code cells)
produced:

```
  after run-all: execution_count = [1, 2, 3, 4]
    cell 1: count=1   -> G = 6.674e-11 m3 kg-1 s-2
    cell 2: count=2   -> spacing = 25.0 m
    cell 3: count=3   -> line length = 1000.0 m
    cell 4: count=4   -> python 3.14.4
```

The counts are the order of execution, and in a run-all they coincide with file
order. They are also the only evidence in the file about order. Their utility is
entirely in what they look like when they are *not* `1..n`.

Re-running the first code cell in the same kernel gave:

```
  after re-running code cell 1 (same kernel): execution_count = [5, 2, 3, 4]
  cells whose count is below the highest count: 3 of 4
```

Three of the four outputs were computed before cell 1's current version, under a
kernel state that existed before the last edit. The file does not record that
the cells were edited between runs — a cell's source is simply its current
source — so the notebook now presents outputs from two different states as if
they belonged together.

> **Rule of thumb.** If the counts are not `1..n` in file order, the notebook is
> not a record of a computation. It is a record of several.

## 4. Order changes the answer

The counts tell you the order was not linear. They do not tell you that it
mattered. This does, and it is the reason the whole discipline exists.

Consider a notebook whose cell 1 defines a density and whose cell 2 uses it.
Clicking cell 2 on its own, in a fresh kernel:

```
  clicking cell 1 on its own -> "NameError: name 'rho' is not defined"
  error outputs stored: ['NameError']
  then cell 0 followed by cell 1 -> 'rho = 2.670 g cm-3'
  error outputs left in the notebook afterwards: []
```

Two lessons are visible in that block. First, the failure is *loud*: a missing
dependency produces an exception, and the file keeps the traceback. Second, and
worse, the traceback is **replaced** when the cell is re-run: after the
successful run, `error outputs left in the notebook afterwards: []`. A reader
opening the file sees `rho = 2.670 g cm-3` and a count of 2, with no hint that an
earlier attempt failed.

Now make the dependency less obvious. In the reproducibility demonstration the
same three cells were executed in two different orders:

```
  cells clicked 0, 1, 2 -> v = 0.098100 m/s
  cells clicked 0, 2, 1 -> v = 0.009810 m/s
  ratio between the two answers: 10.0
  source of cell 1 identical in both files: True
```

There was no exception either time. Cell 3 changed `dt` from 0.01 s to 0.001 s
after cell 2 had already used it. The two notebooks are byte-identical apart
from their outputs and counts, and they disagree by a factor of ten. **A
`NameError` is a gift**: it is the only failure mode that tells you the order was
wrong. Order dependence without a NameError produces plausible numbers.

## 5. What a restart destroys

A kernel restart discards every name. The demonstration defined `kappa` in one
kernel and then evaluated a cell referencing it in a fresh one:

```
  after first kernel: kappa defined, count=1
  new kernel, same-looking cell -> "NameError: name 'kappa' is not defined"
```

This is the mechanism behind **Restart and Run All**, which is the only
operation that makes a notebook's stored outputs a property of the file rather
than of a history of clicks. Everything else — "run all above", individual
re-execution, editing a cell and re-running it — leaves the possibility of stale
output in place.

There is a second consequence, less often stated. A restart also discards
library-level state that no cell mentions: a random number generator's position,
matplotlib's global figure registry, `os.chdir` calls, environment variables set
with `os.environ`, and the import cache. A notebook can be order-dependent
through any of those without a single NameError.

## 6. A derivation: how many execution orders are legal?

The counts told us that the order was wrong. This section makes "wrong" precise,
so that the risk can be quantified instead of feared.

Write the notebook as a set of code cells $C = \{1, \dots, n\}$ and define a
relation $\prec$ on it:

$$i \prec j \quad\text{iff}\quad \text{cell } j \text{ reads a name that cell }
i \text{ writes}.$$

This is a **dependency relation**. It is transitive in principle but not
necessarily complete, and it says nothing about cells that share no names. An
execution order is a permutation $\pi$ of $C$. It is **legal** iff every
dependency runs before its dependent:

$$\forall\, i,j \in C: \quad i \prec j \;\Longrightarrow\; \pi^{-1}(i) <
\pi^{-1}(j).$$

The legal orders are exactly the **linear extensions** of the partial order
generated by $\prec$.

### 6.1 Three cases that can be counted by hand

**No dependencies at all** (an antichain). Every permutation is legal:

$$N_{\text{legal}} = n! = 4! = 24.$$

**A single dependency pair**, say $1 \prec 2$. Exactly half the permutations put
1 before 2:

$$N_{\text{legal}} = \frac{n!}{2} = 12.$$

*Derivation.* Pair each permutation $\pi$ with the permutation obtained by
swapping the positions of the elements 1 and 2 and leaving everything else
fixed. This is an involution with no fixed points, and it maps a legal order to
an illegal one and back again, so the two classes have equal size, $n!/2$ each.
**The answer does not depend on $n$**: with $n = 40$ cells and one dependency
there are $40!/2$ legal orders, which is still exactly half.

**A chain** $1 \prec 2 \prec 3 \prec 4$. One order satisfies all three
constraints:

$$N_{\text{legal}} = 1 = \frac{n!}{n!}.$$

The demonstration counted these by brute force over the 24 permutations of four
cells, which is the honest way to check a combinatorics argument:

```
  no dependencies              legal orders 24 of 24 = 1.0000
  one dependency (2 needs 1)   legal orders 12 of 24 = 0.5000
  a chain 1 -> 2 -> 3 -> 4     legal orders  1 of 24 = 0.0417
  a fork (4 needs 1 and 3)     legal orders  8 of 24 = 0.3333
```

The fork — cell 4 needs both cell 1 and cell 3, which are independent of each
other — admits 8 orders, $24/3$, because the constraint fixes the position of 4
relative to two of the other three and so admits one third of the permutations.

### 6.2 What the count buys

The numbers are practical. A notebook with a *chain* of dependencies — load,
clean, reduce, invert, plot — has exactly one legal order, so any click sequence
other than the top-to-bottom one is wrong. A notebook with a single dependency
has a one-in-two chance of being legal by accident, which is precisely why
out-of-order execution usually *seems* to work: the failures are intermittent,
and intermittency is what lets a bug survive to publication.

## 7. Python demonstration

The demonstration builds notebooks in memory with `nbformat`, runs them through
a real IPython kernel with `nbclient`, and reports what the kernel did. The
essential parts:

```python
async def _execute(nb, plans) -> None:
    client = NotebookClient(nb, kernel_name="python3", timeout=120,
                            allow_errors=True)
    async with client.async_setup_kernel():           # starts the kernel
        for plan in plans:                            # one kernel, many orders
            for index in plan:
                await client.async_execute_cell(nb.cells[index], index)
    # leaving the context manager shuts the kernel down again

def run(nb, plans):
    asyncio.run(_execute(nb, plans))
```

`plans` is a list of cell-index sequences: `[[0, 1, 2, 3, 4]]` is a run-all,
`[range(5), [1]]` is a run-all followed by a click on cell 1, and `[[1], [0],
[1]]` is the out-of-order sequence of Section 4. All plans in one call share a
single kernel, deliberately: a fresh kernel per plan would reset the counters and
hide the thing being measured.

Reading the outputs:

```python
def stream_text(cell) -> str:
    parts = []
    for out in cell.outputs:
        if out.get("output_type") == "stream":
            parts.append(out.get("text", ""))
        elif out.get("output_type") == "error":
            parts.append(f"{out.get('ename')}: {out.get('evalue')}")
    return "".join(parts).strip()
```

What to observe, and what each observation means:

| Observation (measured) | Consequence |
|---|---|
| `after run-all: execution_count = [1, 2, 3, 4]` | A linear run is self-describing |
| `after re-running code cell 1: [5, 2, 3, 4]` | A file can be saved inconsistent |
| Re-running a failed cell leaves `[]` error outputs | The failure history is destroyed |
| Fresh kernel → `NameError: name 'kappa' is not defined` | State lives in the process, not the file |
| `execution_count persisted in the file: [1, 2, 3, 4]` | Outputs and counts are saved |
| `wrote workflow_demo.ipynb: 2623 bytes` | The whole notebook was a few kilobytes |
| `legal orders 12 of 24` for one dependency | One wrong click in two goes undetected |

**Breaking exercise.** Change the third notebook in the demonstration so cell 1
writes two names and cell 2 reads both. Predict, before running, how many of the
24 orders remain legal, then compute it.

## 8. Units and dimensional bookkeeping inside the kernel

State is not only "which names exist". It is also **what units they carry**, and
Python checks none of it. The order-dependence example of Section 4 is that
failure seen through a dimensional lens. Cell 1 defined

$$v = g\,\Delta t, \qquad [v] = \mathrm{m\,s^{-2}} \cdot \mathrm{s}
= \mathrm{m\,s^{-1}},$$

and the two executions of cell 2 disagreed because $\Delta t$ was 0.01 in one
case and 0.001 in the other. Both are dimensionally consistent — there is no unit
error to catch — and both produce a number in m/s. The measured pair was

$$v_1 = 9.81 \times 0.01 = 0.098100\ \mathrm{m\,s^{-1}}, \qquad
v_2 = 9.81 \times 0.001 = 0.009810\ \mathrm{m\,s^{-1}},$$

so $v_1/v_2 = 10.0$ exactly: the factor of ten a mistaken
millisecond-versus-second convention produces. Dimensional analysis cannot find
it, because the *dimensions* are right and only the *convention* is wrong. That
is the strongest argument for putting the unit in the name (`dt_s`) or in a
unit-aware container, and for writing it in the markdown cell beside the code.

A worked conversion, for completeness, in the units the rest of the curriculum
uses:

$$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}} = 10\
\mu\mathrm{m\,s^{-2}}, \qquad 1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}.$$

A notebook that stores a gravity anomaly as `2.0` and calls it "the anomaly" has
discarded a factor of $10^{5}$ relative to SI and cannot say so. Cell-level prose
is the only place that information can live, which is why the markdown half of a
notebook is not decoration — see [lesson 02](./02-markdown-and-latex.md).

## 9. Exercises

Attempt these with the notebook closed; solutions are in
[`exercises/01-notebook-workflow-solutions.md`](./exercises/01-notebook-workflow-solutions.md).

### ★ Foundational

**★1.** A notebook has five code cells, all executed in file order, then the
second is executed twice more. Write down the resulting `execution_count` list.

**★2.** State, for each item, whether it survives a save, a kernel restart, or
neither: (a) cell source, (b) cell outputs, (c) the value of a variable, (d)
`matplotlib`'s current figure, (e) the file the kernel has open.

**★3.** Why does a markdown cell never receive an `execution_count`?

**★4.** Name the two objects a notebook involves that are not the `.ipynb` file,
and say which one "Restart and Run All" destroys.

### ★★ Applied

**★★5.** Three code cells: cell 1 writes `a`, cell 2 writes `b` and reads `a`,
cell 3 reads `b`. How many of the 6 execution orders are legal? Compute it by
hand and then by brute force.

**★★6.** A colleague sends a notebook with counts `[1, 2, 5, 3, 4]`. Give two
distinct histories that could produce those counts, and explain why the stored
outputs cannot all come from one kernel state.

**★★7.** Construct a three-cell notebook in which *every* order produces
identical outputs; then one in which every order except the file order produces
a wrong number with no exception. Run both with `nbclient` and report the
measured outputs.

**★★8.** The demonstration found that re-running a cell that had failed replaced
its traceback with a successful output, leaving `[]` error outputs. Explain why
the file format makes this unavoidable, and describe one workflow that preserves
the evidence.

### ★★★ Research-oriented

**★★★9.** Generalise the count. Compute the number of legal orders for a
notebook organised as $k$ independent chains of length $m$ each ($n = km$), give
the formula, and verify it by brute force for $n \le 7$.

**★★★10.** Measure the frequency of out-of-order execution in practice. Write a
script that inspects a sample of `.ipynb` files you already have (your own, or a
colleague's with permission), extracts `execution_count` sequences, and reports
the fraction that are non-monotonic and the fraction that are not `1..n`. Report
your measured fractions and sample size, and state explicitly why your sample may
not generalise. If you have no sample, say so and stop; do not invent numbers.

## 10. Assumptions and limitations of this model

- **The counts are advisory.** Nothing prevents saving a notebook whose counts
  are `[17, 3, 12]`; Jupyter will do it without complaint. The discipline is
  social, and tooling only makes it visible.
- **Kernels are not sandboxed.** A code cell can read and write the filesystem
  and the network with the privileges of the user who launched the kernel.
  Executing someone else's notebook is executing their code.
- **The language in the kernelspec is not guaranteed.** The demonstration found
  `language_info` unpopulated in a notebook run through `nbclient` without an
  explicit metadata step, even though the kernel was Python 3.14.4. A reader who
  needs the interpreter version should read it from the kernel, as cell 4 did,
  rather than from the metadata.
- **Reproducibility of the file bytes is not reproducibility of the science.**
  The demonstration saved the same notebook twice; the file's SHA-256 digest
  differed between runs while the outputs were identical, because the client
  records timing metadata. Section 4 of the reproducibility lesson takes this
  apart properly.
- **Timing measurements are not quoted here.** Kernels start in a fraction of a
  second to a few seconds depending on the machine and the environment, so this
  lesson quotes counts (cells, executions, errors) and never wall-clock times.

## 11. Worked examples

### 7.1 Reading a notebook you were sent

You receive `inversion.ipynb`. Open the JSON, not the browser, and extract the
counts:

```python
import json
raw = json.loads(open("inversion.ipynb").read())
counts = [c.get("execution_count") for c in raw["cells"] if c["cell_type"] == "code"]
print(counts)
```

If `counts == list(range(1, len(counts) + 1))` the file is *consistent with* a
single linear run — not proof of one, since a restart-and-run-all and a lucky
sequence of clicks both produce it. If the counts are not monotonic, the file
definitely contains outputs from more than one state. That asymmetry is the
useful part: monotonic counts are weak evidence, non-monotonic counts are strong
evidence against.

In the demonstration, the final notebook saved to disk had
`execution_count persisted in the file: [1, 2, 3, 4]` after the linear run, and
`[5, 2, 3, 4]` after the extra click. The second pattern is what an inconsistent
file looks like.

### 7.2 A stale-output case with numbers

A gravity reduction notebook: cell 2 sets the Bouguer density `rho`, cell 3
computes the correction from `rho`, cell 4 plots. The analyst plots, dislikes the
map, goes back and changes `rho` from 2670 to 2400 kg/m³, re-runs cell 2, and
looks at the plot. The plot is now inconsistent with `rho`. Nothing warns them,
because cell 3 was not re-run and cell 4 was not re-run: the figure on screen is
from the old `rho` and the *number printed next to it* is from the new one.

The count column is the tell: `[1, 5, 4]` after that sequence. The fix is not
carefulness; it is `Restart and Run All` followed by re-reading the numbers,
which is a different activity from looking at the figure.

### 7.3 When a script is the better tool

A notebook cannot be imported. It has no entry point, no `__main__`, and its
execution order is whatever the counts say. The moment a computation needs to be
(a) run by someone else without reading it, (b) run in a loop over 40 datasets,
or (c) asserted on, it wants to be a module. Lesson
[04](./04-notebooks-to-scripts.md) does that conversion, and measures what
survives it.

## 12. Common mistakes

1. **Trusting the counts to be `1..n`.** They are whatever the last sequence of
   clicks produced, and Jupyter will save them without complaint.
2. **Editing a cell, re-running only that cell, and reading a downstream
   number.** The most expensive error in this lesson, because nothing fails.
3. **Thinking the file contains the computation.** It contains one set of
   outputs and a recipe for the cells; the kernel is gone.
4. **Assuming two notebooks share a kernel.** They do not, even with the same
   kernelspec; state does not cross.
5. **Believing a `NameError` means the notebook is broken.** It means the
   dependency was not executed in this kernel, which is usually an *ordering*
   error and usually harmless once you know.
6. **Calling a notebook "reproducible" because it displays the same numbers.**
   Displayed numbers are the ones that were not re-run. Only a
   restart-and-run-all makes them properties of the file.
7. **Confusing the front end with the kernel.** Closing the browser tab does not
   stop the kernel; the process keeps holding memory and any open files.

## 13. Real-world applications

- **Processing a field dataset.** A day of gravity readings, read in one cell,
  reduced in the next five, plotted in the sixth. The notebook is a record of
  the reduction, and its counts are the audit trail.
- **Exploring a new dataset.** The whole point is that order does not matter
  yet; the discipline is that before anything leaves the notebook, it is
  restarted and run once from the top.
- **Handing analysis to a co-author.** The counts are the first thing to check
  for both of you. A notebook received with counts `[3, 1, 2]` is a conversation,
  not a result.
- **Teaching.** Cells let a lecture build a computation visibly, which is why
  this curriculum ships its demonstrations as scripts *and* discusses notebooks:
  the script can be asserted on, the notebook can be read.
- **Long-running inversions.** A kernel that has been alive for hours holds a
  model in memory. Restarting it to satisfy a workbook convention costs the whole
  run, which is the real reason this discipline gets skipped — and the reason
  expensive stages belong in scripts, with notebooks used for the last step.

## 14. Further reading

- **Jupyter documentation** (jupyter.org). Level: beginner. The user-facing
  description of kernels, cells and the notebook format; start with the
  "Notebooks" section.
- **The Jupyter Notebook format specification** (nbformat documentation).
  Level: intermediate. The normative description of the `.ipynb` JSON, including
  the meaning of `execution_count` and cell metadata. Referenced throughout this
  lesson because the format is the thing we are reasoning about.
- **Kluyver, T. et al. (2016). *Jupyter Notebooks — a publishing format for
  reproducible computational workflows.* IOS Press.** Level: intermediate. The
  design document for the notebook, including an honest discussion of the
  out-of-order execution problem. Widely available; check your library.
- **Rule, A., Tabard, A. & Hollan, J. D. (2018). Exploration and explanation in
  computational notebooks. *CHI 2018*.** Level: advanced. An empirical study of
  how analysts actually execute cells out of order; the source of the phrase
  "notebooks are used for exploration and explanation, and the two conflict".
- **Pimentel, J. F. et al. (2019). A large-scale study about quality and
  reproducibility of Jupyter notebooks. *MSR 2019*.** Level: advanced. Measured
  statistics on how many public notebooks have non-monotonic execution counts.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> current availability through your library.

## 15. Related lessons

- [02 Markdown and LaTeX in Notebooks](./02-markdown-and-latex.md) — the other
  half of the file: the prose cells.
- [03 Making Notebooks Reproducible](./03-reproducible-notebooks.md) — turns the
  observations of Section 4 into tests.
- [04 Converting Notebooks to Scripts, Tests and Reports](./04-notebooks-to-scripts.md)
  — what happens when the notebook has to serve someone else.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — the tooling that catches what a notebook cannot assert about itself.
- [03-01-07 Errors and Debugging](../01-python-fundamentals/07-errors-and-debugging.md)
  — reading the traceback that a failed cell stores.

## 16. Self-assessment checklist

- [ ] I can name the three objects involved in a running notebook and say which
      survives a save. (§1)
- [ ] I can write down the `execution_count` sequence a given set of clicks
      produces. (§3)
- [ ] I can spot a notebook whose outputs came from more than one kernel state,
      and say what the tell is. (§3)
- [ ] I can explain why an order-dependent notebook without a `NameError` is
      more dangerous than one with. (§4)
- [ ] I can state two kinds of state a restart destroys that no cell mentions.
      (§5)
- [ ] I can say what monotonic counts do and do not prove. (§11.1)
- [ ] I can decide, for a given task, whether it belongs in a notebook or in a
      module. (§11.3)
