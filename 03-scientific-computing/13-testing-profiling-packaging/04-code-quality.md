---
id: 03-13-04
title: "Linting, Formatting, Type Hints and Static Analysis"
level: intermediate
prereqs: ["03-13-01", "03-01-04"]
estimated_minutes: 85
tags: [linting, typing, static-analysis, style, code-quality, mypy, ruff]
---

# Linting, Formatting, Type Hints and Static Analysis

A test suite finds defects by running code on inputs you thought of. A linter
finds a different class of defect by reading the source and never running it:
an unused import, a mutable default argument, a bare `except`, a float compared
with `==`, a call with the wrong number of arguments, an annotation that
contradicts the body. These are cheap to detect and expensive to debug, and the
detection is free in CI.

This lesson takes the unusual position that the *most* useful thing to do with a
linter is to explain why it is not enough. Static analysis reports facts about
the shape of code. It cannot tell you that the free-air sign is wrong — a defect
that is syntactically flawless, type-correct, PEP 8 compliant and physically
69 mGal off. Knowing exactly where the boundary lies is what makes the tool
useful rather than a substitute for thought.

The tools of the trade are `ruff` (lint and format), `black` (format), `mypy`
or `pyright` (types) and `python -m compileall` (syntax). **None of ruff, black
or mypy is installed in this repository's environment**, although
`requirements.txt` declares `ruff>=0.4` and `mypy>=1.10` — the environment audit
in [03-13-08](./08-reproducible-environment.md) reports them among the eight
declared-but-absent packages. So this lesson builds the same class of check from
`ast`, and every number below is measured from that implementation.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what static analysis can and cannot establish, and place a given
   defect on the correct side of that boundary.
2. **Write** an AST-based check for a defect class that matters in numerical
   code, and run it over a whole directory.
3. **Distinguish** syntax errors, lint findings, type errors and behavioural
   failures, and put them in the order that fails fastest.
4. **Add** type annotations that a checker can use, and read them back at
   runtime.
5. **Judge** a formatter's contribution honestly: it is mechanical, unreviewable,
   and it removes a class of argument from review.
6. **Describe** a CI sequence that runs syntax, lint, types and tests, and say
   what each stage catches that the next one would otherwise have to.

## Prerequisites

- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the behavioural layer these checks sit above.
- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — signatures, defaults and imports, the three things most checks inspect.

## 1. Four layers, in order of cost

| Layer | Question | Cost per run | Catches |
|---|---|---|---|
| Syntax | does it parse? | microseconds | a missing colon, an unbalanced bracket |
| Format and lint | is it shaped well? | milliseconds | unused imports, shadowing, long lines, mutable defaults |
| Types | are the interfaces consistent? | seconds | wrong argument count, `str` where `float` is required |
| Tests | does it behave? | seconds to hours | wrong numbers, wrong signs, wrong physics |

Each layer catches a class the next would otherwise have to, and each is
strictly more expensive than the previous. The order is therefore not a
convention, it is an ordering by cost, and a CI pipeline should honour it: a
syntax error should never cost you a five-minute test run.

`compile()` is the cheapest gate in existence. Measured on a deliberately
malformed source string:

```
compile() raised SyntaxError: line 1: expected ':'
```

Nothing was imported; nothing ran. `python -m compileall <dir>` applies the same
check to a tree in milliseconds, and every CI system performs it implicitly the
first time it imports your package.

## 2. What a linter actually inspects

