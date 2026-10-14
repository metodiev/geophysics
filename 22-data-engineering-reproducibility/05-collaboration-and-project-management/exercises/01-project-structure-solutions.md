# Solutions — 22-05-01 Project Directory Structure and Conventions

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [01 Project Directory Structure and Conventions](../01-project-structure.md).

---

## ★1 — The four regions

| Region | Rule |
|---|---|
| code (`src/` or the package) | importable with no I/O at import time |
| data | read-only, versioned by identifier, never written by the project |
| outputs (`results/`, `figures/`) | regenerable, never edited by hand |
| configuration | the only place that contains paths and parameters |

## ★2 — Which references break

Breaking on a move: **absolute** paths (they name a location that no longer exists) and
**working-directory-dependent** paths (they resolve against wherever the shell happens to
be, which changes when the invocation changes). Not breaking: **root-relative** paths
(relative to the project's own root, inside the tree) and **configuration-driven** paths
(the value comes from a file that travels with the project).

A working-directory reference belongs to the breaking group because it is implicitly an
absolute path: `open("data/x.csv")` means `/wherever/I/ran/it/data/x.csv`, and the user is
expected to know where to run it. That knowledge is undocumented, so the reference is
fragile in exactly the way absolute paths are.

## ★3 — The demonstration's project

Reference kinds: 9 absolute, 27 root-relative, 20 working-directory, 4 configuration.
Breaking: $9 + 20 = 29$ of 60 = **48 %** — the printed value. The 27 root-relative and 4
configuration-driven references survive the move.

## ★★4 — A 40-script project

(a) Breaking: $12 + 18 = 30$ of 40 = **75 %**.

(b) Remedies: absolute paths → replace the fixed prefix with a configured project root
(one value read once); working-directory dependence → resolve paths against the package
or the project root, or read them from the configuration. Both require **code changes**;
the configuration item in the demonstration's model is the only kind that is already
safe, so the "remedy" for it is to keep it safe by not reintroducing literals.

(c) The two-item change that reduces breakage most: introduce the configuration file with
the project root and the data identifiers, then rewrite the 30 failing references to use
it. In the demonstration's score, those two items are also the weakest (configuration
10 %, relative paths 45 %), so the structural fix and the weakest-score fix coincide —
which is the usual case, because the score's items *are* the structural rules.

## ★★5 — A module called `types.py`

(a) Any script run from that directory imports the local `types.py` instead of the
standard library's `types` module, so a library that imports `types` gets the wrong module
— potentially a `SyntaxError`, an `AttributeError`, or worse, a subtly different object.
The message is confusing because it appears in a library the user did not touch, and the
file that causes it looks innocuous.

(b) The layout change: move the modules into a package (`src/<package>/…`) so the
namespace is bounded and a file name can no longer shadow a top-level module by accident.

(c) The check: run the test suite (or the entry point) from a directory **other than**
the project root — the portability test of §3 — and add an import-shape assertion, for
example that `import types; types.__file__` names the standard library. A CI job that
runs from a clean clone in a different directory catches the class of failure.

## ★★6 — The portability score

(a) Mean of (45 %, 80 %, 100 %, 10 %, 50 %) $= 285/5 = 57.0$ % — the printed 0.570.

(b) Weakest: **configuration is a file, not a constant** (10 %) and **paths are relative
to the project root** (45 %).

(c) In practice: (i) create `config/*.yml` with the project root, the data identifiers and
the run parameters, and delete the literals from the scripts; (ii) replace each literal
path with a value read from the configuration, so the tree can be moved without edits.
Both are mechanical, both are checkable (grep for path literals, run from a different
directory), and both are the reason the score has a low mean.

## ★★★7 — A five-year project with rotating staff

**Tree.**

```text
project/
  README.md            # purpose, entry points, conventions
  CITATION.cff  LICENSE
  src/<package>/       # importable code; no I/O at import time
  config/              # parameters, data identifiers, no secrets
  data/                # read-only; or a manifest of identifiers if data live elsewhere
  results/  figures/   # regenerable outputs
  notebooks/           # exploration, not artefacts
  tests/               # including fixtures and reference values
  env/environment.yml  docs/
```

