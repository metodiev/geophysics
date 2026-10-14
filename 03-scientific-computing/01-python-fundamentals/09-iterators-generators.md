---
id: 03-01-09
title: "Iterators, Generators and Lazy Evaluation for Large Data"
level: intermediate
prereqs: ["03-01-06"]
estimated_minutes: 75
tags: [generators, iterators, lazy-evaluation, memory, streaming]
---

# Iterators, Generators and Lazy Evaluation for Large Data

A 200,000-row catalogue is 7.7 MB and fits comfortably in memory. A 10⁸-sample
continuous waveform record does not: as a Python list it is tens of gigabytes
before any processing happens. The difference between a pipeline that handles the
first and one that handles the second is not a faster computer. It is *when* the
data comes into existence — and that is what a generator controls.

This lesson is about memory as a first-class design constraint. The demonstration
processes the same 200,000 rows twice, once eagerly and once lazily, and measures
the peak allocation of each with `tracemalloc`: 48.87 MB against 0.15 MB, for the
same answer.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the iterator protocol — `iter`, `next`, `StopIteration` — and
   explain why a `for` loop is that protocol.
2. **Write** a generator function, explain what the `yield` statement does to the
   function's execution, and demonstrate its laziness.
3. **Compose** a pipeline of generators that reads, parses, filters and reduces a
   file with a peak memory cost independent of the file size.
4. **Measure** the peak memory of an eager and a lazy version with `tracemalloc`,
   and state what the measurement does and does not include.
5. **Use** generator expressions and `itertools.islice` to take a finite prefix of
   an infinite sequence.
6. **State** the single-use limitation of a generator and the two legitimate
   responses to it.

## Prerequisites

- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — the file
  the pipeline reads.

## 1. The iterator protocol

An **iterable** is anything you can loop over. An **iterator** is the cursor that
does the looping, and it implements exactly two operations:

```text
  iter([10, 20]) -> <list_iterator object at 0x100d980d0>
  next(values)   = 10.0
  next(values)   = 20.0
  next(values)   -> StopIteration: StopIteration()
```

`iter(obj)` returns an iterator; `next(it)` returns the next value or raises
`StopIteration`. A `for` loop is precisely this: call `next` until `StopIteration`,
then swallow the exception. Nothing else in this lesson is a new idea — every
generator is a way of producing a `next` that holds state between calls.

Two consequences follow immediately and they explain most generator behaviour:

- **An iterator is a cursor, not a container.** It points at a position in a
  sequence; it does not hold the sequence. Storing an iterator therefore stores a
  position, not data.
- **Iterating consumes.** Once the cursor is past an element, the element is gone
  from the iterator's point of view. This is why a generator can be traversed only
  once (§7).

The practical significance for geophysics is that a file *is* an iterable of
lines. `for line in handle` does not read the file; it asks the operating system
for one line at a time. The generator pipeline in this lesson is just that fact,
composed four times.

## 2. Worked walkthrough: laziness, made visible

A function containing `yield` is a *generator function*: calling it does not run
the body at all, it returns a generator object. The demo prints its way through
one:

```text
  defining the generator...
  generator created; no body has run yet
    [generator body entered]
    [yielding 0]
  first next()  -> 0
    [yielding 1]
  second next() -> 1
  only two of the three yields have happened: the function is
  suspended at the second yield, holding its own local state.
    [yielding 2]
  remaining     -> [2]
```

Read the interleaving. `counting(3)` produced no `[generator body entered]` line —
the body had not started. `next(gen)` ran the body until the first `yield` and then
*suspended* it, keeping the local variable `i` alive. The second `next` resumed
from exactly there.

Three properties fall out:

- **Work is deferred until it is asked for.** Nothing expensive happens at call
  time, which means a generator's cost is paid by whoever consumes it, and a
  generator that is created and never consumed costs nothing.
- **State lives in the suspended frame.** The loop variable, the open file
  handle, the running totals — all persist between `next` calls without any
  explicit object to hold them.
- **The function's local state is the pipeline's state.** This is why a chain of
  generators needs no shared mutable buffer: each stage holds its own position.

The deferred-work property is also a hazard. A generator that opens a file and is
never exhausted leaves the file open until it is garbage-collected. **That is the
one scenario in which laziness is worse than eagerness**, and the correct defence
is to consume generators in a `with` block, as §3 does, or to close them
explicitly.

## 3. Worked walkthrough: a four-stage pipeline

The demo's pipeline is four small generators composed into one expression:

