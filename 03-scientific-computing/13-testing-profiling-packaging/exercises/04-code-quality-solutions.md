# Solutions — 03-13-04 Linting, Formatting, Type Hints and Static Analysis

> **Read this after attempting the exercises, not before.** Values attributed to
> the demos are their actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — Four layers

**(a)** In order of increasing cost: **syntax** (`compileall`, microseconds,
catches a source that does not parse) → **lint and format** (`ruff`, milliseconds,
catches unused imports, mutable defaults, bare excepts, long lines) → **types**
(`mypy`, seconds, catches a wrong argument count or a `str` where a `float` is
required, which needs the whole program's interface model) → **tests** (seconds
to hours, catches wrong numbers, wrong signs and wrong physics). Each stage is
strictly cheaper than the next, which is why running them in this order is an
optimisation rather than a convention.

**(b)** All 32 are **missing return annotations**. The number measures the shape
of the code and nothing else: annotating every test function would take it to
zero while changing no behaviour, and it says nothing about whether any function
computes the right thing. Its highest concentration is in the test files — 16 in
`test_pytest_basics.py` and 9 in `test_analytic_solutions.py` — which is exactly
where a return annotation is least useful, because a test either raises or does
not.

**(c)** Because `from __future__ import annotations` is a compiler directive, not
a binding: it changes how annotations are stored (as strings) and creates no name
in the module namespace that could be referenced. Flagging it as unused is a
false positive, and the first version of this checker did exactly that — which is
the point of the exclusion being commented in the source rather than silent.

---

## ★2 — The float-equality check

**(a)** It matches an `ast.Compare` node whose `ops` contain an `ast.Eq` or
`ast.NotEq` and one of whose operands (the left side or any comparator) is an
`ast.Constant` whose `value` is a `float`. In words: **a comparison for equality
or inequality against a floating-point literal**.

**(b)** `test_pytest_basics.py` contains `assert d ** -2 != (1.0 / d) ** 2` — an
inequality between two computed expressions, with no float literal on either
side. The check correctly stays silent, and the assertion is correct: it is
asserting the *dis*equality that the arithmetic guarantees, deliberately, as
documentation. This is the false positive the literal-only rule avoids: banning
all float comparisons outright would flag a legitimate and instructive assertion.

**(c)** It misses a defective assertion against a **computed** reference, e.g.
`assert result == expected` where `expected` is a module-level float derived from
an expression. Detecting that requires knowing the *type* of `expected`, which is
a type-checker's job, not an AST pattern's: `mypy` with the right strictness can
see that both sides are `float` and that an equality comparison between them is
suspicious. In practice the test suite catches it: comparing two computed floats
for equality fails as soon as the accumulation order differs, which is precisely
how the defect manifests.

---

## ★3 — Classifying defects

| defect | layer | first tool |
|---|---|---|
| missing colon in `def f(x)` | syntax | `compileall` / `compile()` |
| one argument to a two-argument function | type | `mypy` (also a custom AST argument-count check) |
| free-air sign error | behaviour | a test against an independent reference |
| unused `import json` | lint | `ruff` F401 |
| `-> float` returning a string | type | `mypy` |

Note that only one of the five is reachable by a checker without interface
information (the argument count), and only one is unreachable by *any* static
tool (the sign). The table is the lesson's Section 1 in one page.

---

## ★4 — Reading the coverage scenarios

**(a)** Coverage measures which lines were executed, not which claims were
checked: two suites with identical coverage can differ in whether they detect a
defect, so a coverage threshold is a floor on *effort* and never a statement about
correctness.

**(b)** Scenario C passes because its expected value, `978969.14`, was captured
from a previous run of the buggy implementation — the test asserts that the code
equals what the code produces. It is the "characterisation test" decay: a
regression test whose reference is the behaviour rather than the specification.
No coverage threshold detects it, because every line is executed and every
assertion is satisfied; the defect is in the *reference*, which coverage cannot
see at all.

**(c)** The 90.9% → 100% increase communicated that the optional
terrain-correction branch now *had* a test executing it. That is exactly what the
signal is for: naming behaviour that nothing exercised. The newly covered branch
turned out to contain the second defect, which scenario E then found — but the
covering test of scenario D alone found nothing, and the distinction between
"now covered" and "now checked" is the whole lesson.

**(d)** `free_air_anomaly` is one `return` statement, so it has exactly one
executable line by `dis.findlinestarts`. Its coverage can only be 0% or 100% —
there is no partial credit and no granularity. A coverage gate therefore cannot
distinguish "the line ran" from "the sign is right"; the line ran, and the sign
is wrong, worth 61.72 mGal. The lesson's point about coverage counting lines
rather than claims has this as its sharpest form: for a dense one-line function,
the measurement is a single bit.

---

## ★5 — The false positive

**(a)** Run as a script, 32 findings; imported as a module, 34 — two extra
`shadowed-builtin` findings naming `get` and `__init__`.

**(b)** `__builtins__` is not a stable object. In the `__main__` module it is the
`builtins` *module*, so `dir(__builtins__)` returns the builtin names. Inside an
imported module it is a *dict* of the same names, and `dir()` of a dict returns
the dict's own methods — including `get`, `items` and `__init__`. The checker
built its name set from whichever object it happened to find, so the *same source
analysed by the same code* produced different answers depending on the calling
context. The fix is `import builtins; dir(builtins)`.

**(c)** The rule: **a false positive costs more than a missed finding.** A missed
finding leaves the code as it was; a false positive trains the reader to skim the
output, and a skimmed linter is a disabled linter within a month. The rule is
stronger because the cost is asymmetric and compounding: one `# noqa` added for a
wrong reason legitimises the next one, and the linter's remaining signal is lost
along with its credibility.

