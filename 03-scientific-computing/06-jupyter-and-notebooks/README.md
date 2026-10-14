# Module 03-06 — Jupyter, Notebooks and Literate Computing

**Stages:** beginner → intermediate · **Prerequisites:**
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for the module and import model a kernel implements, and
[03-01-07 Errors and Debugging](../01-python-fundamentals/07-errors-and-debugging.md)
for reading the tracebacks a failing cell stores.

A notebook is the instrument most working geophysicists actually think in: the
computation, the figure and the sentence that explains the figure in one file.
It is also the only common scientific format in which the stored results can
disagree with the code beside them. This module is about that tension — not as a
caution but as a set of mechanisms, measurements and habits.

Four lessons, in dependency order:

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md) | beginner | Three objects — file, kernel, view — and which one survives a save; counting the legal execution orders |
| 02 | [Markdown and LaTeX in Notebooks](./02-markdown-and-latex.md) | beginner | The half of the file a digest cannot check, and the delimiter rule this repository's gate applies |
| 03 | [Making Notebooks Reproducible (Restart-and-Run-All)](./03-reproducible-notebooks.md) | intermediate | Digests, seeds, order dependence, and the nondeterminism no seed can fix |
| 04 | [Converting Notebooks to Scripts, Tests and Reports](./04-notebooks-to-scripts.md) | intermediate | One source, three artefacts, and exactly what the conversion loses |

## What makes this module different from a notebook tutorial

Three habits, applied in every lesson:

- **The mechanism is demonstrated, not described.** Every claim about execution
  counts, hidden state, digests and exports is produced by running a real kernel
  through `nbclient` and quoting the output. The lessons print the same numbers
  the scripts do.
- **The failure mode is shown, not warned about.** A 6 MB figure, a broken magic,
  a stale output and a traceback that overwrites itself all appear in the
  output rather than in a list of pitfalls.
- **What cannot be checked is named.** A digest cannot check the units in the
  markdown; an export cannot check a formula; a diff cannot detect an error that
  was present in the baseline. Where the method has a limit, the lesson says so.

## Prerequisites in detail

The module assumes you can write and run a Python function and read a traceback.
It does **not** assume a browser, a Jupyter installation in the usual sense, or
any experience with notebooks. Everything is done through
[nbformat](https://jupyter.org) and `nbclient`, the two libraries the Jupyter
interface itself uses, so the mechanism is visible rather than clicked.

## How to run the demos

Every demo runs under the project virtual environment and exits 0 without
network access:

```bash
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebook_workflow_demo.py
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/markdown_and_latex_demo.py
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/reproducible_notebook_demo.py
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebooks_to_scripts_demo.py
```

| Demo | Does | Needs |
|---|---|---|
| `notebook_workflow_demo.py` | executes notebooks through a real kernel, measures counts, errors and saved metadata | nbformat, nbclient, jupyter_client |
| `markdown_and_latex_demo.py` | counts and checks delimiters, generates LaTeX with SymPy, exports to HTML | nbformat, nbconvert, sympy |
| `reproducible_notebook_demo.py` | digests outputs, measures order dependence, summation error and hash randomisation | nbformat, nbclient, numpy |
| `notebooks_to_scripts_demo.py` | converts, runs the converted script, compiles nothing but runs `nbconvert` from the CLI | nbformat, nbclient, nbconvert |

Each demo writes its generated notebooks, scripts and HTML into a scratch
directory under `code/` and deletes that directory before it exits, so running
them leaves no artefacts in the repository. No demo downloads anything, and none
quotes a wall-clock time: where a performance claim would be natural, the demos
count cells, executions, calls and bytes instead.

## Materials in this module

| Path | Contents |
|---|---|
| `01-…04-*.md` | The four lessons |
| [`code/`](./code) | Four runnable demonstrations |
| [`exercises/`](./exercises) | Problem sets and solutions for each lesson, with the measured numbers in the solutions |

## Suggested path

**If you are new to notebooks:** lessons 01 and 02, then run
`notebook_workflow_demo.py` and change one cell order at a time.

**If you already use notebooks daily:** start at lesson 03. The three measured
failures there — hidden state, unseeded draws and hash randomisation — are the
ones that survive into published work.

**If you are building a pipeline:** lesson 04, then
[03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md).

## Related modules

- [03-01-python-fundamentals](../01-python-fundamentals/README.md) — the language
  the kernel runs.
- [03-02-numpy](../02-numpy/README.md) — the random-number interface lesson 03
  tests.
- [03-07-sympy](../07-sympy/README.md) — the source of generated LaTeX in lesson
  02.
- [03-13-testing-profiling-packaging](../13-testing-profiling-packaging/README.md)
  — what makes a notebook's results testable.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)
  — the wider reproducibility infrastructure these lessons feed.

## Self-assessment checklist

- [ ] I can name the three objects a running notebook involves. (§01)
- [ ] I can write down the count sequence a given set of clicks produces. (§01)
- [ ] I can predict whether a source passes the delimiter balance check. (§02)
- [ ] I can compute an output digest that ignores counts. (§03)
- [ ] I can explain why `np.sum([1e16, 1.0, -1e16])` is 0. (§03)
- [ ] I can name a source of irreproducibility no seed fixes. (§03)
- [ ] I can list what a script export preserves and discards. (§04)
- [ ] I can state the difference between a regression test and a correctness test.
      (§04)
