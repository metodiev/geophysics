# Exercises — 03-06-01 Notebook Workflow, Cells, Kernels and Execution Order

> **Attempt these with the notebook closed first.** Solutions, with the measured
> numbers, are in
> [`01-notebook-workflow-solutions.md`](./01-notebook-workflow-solutions.md).

Every exercise below can be answered with `nbformat` and `nbclient` — the two
libraries the Jupyter interface itself uses. Nothing here needs a browser.

---

## ★ Foundational

**★1.** A notebook has five code cells, all executed in file order, then the
second is executed twice more. Write down the resulting `execution_count` list.

**★2.** State, for each item, whether it survives a save, a kernel restart, or
neither: (a) cell source, (b) cell outputs, (c) the value of a variable, (d)
`matplotlib`'s current figure, (e) the file the kernel has open.

**★3.** Why does a markdown cell never receive an `execution_count`?

**★4.** Name the two objects a notebook involves that are not the `.ipynb` file,
and say which one "Restart and Run All" destroys.

**★5.** In the demonstration, the saved notebook was 2623 bytes. State two things
that are in those bytes and two things that are not.

---

## ★★ Applied

**★★6.** Three code cells: cell 1 writes `a`, cell 2 writes `b` and reads `a`,
cell 3 reads `b`. How many of the 6 execution orders are legal? Compute it by hand
and then by brute force with `itertools.permutations`.

**★★7.** A colleague sends a notebook with counts `[1, 2, 5, 3, 4]`. Give two
distinct histories that could produce those counts, and explain why the stored
outputs cannot all come from one kernel state.

**★★8.** Construct a three-cell notebook in which *every* order produces
identical outputs; then one in which every order except the file order produces a
wrong number with no exception. Run both with `nbclient` and report the measured
outputs.

**★★9.** The demonstration found that re-running a cell that had failed replaced
its traceback with a successful output, leaving `[]` error outputs. Explain why
the file format makes this unavoidable, and describe one workflow that preserves
the evidence.

**★★10.** Write a script that takes a `.ipynb` path and prints, for each code
cell, its index, `execution_count` and the first line of its output. Run it on a
notebook of your own and report the output. Then add a check that reports whether
the counts are monotonic.

---

## ★★★ Research-oriented

**★★★11.** Generalise the count of Section 6 of the lesson. Compute the number of
legal execution orders for a notebook organised as $k$ independent chains of
length $m$ each ($n = km$), give the formula, and verify it by brute force for
$n \le 7$. State what the result implies about designing a notebook from
independent sections.

**★★★12.** Measure the frequency of out-of-order execution in practice. Write a
script that inspects a sample of `.ipynb` files you already have (your own, or a
colleague's with permission), extracts `execution_count` sequences, and reports
the fraction that are non-monotonic and the fraction that are not `1..n`. Report
your measured fractions and sample size, and state explicitly why your sample may
not generalise. If you have no sample, say so and stop; do not invent numbers.

**★★★13.** Quantify the cost of a stale output. Build a five-cell notebook whose
third cell sets a parameter and whose fifth computes a result from it; execute the
file order, then change the parameter and re-run only cell 3. Report the two
numbers the notebook now presents side by side (the stored figure caption and the
freshly computed value), the `execution_count` sequence, and the size of the
discrepancy as a percentage.