```python
def iter_lines(path):        # yield non-comment lines
def iter_records(lines):     # yield parsed tuples, skipping the header
def select(records, mc):     # yield records with magnitude >= mc
def depths(records):         # yield the depth field

def pipeline(path, mc):
    return depths(select(iter_records(iter_lines(path)), mc))
```

Consuming it gives:

```text
  catalogue: synthetic_big_catalogue.csv, 7.7 MB, 200,000 rows
  selecting magnitudes >= 2.0
  selected   : 50,561 events in 0.07 s
  mean depth : 30.523 km
```

Fifty thousand events selected out of two hundred thousand, in 0.07 s, with a
memory footprint of one row. Three design points are worth naming.

**Each stage does one thing.** `select` is four lines; `depths` is three. A stage
that both filters and computes is a stage you cannot test or reuse; splitting them
costs nothing, because the composition is free.

**The header is skipped by position, not by guessing.** `iter_records` skips
`index == 0` rather than testing whether each field is numeric. Guessing is how a
real event whose ID happens to look numeric gets silently dropped — and *that* is
a data-integrity failure, not a style issue. The demo's comment says so.

**The pipeline is lazy all the way down.** Calling `pipeline(path, mc)` opens no
file. The file is opened when the first `next` is requested, which is inside the
`for` loop at the bottom of the pipeline expression. This is worth verifying
yourself: call `pipeline(...)` and print nothing, then check that no file handle
was opened.

## 4. Worked walkthrough: peak memory, measured

The measurement is the lesson's central evidence. Both versions compute the same
mean depth; `tracemalloc` reports the peak allocation during each:

```text
  eager  : peak    48.87 MB, mean depth 30.522816 km
  lazy   : peak     0.15 MB, mean depth 30.522816 km
  ratio  : 325x less memory
  absolute difference in the mean: 3.45e-13 km  (1.1e-14 relative)
  agrees to 1e-12 relative: True
```

**The memory ratio is 325×, and it scales.** The eager version materialises
200,000 tuples of five elements; the lazy one holds one tuple plus the running
totals. At 10⁶ rows the eager peak is five times larger and the lazy peak is
unchanged. That is what "O(1) in the file size" means in practice, and it is the
single most important sentence in this lesson.

**The results agree to fourteen digits, and not exactly — and the reason is
instructive.** The eager version sums the depths in the order of a first pass
followed by a separate selection pass; the lazy version sums them in selection
order. Floating-point addition is not associative, so the two partial sums round
differently and the difference is $3.45\times10^{-13}$ km — a relative difference
of $1.1\times10^{-14}$, about one ulp of the total. Both are correct to every digit
that matters, and neither is "the" answer. This is lesson
[02](./02-types-and-variables.md)'s accumulation argument appearing as a
reproducibility caveat: **if you change the order in which a pipeline reduces, you
change the last two digits of the result, and that is not a bug.**

**`tracemalloc` measures what the demo says it measures.** It counts Python-level
allocations tracked by the interpreter, so the numbers are indicative rather than
exact, and the true process footprint includes the interpreter, the imported
modules and any buffers the operating system holds. Read the *ratio* and the
*scaling*, not the absolute megabytes.

## 5. Generator expressions, `islice` and `yield from`

```text
  generator expression : <generator object part5_expressions.<locals>.<genexpr> at 0x1059609b0>
  sum of squares       : 140
  islice on an infinite generator: [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
  yield from          : [1.0, 2.0, 3.0, 4.0]
  flatten(3 groups)   : [1, 2, 3, 4, 5]
```

**A generator expression** is a list comprehension with parentheses: `sum(x*x for x in range(8))` is $140$ without ever building a list. Use it whenever a comprehension is immediately reduced (`sum`, `max`, `min`, `any`, `all`) or immediately consumed.

**`itertools.islice`** takes a finite prefix of an infinite generator. The demo's
`magnitudes_infinite()` never terminates — a magnitude sequence that increases by
0.1 forever — and `islice` pulls the first ten. This is the idiom for a synthetic
or streaming source with no natural end: a continuously sampled instrument, a
Monte-Carlo loop, a random catalogue generator. **Never call `list()` on an
unbounded generator**; the `islice` is the boundary that makes it finite.

**`yield from`** delegates to a sub-iterable without writing the inner loop. It is
the right tool for a generator that concatenates several sources, and it also
forwards `send` and `throw` correctly, which a hand-written loop does not.

