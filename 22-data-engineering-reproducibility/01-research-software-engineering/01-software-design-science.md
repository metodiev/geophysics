---
id: 22-01-01
title: "Designing Software for Scientific Research"
level: advanced
prereqs: ["03-01-08", "03-13-04"]
estimated_minutes: 50
tags: [software-engineering, design, coupling, maintenance, research-software]
---

# Designing Software for Scientific Research

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** research software from product software, and **name** the four
   properties that change the design rules.
2. **Define** cohesion, coupling, fan-in, fan-out and instability, and **compute**
   each on a dependency graph.
3. **Derive** the size of a change's blast radius from the transitive closure of
   the dependency graph, and **measure** the amplification over the direct one.
4. **Design** a module boundary that separates computation from input/output and
   configuration, so that the computation is testable without files.
5. **Predict**, from a stated defect model, how coupling and size change the
   defect density of a module, and **state** what the model does not establish.
6. **Diagnose** a design smell from a metric and a code sample, and **propose**
   the smallest refactoring that removes it.

Research software is written to produce a scientific result, and the code is part
of the method by which that result was obtained. It is therefore an instrument:
it must be trusted, cited, re-run and modified by people who did not write it.
This lesson gives the vocabulary and the measurements that make design decisions
about such code discussable instead of personal.

All model, metric and defect numbers in this lesson are **SYNTHETIC**. They are
printed by the demonstration and come from a generated module graph with chosen
parameters; none of them measures a real project.

## Prerequisites

- [03-01-08 Classes and Object-Oriented Programming](../../03-scientific-computing/01-python-fundamentals/08-classes-and-oop.md) —
  the module and class boundaries this lesson reasons about.
- [03-13-04 Code Quality: Style, Linting and Review](../../03-scientific-computing/13-testing-profiling-packaging/04-code-quality.md) —
  the mechanical half of quality; this lesson is the structural half.

## 1. Intuition: the program is part of the apparatus

A physicist does not accept a measurement from an uncalibrated instrument. A
computational geophysicist routinely accepts a number from an uncalibrated
program. The instrument analogy is not decoration: it fixes what the design has
to guarantee. An instrument must **do the intended thing**, must **say what it
did**, must **be re-runnable in a different laboratory**, and must **be
serviceable by someone other than its builder**.

Those four requirements are the design brief for research software. They are also
exactly where ad-hoc analysis scripts fail, because a script optimised for
yesterday's figure has no obligations to tomorrow's reader.

## 2. What is different about research software

| Property | Product software | Research software | Design consequence |
|---|---|---|---|
| Correctness criterion | Specification, tests, users | Agreement with nature | Verification is empirical; benchmarks become load-bearing |
| Lifetime | Features superseded on a schedule | Frequently a decade, with one author | Prioritise readability over cleverness |
| Requirements | Fixed before coding | Discovered while coding | Design for deletion and replacement |
| Input | Well-formed requests | Ad-hoc files, instrument quirks | Push validation to a boundary |
| Environment | One controlled deployment | Every reader's laptop | Pin and declare the environment |
| Users | Trained by the product | The author, then a stranger | Optimise for the stranger |

The last row is the one that most often decides an outcome. A paper's software is
first used by its author, who holds the entire context in their head, and is
**second** used by a reader who holds none of it. Design for the second use.

## 3. The vocabulary of modular design

A module is a unit with an **interface** (what it promises) and a **body** (how
it delivers). Two quantities describe a module's relationships:

- **Fan-out** — the number of modules it depends on. High fan-out means the
  module is fragile: any dependency change can reach it.
- **Fan-in** — the number of modules that depend on it. High fan-in means the
  module is load-bearing: changing it changes many others.

From these, Martin's **instability** is

$$I = \frac{\text{fan-out}}{\text{fan-in} + \text{fan-out}} \in [0,1],$$

with $I = 0$ for a pure library that nothing should change casually and
$I = 1$ for a leaf that depends on everything and is depended on by nothing.

**Cohesion** is the internal counterpart: whether the parts of one module belong
together. A module that computes a travel time and also writes a colour map has
low cohesion whatever its coupling, and the fix is to split the two, not to
reduce the imports.

## 4. Change propagation: blast radius

Dependencies form a directed graph. The **transitive closure** of that graph
answers the operational question: if module $m$ changes, which modules can be
affected? The answer is the **blast radius** of $m$ — the number of modules that
reach it along dependency edges.

For the demonstration's synthetic package of 60 modules and 101 edges, the
measurements are:

- mean fan-out $= 1.68$, mean fan-in $= 1.68$, maximum fan-in $= 8$, and 17
  modules with no dependencies at all;
- mean direct dependencies $= 1.68$ but **mean transitive dependencies $= 4.72$**,
  an amplification of $2.80\times$;
