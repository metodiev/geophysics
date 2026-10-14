# Solutions — 03-06-04 Converting Notebooks to Scripts, Tests and Reports

> **Read this after attempting the exercises.** All values are the demonstration's
> actual output, produced with nbconvert 7.17.2, nbformat 5.11.1 and Python 3.14.4.

---

## ★1 — Preserved and discarded

Preserved: the code of every code cell (exactly), the markdown cell contents (as
`#` comments), and the cell boundaries (as `# In[ ]:` markers). Measured:
`'# In[' markers in default export: 3` for three code cells.

Discarded: every output (measured: the printed value appears in the export three
times, all of them as source text, never as a result), the rendering of markdown,
the cell metadata, and the figure images.

---

## ★2 — Why stdout should match

Because the script re-executes the same code on the same inputs, so its printed
output should be the notebook's stored output. Conditions: (i) the notebook was
deterministic, (ii) no magics or shell escapes survive into the script, and
(iii) the environment matches. Measured, after deleting the one magic line:
`script stdout matches the notebook stdout exactly: True`.

---

## ★3 — The magic error

`get_ipython` is defined by the IPython kernel, not by a plain interpreter, so the
script raises `NameError: name 'get_ipython' is not defined` with exit code 1
before printing anything (`stdout produced before the failure: ''`).

Two fixes: (1) remove the magic and set the backend explicitly where a script needs
one — for a headless conversion, `matplotlib.use("Agg")`; (2) keep the magic but
convert with a tool that understands it, which nbconvert does not.

---

## ★4 — The report target

`nbconvert --to html`. Measured: 280811 bytes, containing the notebook's stdout
(`contains the notebook stdout line 'slab correction = 1.119637e-04 m/s^2':
True`) and the LaTeX source verbatim (`True`), with zero server-side math
wrappers. The script contains neither the output nor the rendered mathematics.

---

## ★5 — The percent format

Plain Python with `# %%` comment lines marking cell boundaries. It runs because
every marker is a comment: the interpreter sees ordinary statements. Measured:
`'# %%' cell markers written: 3`, `exit code: 0`, and
`stdout matches the notebook: True`.

---

## ★6 — Two exports, two line counts

Measured for the demonstration's four-cell notebook:

```
  default export:      29 lines, 414 characters
  prompts stripped:    16 lines, 296 characters
  '# In[' markers in default export: 3
  '# In[' markers in stripped export: 0
```

The difference is the prompt markers, the blank lines separating the cells, and the
markdown comments removed by `exclude_markdown=True`. The CLI's `--to python`
produces the same content as the default exporter; note that
`--to script` writes `.txt` instead.

---

## ★7 — Shell escape and magic

The exported script contains `get_ipython().system('ls -la')` and
`get_ipython().run_line_magic('matplotlib', 'inline')`. Running it gives exit code
1 and `NameError: name 'get_ipython' is not defined`. Fixes: replace `!ls` with
`subprocess.run(["ls", "-la"])` or `os.listdir(".")`, and delete the magic (or
call `matplotlib.use("Agg")` if the script also draws). The new exit code should
be 0.

---

## ★8 — HTML against script

Measured for the demonstration: HTML 280811 bytes, script 414 characters. The
script is three orders of magnitude smaller because it carries no outputs and no
embedded figure. What its reader loses: the numbers, the figure, and the ability
to read it without running it — which is exactly what the HTML preserves.

---

## ★9 — Two tests, two tolerances

```python
import numpy as np

def test_slab_value():
    slab = 2 * np.pi * 6.674e-11 * 2670.0 * 100.0
    expected = 1.119637e-4
    assert abs(slab - expected) / expected < 1e-6

def test_slab_ratio():
    g1 = 2 * np.pi * 6.674e-11 * 2670.0 * 100.0
    g2 = 2 * np.pi * 6.674e-11 * 2900.0 * 100.0
    assert abs(g2 / g1 - 2900.0 / 2670.0) < 1e-12
```

The tolerance is not zero because both sides are floating-point computations in
different orders. Measured on the demonstration's two densities:
`slab correction = 1.119637e-04 m/s^2` and `1.216085e-04 m/s^2`, with a ratio of
`1.086142` against the exact `2900/2670 = 1.086142`. A tolerance of 1e-12 relative
is comfortable; 1e-16 would fail for arithmetic-ordering reasons and not for
scientific ones.

---

## ★10 — Making the diff blind

Change both the notebook and the "expected" output together — for example, define
the slab correction as $4\pi G\rho h$ (a factor of two out) and update the stored
outputs. The diff then sees no change, because it compares the version under test
with the recorded baseline. **The diff is a regression test, not a correctness
test**: it detects a change and cannot detect an error that was present when the
baseline was recorded.

---

## ★11 — A conversion pipeline

A defensible pipeline and what it typically needs:

| Step | Produces | Hand editing needed |
|---|---|---|
| 1. execute the notebook | `.ipynb` with fresh outputs | no |
| 2. export percent-format module | `.py` with `# %%` | yes — magics must be rewritten |
| 3. split functions out | a library module | yes — by definition |
| 4. write assertions | `test_*.py` | yes — tolerances come from measurement |
| 5. export HTML | `.html` report | no |

What breaks when someone edits the notebook without knowing the pipeline: the
percent-format module is regenerated and their hand edits vanish; a rewritten
magic reappears; an assertion that encodes an old constant fails. The mitigation is
that the pipeline is a script in the repository, run by CI, and that the generated
files carry a header saying they are generated.

---

## ★12 — Round-trip fidelity

Measured facts to expect: the number of cells should match if every code cell is
separated by a `# %%` marker (the demonstration wrote exactly 3 markers for 3 code
cells). What will *not* match: markdown cells (they became comments, and splitting
on `# %%` makes them code cells or loses them), outputs (the script has none), cell
metadata, and any cell whose first line is a comment that looks like a marker.

So the round trip preserves code structure and loses everything else. **That is
the honest summary: a script export is a lossy projection of the notebook onto its
code.** Keep the notebook as the source of record.