The `flatten` example is the pattern to remember for nested data: a list of
groups becomes a flat stream with two generators and no intermediate list, which
is exactly what a catalogue of per-station traces needs.

## 6. Worked walkthrough: streaming the module's complete program

The complete program, [`code/catalog_report.py`](./code/catalog_report.py),
applies this lesson's pattern to its own reader:

```python
def iter_catalogue(path):
    """Yield one typed dict per event, streaming the file a line at a time."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(
            line for line in handle if not line.startswith("#"))
        for row in reader:
            yield {
                "event_id": row["event_id"],
                "latitude": float(row["latitude"]),
                # (depth_km and magnitude follow in the same form)
            }
```

Four separate lessons are visible in nine lines: the explicit encoding and
`newline=""` of lesson [06](./06-files-and-io.md), the comment-filter generator
expression of this lesson, the typed-record conversion that refuses to let a
string reach the arithmetic, and the `with` block that guarantees the file is
closed whether the consumer exhausts the generator or abandons it. It is worth
reading the program's `scan()` function next: one pass over the generator produces
counts, extremes, sums, a distance histogram and a spatial statistic, because a
single pass is all a stream allows — and a single pass is all a stream needs.

## 7. Physical interpretation: memory is part of the experiment design

Choosing between eager and lazy is not a programming preference. In geophysics it
is a decision about what experiment you can run.

**A 10⁸-sample record is 0.8 GB of `float64` in a *contiguous* array**, and
considerably more as a Python list of boxed floats. A pipeline that materialises
it needs a machine with several gigabytes free; a streaming pipeline needs a few
kilobytes and works on a laptop. The scientific consequences are real: a
preprocessing step that cannot run on a field laptop cannot be applied in the
field.

**Streaming forces a single pass, and a single pass forces you to state your
statistics in advance.** If you do not know which columns you need, you cannot
stream efficiently; the discipline of declaring the reduction up front (count,
sum, extremes, histogram) is the same discipline that makes a reduction
reproducible. The complete program's `scan()` computes six quantities in one pass
precisely because a second pass would mean re-opening the file.

**Memory and time trade against each other, and the trade is measurable.** The
lazy pipeline in the demo took 0.07 s and 0.15 MB; the eager one took a comparable
time and 48.87 MB. Laziness buys memory, not speed — and on a machine where the
file is in the page cache, both are I/O-bound. Where laziness wins decisively is
*scale*: at 10⁸ rows the eager version is not slower, it is impossible.

