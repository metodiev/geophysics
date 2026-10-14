# Module 03-01 — Python Programming Fundamentals

**Stages:** beginner → advanced · **Prerequisites:** the orientation folder,
specifically
[00-02-01 The Master Map of the Curriculum](../../00-orientation/02-curriculum-map/01-master-map.md)
for where this module sits, and
[00-03-02 Setting Up the Environment](../../00-orientation/03-how-to-use-this-repo/02-environment-setup.md)
for getting an interpreter that runs the demos.

This module treats a program as a **scientific instrument**: something with a
specification, a calibration, a precision, a failure mode and a cost. It is the
only module in the folder that uses **nothing but the Python standard library**,
and that is a deliberate design decision rather than an accident of scope.

Two reasons. First, the standard library is always present, so every demo here
runs on any installation, in five years, on any platform — the calibration of
the instrument does not depend on a package index being reachable. Second, and
more important, **the libraries hide exactly the things this module is about**:
NumPy hides the loop, pandas hides the type conversion, ObsPy hides the file
format. You cannot reason about loop-invariant hoisting if a library has already
vectorised the loop away, and you cannot debug an encoding error that was
silently swallowed by a reader. Learn the layer underneath once, and every
library in modules 02–13 becomes transparent.

The module also builds **one complete program**, in pieces, across ten lessons:
[`code/catalog_report.py`](./code/catalog_report.py) writes a synthetic
earthquake catalogue, streams it back, computes a magnitude-frequency
$b$-value with a Monte-Carlo uncertainty, formats a report, writes it
atomically, reads it back and verifies it. Lesson 04 introduces the functions,
lesson 06 the file I/O, lesson 09 the streaming reader and lesson 10 the
decorators and the atomic write. When you reach the end of the module you have
assembled it, and you have run it.

## Learning objectives

By the end of this module you will be able to:

1. **Explain** why Python is the working language of the geosciences, what the
   ecosystem's divisions of labour are, and what the standard library alone can
   already do.
2. **Reason** about types and representations: integers are exact, `float64` is
   IEEE-754, `0.1 + 0.2 != 0.3`, and a 53-bit mantissa is why a gravity survey
   resolves part in 10⁹ while a coordinate has a hard floor at the metre.
3. **Write** conditionals and loops that express a survey reduction, and decide
   which quantities are loop-invariant — the same judgement that decides what may
   be hoisted, vectorised or parallelised later.
4. **Package** a formula as a named, documented, importable function inside a
   module, with default arguments used safely and scope understood.
5. **Choose** a container on the evidence of complexity: measure an O(n) list
   scan against an O(1) dictionary lookup, and state why a nested O(n²) pass
   cannot be rescued by optimisation.
6. **Read and write** real text data: delimited files with quoted fields, UTF-8
   versus Latin-1, byte-order marks, and the `\r\n` that breaks a naive parser.
7. **Use** assertions as physical sanity checks, design exceptions that carry the
   offending value, and debug by bisecting the *first divergence* rather than by
   staring.
8. **Decide** when a class earns its place (state plus invariants) and when a
   function or a dataclass is the better instrument.
9. **Stream** a large file with a generator pipeline, and measure the memory
   difference against loading it.
10. **Wrap** work in context managers and decorators so that bookkeeping — closing
    a file, timing a call, publishing a result atomically — is written once and
    cannot be forgotten.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Why Python for Geophysics: The Scientific Ecosystem](./01-why-python.md) | beginner | The standard library is already a scientific instrument; libraries add speed and breadth |
| 02 | [Types, Variables, Expressions and Operator Semantics](./02-types-and-variables.md) | beginner | A `float` is a 53-bit binary rational, and that decides what a survey can resolve |
| 03 | [Conditionals, Loops and Loop-Invariant Reasoning](./03-control-flow.md) | beginner | The loop-invariance test is a correctness tool first and a speed tool second |
| 04 | [Functions, Scope, Modules and Packages](./04-functions-modules.md) | beginner | A formula becomes an instrument when it is named, documented, importable and tested |
| 05 | [Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md) | beginner | The container decides whether the script finishes; O(n²) is a scaling error, not a slowdown |
| 06 | [Files, Text I/O and Data Encodings](./06-files-and-io.md) | beginner | Bytes on disk are not characters in memory, and a silent mojibake is worse than a crash |
| 07 | [Exceptions, Assertions and Systematic Debugging](./07-errors-and-debugging.md) | intermediate | An assertion is a physical statement; a swallowed exception is a result you cannot trust |
| 08 | [Classes, Objects and When Not to Use OOP](./08-classes-and-oop.md) | intermediate | A class is justified by invariants and shared state, not by the existence of data |
| 09 | [Iterators, Generators and Lazy Evaluation for Large Data](./09-iterators-generators.md) | intermediate | A generator pipeline has a memory cost that does not grow with the file |
| 10 | [Context Managers, Decorators and Functional Idioms](./10-context-managers-decorators.md) | advanced | Write the bookkeeping once, and make the failure mode part of the design |

Lesson 05 is the module's **mastery lesson**: if you can state, for any task, the
container you would use and its complexity, you have the skill that the rest of
the folder assumes. Lesson 10 is the lesson that assembles the complete program.

