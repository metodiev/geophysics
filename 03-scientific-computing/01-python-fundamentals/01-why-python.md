---
id: 03-01-01
title: "Why Python for Geophysics: The Scientific Ecosystem"
level: beginner
prereqs: ["00-02-01", "00-03-02"]
estimated_minutes: 75
tags: [python, scientific-computing, ecosystem, reproducibility]
---

# Why Python for Geophysics: The Scientific Ecosystem

A geophysical result is a chain: a measurement, a reduction, a model, an
inversion, a figure and a number in a paper. Every link in that chain is
computation, and the strength of the chain is set by its weakest link — which is
almost never the physics. It is a unit that was assumed, a file that was decoded
with the wrong encoding, a distance that was computed on a sphere when the
question needed an ellipsoid, or a loop that silently dropped the rows it could
not parse.

This module is about the *instrument* that does the computing. And the first
question about any instrument is not "what does it cost?" but "what does it
claim to measure, and how would I know if it were lying?"

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the five properties that make a piece of scientific code an
   instrument: specification, calibration, precision, failure mode and cost.
2. **Describe** what the Python standard library already provides for scientific
   work, and what it does not.
3. **Name** the divisions of labour in the scientific Python ecosystem, and say
   which one solves which class of problem.
4. **Write** and run a complete gravity forward model using nothing but the
   standard library, and quote its actual output.
5. **Estimate** the cost of a pure-Python numeric loop from a measurement, and
   decide when that cost is the reason to move to an array library.
6. **Explain** why "the standard library is slower" is a performance claim and
   not a correctness claim.

## Prerequisites

- [00-02-01 The Master Map of the Curriculum](../../00-orientation/02-curriculum-map/01-master-map.md)
  — where this folder sits and what depends on it.
- [00-03-02 Setting Up the Environment](../../00-orientation/03-how-to-use-this-repo/02-environment-setup.md)
  — a working `python3` and how to run a script from a terminal.

You need no prior programming experience for this module. You do need to be able
to open a terminal, change directory and run `python3 something.py`. Every demo
in this module works that way.

## 1. Five properties of a scientific instrument

Before any syntax, fix the vocabulary. When you write code that computes a
geophysical quantity, you are building an instrument, and instruments are judged
on five things.

| Property | For a gravimeter | For a Python program |
|---|---|---|
| Specification | Measures vertical gravity acceleration, range ±10 000 mGal | Computes the vertical anomaly of a buried sphere of excess density $\Delta\rho$ |
| Calibration | Known mass, known spring constant | A test with an analytically known answer |
| Precision | Repeatability, drift, resolution | The number of surviving digits, set by `float64` |
| Failure mode | Tilt, temperature, tares, clipping | Bad input, wrong units, silent `except`, overflow |
| Cost | Weight, power, time per station | Seconds per station, bytes per sample |

The interesting column is the middle one. A specification that is one sentence
long is a specification worth trusting; a specification that is "it computes
gravity" is not a specification at all. In the demo below the specification is:
*given a sphere of radius $a$, excess density $\Delta\rho$ and centre depth $z$,
return the vertical gravity anomaly at surface offset $x$*. Three parameters in,
one number out, one assumption stated. That is a testable object.

The fourth property, failure mode, is the one beginners skip and the one that
costs the most. A library call that raises an exception is a gift. A library call
that returns `0.0` for a row it could not parse is a liability, and the compute
time you saved by not checking will be spent three months later explaining why a
survey line is 3 per cent low.

## 2. What Python is, in four facts

Python is a language *specification* and a reference *implementation*. The
implementation you will almost certainly be using is CPython, which compiles
source to bytecode and interprets it. Four consequences matter for scientific
work:

1. **It is interpreted, so it is slower per operation than compiled code.** The
   interpreter's work — type dispatch, reference counting, bytecode — happens on
   every operation. For a kernel of ten floating-point operations, that overhead
   dominates: 170 ns per station in the demo below, where the arithmetic itself
   is a few nanoseconds.
2. **It is dynamically typed, so types travel with values, not variables.** A
   name can hold a `float` now and a `str` later. This is enormously convenient
   for exploratory work and is why validation matters: nothing in the language
   prevents a station name from reaching a division.