**And laziness has one real cost, which must be managed.** A generator tied to an
open file that is never exhausted holds the handle. In a long-running service that
processes many files, this is a file-descriptor leak. The defence is structural:
consume generators inside `with` blocks, or make the generator itself own the
resource (as `iter_catalogue` does, with the `with` inside the generator body, so
that the handle lives exactly as long as the generator's frame).

## 8. Assumptions and limits

1. **Generators are single-use.** §1. Re-iterating an exhausted generator yields
   nothing, silently. The two responses are to re-open the source (cheap for a
   file, and what the demo does) or to materialise deliberately (`list(...)`), and
   to write a comment saying which you chose and why.
2. **The peak-memory comparison is a `tracemalloc` measurement of Python-level
   allocations.** It excludes the interpreter, imports and OS buffers; the ratio
   and the scaling are the transferable facts.
3. **The 200,000-row file is synthetic** with a fixed seed, so its 50,561 selected
   events and 30.523 km mean depth are properties of the generator.
4. **Laziness does not make anything faster.** It bounds memory. A pipeline that is
   I/O-bound remains I/O-bound; a pipeline that is compute-bound remains
   compute-bound and may be marginally slower because the interpreter moves
   between frames more often.
5. **Generator expressions and `itertools` are no substitute for array
   operations.** For elementwise arithmetic on numeric arrays, vectorisation
   (module [03-02](../02-numpy/README.md)) is both faster and more compact; the
   generator idiom is for *streams* — files, networks, unbounded sequences — where
   an array cannot exist.
6. **Debugging a lazy pipeline is harder than debugging an eager one.** The
   traceback of a generator shows the consuming frame, not the stage that raised,
   unless you keep the stages as named functions so the frames appear.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 iterators_generators_demo.py
```

The script writes a 7.7 MB synthetic catalogue into a `_scratch_gen` directory,
processes it four ways, and removes the directory on exit. Change `N_EVENTS` to
2,000,000 and re-run if you want to see the eager peak grow while the lazy one
does not — that is the demonstration that the measurement is about scaling rather
than about this particular file.

## 10. Common mistakes

1. **`list(gen)` on a large stream.** The eager peak, dressed as a convenience.
2. **Consuming a generator twice.** The second pass silently yields nothing.
3. **An unbounded generator without `islice`.** `list()` on an infinite source
   hangs, and correctly so.
4. **A generator holding an unclosed resource.** Consume it, or own the resource
   inside it with a `with`.
5. **Returning a generator where a list is needed.** A function annotated `->
   list` that returns a generator will fail a `len()` call three modules later.
6. **Reaching into a pipeline stage.** A generator has no public state; if you
   need the intermediate result, assign it inside a `for` loop or add a stage.
7. **Assuming laziness is faster.** Measure; it is a memory optimisation.
8. **Deeply nested generator expressions.** Readable at one level of nesting,
   opaque at three; use named generator functions.
9. **Mixing eager and lazy in one reduction.** `len(list(x))` is both.
10. **Forgetting that `zip` and `enumerate` are also lazy.** They are; the same
    consumption rules apply to them and to `map`/`filter`.

## 11. Real-world applications

- **Continuous waveform archives.** A day of a 100 Hz broadband channel is
  8.6 × 10⁶ samples; a station-year is 3 × 10⁹. Streaming is the only way to
  scan such an archive for a detection statistic, and it is what ObsPy's
  read-and-process workflows do under their convenience APIs
  ([docs.obspy.org](https://docs.obspy.org)).
- **Large event catalogues.** The USGS event service
  ([earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/))
  returns text that streams naturally; a generator pipeline computes a
  magnitude-frequency distribution without holding the catalogue.
- **Gridded data at scale.** netCDF files are read in chunks; xarray's lazy
  loading is the same idea with a labelled index (module
  [03-08](../08-gridded-geospatial-data/README.md)).
- **Monte-Carlo and bootstrap.** An infinite generator of synthetic realisations,
  bounded by `islice` or accumulated in a running estimate, is the standard shape;
  so is a random catalogue for method testing.
- **Log and metadata scanning.** Finding the calibration block in a decade of
  instrument logs is a streaming filter, not a load.

## 12. Further reading

- ObsPy — [docs.obspy.org](https://docs.obspy.org): `read()` with a time window,
  and the streaming/preprocessing workflows built on it; module
  [03-10](../10-obspy-and-seismic-data/README.md).
- NumPy — [numpy.org](https://numpy.org): the opposite strategy for in-memory
  numeric work, and `numpy.memmap` for the case where an array is larger than
  memory; module [03-02](../02-numpy/README.md).
- NOAA National Centers for Environmental Information — [www.ncei.noaa.gov](https://www.ncei.noaa.gov):
  archives whose size is the reason streaming exists.

## 13. Related lessons

- [03-01-06 Files, Text I/O and Data Encodings](./06-files-and-io.md) — the reader
  that the pipeline wraps.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md)
  — the eager alternative, and its cost.
- [03-01-10 Context Managers, Decorators and Functional Idioms](./10-context-managers-decorators.md)
  — the resource discipline a generator needs.
- [03-08 xarray, netCDF, and Gridded Earth Data](../08-gridded-geospatial-data/README.md)
  — lazy loading with labels and chunks.
- [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md)
  — streaming pipelines over archives that do not fit anywhere.

## 14. Exercises

[`exercises/09-iterators-generators-exercises.md`](./exercises/09-iterators-generators-exercises.md) —
eight problems, ★ to ★★★. Problem ★★4 requires the measured memory numbers;
problem ★★★7 asks you to convert a two-pass eager script into a single-pass
streaming one, and problem ★★★8 to prove the two agree to floating-point
tolerance — the same
argument the demo's 3.45 × 10⁻¹³ km makes.

## 15. Self-assessment checklist

- [ ] I can describe the iterator protocol and explain a `for` loop in terms of it.
- [ ] I can explain what `yield` does to a function's execution and state.
- [ ] I can compose a four-stage generator pipeline over a file.
- [ ] I have reproduced a measured peak-memory ratio of several hundred between
      eager and lazy processing of the same data.
- [ ] I can explain why the two means differ in the last two digits, and why that
      is not a bug.
- [ ] I can take a finite prefix of an infinite generator with `islice`.
- [ ] I can state the single-use limitation and name the two legitimate responses.
- [ ] I can say why laziness is a memory optimisation rather than a speed one.