## Suggested path

**If you are new to programming:** all ten lessons in numeric order, typing every
demo. Expect lessons 02, 05 and 06 to take twice as long as their length
suggests, because they are where the mental model is built rather than extended.
Do the exercises — the module's exercises are graded ★ (foundational), ★★
(applied) and ★★★ (research-oriented), and the ★★★ problems in lessons 05, 07 and
09 are the ones that mirror the mistakes professional code actually makes.

**If you already program but are new to Python:** start at
[02](./02-types-and-variables.md) and read [03](./03-control-flow.md) quickly,
then take [05](./05-data-structures.md), [06](./06-files-and-io.md) and
[09](./09-iterators-generators.md) carefully — those three hold the Python-specific
idioms that a programmer from C, Fortran, MATLAB or Java has to unlearn
something to acquire. Skip nothing in [07](./07-errors-and-debugging.md): the
assertion discipline there is what makes the later modelling modules verifiable.

**If you are here for a later folder:** read [01](./01-why-python.md) §3–§5 and
[10](./10-context-managers-decorators.md), then move to
[03-02 NumPy](../02-numpy/README.md). Come back to
[05](./05-data-structures.md) and [09](./09-iterators-generators.md) the first
time a script is too slow or runs out of memory, which will be sooner than you
expect.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-why-python.md`](./01-why-python.md) … [`10-context-managers-decorators.md`](./10-context-managers-decorators.md) | The ten lessons |
| [`exercises/01-why-python-exercises.md`](./exercises/01-why-python-exercises.md) … [`exercises/10-context-managers-decorators-exercises.md`](./exercises/10-context-managers-decorators-exercises.md) | Ten problem sets, ★ to ★★★ |
| [`exercises/01-why-python-solutions.md`](./exercises/01-why-python-solutions.md) … [`exercises/10-context-managers-decorators-solutions.md`](./exercises/10-context-managers-decorators-solutions.md) | Full worked solutions with the numbers |
| [`code/geophys_core.py`](./code/geophys_core.py) | The module's shared standard-library library: gravity, geometry, statistics, with a self-test |
| [`code/velocity_lib.py`](./code/velocity_lib.py) | The worked example of a reusable, testable module (lesson 04) |
| [`code/catalog_report.py`](./code/catalog_report.py) | **The complete program**: data in, geophysics computed, report out, verified |
| [`code/*.py`](./code) | One runnable demo per lesson, standard library only |

Every demo prints its own numbers; the lessons quote the real output. Run them
from inside `code/`:

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 catalog_report.py
```

## What "standard library only" costs you

Honesty demands the counterweight. Pure Python is roughly one to two orders of
magnitude slower than compiled numeric loops, and the demos here are small on
purpose because of it. The module's own measurements make the point: a
2,000-station list scan and a 20,000-lookup dictionary differ by a factor of
about 500 on a re-run, and a 4.5 × 10⁶-comparison nested loop costs about 65 ms in
this interpreter — a number that becomes about 72 s at 10⁵ stations. That is the
quantitative case for module 02, and it is a case about *scale*, not about
correctness. The standard-library version of a gravity model is exactly as
accurate as the vectorised one, because both use `float64` throughout.

## Common pitfalls across this module

1. **Comparing floats for equality.** Use `math.isclose`; `0.1 + 0.2` is not
   `0.3`, and neither is any rounded measurement value.
2. **`4 / 3` written as `4 // 3`.** A 25 per cent error in a source mass that
   looks like a formatting choice.
3. **A mutable default argument.** The default list is created once and then
   shared by every call.
4. **The wrong container.** A list where a dictionary belongs turns a linear
   algorithm into a quadratic one, and no amount of tuning recovers it.
5. **`except Exception: pass`.** The single most expensive line in scientific
   code: it converts a crash into a wrong number.
6. **Assuming UTF-8.** Or assuming Latin-1, or forgetting the BOM. Decode
   explicitly, and never in "ignore" mode.
7. **Materialising a file you only needed to scan.** `readlines()` on a 10 GB
   file is a decision, and usually the wrong one.
8. **A class with no invariant.** If every field is settable to anything at any
   time, the class is a dictionary with extra typing.
9. **Timing a function once.** Wall-clock time on a laptop varies by tens of per
   cent; the module's benchmarks use enough repetitions to mean something, and
   each lesson says which measurement it quotes.
10. **Using a nominal rock property as if it were measured.** Density, velocity
    and conductivity vary by factors between rocks, not by percentages.

## Related lessons in other folders

- [01-01-04 Floating Point Representation and Rounding](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — the mathematics behind lesson 02 here.
- [01-12 Numerical Methods](../../01-mathematics/12-numerical-methods/README.md)
  — the methods SciPy implements in module 03.
- [02-01-01 Physical Quantities and SI Units](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md)
  — the units every variable name in this module carries.
- [03-02 NumPy](../02-numpy/README.md) — the direct sequel: the same problems,
  vectorised, and the measurement of how much it buys.
- [03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
  — where this module's assertions and self-tests become a proper test suite.
