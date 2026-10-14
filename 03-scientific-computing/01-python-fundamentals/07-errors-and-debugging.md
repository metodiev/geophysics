---
id: 03-01-07
title: "Exceptions, Assertions and Systematic Debugging"
level: intermediate
prereqs: ["03-01-06"]
estimated_minutes: 75
tags: [exceptions, assertions, debugging, validation, uncertainty]
---

# Exceptions, Assertions and Systematic Debugging

Every number a program produces is either right or wrong, and the program almost
never tells you which. Exceptions are the mechanism by which a program refuses to
produce a wrong number, and assertions are the mechanism by which it refuses to
produce a *physically impossible* one. Used well, they convert the two failure
modes that plague scientific code — a silent wrong answer and a crash three hours
into a run — into a single, immediate, informative error.

This lesson is deliberately placed after file I/O, because that is where bad data
enters. It is also the lesson that makes every later module verifiable: a
numerical solver with no assertions cannot be distinguished from a numerical
solver with a bug.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** an assertion (a statement about the physics that must be true)
   from validation (a check on what the user supplied), and place each correctly.
2. **Design** a custom exception that carries the offending field, value and
   unit, and explain what that buys over a bare `ValueError`.
3. **Use** the four clauses `try`, `except`, `else`, `finally` for what each is
   for, and catch only the exception types you mean.
4. **Quantify** the cost of `except ...: pass`, and state what a counted skip
   reports that a silent one does not.
5. **Read** a traceback bottom-up, and explain what the *call path* contributes
   that the final message does not.
6. **Debug** by bisecting to the first divergence between an expected and an
   observed result, using a five-question checklist.

## Prerequisites

- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — where the
  bad data comes from.

## 1. Assertions are physics, not checks

An assertion states something that must be true. The mistake is to confuse the two
kinds of "must be true":

| | Assertion | Validation |
|---|---|---|
| Subject | The model | The input |
| Example | `0 < vs < vp` for an isotropic solid | `rho` must be a positive number |
| Can a user trigger it? | No, unless the code is wrong | Yes, with a bad file |
| Response to failure | Stop; the code is broken | Report why and where |
| Survives `python3 -O`? | No — assertions are stripped | Yes |

Both are checks, and they belong in different places. An assertion that a *user*
can trigger is a validation check wearing the wrong clothes, and it will silently
disappear when someone runs the script with `-O` for speed.

Here is an assertion block, from the demo, of the kind that belongs in every
forward model:

```python
lam, mu, rho = 9.0e9, 8.0e9, 2350.0
vp = math.sqrt((lam + 2.0 * mu) / rho)
vs = math.sqrt(mu / rho)
assert rho > 0.0, "density must be positive"
assert 0.0 < vs < vp, f"an isotropic solid requires 0 < vs < vp, got {vs:.1f}, {vp:.1f}"
assert -1.0 < (vp**2 - 2*vs**2) / (2*(vp**2 - vs**2)) < 0.5, "Poisson ratio out of range"
```

```text
  vp = 3261.6 m/s, vs = 1845.1 m/s, both assertions held
```

Three properties make this a good assertion block.

**Each assertion is a physical statement with no exceptions.** A solid transmits
shear waves more slowly than compressional waves, always. Poisson's ratio for an
isotropic solid lies strictly between −1 and 0.5, always. There is no dataset for
which the assertion should be skipped, which is precisely the test for
"assertion" rather than "validation".

**Each carries a message with the values.** `got 1845.1, 3261.6` converts a
failure into a diagnosis. An assertion without a message is a stack trace with the
interesting numbers missing.

**Each is at the boundary where the assumption is made.** The velocities are
asserted immediately after they are computed, in the same function that computed
them. An assertion 200 lines later detects the same bug but tells you far less.

Note also what is *not* asserted: the code does not assert that `lam` is positive
(an auxetic or pre-stressed medium can have a negative effective $\lambda$), nor
that the values came from a particular rock. Assertions that encode a preference
rather than a law are noise, and noise erodes trust in the real ones.