- mean blast radius $= 4.72$ modules, largest $= 25$ modules, and two modules
  (3.3 % of the package) reach more than 20 others;
- the **median** module reaches only 2 others.

The arithmetic of the amplification is unremarkable and that is the point: a
small number of edges ($101$ out of a possible $1770$ ordered pairs, i.e. a
density of 5.7 %) produces a graph in which the average change is not local. The
median is small because the graph is sparse; the mean and the maximum are large
because a few hub modules dominate.

Fan-in predicts blast radius well on this graph: the Pearson correlation is
$0.831$. A module is dangerous in proportion to how many others import it, which
is a quantity you can count before anyone changes anything.

## 5. Coupling and defect density

Design metrics earn their place only if they connect to an outcome. The
demonstration uses an explicit, chosen defect model,

$$\text{density}_m = 0.50 + 0.30 \times \left(1 + \text{fan-out}_m +
\text{fan-in}_m\right) \quad [\text{defects per KLOC}],$$

that is, a baseline of 0.50 defects per thousand lines plus 0.30 per effective
decision, where a dependency in either direction is treated as a decision. On the
synthetic package this gives a mean of $1.81 \pm 0.58$ defects per KLOC over
19.32 KLOC, or 39.5 predicted defects in total, and it separates the graph:

- modules with blast radius above 20: mean density $2.45$ per KLOC;
- all other modules: mean density $1.79$ per KLOC;
- ratio $1.37\times$.

Read the direction, not the digits. The lesson does **not** claim that 0.30
defects per decision is a measured constant — it is a teaching parameter chosen
so the model can be evaluated at all. What the experiment establishes is the
structural fact: because defect density is monotone in coupling, the modules
that are hardest to change are also the modules predicted to contain the most
defects. The two worst properties coincide.

## 6. Design rules that follow

1. **Separate the computation from its surroundings.** A function that takes an
   array and returns an array is testable with no files, no clock and no network.
   Read the file in one place at the edge of the program and pass data inward.
2. **Make the interface narrow and explicit.** A function with four scalar
   parameters is easier to test, cite and reason about than one with a
   dictionary of options. Options belong in a configuration object at the top.
3. **Prefer pure functions to hidden state.** A result that depends on module
   state depends on the order of calls, which is precisely the failure mode of
   notebook-driven research (see
   [22-02-04 Notebooks vs Pipelines](../02-reproducible-workflows/04-notebooks-vs-pipelines.md)).
4. **Invert the dependency direction at the layer you expect to replace.** The
   forward model should not import the plotting code; the plot should import the
   model. This keeps the high fan-in node focused.
5. **Keep one representation of a physical quantity.** One function converts
   units and one module owns the convention; units in two places are a bug
   waiting for a paper deadline.
6. **Design for deletion.** Aim for a design where a component can be removed by
   deleting one directory and one import. Code that cannot be deleted is code
   that cannot be improved.

## 7. Worked example: reading a metric report

A collaborator's package reports 60 modules, 101 dependency edges, mean fan-out
1.68, mean fan-in 1.68, mean blast radius 4.72 and a maximum of 25.

1. **Is the package over-coupled?** At 5.7 % density the graph is sparse; the
   mean is not the problem.
2. **Is the maximum a problem?** The largest blast radius of 25 means one change
   can reach 42 % of the package ($25/60$). Locate that module and check its
   fan-in: given $\text{corr} = 0.831$, it is very likely the hub with fan-in 8.
3. **What is the cheapest intervention?** Not "write fewer imports" but "split
   the hub", which converts one module with fan-in 8 into two with fan-in 4 and
   reduces the worst-case radius directly.
4. **What does the report not say?** Nothing about correctness, cohesion or
   runtime. A graph metric is a prior for where to read the code, not a verdict
   on the code.

## Assumptions and regime of validity

1. **The graph is the dependency graph of imports, not of data flow.** A module
   that reads a file another module wrote is coupled through the filesystem and
   is invisible here; the true blast radius is larger.
2. **Closure is transitive and unweighted.** Any path counts once. A single
   inherited dependency that reaches everything would collapse the metric.
3. **The defect model is additive and monotone.** Real defect density is driven
   by churn, developer experience and problem difficulty as much as structure;
   the model isolates structure to make the direction of the effect visible.
4. **Package size is fixed at 60 modules.** Blast radius in absolute modules
   grows with package size, so compare fractions, never raw counts between
   packages.
5. **Metrics describe a snapshot.** Renaming, splitting and adding tests all
   change the graph; a metric report is only meaningful with a date and a commit.

## The honest summary