A linter parses source into an abstract syntax tree (AST) and pattern-matches it,
exactly as this lesson's implementation does with
[`ast`](https://docs.python.org/3/library/ast.html). It never executes the
module. That single fact explains both its power and its ceiling.

The seven checks implemented in `code/code_quality_demo.py`, each a few lines of
AST walking:

1. **float-equality** — `==` or `!=` against a float literal, the defective
   numerical assertion of [lesson 01](./01-pytest-basics.md).
2. **mutable-default** — a list, dict or set literal as a default argument, which
   is shared between calls.
3. **bare-except** — `except:` with no type, which swallows `KeyboardInterrupt`
   and `SystemExit`.
4. **unused-import** — an imported name never referenced. `from __future__
   import ...` is excluded, because it is a compiler directive rather than a
   binding; the first version of this checker reported it as unused, which is
   exactly the false positive that trains people to ignore a linter.
5. **shadowed-builtin** — assigning to `sum`, `list`, `id` and friends.
6. **long-line** — the only text-level check, because the AST discards layout.
7. **missing-return-annotation** — a function without `->`.

Applied to a deliberately defective snippet, they report **9 findings**: 2
unused imports, 1 mutable default, 1 bare `except`, 1 float equality, 1 shadowed
builtin and 3 missing return annotations.

Applied to this module's own fourteen `code/*.py` files, they report **32
findings**, and the distribution is the informative part:

| file | lines | findings |
|---|---|---|
| `test_pytest_basics.py` | 194 | 16 |
| `test_analytic_solutions.py` | 138 | 9 |
| `profiling_demo.py` | 303 | 3 |
| `analytic_solutions_demo.py` | 260 | 2 |
| `coverage_demo.py` | 233 | 1 |
| `git_workflow_demo.py` | 274 | 1 |
| the remaining eight files | — | 0 |

All 32 are missing return annotations; the other six checks report nothing. That
is a real, measured statement about this code base, and it is also a statement
about the limits of the check: annotating every test function would make the
count zero and would not change a single behaviour. The count is highest in the
test files, which is where a return annotation is least useful — a test either
raises or does not. **A clean lint run is a claim about the shape of the code,
not a claim that it is correct.**

### 2.1 A false positive in this lesson's own linter

The first version of the shadowed-builtin check used
`frozenset(dir(__builtins__))`. That looks equivalent to `dir(builtins)` and is
not: `__builtins__` is a *module* in `__main__` but a **dict** inside an imported
module, and `dir()` of a dict returns dict methods. The consequence was measured
and reproduced twice:

| how the checker was invoked | findings reported |
|---|---|
| as a script (`python code_quality_demo.py`) | 32 |
| imported (`import code_quality_demo`) | 34, including `get` and `__init__` as "shadowed builtins" |

The same source analysed by the same code gave two different answers depending on
the calling context. This is precisely the failure mode that teaches people to
ignore a linter, and it is why the fix — `import builtins` — is accompanied by a
comment in the source rather than a silent edit. **A false positive costs more
than a missed finding**, because it erodes the habit of reading the output.

## 3. What static analysis cannot do

The most valuable line in this lesson: **no lint rule can tell you the free-air
sign is wrong.**

Consider `code/survey_stats.py`:

```python
def free_air_anomaly(elevation_m: float, observed_mgal: float) -> float:
    return observed_mgal - FREE_AIR_GRADIENT_MGAL_PER_M * elevation_m
```

It parses. It is fully annotated. It imports nothing unused. It shadows no
builtin. It is under 99 characters. It type-checks. Its docstring even states
the correct rule, and the body implements the opposite. Evaluated at
100 m and 979 000 mGal it returns **978 969.14** where the free-air correction
requires **979 030.86**: an error of **61.72 mGal**, which is
$2 \times 0.3086 \times 100$, larger than the entire anomaly of most targets.

Only a reference *outside the code* refutes it: an analytic formula, an
instrument, or a second independent implementation. That is the domain of
[lesson 02](./02-testing-scientific-code.md), and it is why the layers in
Section 1 are complementary rather than alternatives.

### 3.1 One thing a checker does catch that a linter cannot

A related but genuinely static check does reach further, because it needs the
*signature* rather than one function body: an argument-count check. Measured on
a snippet that calls a two-parameter function with one argument:

```
line 5: bouguer_slab() with 1 positional argument(s) -> ERROR: expected 2..2, got 1
```

This is the class `mypy` reports as "Missing positional argument", and it is
exactly the class a test that never executes that line cannot find. The
distinction matters: the linter inspects one function in isolation; the type
checker builds a model of the whole program's interfaces. Building that model is
what costs seconds instead of milliseconds.

## 4. Where the coverage signal sits

Line coverage is the quantity people quote when they want a single number for
"how well tested is this". It belongs in this lesson because it is a *static
summary of dynamic evidence*, and it is routinely over-read.

`code/coverage_demo.py` measures coverage with the standard library and runs
five scenarios against the same deliberately defective module. Measured:

| scenario | assertions | line coverage | tests | defect found? |
|---|---|---|---|---|
| A — calls, no assertions | 0 | 90.9% | pass | no |
| B — one assertion | 1 | 90.9% | **fail** | yes |
| C — expected value copied from the code | 1 | 90.9% | pass | no |
| D — untested branch exercised | 0 | 100.0% | pass | no |
| E — branch exercised and checked | 1 | 100.0% | **fail** | yes |

Four facts, each measured, and each a distinct failure of the coverage signal:

1. **Scenario A** reaches 90.9% coverage, passes, and hides a 61.72 mGal sign
   error. Coverage counts execution, not claims.
2. **Scenario B** has the *same* coverage and one assertion, and fails — the
   correct message is not "coverage is useless" but "coverage counts lines, not
   claims".
3. **Scenario C** is the most dangerous: a "regression test" whose expected value
   was captured from the code under test. It passes forever and pins the bug in
   place. No coverage threshold can detect this, and neither can a linter or a
   type checker.
4. **Scenarios D and E** show what the signal is genuinely for: coverage rose
   from 90.9% to 100% only when the optional terrain-correction branch was
   executed, and that branch contained the second defect. **Coverage names the
   behaviour nothing tests.** That is its real job.

A coverage gate is therefore worth having, and worth having with a *branch*
requirement rather than only line coverage. But it is a floor, never a
certificate.

## 5. Type hints: annotations are data

PEP 484 annotations are evaluated (or stored as strings) at runtime, which makes
them introspectable and makes them a contract a machine can check. The
demonstration reads them three ways:

```
GravityStation.__annotations__ = name: str, latitude_deg: float,
                                 elevation_m: float, observed_mgal: float, tags: list[str]
dataclasses.fields -> 5 fields: name, latitude_deg, elevation_m, observed_mgal, tags
resolve() raw annotation        = "'GravityStation'" (a string: a forward reference)
typing.get_type_hints(resolve)  = <class '__main__.GravityStation'>
VelocityPick._fields            = ('offset_m', 'time_s')
```

Three practical consequences.

- **`from __future__ import annotations` makes every annotation a string.**
  Nothing breaks, and `typing.get_type_hints` resolves them on demand. A checker
  reads the strings; runtime code that needs the objects must call
  `get_type_hints`.
- **`dataclasses` and `NamedTuple` consume annotations as their field
  declarations**, so a wrong annotation becomes a wrong runtime type, not a
  wrong comment.
- **A checker rejects `GravityStation('A', 45.0, 'one hundred', 979000.0)`** — a
  string where a float is required — before anything runs. That is the whole
  proposition of gradual typing: the annotations you already wrote to explain
  yourself become a machine-checkable specification at no extra cost.

Where the annotations are *wrong* rather than missing, the checker earns the most:
a function annotated `-> np.ndarray` that returns a list, or a parameter
annotated `float` that callers pass a `None` to. `mypy --strict` is the
conventional setting for numerical library code; it is loud, and the noise is
mostly about optional values and NumPy dtypes, which is precisely where the bugs
are.

## 6. Formatting: the honest assessment

A formatter decides line breaks, quoting and spacing. Its contribution is
mechanical: fixing the long lines in this module's files reduces the finding
count immediately, with no change in behaviour. Making the uninteresting
findings go away is not an achievement, and a lint count is a poor proxy for
quality.

What the formatter actually buys is social, and the argument is worth stating
plainly because it is not obvious:

- **It removes a class of review comment.** Reviewers spend attention on
  whitespace when whitespace varies; making it mechanical reclaims that
  attention for the physics.
- **It makes diffs semantic.** A re-indent that touches thirty lines hides a
  one-line logic change. A formatter normalises the layout once so that later
  diffs show only what changed.
- **It is unreviewable, deliberately.** Once `black` or `ruff format` owns
  layout, nobody argues about layout. The configuration decision — line length,
  which is where most of the argument actually lives — happens once.

The cost is real too: a formatter rewrites history in a single commit that
touches everything, and it makes some hand-aligned tables and matrices uglier.
The honest position is that the benefit is about *attention*, not about
correctness, and it should be justified that way.

## 7. Python demonstration

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/code_quality_demo.py
```

The script runs the seven checks over the defective snippet and over the
module's own `code/` directory, demonstrates the syntax gate and the
argument-count check, and reads annotations back at runtime. It writes nothing to
disk; every check is a pure function of a source string.

What it would look like with the real tools, stated from their documentation —
these commands were **not** run here, because none of the three is installed and
this environment is offline:

```bash
python -m compileall -q 03-scientific-computing/13-testing-profiling-packaging/code
ruff check .            # lint; --fix applies the safe subset
ruff format --check .   # layout, without rewriting
mypy --strict package/  # interfaces
```

The CI ordering that follows costs the least:

```yaml
      - run: python -m compileall -q .
      - run: ruff format --check .
      - run: ruff check .
      - run: mypy --strict .
      - run: python -m pytest -q
```

with lint and type findings allowed to be warnings in a legacy code base but
required to be clean on new files — the only version of "adopt a linter" that
survives contact with a real repository.

## 8. Assumptions and limits

- **Static checks approximate**. A linter reports patterns, not semantics; a
  `# noqa` is a promise by a human, and it can be wrong.
- **Types are not specs.** A function annotated `float -> float` allows an
  infinity, a NaN, a negative velocity and a mistyped constant.
- **A formatter's diff is large and its value is social.** Do not sell it as a
  correctness improvement.
- **Coverage measures execution.** Measured above: 90.9% coverage with zero
  assertions, passing, over a 61.72 mGal error.
- **Linters must not be silenced to green.** A checker whose bypass is easier
  than its fix is a checker that will be bypassed.

## 9. Common mistakes

1. Believing a clean lint run means correct code. It means well-shaped code.
2. Adding `# noqa` to silence a real finding rather than fixing it.
3. Enabling every rule at once on a large code base, generating hundreds of
   findings, and disabling the linter within a week. Start with the four or five
   that catch real defects.
4. Treating a coverage percentage as a quality score, or a target to be hit by
   writing assertion-free tests.
5. Annotating everything and running no checker, which produces documentation
   that is wrong in the same places the code is.
6. Formatting and logic changes in the same commit, so the logic change cannot be
   reviewed.
7. Using `# type: ignore` without a comment naming the reason.
8. Forgetting that a checker is run *before* the tests in CI, and paying for a
   full test run to discover a syntax error.

## 10. Real-world applications

- **A library with external users.** Type annotations are documentation that
  cannot silently rot; a stub or `py.typed` marker makes a type checker work for
  downstream users, including the ones reading your code in an editor.
- **A long-lived institutional code base.** A linter plus a formatter plus an
  enforced format check is the cheapest way to make a decade of contributions
  look like one code base.
- **Publication code.** Annotated, formatted, lint-clean code is materially
  easier to re-run by someone else, which is the point of publishing it.
- **Teaching.** The float-equality check in Section 2 is a lint rule that
  directly prevents the most common defect in this curriculum; a project-specific
  rule is legitimate and cheap.

## 11. Further reading

- **PEP 8 — Style Guide for Python Code.** <https://peps.python.org/pep-0008/>
  Level: reference.
- **PEP 484 — Type Hints.** <https://peps.python.org/pep-0484/> Level:
  reference. Read it alongside `typing.get_type_hints`, since the runtime
  behaviour of annotations is where the surprises live.
- **Python standard library.**
  [`ast`](https://docs.python.org/3/library/ast.html),
  [`typing`](https://docs.python.org/3/library/typing.html),
  [`dataclasses`](https://docs.python.org/3/library/dataclasses.html). Level:
  reference for the introspection used in Section 5.
- **Benoit, N. (2022). *Python Testing with pytest* (2nd ed.). Pragmatic
  Booksellers.** Level: intermediate. Chapters on CI configuration, which is
  where the four layers of Section 1 get wired together.
- **Zeller, A. (2009). *Why Programs Fail: A Guide to Systematic Debugging*
  (2nd ed.). Morgan Kaufmann.** Level: intermediate. The framing of static
  analysis as "defects that do not depend on execution" is a debugging
  methodology, not a tool description.

> Note on citations: bibliographic details are given so you can locate the
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03-13-01 pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md)
  — the behavioural layer, and the float-equality defect the first lint rule
  targets.
- [03-13-02 Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md)
  — the only layer that can catch a sign error.
- [03-13-05 Packaging and Distributing a Python Library](./05-packaging.md) —
  where `type: ignore` comments and `py.typed` markers end up shipping.
- [03-13-06 Git for Scientific Collaboration](./06-git-workflow.md) — why a
  formatting commit must be separated from a logic commit.
- [03-01-08 Classes, Objects and Dataclasses](../01-python-fundamentals/08-classes-and-oop.md)
  — the dataclass machinery whose fields are annotations.

## 13. Self-assessment checklist

- [ ] I can place a defect on the correct side of the static/dynamic boundary and
      say which layer would catch it. (§1, §3)
- [ ] I can write an AST check for a defect class that matters to me. (§2)
- [ ] I can state what a clean lint run does and does not claim. (§3)
- [ ] I can give one measured example of a defect that is lint-clean,
      type-clean and wrong. (§3)
- [ ] I can say what coverage is genuinely good for, using a measured
      before/after number. (§4)
- [ ] I can read annotations back at runtime and explain forward references. (§5)
- [ ] I can justify a formatter in terms of review attention rather than
      correctness. (§6)
- [ ] I can order the CI stages by cost and say what each one saves. (§7)