## 2. Validation with an exception that carries the value

Input validation is a different job, and it deserves a different mechanism: an
exception type of your own, carrying the field, the value, the unit and the
reason.

```python
class DataError(ValueError):
    def __init__(self, field, value, unit, reason):
        self.field, self.value, self.reason = field, value, reason
        super().__init__(f"{field} = {value!r} {unit}: {reason}")
```

Why subclass `ValueError`? Because an upstream caller that already handles
`ValueError` — the `csv` module, `float()`, most parsers — will handle this too,
while a caller that wants the extra structure can catch `DataError`
specifically. The subclass is a strict refinement, not a new hierarchy.

The demo runs a density validator over six inputs:

```text
  density 2670.0     -> accepted, ok
  density 8100.0     -> accepted, warning: denser than iron (7874 kg m^-3)
  density 30000.0    -> REJECTED: density = 30000.0 kg m^-3: exceeds osmium (22590 kg m^-3)
  density 0.0        -> REJECTED: density = 0.0 kg m^-3: must be positive
  density nan        -> REJECTED: density = nan kg m^-3: NaN: the measurement failed
  density '2670'     -> REJECTED: density = '2670' kg m^-3: not a number
```

Four design decisions are embedded in that output, and each is a choice you will
have to make in your own code.

**A physically impossible value is an error; a physically unusual one is a
warning.** 8,100 kg m⁻³ is denser than iron — unusual for a crustal rock, entirely
possible for a massive sulphide or magnetite ore body — so the function accepts it
and returns a note. 30,000 kg m⁻³ exceeds osmium, the densest element at
22,590 kg m⁻³, so it is impossible and the function raises. **This distinction is
the difference between a validator that helps and a validator that gets switched
off.** A checker that rejects real ore bodies will be bypassed within a week.

**The unit is in the message, not only in the docstring.** `30000.0 kg m^-3` is
unambiguous; `30000.0` invites the reader to guess whether it was in g cm⁻³.

**`NaN` gets its own message.** A NaN is not a missing value in the CSV sense —
it is a measurement that produced a number the arithmetic cannot interpret. It
compares `False` to everything, including itself, so it propagates silently
through a whole reduction and destroys the final statistic. Catching it at the
boundary is the cheapest possible place.

**A string gets rejected, with the repr visible.** `'2670'` is printed with
quotes, so the type error is obvious; had the function coerced the string with
`float()`, a downstream unit error would have been hidden.

## 3. The four clauses of `try`

```text
  reciprocal_velocity(3000.0)
    else: slowness = 3.333333e-04 s/m
    finally: this runs either way (closing files, releasing locks)
  reciprocal_velocity(0.0)
    except: velocity was zero
    finally: this runs either way (closing files, releasing locks)
```

- **`try`** holds the smallest possible amount of code — ideally one statement.
  A wide `try` is a bug magnet, because it catches exceptions from operations you
  did not intend to guard (see §5).
- **`except`** names the exception types you can actually handle. `except
  ZeroDivisionError` says "I know what to do when the velocity is zero". `except
  Exception` says "I do not know what can go wrong here", which is almost never
  true and always expensive.
- **`else`** runs when no exception occurred. It exists so that the code that
  should *not* be guarded is not inside the `try`. This is the clause everybody
  forgets and the one that keeps `try` narrow.
- **`finally`** runs either way. It is for releasing what you acquired: closing a
  file, deleting a temporary file, unlocking. Lesson
  [10](./10-context-managers-decorators.md) shows the same pattern as a context
  manager, which is almost always what you actually want.

Two idioms worth knowing. `raise ... from exc` preserves the causal chain when you
translate a low-level exception into a domain one, so the traceback shows both.
And `except SomeError as exc` binds the exception object, which is how you log
`exc.value` for a `DataError` instead of just its message.

## 4. The cost of swallowing an exception

Here is the most expensive line in scientific Python:

```python
try:
    total += float(text)
except ValueError:
    pass
```

The demo measures the two behaviours side by side:

```text
  with 'except ValueError: pass' -> total = 21.5
  with a counted skip            -> total = 21.5, skipped = 1
```

Both produced the number 21.5. Only the second reported that one third of the
input never entered the sum. The data were `["12.4", "oops", "9.1"]`, and
$12.4 + 9.1 = 21.5$ — a *correct* sum of a *wrong set of rows*.

Now scale it. In a catalogue of 10⁶ rows, a `pass` that fires once per row yields
a total that is not merely imprecise, it is a total of something else. In a
processing pipeline, a swallowed exception means the output has a different number
of samples than the input, and every downstream operation that assumes a fixed
trace length is now wrong. In an inversion, a swallowed exception means a residual
that is *smaller than it should be*, so the misfit looks better and the model is
accepted.

The rule is not "never catch". It is: **if you catch, then either handle it, or
count it, or re-raise it — and if you count it, report the count.** A pipeline
that prints `skipped 1 row (0.02%)` at the end has told you whether to trust the
result.

The related pattern to avoid is catching too much:

```python
try:
    value = anomaly(0.0, depth_km)      # depth_km is 0.5, meaning 0.5 km
except (TypeError, ValueError, ZeroDivisionError):
    pass
```

```text
  anomaly(0, 0.5) = 8.000000e+00 - a legal float, a wrong physics
```

No exception is raised at all, because nothing illegal happened: 0.5 is a
perfectly good float and `(0 + 0.25)**1.5` is a perfectly good denominator. The
bug is a *unit* bug, and no `except` clause anywhere can catch it. The defences
are a unit-carrying name (`depth_m`, not `depth`), a docstring that states the
unit, and a test with a known answer — which is exercise ★★★6 of this lesson and
the reason assertions exist in the first place.

**Broad `except` clauses create the illusion of robustness while converting loud
failures into quiet wrongness.** The demo's advice is the correct one: the defence
against a unit bug is a test, not a `try`.

## 5. Reading a traceback

A traceback is a *path*, and the path is the part people skip. The demo builds a
four-frame call chain and prints the frames as objects:

```text
  the call path, outermost first (4 frames):
    part6_traceback()  line 178:  outer(5.0)
    outer()  line 169:  return middle(n)
    middle()  line 172:  return inner(n)
    inner()  line 175:  return [0.0] * n[0]         # n is a float, not a sequence
  the exception: TypeError: 'float' object is not subscriptable
```

Read it in three steps.

1. **The last line is the symptom.** `'float' object is not subscriptable` means
   something wrote `x[0]` where `x` was a number. That is a fact about the
   immediate expression only.
2. **The last frame is the site.** `inner()` at line 175. The expression is right
   there.
3. **The frames above it are the diagnosis.** `outer(5.0)` was called with a
   scalar where a sequence was expected. The bug is not in `inner()` — `inner()`
   is behaving exactly as written — it is in the *caller's* assumption.

That is the general shape of every traceback bug: the crash site and the bug site
are different frames, and the frames in between are the evidence. In a real
symbolic-geophysics code base the chain may be twenty frames; the discipline is
the same — find the lowest frame whose arguments are already wrong, and that is
where to look.

Two improvements over printing raw tracebacks. `traceback.extract_tb` gives frames
as objects, so a log line can carry the function names and line numbers without an
absolute file path (which is machine-specific and, on a shared cluster, useless).
And a `try/except` that logs and *re-raises* preserves both the diagnosis and the
original traceback — use `raise` with no argument inside the handler.

## 6. Systematic debugging: the five questions

Debugging is not staring at code. It is bisection on the first point where the
expected and the observed diverge, and it has a procedure:

1. **What is the input, exactly, with its type and shape?**
2. **What is the expected output, and how do you know?** (A hand calculation, a
   physical limit, an analytic solution, a second implementation.)
