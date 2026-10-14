# Exercises — 22-02-04 Notebooks vs Pipelines: Choosing the Right Tool

Attempt these before reading the
[solutions](./04-notebooks-vs-pipelines-solutions.md). The lesson is
[04 Notebooks vs Pipelines](../04-notebooks-vs-pipelines.md). All counts refer to
the **SYNTHETIC** cell graphs of `code/notebooks_vs_pipelines_demo.py` (14 cells,
20 dependencies, 913 584 valid orders out of 87 178 291 200).

## ★ Foundational

**★1.** Define a **linear extension** of a dependency graph in one sentence, and
compute the number of valid execution orders for a four-cell notebook in which cell
3 depends on cells 1 and 2, and cell 4 depends on cell 3.

**★2.** The demonstration reports $n! = 87\,178\,291\,200$ and $L = 913\,584$ for
its 14-cell graph. (a) Compute $L/n!$ and state it in words. (b) State what the
ratio would be for a strictly sequential notebook of 14 cells, and for a notebook of
14 mutually independent cells.

**★3.** The demonstration measures a mean of 2.8 and a maximum of 7 stale
downstream cells after editing one cell of 14, and three cells with no downstream
dependents. (a) State why a stale cell is invisible. (b) State what the three cells
with no dependents tell you about where to put cosmetic edits.

## ★★ Applied

**★★4.** For the eight-cell notebook of the lesson's mastery checkpoint — 4 uses
{1, 2, 3}; 5 uses {2, 4}; 6 uses {2, 4}; 7 uses {6}; 8 uses {7} — count the valid
execution orders by hand, explaining the structure of the count. Then compute the
probability that a random order is valid.

**★★5.** Convert this notebook sequence into rules: cell 1 loads `raw.csv`; cell 2
sets a filter corner from a parameter file; cell 3 applies the filter and saves
`filtered.npz`; cell 4 plots the spectrum to `spectrum.png`. Write the rule set with
declared inputs and outputs, and state which of the four cells becomes which rule
and which becomes a parameter.

**★★6.** A notebook takes 20 s to re-run from an edited intermediate cell and 14 min
to restart and run all. A pipeline re-runs one rule in 3 min but needs a full graph
restart to change a parameter (11 min end to end).

(a) Compute the number of exploration edits per hour the notebook supports and the
number the pipeline supports. (b) Compute the wall time to produce the final figure
from scratch with each. (c) State the decision rule this implies.

## ★★★ Research-oriented

**★★★7.** Design the restart-and-run-all check as a continuous-integration job for
a group's notebooks: state what is executed, on what input, what is compared, the
tolerance, and how you would handle notebooks that legitimately take too long to run
in CI. State what the check cannot detect.

**★★★8.** The demonstration's graph counts only definition-use dependencies.
Specify a measurement of the *hidden* state of a real notebook — the state that
survives a cell edit without appearing in the cell graph — and state the two
observables that would reveal it. Say what the measurement cannot tell you.

**★★★9.** Write a group policy for when a notebook may be the published artefact.
State the criteria, the checks that enforce them, the cases the policy must exclude,
and the failure the policy prevents that a "pipelines only" rule would not.
