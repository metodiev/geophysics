# Solutions — 03-06-01 Notebook Workflow, Cells, Kernels and Execution Order

> **Read this after attempting the exercises.** Values attributed to the
> demonstration are its actual output, produced with nbformat 5.11.1,
> nbclient 0.11.0, jupyter_client 8.10.0 and Python 3.14.4 in this repository's
> virtual environment.

---

## ★1 — Counts after two extra executions

The five cells produce counts `[1, 2, 3, 4, 5]`, then the second cell executed
twice more becomes 6 and then 7:

```
[1, 7, 3, 4, 5]
```

The order within the list is file order; the values are execution order. The
demonstration's equivalent experiment on four code cells printed
`after re-running code cell 1 (same kernel): execution_count = [5, 2, 3, 4]`, and
`cells whose count is below the highest count: 3 of 4`.

---

## ★2 — What survives what

| Item | Save | Restart |
|---|---|---|
| (a) cell source | survives (it *is* the save) | survives |
| (b) cell outputs | survives | survives (they are in the file) |
| (c) a variable's value | lost | lost |
| (d) `matplotlib`'s current figure | lost | lost |
| (e) the file the kernel has open | lost | lost (the handle is closed) |

Only (a) and (b) are properties of the file. The distinction that matters: a
restart does **not** erase stored outputs — it makes them unverifiable.

---

## ★3 — Why markdown cells have no count

`execution_count` is assigned by the kernel when it executes a code cell. A
markdown cell is never sent to the kernel; it is rendered by the front end. The
demonstration measured this directly: `run(nb, [<markdown index>])` left the
counts at `[1, 2, 3, 4]`, unchanged.

---

## ★4 — The two other objects

The **kernel process** (an ordinary interpreter started with
`python -m ipykernel_launcher`) and the **browser view**. Restart and Run All
destroys the kernel process, discarding every variable, and re-executes the file
in order in a new one.

The kernelspec measured on this machine:

```
argv = ['python', '-m', 'ipykernel_launcher', '-f', '{connection_file}']
resource_dir = .../geophysics/.venv/share/jupyter/kernels/python3
```

---

## ★5 — What is in 2623 bytes

In: every cell's source, every cell's outputs, and the `execution_count` of each
code cell (measured: `execution_count persisted in the file: [1, 2, 3, 4]`).

Not in: the variables, the libraries' state, the kernel, the data files the code
read, and the package versions. The demonstration reports `nbformat 4.5` for the
file format and `language_info populated by the run: not populated` — the
interpreter version is not recorded unless something writes it.

---

## ★6 — Legal orders for a three-cell chain

Cells: 1 writes `a`; 2 writes `b`, reads `a`; 3 reads `b`. The dependencies are
$1 \prec 2$ and $2 \prec 3$, a chain of three, so exactly **one** of the six
orders is legal: `(1, 2, 3)`.

Brute force:

```python
import itertools
legal = [o for o in itertools.permutations(range(1, 4))
         if o.index(1) < o.index(2) < o.index(3)]
print(len(legal), legal)      # 1 [(1, 2, 3)]
```

Checking the arithmetic against the lesson's four-cell table: a chain of length 4
gave `legal orders 1 of 24 = 0.0417`, and a single dependency gave
`12 of 24 = 0.5000`.

---

## ★7 — Two histories for `[1, 2, 5, 3, 4]`

- **History A:** the linear run gave `[1, 2, 3, 4, 5]`; the third cell was then
  clicked twice, raising its count to 5 and re-running it *before* cells 4 and 5
  had ever been run in a state that included the third cell's change.
- **History B:** the notebook was executed twice: the first execution produced
  `[1, 2, 3, 4, 5]` in one kernel and the second (say after a partial re-run)
  assigned 5 to cell 3 while 4 and 5 kept their earlier counts.

The stored outputs cannot all come from one state because cell 3's output was
produced *after* cells 4 and 5's outputs but sits before them in the file — so
whatever cell 3 wrote to the kernel's state was not present when cells 4 and 5
ran. Any downstream cell that reads what cell 3 writes is therefore displaying a
result computed from an older value.

---

## ★8 — Building the two notebooks

Every order gives identical outputs when the cells share nothing:

```python
cells = [code_cell("a = 1"), code_cell("b = 2"), code_cell("print(a + b)")]
```

This one differs between orders, with no exception in any order:

```python
cells = [code_cell("dt = 0.01"),
         code_cell("print(f'{9.81 * dt:.6f}')"),
         code_cell("dt = 0.001")]
```

Measured, using the demonstration's `run()` helper with one kernel per plan:

```
  order [0, 1, 2] -> 0.098100 m/s
  order [0, 2, 1] -> 0.009810 m/s
  ratio between the two answers: 10.0
```

Both notebooks are the same *file* in every cell's source; only the order and the
3-number count sequence differ. This is the strongest available demonstration
that a notebook's stored numbers are a property of its execution history.

---

## ★9 — Why the traceback is destroyed

An output is a *field of the cell*, not an append-only log. When a cell is
executed, the client clears `cell.outputs` and writes the new ones; there is no
history field in the notebook format. Measured:

```
  clicking cell 1 on its own -> "NameError: name 'rho' is not defined"
  error outputs stored: ['NameError']
  then cell 0 followed by cell 1 -> 'rho = 2.670 g cm-3'
  error outputs left in the notebook afterwards: []
```

Workflow that preserves the evidence: run the notebook non-interactively in CI
with errors fatal (`allow_errors=False`, which is what
`jupyter nbconvert --execute` does by default), so the failure stops the run and
is recorded in the CI log rather than being overwritten by the next click.
Measured in the reproducibility demonstration:
`allow_errors=False -> raised CellExecutionError`, with
`cells with a stored output afterwards: 2 of 3 (cell 3 untested and unrecorded)`.

---

## ★10 — A cell inventory script

```python
import json, sys

raw = json.loads(open(sys.argv[1]).read())
counts = []
for index, cell in enumerate(raw["cells"]):
    if cell["cell_type"] != "code":
        continue
    counts.append(cell.get("execution_count"))
    first = ""
    for out in cell.get("outputs", []):
        if out.get("output_type") == "stream":
            first = out["text"].splitlines()[0] if out["text"] else ""
        elif out.get("output_type") == "error":
            first = f"{out['ename']}: {out['evalue']}"
        if first:
            break
    print(f"cell {index:>3} count={cell.get('execution_count')!s:>6}  {first}")
print("counts:", counts)
print("monotonic:", counts == sorted(c for c in counts if c is not None))
```

On the demonstration's saved notebook the counts line reads `[1, 2, 3, 4]` after
the linear run and `[5, 2, 3, 4]` after the extra click, so `monotonic` is `True`
then `False`. **Monotonic counts are weak evidence of a linear run; non-monotonic
counts are strong evidence against one.**

---

## ★11 — $k$ chains of length $m$

A chain of length $m$ has one legal internal order; $k$ independent chains can be
interleaved in any order that preserves each chain's internal sequence. The number
of such interleavings is the multinomial coefficient

$$N(k \text{ chains of } m) = \frac{(km)!}{(m!)^{k}}.$$

Check against the lesson's brute-force table: $k=1, m=4$ gives $24/24 = 1$
(a single chain); $k=4, m=1$ gives $24/1 = 24$ (independent cells); $k=2, m=2$
gives $24/4 = 6$. Brute force for $n \le 7$ reproduces these.

The design implication is stark: splitting a notebook into $k$ independent
sections of $m$ cells increases the number of legal orders from 1 (a single chain)
to $(km)!/(m!)^k$, an enormous number. **Independence is what makes a notebook
order-robust; a chain of dependencies is what makes it fragile.**

---

## ★12 — Nothing to report

This exercise cannot be answered without a sample of real notebooks. If you have
one, report the measured fractions and the sample size, and state the selection
bias (your own notebooks are not a random sample of the field). If you do not,
stop — the lesson deliberately does not supply a number here, because inventing
one would be worse than leaving the question open.

---

## ★13 — The cost of a stale output

A five-cell notebook: cell 1 loads, cell 2 sets `rho = 2670`, cell 3 computes the
slab correction $2\pi G \rho h$ with $h = 100$ m, cell 4 makes a figure, cell 5
prints the correction. Execute in file order, then edit cell 2 to `rho = 2400` and
re-run only cell 2.

The notebook now shows:

- cell 3's stored output: the correction for 2670 kg/m³;
- cell 5's stored output: the same number again;
- cell 2's fresh output: a density that disagrees with both;
- counts `[1, 6, 3, 4, 5]`, which is the tell.

The discrepancy is the ratio of the densities,
$2670/2400 = 1.1125$, i.e. **11.25 %** — the correction scales linearly in
$\rho$, as $g_{\text{slab}} = 2\pi G\rho h$ requires. The measured values from
[03-06-04's demonstration](../04-notebooks-to-scripts.md) are
$1.119637\times10^{-4}$ m/s² at 2670 kg/m³ and $1.216085\times10^{-4}$ m/s² at
2900 kg/m³, a ratio of 1.086142 for a density ratio of 1.086142.