3. **What did you actually get?**
4. **Where do the two first diverge?** Not "where is the bug" — *first* divergence.
5. **What is the smallest input that shows the divergence?** (Minimise it; small
   cases are diagnosable.)

The demo runs those five questions on a real off-by-one:

```text
  Task: mean of the first half of a 4-value list.
  data = [10.0, 20.0, 30.0, 40.0]
  naive (first half)   = 15.0
  buggy   (n//2+1)/(n//2) = 30.0  <- wrong, and plausible-looking
```

The buggy line slices three values but divides by two, giving 30.0 instead of
15.0. It looks plausible — it is a real number in the right range — and it survives
review because the arithmetic is not *obviously* wrong. The five questions catch it
at step 4: the slice and the divisor diverge in their notion of "half". The
minimal test is n = 4, as the demo says; n = 3 would give 2.0 versus 25.0 and be
just as diagnostic.

Two habits that make this procedure cheap:

- **Print the intermediate quantities, with units.** A debugger is often slower
  than five `print` statements carrying `f"{depth_m:.3f} m"`.
- **Compare against a second implementation.** The module's complete program
  checks its $b$-value estimator against a Monte-Carlo mean of a known input
  $b$ — an independent route to the same answer. In this module you already have
  two implementations of every forward model: the documented code and the equation
  in the lesson.

## 7. Physical interpretation: why a swallowed exception changes the physics

This is the part of the lesson that is not about programming practice.

A geophysical reduction is a *chain of physical statements*: this sample's
amplitude, this station's elevation, this event's magnitude, this rock's density.
Each link is a quantity with a unit and an uncertainty. An exception is the
program's way of saying "this link is not what it appears to be". Swallowing it
does not remove the defect from the physics; it removes the *evidence* from the
result.

Three concrete mechanisms.

**Silent row loss biases by selection.** The rows that fail to parse are not a
random sample. A magnitude that failed to parse is more likely to be a
`-` placeholder, a blank field or a precision glitch, and those correlate with
specific events, networks or epochs. The surviving set is a biased sample, and the
resulting $b$-value or heat-flow average is biased in a direction you cannot
estimate without knowing what was dropped.

**Swallowed exceptions change the denominator.** A mean computed over the rows
that happened to parse is a mean over a different sample than the one you
intended. Now the statistic and its uncertainty belong to different populations,
and the confidence interval is meaningless.

**An impossible value is a detector.** 30,000 kg m⁻³ is not a data-entry error; it
is almost certainly a unit error somewhere upstream (g cm⁻³ read as kg m⁻³, or a
m³ read as cm³). A validator that raises on it has found a bug three steps earlier
than any downstream symptom would. That is why the density thresholds in §2 are
*physical* thresholds — osmium's density is a fact about the periodic table, not a
matter of taste — and why a good scientific program asserts physical invariants
everywhere cheaply possible.

## 8. Assumptions and limits

1. **Assertions vanish under `-O`.** Anything that must happen for correctness
   must not be an assertion. This is a language guarantee, so it can be relied on
   (and it is why a validation check written as an `assert` is a real bug).
2. **Exceptions cost time.** Raising and catching is far more expensive than a
   branch — microseconds versus nanoseconds. In a 10⁶-row loop, using exceptions
   for ordinary control flow is measurably wrong; use them for the exceptional
   case and a branch for the common one.
3. **The density thresholds are physical facts about elements**, but "denser than
   iron is a warning" is a *convention* for crustal rock. A mantle or core context
   would move it, which is why the threshold is a named constant with a comment
   rather than a literal.
4. **A traceback is not a reproducible report.** It contains file paths and
   process state; what belongs in a log line is the frame names, line numbers and
   values.
5. **Validation cannot detect a unit bug.** §5's `anomaly(0, 0.5)` is the proof:
   no type is wrong and no invariant is violated. Only a dimensional check or a
   test with a known answer catches it.
6. **The demo's traceback is generated by calling deliberately wrong code.** It is
   the module's own construction, not a record of a real incident.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 errors_debugging_demo.py