**Entry points.** Two or three commands, each documented in the README and runnable from
a clean clone: `make prepare`, `make invert`, `make figures` (or the equivalent script
names). Everything else is internal and marked as such.

**Naming rules.** Data files named by *what they are and their version identifier*, never
by `FINAL`; scripts named by role; branches and releases named by the tag convention the
group uses for citations
([22-01-02](../../01-research-software-engineering/02-version-control-git.md) §6).

**Data strategy.** Raw field data are archived with identifiers and checksums; the
project's `data/manifest.yml` names the identifiers, so the tree contains no irreplaceable
bytes. Derived products are regenerated.

**CI checks.** Move-the-project test (clone to a different path, run the entry points);
path-literal check (grep for absolute paths outside `config/`); import check from a foreign
working directory; notebook restart test if notebooks are artefacts
([22-02-04](../../02-reproducible-workflows/04-notebooks-vs-pipelines.md) §6); and the
reference-result regression tests.

**The convention I would not automate.** *Which figure is the paper's figure 3* — the
mapping from a scientific claim to an artefact. It changes with the science, needs a
human, and belongs in the README's table of results, reviewed at release.

**What the structure makes hard.** Sharing a single file with an external collaborator who
does not use the repository: the four regions assume the tree travels as a unit, so
one-file exchanges (a spreadsheet, a revised table) have to be brought in through the data
region with a version, which is deliberate friction.

## ★★★8 — Measuring a repository's structural health

**Data extracted.** For every file: `import` statements (and their resolution root),
string literals used in path-like calls (`open`, `Path`, `np.loadtxt`, …), reads of
configuration files, and the presence of an installed distribution (a build or project
metadata file).

**Statistics.** (i) The fraction of path references that would break on a move (absolute
or working-directory dependent); (ii) the number of distinct import roots; (iii) the number
of module names that collide with the standard library or with installed packages;
(iv) the fraction of documented entry points that run from a directory other than the
project root.

**Two ways the measurement could mislead.** (i) **Dynamic paths**: a path built at run time
from a configuration value or an environment variable looks like a literal to a static
parser, or hides a literal that appears only on a branch; (ii) **generated code** and
vendored dependencies: files copied from elsewhere inflate the collision and reference
counts without being the group's problem. Both require inspecting the flagged files rather
than trusting the aggregate.

**What it cannot tell you.** Whether the code is correct, or whether the entry points
produce the right numbers: the measurement is about structure, and a perfectly structured
project can compute the wrong thing. It also cannot see the coupling through the
filesystem, which the pipeline's own provenance record
([22-02-03](../../02-reproducible-workflows/03-workflow-managers.md) §8) is the place to
measure.

## ★★★9 — Merging three projects into one repository

**Criteria for merging.** (i) Shared code that both projects currently duplicate, where a
fix must reach both; (ii) a shared data or environment discipline, so the CI checks are
the same; (iii) overlapping people, who can maintain one tree; (iv) compatible release
cadences, so one project's release does not block the other's.

**Stay separate.** Projects with different stakeholders (a teaching repository, a
collaboration with another group), different licences or data-access rules, and different
release cycles. A paper's frozen code may *live* in the monorepo, but as an archived
release rather than a live package.

**Duplicated deliberately.** The environment definitions stay per package (different
dependency sets), while the boundaries (config structure, test harness) are shared.
Duplication of a *convention* is fine; duplication of an *implementation* is what the merge
exists to remove.

**The failure mode of merging.** A single tree couples unrelated projects: one project's
broken dependency or failing test blocks the other's release, and a change made for one
purpose forces a review by people who do not care about it. **The measurement** that
detects it is the *cross-project change rate*: the fraction of changes that touch more than
one project's directory. If that fraction rises after the merge, the coupling is real —
compare it with the pre-merge rate, and with the number of blocked releases attributable to
another project's state.

**What you cannot decide without the authors.** Which code is genuinely shared versus
coincidentally similar (two implementations of the same equation that are deliberately
different), and who will answer questions about a component after its author graduates —
the maintenance commitment is a person-level fact, not a code-level one.
