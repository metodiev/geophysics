# Exercises — 03-13-04 Linting, Formatting, Type Hints and Static Analysis

Attempt these **closed-book** before opening the
[solutions](./04-code-quality-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/code_quality_demo.py`](../code/code_quality_demo.py) and
[`../code/coverage_demo.py`](../code/coverage_demo.py):

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/code_quality_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/coverage_demo.py
```

The lesson is [`../04-code-quality.md`](../04-code-quality.md).

---

## ★ Foundational

**★1. [demo]** The linter reports 9 findings on the defective snippet and 32
across the module's own fourteen `code/*.py` files.

(a) State the four layers of static and dynamic checking in order of increasing
cost, and say what each catches that the next would otherwise have to.
(b) The module's 32 findings are all of one kind. Name it, and say what the
number is and is not a measure of.
(c) Explain why `from __future__ import annotations` is excluded from the
unused-import check.

**★2. [demo]** On the defective snippet the float-equality check fires once:

```
[float-equality] line 21: float equality against 0.1; use a tolerance
```

(a) Write the AST pattern the check matches, in words.
(b) Give one comparison in this module's own `code/` directory that the check
correctly does *not* fire on, and say why not.
(c) The check fires on literals only. Describe a defective assertion it therefore
misses, and how a test could catch that one.

**★3.** Classify each defect as syntax, lint, type or behaviour, and name the tool
that catches it first: (a) a missing colon after `def f(x)`; (b) a call with one
argument to a function that needs two; (c) a free-air correction with the wrong
sign; (d) `import json` that is never used; (e) a function annotated `-> float`
that returns a string.

---

## ★★ Applied

**★★4. [demo]** The coverage demonstration runs five scenarios:

| scenario | assertions | coverage | tests | defect found? |
|---|---|---|---|---|
| A calls, no assertions | 0 | 90.9% | pass | no |
| B one assertion | 1 | 90.9% | fail | yes |
| C expected value copied | 1 | 90.9% | pass | no |
| D branch exercised | 0 | 100.0% | pass | no |
| E branch exercised and checked | 1 | 100.0% | fail | yes |

(a) A and B have identical coverage and different outcomes. State the conclusion
about coverage that follows, in one sentence.
(b) Explain scenario C precisely: what makes it pass, and why no coverage
threshold could detect it.
(c) Scenario D raises coverage from 90.9% to 100% while finding nothing. State
what the coverage increase actually communicated, and why that is useful.
(d) The coverage instrument uses `dis.findlinestarts` for the denominator. Explain
what `free_air_anomaly`'s coverage can be, given that it is a single-line
function, and why that limits what coverage can say about it.

**★★5. [demo]** The linter's shadowed-builtin check reported different results
depending on how the checker was invoked.

(a) State the two invocation modes and the two counts.
(b) Explain the mechanism: what is `__builtins__` in `__main__` versus inside an
imported module?
(c) State the rule that follows about false positives, and why it is stronger than
the rule about missed findings.

**★★6.** Write an AST check that detects a numerical defect of your choosing that
none of the seven implemented checks covers. State the defect, the pattern, the
false positives you expect, and one test that would exercise the check.

---

## ★★★ Research-oriented

**★★★7.** A team wants "80% coverage and a clean lint run" in CI as its quality
bar.

(a) Using the measured scenarios, state the strongest defect the bar admits
through.
(b) Propose a replacement bar that consists of three measurable conditions and
would have caught all three of the module's planted defects.
(c) State one defect that even the replacement bar admits, and describe the review
practice that catches it instead.

**★★★8.** `survey_stats.py` in this module contains two planted defects and a
branch that the coverage demonstration never exercises.

(a) Describe how you would find the second defect without running any test: what
static information would you use?
(b) Explain why the answer is "read the code against its docstring", and what that
implies about the relationship between annotations, docstrings and checkers.
(c) Design a lint rule that would flag the second defect, and state honestly why
such a rule is not general enough to ship.

**★★★9.** The lesson says a formatter's value is review attention rather than
correctness.

(a) Construct an argument *against* adopting a formatter, from the measured
finding counts.
(b) Construct the counter-argument, and state which side a paper's reproducibility
argument favours.
(c) A formatting commit touches 240 files. State the review procedure that keeps
it reviewable, and the one that destroys the review.
