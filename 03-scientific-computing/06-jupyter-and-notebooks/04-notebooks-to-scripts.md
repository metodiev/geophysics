---
id: 03-06-04
title: "Converting Notebooks to Scripts, Tests and Reports"
level: intermediate
prereqs: ["03-06-01", "03-06-03"]
estimated_minutes: 90
tags: [nbconvert, notebooks, testing, reporting, reproducibility]
---

# Converting Notebooks to Scripts, Tests and Reports

A notebook is not a program, a test or a report, but it is the place where most
of the work that becomes a program, a test or a report is first done. This lesson
is about the conversion step: what `nbconvert` preserves, what it silently
drops, and what has to be added by hand before the result can be trusted.

The conversion is mechanical, and it fails in exactly two ways: it can produce a
script that does not run, and it can produce a script that runs and quietly
computes something different from the notebook. Both are measurable, and both are
measured below.

```bash
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebooks_to_scripts_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a `PythonExporter` conversion preserves — cell boundaries, code,
   markdown as comments — and what it discards, with measured counts.
2. **Predict** which notebook features break a converted script, and verify the
   failure with an exit code.
3. **Compare** the notebook's stdout with the converted script's stdout and
   explain why they can be made identical.
4. **Write** the percent (`# %%`) module format and explain why it serves both
   audiences.
5. **Decide** between executing a notebook as a regression test and asserting on
   a function, and **justify** the decision with a measured case.

## Prerequisites