```

The demo is seven sections of *deliberate misbehaviour*, which is worth noting: a
lesson about error handling has to generate errors, and generating them on purpose
in a scratch directory is far better than meeting them in a production run.

## 10. Common mistakes

1. **`except Exception: pass`.** §4. The most expensive line in the file.
2. **A validation check written as an `assert`.** It disappears under `-O`.
3. **An assertion with no message.** The failure gives you a line number and
   nothing else.
4. **A `try` block containing ten statements.** Nobody can say which one raised.
5. **Catching an exception and raising a different one without `from`.** The cause
   is discarded.
6. **Using exceptions for ordinary control flow.** Correct, and slow.
7. **Comparing a `NaN`.** `x == float('nan')` is always `False`; use
   `math.isnan`.
8. **Returning a default value instead of raising** (`return 0.0` on a parse
   failure). A zero is a datum; a failure is not.
9. **Debugging by editing.** Change one thing, re-run, compare — otherwise you
   cannot attribute the change.
10. **Trusting a plausible number.** The 30.0 above is plausible. `math.isclose`
    against an independent implementation is what makes a number trustworthy.

## 11. Real-world applications

- **Catalogue ingestion** is the canonical validation pipeline: parse, validate
  against physical ranges (magnitude, depth, latitude ±90), count and report
  rejections, and only then compute.
- **Instrument data QC.** Clipping, dead channels, timing glitches and saturation
  are detected by range and continuity assertions on the raw series, before any
  processing — the theme of module
  [20 Signal Processing](../../20-signal-processing/README.md).
- **Numerical solvers.** Every iterative solver asserts that its residual
  decreases and that its state stays finite; a NaN appearing at iteration 400 is a
  stability problem, and the assertion tells you *where* rather than letting the
  NaN propagate to the output.
- **Reproducible pipelines.** A stage that reports "read 1,000,000 rows, skipped
  0, wrote 1,000,000" is auditable; one that reports "done" is not.

## 12. Further reading

- USGS earthquake catalogue web service — [earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/):
  a real service whose responses need exactly the validation this lesson teaches,
  because magnitudes, depths and coordinates arrive as strings with documented
  ranges.
- NIST CODATA fundamental constants — [physics.nist.gov/cuu/Constants/](https://physics.nist.gov/cuu/Constants/):
  each constant carries an uncertainty and a unit, the model to imitate when
  deciding what an exception message must contain.

## 13. Related lessons

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  where validation lives in a module, and the self-test convention.
- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — the source
  of the bad rows counted in §4.
- [03-01-10 Context Managers, Decorators and Functional Idioms](./10-context-managers-decorators.md)
  — `finally` as a context manager, and a retry decorator built from `except`.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — turning this lesson's assertions and known-answer tests into a suite.
- [21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — how silently dropped rows bias a result, quantitatively.

## 14. Exercises

[`exercises/07-errors-and-debugging-exercises.md`](./exercises/07-errors-and-debugging-exercises.md) —
nine problems, ★ to ★★★. Problem ★★5 requires the counted-skip numbers;
problem ★★6 is the unit-bug problem the demo sets up, in which no exception is
raised and only a known-answer test finds the error; problem ★★★7 asks you to
write a validator for a layered velocity model whose physical bounds you must
derive.

## 15. Self-assessment checklist

- [ ] I can state the difference between an assertion and a validation check, and
      say what happens to each under `python3 -O`.
- [ ] I can write a custom exception carrying field, value, unit and reason.
- [ ] I can explain why a density above osmium's is an error while a density above
      iron's is only a warning.
- [ ] I can use all four clauses of `try` for their intended purposes.
- [ ] I can explain what a counted skip reports that `pass` does not.
- [ ] I can read a four-frame traceback and identify the *caller* as the bug site.
- [ ] I can apply the five debugging questions to a small numeric discrepancy and
      find the first divergence.
- [ ] I can name three mechanisms by which silently dropped rows bias a result.