---

## ★6 — A check of your own

A defect none of the seven covers, of real value in numerical code: a
**normalisation that does not guard against a zero denominator**.

```
pattern:  <expr> = <something> / <name>
          where <name> is not preceded in the same function by a
          comparison against 0, a max(..., tiny), or an in a guard clause
expected false positives: a denominator that the module docstring
          guarantees non-zero (a positive thickness, a grid spacing)
```

Sketch:

```python
def check_unguarded_division(tree):
    problems = []
    for fn in [n for n in ast.walk(tree)
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
        guarded = set()
        for node in ast.walk(fn):
            if isinstance(node, ast.Compare) and any(
                isinstance(c, ast.Constant) and c.value == 0 for c in node.comparators
            ):
                guarded |= {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
        for node in ast.walk(fn):
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
                names = {n.id for n in ast.walk(node.right) if isinstance(n, ast.Name)}
                if names and not names & guarded:
                    problems.append(f"line {node.lineno}: division by {sorted(names)} "
                                    f"with no zero guard in this function")
    return problems
```

Expected false positives: any function whose contract makes the denominator
provably non-zero from the caller's side, which an intra-function analysis cannot
see. A test that exercises the check: parse two snippets, one with
`if drho == 0: raise ValueError(...)` before the division and one without, and
assert that only the second produces a finding. That test is what makes it a rule
rather than a regex.

---

## ★7 — A better quality bar

**(a)** The strongest defect admitted is the characterisation trap, scenario C: a
test whose expected value came from the code under test. 90.9% line coverage and
a clean lint run are both satisfied while a 61.72 mGal sign error is pinned in
place and a second defect sits in an untested branch.

**(b)** Three conditions, all measurable:

1. **Branch coverage, not line coverage, at a threshold** — scenario D's branch
   is what raises 90.9% to 100%, and branch coverage forces the exercise of the
   optional path (the second defect).
2. **Every numerical claim in a test must trace to a reference outside the
   module under test** — checkable by a convention plus review: the test must name
   the formula, instrument or publication its expected value came from. This is
   the only condition that catches scenario C.
3. **Every public function has at least one assertion on a computed value, not
   merely on its type or its shape** — again partly a convention, but rejectable
   mechanically by requiring that each public function's name appears in a test
   file together with an `assert` on a returned value.

Together, (1) catches the branch defect, (3) catches the smoke-test-only suite,
and (2) is the only one that reaches the sign error.

**(c)** Even this bar admits a wrong *reference*: a test that cites a formula
which is itself the wrong physics — the spherical-versus-conventional free-air
gradient of the previous lesson's exercises is exactly that. Catching it requires
a human who knows the geophysics, reading the derivation rather than the test.
That is a review practice, not a metric, and it is the honest reason a numerical
code base cannot be gated to correctness.

---

## ★8 — Finding the second defect by reading

**(a)** The static information is the **discrepancy between the docstring and the
body**: `station_anomaly`'s docstring says the terrain correction is applied, and
the body subtracts it. The other static signals are the inconsistency between
`free_air_anomaly` (which adds in the correct convention) and the caller's
handling of the correction, and the sign convention named in the function name.
No AST rule matches it; a reader with the physics does, in seconds.

**(b)** Because the defect is a *semantic* mismatch between two pieces of prose
and code that the compiler cannot see. Annotations are types, not meanings: a
function annotated `(float, float, float | None) -> float` admits both signs.
That is the implication the lesson draws — annotations and docstrings carry the
semantic content, and the tooling can only enforce the part that is expressible
as a type. The gap is exactly where the interesting bugs live.

**(c)** A rule that would flag it: **a docstring asserting a directional relation
(text containing "added", "increases with", "positive") whose body contains a
subtraction of the same symbol**. This is a natural-language pattern, not a
program analysis, and it would fire on every false positive the words "added" and
"subtract" ever co-occur with — including correct code that subtracts something
else. It is not general enough to ship, which is why it lives in this exercise and
not in `code_quality_demo.py`. The honest version of the rule is a human reading
the diff with the formula open beside it.

---

## ★9 — The formatter argument

**(a)** Against: the measured lint contribution of layout is that fixing long
lines changes the finding count and nothing else; the checker's own output says
so. A 240-file rewrite in one commit is large, unreviewable, and can hide a
genuine change; it makes some hand-aligned matrices and tables (which exist in
numerical code) worse, not better; and it introduces a tool dependency that every
contributor must install and every CI job must run. None of that is a
correctness improvement.

**(b)** For: the value is not in the diff but in the *absence of future diffs*.
Once layout is mechanical, a reviewer reading a change sees only semantic
content, which is where the physics is; and a re-indent can no longer hide a
one-line logic change inside a thirty-line diff. The two sides are arguing about
different quantities — (a) about the cost measured in this commit, (b) about the
return measured over all future commits — and the counter-argument is the
stronger one only if the project has future commits. A reproducibility argument
favours the formatter slightly, and for a specific reason: a repository whose
layout is mechanical is one fewer source of spurious diffs for someone trying to
diff two revisions of the code to find what changed between two published
results.

**(c)** Keep it reviewable: **one commit that is purely mechanical and provably
so** — CI checks that the only differences are whitespace, by comparing
`git diff -w` against the full diff, and the commit message states "no semantic
change" and nothing else. The procedure that destroys the review is the same
change bundled with feature work, or a "formatting plus small fixes" commit:
at that point the reviewer must read 240 files, and the one semantic change
becomes invisible.