3. **It has arbitrary-precision integers and IEEE-754 doubles by default.**
   `10 ** 30` is exact; `10.0 ** 30` is a double. Earthquake counters never
   overflow, and gravity arithmetic has 53 bits of mantissa.
4. **It is a hostile target for optimisation by the programmer.** Micro-
   optimising pure Python rarely wins more than tens of per cent. The wins of one
   to two orders of magnitude come from *not interpreting* — from handing a whole
   array to compiled code, which is exactly what module
   [03-02 NumPy](../02-numpy/README.md) does.

Fact 4 is the reason this module is short on tricks. The right response to "pure
Python is slow" is not "write cleverer pure Python"; it is "measure first, then
change the data structure, then vectorise or compile".

## 3. What the standard library already gives you

The standard library is a set of modules that ship with every Python
installation. It is the floor of the ecosystem, and for geophysics the floor is
higher than most people expect.

| Module | What it is for | Where the curriculum uses it |
|---|---|---|
| `math` | libm: trigonometry, logarithms, `hypot`, `fsum`, `isclose` | Every formula in the folder |
| `statistics` | mean, median, variance, correlation | Quick reductions before pandas |
| `csv` | RFC-4180 delimited-file reading and writing, with quoting | Earthquake catalogues, station lists |
| `json` | Structured metadata, GeoJSON | Station metadata, web services |
| `pathlib` | Portable filesystem paths and file operations | Every script in the folder |
| `random` | Seeded Mersenne Twister | Synthetic data, bootstrap, Monte Carlo |
| `decimal`, `fractions` | Exact decimal and rational arithmetic | Auditing a calculation without rounding |
| `complex` (built-in) | Native complex numbers | Fourier and impedance work, module 20 |
| `collections` | `Counter`, `defaultdict`, `namedtuple`, `deque` | Grouping, records, queues |
| `itertools` | `islice`, `chain`, `groupby`, `product` | Lazy pipelines over large files |
| `dataclasses` | Records with generated `__init__`, `__repr__`, `__eq__` | Station and trace records |
| `time`, `timeit`, `tracemalloc` | Timing and memory measurement | Module 13; used throughout this module |
| `unittest` | A test framework | Module 13 |
| `sqlite3` | A real database with no server | Module 22, data engineering |

Two of these deserve a sentence now. `math.fsum` is *compensated* summation: it
returns the correctly rounded sum of a sequence, which matters when a million
terms accumulate an error of many units in the last place. `random.Random(seed)`
gives a *reproducible* random stream; every synthetic data set in this module is
generated from a fixed seed so that the numbers in the lessons can be checked.

What the standard library does **not** give you is an array type. A list of
`float` is a list of pointers to boxed objects, not a contiguous block of
doubles. That single fact is the reason NumPy exists, and it is the subject of
the next module.

## 4. The divisions of labour in the ecosystem

The scientific Python ecosystem is not one library; it is a set of libraries with
non-overlapping responsibilities. Learn the map and you stop looking in the
wrong place.

