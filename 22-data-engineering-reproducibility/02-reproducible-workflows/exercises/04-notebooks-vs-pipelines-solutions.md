# Solutions — 22-02-04 Notebooks vs Pipelines: Choosing the Right Tool

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [04 Notebooks vs Pipelines](../04-notebooks-vs-pipelines.md).

---

## ★1 — Linear extensions, and a four-cell count

A **linear extension** of a dependency graph is a permutation of its cells in which
every cell appears after all of its dependencies.

For cells 1, 2, 3, 4 with 3 depending on $\{1,2\}$ and 4 depending on $\{3\}$:
cells 1 and 2 can be in either order (2 ways), then 3, then 4 →

$$L = 2 \times 1 \times 1 = 2\ \text{valid orders}.$$

(Out of $4! = 24$ permutations, so the fraction is $2/24 = 0.083$.)

## ★2 — Interpreting the 14-cell ratio

(a) $L/n! = 913584 / 87178291200 = 1.048 \times 10^{-5}$, i.e. **about one order in
95 000 is valid**. The notebook's saved outputs correspond to exactly one of the
913 584 valid orders.

(b) A strictly sequential notebook (every cell depends on the previous one) has
exactly **one** valid order: $L/n! = 1/87178291200 = 1.147 \times 10^{-11}$. A
notebook of 14 mutually independent cells has **all** orders valid:
$L/n! = 1$. The demonstration's graph sits between the two, near the sequential end
because 20 dependencies over 14 cells is a dense-looking constraint set for this
small $n$.

## ★3 — Stale output

(a) A cell's stored output is a value, not a proof of currency: the notebook stores
the output object and its execution count, and neither is invalidated when an
upstream cell is edited. Nothing in the display distinguishes a fresh value from one
computed with a superseded input, so the stale value is read as current.

(b) A cell with no downstream dependents can be edited with **no** invalidation
consequence elsewhere: in the demonstration three cells are terminal, so cosmetic
and reporting edits belong there. Conversely, an edit to a cell that everything
depends on is the expensive one, and that is where the discipline (or a pipeline) is
needed.

## ★★4 — Counting the checkpoint notebook by hand

Constraints: $4$ after $\{1,2,3\}$; $5$ after $\{2,4\}$; $6$ after $\{2,4\}$;
$7$ after $\{6\}$; $8$ after $\{7\}$.

**Structure.** At the start only cells 1, 2, 3 are available, and no constraint
orders them relative to each other, so the prefix is any of $3! = 6$ orders of
$\{1,2,3\}$. Next comes cell 4 (nothing else is available: 5 and 6 both need 4,
and 7, 8 need 6). After cell 4, the remaining cells are $5, 6, 7, 8$ with the
constraint $6 \prec 7 \prec 8$; cell 5 depends only on $\{2,4\}$, both already
executed, so **cell 5 may be placed anywhere** in that sequence of four slots.

Total:

$$L = 6 \times 4 = 24\ \text{valid orders}, \qquad
P = \frac{24}{40320} = 5.952 \times 10^{-4}.$$

The structure that makes this countable: a strongly ordered backbone
($4 \prec 6 \prec 7 \prec 8$) with an unordered prefix and one free cell. Inserting
one extra independent cell into an ordered chain multiplies the count by the number
of slots, not by a factorial — a useful intuition for real notebooks, where a few
"parameter" cells at the top are what generate most of the ordering freedom.

## ★★5 — Converting the sequence into rules

| Cell | Becomes |
|---|---|
| 1 (`load raw.csv`) | the `input:` of the `filter` rule — a data file, not a rule, unless loading involves work |
| 2 (filter corner from a parameter file) | a **parameter** declared as an input file (so the rule invalidates when it changes) |
| 3 (apply filter, save `filtered.npz`) | the `filter` rule |
| 4 (plot to `spectrum.png`) | the `plot` rule |

```python
rule filter:
    input:
        raw="data/raw.csv",
        params="config/filter.yml"
    output:
        "results/filtered.npz"
    script:
        "scripts/filter.py"

rule plot:
    input:
        "results/filtered.npz"
    output:
        "figures/spectrum.png"
    script:
        "scripts/plot_spectrum.py"
```

The decision that matters is cell 2: if the corner frequency is read inside the
script from an undeclared file, the rule will not re-run when the parameter
changes. Declaring it as an input (and reading it in a `params` block) is what makes
the pipeline's invalidation correct.

## ★★6 — Notebook versus pipeline economics

(a) **Exploration edits per hour.** Notebook: 20 s per edit → $3600/20 = 180$ edits
per hour. Pipeline: 3 min per rule re-run → $3600/180 = 20$ edits per hour. The
notebook is **9× faster** for the edit–look–edit loop.

(b) **Time to a complete figure from scratch.** Notebook: 14 min restart-and-run-all
(assuming it passes). Pipeline: 11 min end to end. The pipeline is faster for a full
run because it can schedule independent rules in parallel and skips nothing it needs.