- [03-06-01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
- [03-06-03 Making Notebooks Reproducible](./03-reproducible-notebooks.md) —
  a converted script is only a test if the notebook was deterministic to begin
  with.

## 1. Intuition: a notebook is a script with a rendering layer

Look at what a notebook consists of, from the point of view of an interpreter:
code cells, in an order. If you strip the markdown, the outputs and the cell
metadata, what remains is *almost* a Python module — and the "almost" is the
interesting part, because the layer that a notebook adds (the `%` magics, the `!`
shell escapes, the display protocol) is what makes it pleasant to use and
un-portable.

Conversely, what a notebook *adds* over a script is the outputs: the numbers and
figures that were true at the moment of the last save. Converting to a script
throws those away, so a script is always a *rerun* of the analysis, never a
transcript of it. The demonstration measures that explicitly:

```
  occurrences of the printed value in the default export: 3
```

The three occurrences are the markdown comment, the source line, and the
constructed f-string — not one is an output. The value `1.119637e-04` appears
nowhere in the export.

## 2. Definitions

**Exporter.** An `nbconvert` class that turns a notebook into another format.
`PythonExporter` (script), `HTMLExporter` (report), `MarkdownExporter`,
`LatexExporter`.

**Percent format.** Plain Python in which code cells are separated by `# %%`
comment lines. It is valid Python, valid to the interpreter, and recognised as
cell boundaries by editors and by Jupyter.

**Executed notebook.** A notebook whose outputs were produced by running it, as
opposed to one whose outputs were accumulated interactively.

**Regression test.** A check that a result has not changed. Distinguish it from a
*correctness test*, which checks that a result is right.

**`# %%` versus `# In[ ]`.** `nbconvert` in version 7 inserts `# In[ ]:` markers
by default; both are comments, and both are inert to Python. The difference is
only who reads them.

## 3. What the conversion preserves, measured

The demonstration builds a four-cell notebook (one markdown, three code), executes
it, and exports it twice:

```
  default export:      29 lines, 414 characters
  prompts stripped:    16 lines, 296 characters
  '# In[' markers in default export: 3
  '# In[' markers in stripped export: 0
  occurrences of the printed value in the default export: 3
```

Reading it:

- **Code is preserved exactly.** Every line of every code cell appears.
- **Markdown becomes comments.** The `# Bouguer slab correction` heading and the
  LaTeX are present as `#`-prefixed lines — a loss of structure, and a gain in
  that the reasoning travels with the script.
- **Cell boundaries become `# In[ ]:` markers**, three of them for three code
  cells. With `exclude_input_prompt=True` they vanish and the export shrinks from
  29 lines to 16 (a 45 % reduction in line count, mostly blank lines and markers).
- **Outputs are absent.** Zero of the printed values are in the file.

That last point is the one to remember: **the script does not contain the
answer**, only the instructions that produce it. A repository that ships only
converted scripts has to re-run them to know what they said.

## 4. Derivation: what a script can and cannot promise

Let a notebook have code cells $c_1, \dots, c_n$ with sources $s_1, \dots, s_n$
and outputs $o_1, \dots, o_n$. A conversion $T$ produces a text file

$$T: \; (s_1, \dots, s_n) \;\longmapsto\; \hat{s}_1 \Vert \hat{s}_2 \Vert
\cdots \Vert \hat{s}_n$$

with **no dependence on the outputs**: $\partial T / \partial o_i = 0$ for every
$i$. That is a strong statement, and it is why conversion is stable: change a
figure and the script does not move; change a cell's source and it does.

The information lost is exactly

$$L = \sum_i \left( H(o_i) + H(m_i) - H(\text{comment}(m_i)) \right),$$

where $m_i$ are markdown cells and $H$ is any reasonable measure of content.
Concretely, for the demonstration's notebook: **3 numeric outputs and one
rendered heading** were reduced to text comments and one LaTeX string.

The obligation that follows is that whoever receives the script must be able to
recover $L$ — which means either shipping the notebook too, or having the script
print what the notebook displayed. The second is the better engineering choice:
**a script that prints its results with labels is self-documenting**, and it is
what this repository's `code/` directories do.

## 5. Where conversion fails, measured

The demonstration's notebook contains one magic, `%matplotlib inline`, which is
what a reader of any plotting notebook has in their first cell. The exporter
rewrites it:

```
  'get_ipython()' calls in the exported script: 1
  the rewritten line: ["get_ipython().run_line_magic('matplotlib', 'inline')"]
  running that script: exit code 1
  first stderr line: NameError: name 'get_ipython' is not defined
  stdout produced before the failure: ''
```

The conversion is *faithful* and the result is *unrunnable*: `get_ipython()` is
defined inside a kernel, not in a plain interpreter. The same applies to `!`
shell escapes, which become `get_ipython().system(...)`, and to other magics.

Removing the magic line and re-running gives the payoff:

```
  after deleting the magic line: exit code 0
  script stdout matches the notebook stdout exactly: True
```

The script's stdout is *identical* to the notebook's, which is the useful
invariant: **a converted script is a re-execution of the notebook's code, so its
printed output should match the notebook's stored output exactly**, once the
magics are dealt with.

### 5.1 The command line, and a naming trap worth measuring

```
  '--to script'  exit code: 0; wrote ['analysis_script.txt']
  '--to python'  exit code: 0; wrote ['analysis_python.py']
  running the CLI-produced .py: exit code 1 (NameError: name 'get_ipython' is not defined)
  '--to html'    exit code: 0
  produced analysis_report.html: 280811 bytes
  contains the notebook stdout line 'slab correction = 1.119637e-04 m/s^2': True
  contains the LaTeX source '2\pi G\rho h' verbatim: True
  '<span class="math' wrappers (server-side rendering): 0
```

Two facts to take away. First, in `nbconvert` 7.17.2 the `--to script` exporter
writes **`.txt`**, while `--to python` writes **`.py`**, from the same content.
A build step that globs `*.py` will silently find nothing. Second, the HTML
export contains both the output and the LaTeX *verbatim*, with zero server-side
math wrappers — consistent with lesson
[02](./02-markdown-and-latex.md)'s finding that the mathematics is left for
MathJax.

## 6. The percent format

The conversion that serves both audiences is not the exporter's default. It is
plain Python with cell markers:

```python
# %%
import numpy as np
G = 6.674e-11
rho = 2670.0  # kg m-3

# %%
h = 100.0  # m
slab = 2.0 * np.pi * G * rho * h
print(f"slab correction = {slab:.6e} m/s^2")

# %%
print(f"            in mGal = {slab / 1e-5:.6f}")
```

Measured:

```
  '# %%' cell markers written: 3
  exit code: 0
  stdout matches the notebook: True
```

Why this format is better than either extreme:

- It runs as a script (`python file.py`), so it is testable, importable and
  lintable with the same tools as any module.
- It carries cell boundaries, so an editor or Jupyter can open it as a notebook.
- Magics must be removed by hand — which is a feature, because it forces the
  question "does this analysis need a notebook feature, or was that a
  convenience?".

## 7. Worked examples

### 7.1 The Bouguer slab, and why the number is the check

The demonstration's notebook computes the Bouguer slab correction

$$g_{\text{slab}} = 2\pi G \rho h,$$

and reports

$$g_{\text{slab}} = 2\pi \cdot 6.674\times10^{-11} \cdot 2670 \cdot 100
= 1.119637\times10^{-4}\ \mathrm{m\,s^{-2}} = 11.196372\ \mathrm{mGal}.$$

The dimensional check is worth doing once by hand:

$$[\mathrm{m^3\,kg^{-1}\,s^{-2}}] \cdot [\mathrm{kg\,m^{-3}}] \cdot
[\mathrm{m}] = \mathrm{m\,s^{-2}}.$$

This is the number the converted script must reproduce, and it does — the
measured agreement is `True` to the printed precision. It is also the number a
regression test compares.

### 7.2 A converted notebook as a regression test

Change the Bouguer density in the notebook and re-run both versions:

```
  baseline rho = 2670 kg/m3 -> slab correction = 1.119637e-04 m/s^2
  changed  rho = 2900 kg/m3 -> slab correction = 1.216085e-04 m/s^2
  stdout identical: False
  expected ratio of the corrections, 2900/2670 = 1.086142
```

The measured ratio of the two values is $1.216085/1.119637 = 1.08614$, which is
$2900/2670$ to the printed precision — the correction is linear in $\rho$, as
the formula says. So "execute and diff the stdout" detects the change.

What it does **not** do: detect a formula that is wrong in the same way in both
versions. If the notebook had omitted the factor $2\pi$ from the beginning, both
runs would agree and the test would pass. **A regression test answers "did this
change?", never "is this right?"** The second question needs an assertion against
an independent expectation:

```python
expected = 2 * np.pi * 6.674e-11 * 2670.0 * 100.0
assert abs(slab - expected) / expected < 1e-12, slab
```

That is a correctness test, and it belongs in `pytest`, not in a notebook diff.
The tooling is the subject of
[03-13](../13-testing-profiling-packaging/README.md).

### 7.3 A report

The HTML export is the third product. Measured: 280811 bytes, containing the
stdout line and the LaTeX source verbatim. It is a report — self-contained,
readable by a non-Python reader, with the numbers frozen at export time — and it
is *not* a script: nothing in it can be re-run. Ship the pair.

## 8. Assumptions and limitations

- **All measurements are from `nbconvert` 7.17.2 on Python 3.14.4.** Marker
  syntax, default exporters and file extensions have changed between major
  versions; the `.txt` extension for `--to script` is version-specific and should
  be re-measured rather than assumed.
- **The comparison is on stdout, not on plotted figures.** Plot output is not
  compared here; a figure's bytes depend on the font stack and the backend, so a
  byte comparison is usually the wrong test.
- **Magics are not fully un-portable.** Some have script equivalents
  (`%matplotlib inline` is unnecessary in a script that never displays;
  `%timeit` becomes `timeit`), so the fix is a rewrite, not a deletion.
- **No execution times are quoted.** Converting a notebook is fast on this
  machine and would not be on another; the lesson quotes line counts, byte sizes
  and exit codes instead.

## 9. Python demonstration

`code/notebooks_to_scripts_demo.py` runs in six parts:

| Part | Measures | Key measured output |
|---|---|---|
| 1 | Executes the notebook | `slab correction = 1.119637e-04 m/s^2`, `11.196372 mGal` |
| 2 | Exports and counts | 29 lines vs 16, `# In[` 3 vs 0, output text absent |
| 3 | Runs the export | exit `1`, `NameError: name 'get_ipython' is not defined` |
| 4 | Percent format | 3 markers, exit `0`, stdout matches exactly |
| 5 | The CLI | `--to script` → `.txt`, `--to python` → `.py`, `--to html` → 280811 bytes |
| 6 | Regression testing | stdout differs under a changed density; ratio `1.086142` |

The script writes its notebooks, scripts and HTML into a scratch directory under
`code/` and deletes the directory before it exits, so running it leaves no
artefacts in the repository.

## 10. Exercises

Solutions are in
[`exercises/04-notebooks-to-scripts-solutions.md`](./exercises/04-notebooks-to-scripts-solutions.md).

### ★ Foundational

**★1.** List three things a `PythonExporter` conversion preserves and three it
discards.

**★2.** Why is the exported script's stdout supposed to match the notebook's
stored output? State the condition that has to hold for it to do so.

**★3.** A converted script starts with
`get_ipython().run_line_magic('matplotlib', 'inline')`. Explain the error it
raises and give two ways to fix the notebook.

**★4.** Which `nbconvert --to` target produces a file that a non-Python reader
can open, and what does it contain that the script does not?

### ★★ Applied

**★★5.** Convert a notebook of your own to a script with both
`PythonExporter(exclude_input_prompt=True)` and the CLI, and report the line
counts of the two outputs. Explain any difference.

**★★6.** Take a notebook with a shell escape (`!ls`) and a timing magic. Export
it, run the export, and report the exit code and the first error line. Then fix
it properly and report the new exit code.

**★★7.** Convert a notebook containing a plot into (a) HTML and (b) a script, and
report the size of each. Explain why the script is smaller and what the script
reader loses.

**★★8.** Write a `pytest` test that asserts the Bouguer slab value to a relative
tolerance of 1e-12, and a second test that asserts the *ratio* of two densities
equals the ratio of the two corrections. Report the tolerance you had to use and
why it is not zero.

### ★★★ Research-oriented

**★★★9.** Design a conversion pipeline and measure it. For a notebook of your
choice, produce: a percent-format module, a `pytest` module that imports it, and
an HTML report — all generated by one script. Report the number of steps, the
files produced with their sizes, and which step needed hand editing. Then state
what would break if the notebook were edited by someone who did not know about
the pipeline.

**★★★10.** Measure the fidelity of a round trip. Take a notebook, export it to a
script, and convert the script back into a notebook with
`nbformat.v4.new_notebook` splitting on `# %%` markers. Compare the two notebooks
cell by cell: report the number of cells, the number whose source is identical,
and the cells that differ with the reason. Conclude with a statement of what the
round trip can and cannot preserve.

## 11. Common mistakes

1. **Committing only the converted script.** The outputs are gone; a reader
   cannot tell what the analysis said.
2. **Assuming the exported script runs.** Any magic or shell escape breaks it, and
   the failure is at import.
3. **Using the export as a test.** It is a rerun; it has no assertions.
4. **Globbing `*.py` after `--to script`.** It wrote `.txt`.
5. **Editing the generated script.** The next export overwrites the edit.
6. **Treating a diff of stdout as a correctness test.** It detects change, not
   error.
7. **Forgetting that markdown becomes comments.** Long derivations become long
   comment blocks; keep the notebook.

## 12. Real-world applications

- **Submitting a paper's analysis.** Ship the notebook (readable), the
  percent-format module (testable) and the HTML report (readable by anyone) — all
  three from one source.
- **A processing pipeline.** The exploratory notebook becomes a module with
  functions; the notebook remains as documentation of how the functions were
  found.
- **CI for a geophysical workflow.** `jupyter nbconvert --execute` with errors
  fatal runs the notebook in CI; a stdout diff flags unintended changes; a pytest
  module checks the intended ones.
- **A consulting deliverable.** The client wants a report, not a repository.
  Convert to HTML, include the figure at 300 dpi, and keep the module under
  version control for the next phase.
- **Teaching.** Students receive a percent-format module that runs as a script and
  opens as a notebook, so the same artefact serves the lecture and the exercise.

## 13. Further reading

- **Jupyter documentation** (jupyter.org). Level: beginner. The notebook format
  and the export options discussed here.
- **nbconvert documentation.** Level: intermediate. Exporter classes, template
  configuration and the `--execute` flag, which is the CI-relevant option.
- **Pérez, F. & Granger, B. E. (2007). IPython: a system for interactive
  scientific computing. *Computing in Science & Engineering*, 9(3), 21–29.**
  Level: intermediate. The original case for the interactive shell and the
  notebook, including an early statement of the reproducibility problem.
- **Rule, A., Tabard, A. & Hollan, J. D. (2018). Exploration and explanation in
  computational notebooks. *CHI 2018*.** Level: advanced. Why the exploratory
  notebook and the report have different requirements — the argument of this
  lesson, made empirically.
- **The `pytest` documentation** (docs.pytest.org). Level: intermediate. The
  assertion machinery for the correctness tests of Section 7.2.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
- [02 Markdown and LaTeX in Notebooks](./02-markdown-and-latex.md) — where the
  prose goes in each export format.
- [03 Making Notebooks Reproducible](./03-reproducible-notebooks.md) — the
  precondition for executing a notebook as a test.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — pytest, packaging and CI.
- [03-01-06 Files, Paths and Input/Output](../01-python-fundamentals/06-files-and-io.md)
  — the file handling a converted script usually needs.

## 15. Self-assessment checklist

- [ ] I can list what a script export preserves and discards. (§3)
- [ ] I can predict which notebook features break a converted script. (§5)
- [ ] I can explain the `.txt` versus `.py` difference on the command line. (§5.1)
- [ ] I can write the percent format by hand. (§6)
- [ ] I can make a converted script's stdout match the notebook's. (§5)
- [ ] I can state the difference between a regression test and a correctness
      test. (§7.2)
- [ ] I can produce a notebook, a module and an HTML report from one source. (§12)