| Domain | Library | Responsibility |
|---|---|---|
| Arrays | [NumPy](https://numpy.org) | Contiguous N-dimensional arrays, elementwise arithmetic, linear algebra, random |
| Algorithms | [SciPy](https://scipy.org) | Quadrature, ODE integration, optimisation, interpolation, signal processing, sparse matrices |
| Tables | pandas | Labelled 1-D and 2-D data, cleaning, group-by, time series |
| Labelled N-D | xarray | Arrays with named dimensions, netCDF I/O, chunked access |
| Plotting | Matplotlib | The object model behind almost every scientific figure |
| Maps | [PyGMT](https://pygmt.org) | Cartographic projections and shaded relief via the GMT engine |
| Vector GIS | GeoPandas | Geometries, coordinate reference systems, spatial joins |
| Seismology | [ObsPy](https://docs.obspy.org) | miniSEED and StationXML, instrument response, preprocessing |
| Symbolic maths | SymPy | Deriving formulas, then generating code |
| Interactive work | Jupyter | Literate analysis with a persistent kernel |

Three consequences follow, and they are the organisational principles of this
folder:

- **The divisions are by problem shape, not by scientific discipline.** "My data
  is a labelled table" points at pandas whatever the discipline; "my data is a
  grid with coordinates" points at xarray.
- **The layers stack.** ObsPy reads a miniSEED file and hands back NumPy arrays;
  pandas is built on NumPy; xarray is built on NumPy and pandas. Learning NumPy
  once pays in four places.
- **The layers hide things you sometimes need.** ObsPy's instrument-response
  removal is a large, correct, well-tested piece of code — and if you cannot say
  what a transfer function is, you cannot tell whether it was applied twice. The
  fundamentals in this module are what let you read the documentation critically.

## 5. Worked walkthrough: a forward model with no dependencies

The demo for this lesson is
[`code/why_python_demo.py`](./code/why_python_demo.py). It contains one complete
gravity model, one timing measurement and one honest table of what the standard
library provides. Its specification, in the sense of §1, is a sphere of excess
density $\Delta\rho$, radius $a$ and centre depth $z$, with the vertical anomaly
at surface offset $x$ given by the point-mass expression

$$g_z(x) = \frac{G M z}{(x^2 + z^2)^{3/2}}, \qquad M = \tfrac{4}{3}\pi a^3 \Delta\rho,
\tag{1}$$

where $G$ is the Newtonian constant of gravitation. Equation (1) is exact for a
uniform sphere in a homogeneous half-space and is the standard first-order model
for a compact ore body. Two assumptions are stated in that sentence; §7 discusses
what breaks them.

Run it and the first block of output is the specification made concrete:

```text
  excess density  delta_rho = 300 kg/m^3
  body radius     a         = 200 m
  centre depth    z         = 500 m
  mass contrast   M         = 1.005310e+10 kg
  peak anomaly    g_z(0)    = 0.268390 mGal

  Offset (m)   anomaly (mGal)   fraction of peak
         0.0         0.268390            1.0000
       200.0         0.214822            0.8004
       400.0         0.127791            0.4761
       600.0         0.070418            0.2624
       800.0         0.039957            0.1489
      1000.0         0.024005            0.0894
```

Read the fourth line as a calibration. With $a = 200$ m and
$\Delta\rho = 300$ kg m⁻³, the mass contrast is $1.005310\times10^{10}$ kg. The
peak anomaly is 0.268 mGal, which is a *small* anomaly — routinely measurable
with a modern relative gravimeter, and far below what a school pendulum could
resolve. The table is the instrument's response curve, and the *shape* of the
curve is the geophysics: the anomaly halves at 0.476 of its peak by 400 m offset,
which is close to $z\sqrt{2^{2/3}-1} = 383$ m — a compact body's anomaly profile
encodes its depth. That is the entire basis of depth estimation from a single
profile.

Now the cost measurement, which is the part people skip:

```text
  stations computed      : 200,000
  station spacing        : 20.000 mm
  peak anomaly recovered : 0.268390 mGal
  mean anomaly over line : 0.065094 mGal
  wall-clock time        : 0.034 s
  per-station cost       : 172 ns
```

Three things to notice, in order of importance.

**The standard-library result is not approximate.** The peak recovered over
200 000 stations is 0.268390 mGal, identical to the single-station value to six
decimals. Both use `float64`; the loop does not lose accuracy, it loses *time*.

**172 ns per station is the right order of magnitude to remember.** A station
costs roughly two hundred nanoseconds in this interpreter, for one square root,
one exponentiation and four multiplications. A survey of 10⁵ stations is
therefore tens of milliseconds — fine. A processing run of 10⁹ samples is
minutes to hours, and *that* is where the vectorised library stops being an
optimisation and becomes a necessity.

**20 mm station spacing is absurd, and the demo says so.** The line is 4 km long
with 200 000 stations, which no survey would ever acquire. It is there only so
that the timing is measurable above the timer's own resolution. This is a
general hazard in benchmarking: the setup that makes a number visible often
destroys the realism of the problem. State it, as the demo does, rather than
quoting an unrepresentative figure.

The script's final line is the other half of a benchmark's specification:

```text
Python version used: 3.14.4
```

A timing without an interpreter version and a machine description is not a
measurement, it is an anecdote. That is why the repository's
[`environment.yml`](../../environment.yml) exists and why every measurement quoted
in this module names the version it came from.

## 6. Physical interpretation: why this matters

The reason to care about the *program* rather than only the physics is that the
program is where the error budget actually lives.

Consider what happens when the same model is used to *estimate* depth from a
measured peak anomaly. Equation (1) at $x = 0$ gives $g = GM/z^2$, so

$$\frac{\mathrm{d}z}{\mathrm{d}g} = -\frac{z}{2g}. \tag{2}$$

For the numbers above, $z = 500$ m and $g = 0.268390$ mGal, so
$|\mathrm{d}z/\mathrm{d}g| = 931$ m per mGal. A 1 per cent error in the anomaly —
0.0027 mGal, well inside the accuracy of a good survey after reduction — moves
the inferred depth by 2.5 m. That is comfortable. But the same sensitivity applies
to the *mass contrast*: a $\Delta\rho$ wrong by a factor of two puts the depth
wrong by $\sqrt{2}$, and the excess density of an ore body is exactly the
quantity you do not know a priori. The lesson generalises: **inversion amplifies
input error by a factor that depends on the model**, and the only way to see it
is to compute the derivative. Lesson 03 does this numerically with Newton's
method; module [18 Inverse Problems](../../18-inverse-problems/README.md) does it
properly.

There is a second, cultural reason. Geophysics is a field in which the same
catalogue, the same grid and the same waveform format are shared across decades
and institutions. A result that cannot be regenerated from its own inputs is not
a result that others can build on. Python is the lingua franca partly because the
ecosystem's file-format libraries (ObsPy, xarray, GeoPandas, PyGMT) are good, and
partly because a script is a *readable* specification: shorter, more portable and
more auditable than a GUI session, and easier to version than a spreadsheet.

## 7. Assumptions and limits

Every claim in §5 comes with a regime. State them or they will bite.

1. **The point-mass approximation.** Equation (1) treats the sphere as a point
   mass at its centre, which is exact for a uniform sphere in an infinite
   homogeneous medium. Real bodies are not spheres and their host is not
   homogeneous, so the modelled anomaly is a *shape*, not a measurement. A
   dipping sheet, a sill or a 2-D prism has a different curve with the same peak.
2. **The half-space assumption.** Topography, weathering and lateral density
   changes of the overburden contribute anomalies of the same order. That is what
   free-air and Bouguer reductions exist to remove, and they are approximate.
3. **Gravity is a vector, measured as its vertical component.** Equation (1)
   is the vertical component; the horizontal one is nonzero and is ignored by
   every relative gravimeter, correctly, because the instrument is levelled. If
   it is not levelled, the error is first order in the tilt.
4. **Timing numbers are machine-dependent.** The 172 ns above is from one laptop,
   one interpreter (CPython 3.14), one run. Wall-clock measurements on shared
   hardware vary by tens of per cent. Benchmark claims without a machine and a
   version are folklore.
5. **"Slower" is not "less accurate".** Pure Python and NumPy share IEEE-754
   doubles. The difference is speed and memory layout, not precision. The one
   place accuracy does differ is *summation order*: naive Python summation of a
   long sequence accumulates error that `math.fsum` and NumPy's pairwise
   summation reduce. Lesson 02 measures that.

## 8. Python demonstration

The demonstration is the script you have just read about; run it yourself and
reproduce the numbers:

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 why_python_demo.py
```

The last block of its output is the summary table worth keeping:

```text
  int                  arbitrary precision - no overflow on event counts
  float                IEEE-754 double, same bits as C, Fortran and NumPy
  complex              native complex arithmetic for Fourier and impedance work
  math                 libm: trig, log, gamma, hypot, and correct rounding edge cases
  csv                  RFC-4180 quoting handled for you - see lesson 06
  statistics           mean, median and variance without a dependency
  decimal / fractions  exact decimal and rational arithmetic for audits
  random               seeded Mersenne Twister - reproducible synthetic data
  pathlib              portable paths, no string joining with '/'
  timeit / time        measure before you optimise - see lesson 05
```

The exercise for this lesson is to *change* the model, not to admire it. Halve
the excess density and predict the new peak before you run it; move the body to
1 km depth and check that the anomaly falls by a factor of four, not two, because
$g \propto z^{-2}$ for a fixed mass; then check whether it does, given that the
mass is held fixed by the code. Each of those is a falsifiable prediction, which
is the whole point.

## 9. Common mistakes

1. **Believing the language is the interesting part.** The interesting part is
   the model, the units and the failure modes. Syntax is learned in an afternoon;
   the discipline takes longer.
2. **Optimising before measuring.** Rewriting a loop for speed without timing it
   is how a correct program becomes a fast wrong one.
3. **Timing one run.** The first execution of a function pays import and
   warm-up costs. Repeat, and report the spread, not the best case.
4. **Comparing across machines.** A benchmark without an interpreter version and
   a machine description is not a measurement.
5. **Assuming a library is correct because it is popular.** Popular libraries are
   usually correct *for the stated assumptions*. Reading the assumptions is the
   skill.
6. **Confusing the standard library with the ecosystem.** `import math` works
   everywhere forever; `import obspy` requires an environment that was installed
   and pinned. Both are fine; knowing which you are relying on decides whether
   your script is portable.
7. **Quoting a number you did not compute.** Every figure in this module is the
   printed output of a demo you can run. Keep that habit.

## 10. Real-world applications

- **Exploration gravity.** The forward model of equation (1) in a different
  geometry (prism, sheet, polyhedron) is what a survey is inverted against, and
  the same profile-shape reasoning is used in the field to decide whether a
  reconnaissance anomaly is worth a drill hole.
- **Microgravity monitoring.** Time-lapse gravity over a reservoir or a volcano
  resolves anomalies of a few microgal, thirty thousand times smaller than the
  0.268 mGal peak above. At that level the processing script — its reductions,
  its drift correction, its summation order — is the instrument.
- **Archival reprocessing.** National data centres hold decades of waveforms and
  catalogues. Reprocessing them is a pure computing task: read, validate, reduce,
  store, at scale. Module [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md)
  is about exactly that.
- **Teaching and outreach.** A twenty-line script that produces a physically
  correct anomaly curve is a better teaching object than a screenshot from a GUI,
  because a student can change one number and predict the result.

## 11. Further reading

- NumPy — [numpy.org](https://numpy.org), the array library that the rest of the
  ecosystem is built on; module [03-02](../02-numpy/README.md).
- SciPy — [scipy.org](https://scipy.org), the algorithms layer.
- ObsPy — [docs.obspy.org](https://docs.obspy.org), seismological data handling;
  module [03-10](../10-obspy-and-seismic-data/README.md).
- PyGMT — [pygmt.org](https://pygmt.org), cartography; module
  [03-11](../11-pygmt-and-mapping/README.md).
- NIST CODATA fundamental constants — [physics.nist.gov/cuu/Constants/](https://physics.nist.gov/cuu/Constants/),
  the source of the value of $G$ used here.
- USGS earthquake catalogue web service — [earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/),
  the catalogue endpoint used by the module's complete program.

## 12. Related lessons

- [03-01-02 Types, Variables, Expressions and Operator Semantics](./02-types-and-variables.md)
  — what `float` really is, and what that costs a survey.
- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](./03-control-flow.md)
  — the survey loop, measured, and the invariance test.
- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md)
  — turning equation (1) into an importable instrument.
- [03-02 NumPy](../02-numpy/README.md) — the same computation, vectorised, and
  the measurement of what that buys.
- [01-01-04 Floating Point Representation and Rounding](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — the mathematics behind the precision claims made here.

## 13. Exercises

[`exercises/01-why-python-exercises.md`](./exercises/01-why-python-exercises.md) —
seven problems, ★ to ★★★. Problem ★★4 requires you to run the demo and report
its numbers; problem ★★6 asks you to find the density contrast of a body whose
peak is below the noise floor of a stated instrument.

## 14. Self-assessment checklist

- [ ] I can state the five properties of a scientific instrument and give the
      gravimeter-to-program correspondence for each.
- [ ] I can explain why an interpreted language is slower per operation and why
      that is not an accuracy claim.
- [ ] I can name at least six standard-library modules useful in geophysics and
      say what each does.
- [ ] I can name the ecosystem library responsible for arrays, algorithms,
      tables, grids, plots, maps, GIS and seismic formats.
- [ ] I can write equation (1) from memory, with units, and say which of its
      assumptions I would relax first.
- [ ] I have run `why_python_demo.py` and can quote its peak anomaly, its
      per-station cost and its interpreter version.
- [ ] I can compute $\mathrm{d}z/\mathrm{d}g$ for a peak-anomaly inversion and
      say what error it puts on an inferred depth.
