# Exercises — 22-05-01 Project Directory Structure and Conventions

Attempt these before reading the
[solutions](./01-project-structure-solutions.md). The lesson is
[01 Project Directory Structure and Conventions](../01-project-structure.md). All
counts refer to the **SYNTHETIC** project of `code/project_structure_demo.py`:
60 scripts, 40 data files, 8 documented entry points, and reference kinds split
9 absolute / 27 relative / 20 working-directory / 4 configuration.

## ★ Foundational

**★1.** Name the four regions of a project tree, and for each state the one rule that
makes it safe.

**★2.** State which reference kinds break when a project moves and which do not, and
explain why a working-directory-dependent reference belongs to the first group.

**★3.** Compute the fraction of the demonstration's scripts that break on a move, and
state how many use each reference kind.

## ★★ Applied

**★★4.** A project has 40 scripts: 12 absolute, 18 working-directory dependent,
8 root-relative and 2 configuration-driven.

(a) Compute the fraction that break on a move. (b) State the remedy for each failing
kind and which requires editing code. (c) State the two-item change that would reduce
the breakage most.

**★★5.** A colleague's module is called `types.py` and lives in the project root.

(a) State the failure it can cause and why the error message is confusing. (b) State
the layout change that removes the class of failure. (c) State the check that would
detect a recurrence.

**★★6.** Using the portability score's five items (coverage 45 %, 80 %, 100 %, 10 %,
50 %): (a) compute the mean; (b) list the two weakest items and their coverage; (c) state
what each improvement would require in practice, in one line.

## ★★★ Research-oriented

**★★★7.** Design the structure and conventions for a five-year project with field data,
a modelling code, a publication pipeline and a rotating cast of students. State the
tree, the entry points, the naming rules, the data-identifier strategy, the CI checks
that enforce the conventions, and the one convention you would *not* automate. State what
your structure makes hard.

**★★★8.** Design a measurement of a real repository's structural health: state the data
you extract (import statements, path literals, configuration reads), the statistics
(fraction of breakable references, number of import roots, entry-point coverage), and the
two ways the measurement could mislead (dynamic paths, generated code). State what the
measurement cannot tell you about the code's quality.

**★★★9.** A group must merge three research projects into one repository to share code.
State the criteria you would use to decide what merges, what stays separate, and what is
duplicated; state the failure mode of merging (a single tree that couples unrelated
projects) and the measurement that would detect it. State what you cannot decide without
talking to the authors.