Design metrics cannot tell you whether code is correct, and they do not replace
reading it. They do something narrower and genuinely useful: they identify, from
pure structure, which parts of a package are expensive to change, and they
quantify why. On a sparse synthetic graph, a change reaches $2.80\times$ more
modules transitively than directly, and the mean blast radius is 4.72 modules
with a maximum of 25. Coupling predicts where the defects are expected to
concentrate — $1.37\times$ higher modelled density on the most-reached modules —
so the same modules are both expensive to fix and likely to need fixing. The
design rules in §6 are the standard response to that coincidence, and none of
them requires a tool beyond a text editor and the willingness to move one
function.

## Python demonstration

[`code/software_design_science_demo.py`](./code/software_design_science_demo.py)
generates the synthetic module graph with `np.random.default_rng(20261014)` and
prints, under four numbered banners:

1. the graph's shape: 60 modules, 101 edges, mean fan-in and fan-out, leaves;
2. direct versus transitive reach, the $2.80\times$ amplification, and the
   distribution of blast radii;
3. instability, the count of unstable modules, and the correlation between
   fan-in and blast radius;
4. the coupling-driven defect model and its separation of high- versus
   low-blast modules, labelled as a model output.

```bash
cd 22-data-engineering-reproducibility/01-research-software-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python software_design_science_demo.py
```

## Exercises

Graded problems and fully worked solutions are in
[`exercises/01-software-design-science-exercises.md`](./exercises/01-software-design-science-exercises.md)
and
[`exercises/01-software-design-science-solutions.md`](./exercises/01-software-design-science-solutions.md).
They ask you to compute a blast radius by hand, to re-design a boundary, and to
state what a metric report does not establish.

## Mastery checkpoint

Without notes: a package has 40 modules and 60 edges. Module A has fan-in 6 and
fan-out 0; module B has fan-in 0 and fan-out 6.

1. Compute the instability of A and of B, and say which one you would expect to
   change more often and why.
2. A change to A affects at most 6 modules directly. Explain, without computing
   the closure, why the transitive effect can be larger but can never exceed 39.
3. You must add one dependency. State two questions that decide where it should
   point, one about blast radius and one about cohesion.

## Common pitfalls

1. **Treating a low edge count as proof of good design.** 101 edges in a 60-module
   package already produce a mean blast radius of 4.72 and a maximum of 25.
2. **Splitting by layer instead of by responsibility.** A `utils.py` with fan-in
   30 is a hub with extra steps.
3. **Counting lines as the measure of module size.** Coupling, not length, sets
   the cost of change; a long pure function is often cheaper than a short one
   with five imports.
4. **Reading a metric without its regime.** Graph metrics ignore filesystem,
   process and database coupling, and a snapshot without a commit is not
   reproducible.
5. **Refactoring without a test.** A structural change with no test is a
   behaviour change with no evidence.

## Where this is used

- **Preparing code for publication** — the design decides whether a reader can
  run the analysis: see [22-02-01](../02-reproducible-workflows/01-reproducibility-crisis.md).
- **Handing a project to a student** — narrow interfaces and explicit
  configuration are what make an instrument usable by a newcomer.
- **Deciding whether to refactor or rewrite** — the blast radius of the hub
  modules is the quantity that turns the argument into arithmetic.
- **Reviewing a paper's software** — a publishable package must separate
  computation from plotting, data from code, and configuration from constants:
  see [22-01-03](./03-code-review.md).
- **Long-running models and inversion codes** — coupling determines how easily a
  forward model can be swapped for another, which is the recurring requirement
  of every modelling project (see
  [19-numerical-modeling-hpc/07-verification-validation-uncertainty](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md)).

## Related lessons

- [22-01-02 Version Control with Git](./02-version-control-git.md) — the mechanism
  by which structural change is recorded and reviewed.
- [22-01-03 Code Review and Collaborative Development](./03-code-review.md) —
  how a design decision is inspected by a second person.
- [22-01-04 Documentation, Docstrings and READMEs That Work](./04-documentation.md) —
  the interface written for the reader who was not there.
- [22-07-01 Test Strategy for Numerical and Data Code](../07-software-testing-quality/01-test-strategy-science.md) —
  the tests that make a refactoring safe.
- [03-13-04 Code Quality: Style, Linting and Review](../../03-scientific-computing/13-testing-profiling-packaging/04-code-quality.md) —
  the mechanical checks that complement this lesson's structural ones.

## Self-assessment checklist

- [ ] I can state four properties that make research software different.
- [ ] I can define cohesion, coupling, fan-in, fan-out and instability.
- [ ] I can explain blast radius as the transitive closure of the dependency graph.
- [ ] I can compute the amplification of a change from direct to transitive reach.
- [ ] I can write a computation as a pure function separated from file input.
- [ ] I can state what a coupling-driven defect model does and does not establish.