(c) **Decision rule.** Use the notebook while the *ratio* of edits to full runs is
high — the notebook's advantage is the $20\times$ lower iteration cost, and it
disappears as soon as a single edit starts requiring a full re-run (at which point
both tools cost the same and only the pipeline's ordering guarantees remain). Publish
from the pipeline, and keep the notebook for exploration with the restart-and-run-all
test as the exit criterion.

The arithmetic generalises: the crossover happens when the notebook's edits per hour
fall to the pipeline's, i.e. when an edit invalidates so much of the notebook that
its re-run approaches the full 14 min. That is the same caching question as
[22-02-03](../03-workflow-managers.md) §6.

## ★★★7 — The restart-and-run-all CI job

**What is executed.** Every notebook in the repository that is declared an artefact
(not the scratch ones, which should live outside version control), run from a clean
kernel with `nbconvert --execute`, under the pinned environment, on a **reduced
input**: a small subset of the data (for example, three stations instead of three
hundred) selected by the same configuration mechanism the notebook uses for the full
run. The reduction is what makes the check affordable; the notebook must be
parameterised so the subset is a configuration value, not an edit.

**What is compared.** For each notebook, the *values* it asserts, not its rendered
outputs: the check should run the notebook's own assertion cells (or a companion
test module) against reference values with an explicit tolerance. Comparing rendered
PNGs or stored outputs is brittle and measures formatting; comparing the headline
numbers with a tolerant assertion measures the computation. Record the reference
values with their tolerance and their provenance.

**Tolerance.** Use a relative tolerance sized to the numerical effect measured in
[22-02-06](../06-containers-reproducibility.md)
(a relative difference of $1.04 \times 10^{-7}$ between float32 and float64
accumulation of a million samples) — e.g. `rtol=1e-6` for float64 pipelines — and
document the reason for the value rather than choosing a round number.

**Long-running notebooks.** Split the check: run the reduced-input notebook on every
commit, and the full-input notebook on a nightly schedule. Both must pass before a
release. Notebooks that legitimately cannot run in CI at all (hardware, licensed
data) must be declared as such and covered by a manual checklist in the release
notes.

**What the check cannot detect.** A dependency on state that is *also* absent in the
reference environment — a shared network drive, a Python global set by an earlier
notebook, the analyst's local configuration file. If the CI environment happens to
have the same hidden input, the check passes for the same wrong reason the notebook
did. It also cannot detect that the analysis is scientifically wrong.

## ★★★8 — Measuring hidden notebook state

**What "hidden state" is.** State that affects a cell's result without appearing in
the definition-use graph: files read and written by cells, module-level globals set
by a `%run` or an imported helper, mutable objects mutated in place, environment
variables, the working directory, and random-number generator state.

**Specification.** Instrument a kernel with an audit hook (`sys.addaudithook` for
`open`, `os.chdir`, `import`) plus a tracer that records every name a cell reads and
where it was bound, then replay the notebook three ways: (i) in the recorded order,
(ii) restart-and-run-all, and (iii) in the recorded order with the file system
restored to its initial state. Compare the final value of every name and the hash of
every produced file across the three.

**Two observables that reveal hidden state.**

1. **Divergence between (i) and (ii)**: a value that differs between the recorded
   order and restart-and-run-all is caused by state, not by the code.
2. **File writes not matched by reads in the graph** (and vice versa): an audit-hook
   trace showing a cell reading a path no cell declared, or writing a path another
   cell later reads, is hidden coupling — the notebook's undeclared input.

**What the measurement cannot tell you.** Whether the *result* is correct: hidden
state explains why a notebook is fragile, not whether the number is right. It also
cannot enumerate the hidden inputs the analyst's machine has but the CI machine does
not — those are discovered only by running in a second environment.

## ★★★9 — When a notebook may be the published artefact

**Criteria (all must hold).**

1. The notebook passes restart-and-run-all on the declared input in CI, with its
   assertions checked against reference values within a stated tolerance.
2. Every input is declared and versioned: data by identifier, parameters in a
   declared file, environment pinned (levels 3–4 of
   [22-02-02](../02-environment-pinning.md)).
3. It contains no cell whose output is required and is unreachable from a fresh run
   (no "run this one twice" instructions).
4. Its narrative order is the content — a tutorial, a review demonstration, or an
   analysis whose reasoning is the deliverable — rather than an artefact of when
   cells were written.

**Checks that enforce them.** The CI job of ★★★7; an input-declaration check (audit
hook or static scan for `open()` calls with undeclared paths); a reproducibility
manifest stored with the notebook recording environment and data identifiers; and a
review step that inspects execution counts for non-monotone order.

**Excluded cases.** Notebooks with interactive widgets or manual inputs; notebooks
whose runtime exceeds the CI budget without a reduced-input mode; notebooks that
depend on licensed or restricted data that cannot be shipped, unless a reduced
synthetic input is provided; and notebooks that require GPU or cluster resources not
available in CI — those go through the pipeline path.

**The failure the policy prevents that "pipelines only" would not.** The exchange
above shows the notebook's $9\times$ faster iteration and its ability to carry the
reasoning alongside the computation. A "pipelines only" rule removes both and pushes
analysts to keep their real exploration in untracked files, which is strictly worse
for reproducibility: unversioned scratch work is invisible, while a checked notebook
that fails the policy is at least reviewable. The policy's purpose is to make the
notebook's costs explicit and enforced, not to remove the tool.
