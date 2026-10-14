---
id: 03-01-08
title: "Classes, Objects and When Not to Use OOP"
level: intermediate
prereqs: ["03-01-04", "03-01-05"]
estimated_minutes: 75
tags: [object-oriented, classes, dataclasses, invariants, seismic-trace]
---

# Classes, Objects and When Not to Use OOP

A class is the right tool when data and the rules that constrain it must travel
together. A seismic trace is the canonical geophysical example: a list of samples
is meaningless without the sampling rate, and a sampling rate is meaningless
without the samples. Neither can be validated alone, and every operation on either
depends on both. That is a class.

A class is the wrong tool when you have a bag of numbers and no rules. A station's
latitude and longitude need no behaviour, so they are a dataclass or a tuple, not
a hand-written class with twelve methods. Most over-engineering in scientific code
is a class wrapped around a dict.

This lesson teaches the boundary, and it is deliberately more interested in the
boundary than in the machinery.

## Learning objectives

By the end of this lesson you will be able to:

1. **Decide** whether a problem needs a class, a dataclass, a namedtuple or a
   plain function, and justify the choice in one sentence.
2. **Write** a class whose constructor enforces the type's invariants, and
   explain what the invariant buys the methods that follow.
3. **Implement** `__repr__`, `__eq__` and `__len__`, and explain why `__repr__`
   and `__eq__` are part of a class's *interface*, not its cosmetics.
4. **Use** `@property` for computed quantities, and say why a derived value with
   an off-by-one risk should never be a stored attribute.
5. **Distinguish** an instance method, a `classmethod` and a `staticmethod`, and
   give the test that decides between them.
6. **Write** a frozen dataclass with `__post_init__` validation, and state what it
   provides that a plain class does not.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  methods are functions with a first argument.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md)
  — the containers a class replaces, and the record alternatives.

## 1. The decision procedure

Before writing `class`, answer four questions in order.

1. **Is there more than one piece of data that must stay consistent?** A trace's
   samples and its rate; a survey's stations and its instrument calibration; a
   seismic event's hypocentre and origin time. If yes, continue. If it is one
   scalar, write a function.
2. **Is there an invariant — a statement that must be true of every instance?**
   "The sampling rate is positive", "the latitude is in $[-90, 90]$", "the
   covariance matrix is symmetric positive definite". If yes, a class or a
   validating dataclass can *enforce* it, once, at construction. If there is no
   invariant, a dict is simpler and honest.
3. **Are there operations that need that state?** A trace can be detrended,
   decimated, resampled, stacked. Those operations need the samples *and* the rate.
   Operations that need neither belong in a function.
4. **Will there be more than one instance?** A class with exactly one instance is
   usually a module in disguise.

Two of four answers being "yes" is enough. None of them being "yes" is the
over-engineering case, and §6 gives a worked counter-example.

## 2. Worked walkthrough: a trace that carries its metadata

The demo's `SeismicTrace` is deliberately small: four attributes, four properties,
three methods, and one invariant block. The invariant block is the reason the
class exists:

```python
def __init__(self, station, sampling_rate_hz, samples, units="V"):
    if not isinstance(station, str) or not station:
        raise ValueError(f"station must be a non-empty string, got {station!r}")
    if sampling_rate_hz <= 0:
        raise ValueError(
            f"sampling rate must be positive, got {sampling_rate_hz!r} Hz")
    if not samples:
        raise ValueError("a trace with no samples is not a trace")
        # (the assignments to self follow; the full constructor is in
        #  code/classes_oop_demo.py)
```

and the object prints as:

```text
  SeismicTrace('STA01', 100 Hz, 500 samples, peak 2.373e+00 V)
  npts          = 500
  duration_s    = 4.9900 s  (= 499 intervals at 100 Hz)
  mean          = 1.946121e-02 V
  rms           = 6.119624e-01 V
  peak          = 2.373381e+00 V
  len(trace)    = 500
```

Four things to read from that output.

**The specification is the object's invariants plus its accessors.** "Samples in
volts at a stated rate, for a stated station; length, mean, rms and peak are
defined for it." That is a specification a reader can check.

**The constructor is the single place the rules are enforced.** Every method can
then *assume* a positive rate and a non-empty sample list. That assumption is what
turns a class from a container into an abstraction: 40 lines of defensive checks
in four methods collapse into 6 lines in `__init__`.

**The rules are enforced for impossible inputs, not merely unlikely ones.** A zero
sampling rate is not an unusual measurement; it is a corrupt header. Rejecting it
is safe. Rejecting a 10 Hz rate as "too low" would not be — 10 Hz is a perfectly
real, if unusual, acquisition rate, and a class that refuses it will be worked
around.

**`duration_s` is 4.99 s, not 5.00 s.** A trace of $n = 500$ samples at 100 Hz
spans $n - 1 = 499$ sample *intervals*: 4.99 s. This is the most common
off-by-one in observational seismology, and the reason `duration_s` is a
`@property` computing `(npts - 1) / rate` rather than a stored attribute that
someone set once from `npts / rate` and then copied into three other functions.
**A derived quantity with an off-by-one risk should be computed, not stored.**

## 3. `__repr__`, `__eq__` and `__len__`

```text
  a == b (same data)  : True
  a is b              : False
  a == c (other code) : False
  repr(b)             : SeismicTrace('STA01', 100 Hz, 500 samples, peak 2.373e+00 V)
```

**`__repr__` is a debugging interface.** With it, a failing assertion prints the
data; without it, it prints `<SeismicTrace object at 0x10f2a1c50>`, which tells you
nothing. Write `__repr__` for every class you will ever debug, which is every
class.

**`__eq__` turns a question into a one-liner.** "Did this processing step change
the trace?" becomes `processed == original`. It also makes a class usable in a
test suite, which is where it earns its keep: the canonical unit test of a filter
is that filtering a known input gives a known output, and `==` is how you assert
it.

Two details that matter in scientific code. `__eq__` should return `NotImplemented`
for a foreign type rather than raising, so that Python can try the reflected
comparison; and a class with `__eq__` and no `__hash__` is unhashable, which is
correct for a mutable object and is why the *frozen* dataclass in §5 can be a dict
key while `SeismicTrace` cannot. And note the limitation: `__eq__` on floats
inherits every floating-point comparison problem, so an exact `==` on two traces
computed by different routes is a test that will fail for reasons that are not
bugs.

**`__len__`** makes `len(trace)` mean `npts` and makes the object iterable in a
`for` loop over samples. Convenient, and worth doing only when the object really
is a sequence of one thing.

## 4. Methods, `classmethod` and `staticmethod`

```text
  from_row -> SeismicTrace('STA07', 50 Hz, 4 samples, peak 1.000e+00 V)
  impedance(2670.0, 3000.0) = 8,010,000.0 kg m^-2 s^-1
```

The test that decides between the three is one question: **what does the function
need?**

| Needs | Definition | Example |
|---|---|---|
| The instance's data | plain method (`self`) | `trace.detrend()` |
| The class, but not an instance | `@classmethod` (`cls`) | `SeismicTrace.from_row(row)` |
| Neither | `@staticmethod` | `SeismicTrace.impedance(rho, v)` |

**`from_row` is a classmethod** because it constructs a new instance and should
respect subclasses: `cls(...)` rather than `SeismicTrace(...)`. Alternative
constructors are the classic classmethod use — reading from a CSV row, a miniSEED
header, an ObsPy object — and they keep the parsing outside the constructor, which
keeps the constructor's contract simple.

**`impedance` is a staticmethod** because it touches neither `self` nor the class.
It is a *namespace* decision: the formula lives with the class because that is
where a reader would look for it. If that argument feels weak, make it a module
function — that is what `geophys_core` does. A staticmethod that is not a
discoverability win is a module function in the wrong place.

**The instance method is the default** and needs no justification.

## 5. Dataclasses: records with rules

For a record, the demo's dataclass is the right instrument:

```python
@dataclass(frozen=True, order=True)
class Station:
    code: str
    latitude: float
    longitude: float
    elevation_m: float = field(default=0.0)

    def __post_init__(self):
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError(f"latitude out of range: {self.latitude}")
            # (the longitude check is identical in form)
```

```text
  Station(code='STA02', latitude=47.3769, longitude=8.5417, elevation_m=408.0)
  frozen: assignment is refused -> FrozenInstanceError: cannot assign to field 'elevation_m'
  order=True, sorted : ['STA01', 'STA02']
  validation fires   : latitude out of range: 91.0
```

Every line of that output is a feature that would otherwise be hand-written:

- **`__init__`, `__repr__` and `__eq__` are generated.** The parameters, their
  order and their names are the field declarations, so there is exactly one place
  where the record's shape is defined.
- **`frozen=True` makes the instance immutable and hashable.** Immutability is
  what allows a station to be a dictionary key or a set member, and what makes
  `order=True` coherent — an ordered, mutable record has no stable sort key.
- **`order=True` generates the comparison operators**, so `sorted(stations)` works
  and is the physical ordering (by code, then latitude, …), not an arbitrary one.
- **`__post_init__` is the validation hook.** A dataclass has no constructor body
  to write, so this is where the rules go. It runs after the generated `__init__`
  assigns the fields, which is exactly when the values are available.
- **Field defaults with `field(default=0.0)`** are how you give an optional field
  a default without the mutable-default hazard of lesson
  [04](./04-functions-modules.md) §4: a bare mutable default would be shared
  between instances, and `field(default_factory=list)` is the fix when you need
  one.

**Units in dataclass fields are the same discipline as everywhere else**:
`elevation_m`, not `elevation`; `latitude`, `longitude` in degrees by the EPSG
convention, and said so in the docstring. The record is the last place where a
unit can be recorded before the value becomes an unlabelled float.

## 6. The counter-example: a function is better

```text
  bouguer_slab_mgal(100.0) = 11.1969 mGal
```

This is $2\pi G \rho h$ — three multiplications, no state, no invariant beyond the
sign convention, no second operation that shares anything with it. Written as a
`BouguerCorrector` class it would gain a constructor, an attribute, a lifecycle
and a name to learn, and lose nothing. The demo says exactly this in its own
output.

Three more cases where a class is the wrong answer:

- **A bag of fields with no invariant.** A dict, or a dataclass if you want
  attribute access and validation.
- **A "utility" class that is never instantiated.** That is a module. Put the
  functions at module level.
- **Inheritance used to share a method.** If two classes share one method, they
  need a function, not a base class. Inheritance is for *substitutability*: a
  `FilteredTrace` should be usable everywhere a `SeismicTrace` is, and the demo's
  `decimate` returning a `SeismicTrace` is the alternative that avoids the whole
  question.

## 7. Sizes and clarity, measured

```text
  form             sys.getsizeof   has names  immutable
  tuple                       80       False       True
  namedtuple                  80        True       True
  dataclass                   48        True       True
  plain class                 48        True      False
```

The measurements are shallow — `sys.getsizeof` reports the container, not the
objects it references, and a dataclass instance with a `__dict__` carries an extra
hidden dict — so read the table as a comparison of *designs*, not as an accounting
of process memory. The useful facts are these:

- **`namedtuple` and `tuple` have identical per-instance size.** The names cost
  nothing; use them.
- **A frozen dataclass is smaller and immutable and validated.** It is the best
  default for a record that needs rules.
- **A plain mutable class is the only one that is not immutable**, which is
  sometimes what you need (a trace whose samples are processed in place) and
  sometimes what bites you.
- **`__slots__` removes the per-instance `__dict__`.** `SeismicTrace` uses it. In
  a loop over 10⁶ traces it is a real memory saving; it also means you cannot add
  attributes dynamically, which is a feature.

## 8. Physical interpretation: the invariant is the science

Why does a geophysicist care about object invariants? Because the invariant is
usually the physics.

**Sampling rate and samples are one quantity.** A time series is a function of
time; the samples are its values and the rate is the grid they live on. Splitting
them across two variables is a modelling error that the class prevents: with the
rate inside the object, it is impossible to detrend a trace and forget its rate,
because the method returns (or mutates) a trace that still has one. That is why
`decimate` returns a new trace with `sampling_rate_hz / factor` rather than
returning a bare list — the units follow the data.

**`duration = (n - 1) / rate` is physics, not arithmetic.** The interval between
the first and last sample is $n - 1$ intervals. Observational seismology has a
long history of trace-length off-by-ones that became apparent only when arrival
times were compared across networks. A computed property makes the mistake
impossible rather than noting it.

**Validation bounds are physical bounds.** Latitude within ±90° is a fact about
the Earth. A covariance matrix being symmetric positive definite is a fact about
covariance matrices. A density below osmium's is a fact about the periodic table
(lesson [07](./07-errors-and-debugging.md)). An object that enforces such bounds
at construction is a *type* in the strong sense: an invalid instance cannot exist,
so no downstream function needs to check.

**And the counter-example is physical too.** The Bouguer slab formula has no
invariant beyond the sign convention, because the correction is not a thing in the
world — it is a computation, applied to a station that is a record and a survey
that is a collection. Recognising "this is a computation, not a thing" is the skill
this lesson is really teaching.

## 9. Assumptions and limits

1. **The synthetic trace is a decaying sinusoid with no noise.** Its mean, rms and
   peak are properties of that function, not of a seismogram. The demo labels it
   `synthetic_trace` and generates it deterministically for that reason.
2. **`__eq__` on floats is exact.** Two traces that differ by one ulp compare
   unequal. Use `==` for reporting and a tolerance for testing, and expect to be
   asked which you meant.
3. **`__slots__` prevents dynamic attributes.** Pickling, mocking and some
   libraries rely on attributes being addable; `__slots__` is a deliberate
   trade-off, not a free win.
4. **Frozen dataclasses are shallowly immutable.** A frozen record holding a list
   can still have that list mutated. True immutability requires immutable fields.
5. **`order=True` is a total order on the fields in declaration order**, which is
   only the *physical* order you want if you declared the fields thoughtfully.
6. **Inheritance hierarchies are not shown here because they are usually the wrong
   answer in scientific code.** Composition — a trace that *has* metadata —
   composes; a `FilteredTrace` that *is* a trace drags a class hierarchy into every
   function that takes a trace.

## 10. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 classes_oop_demo.py
```

Note the demo's own structure: it uses `SeismicTrace` for a trace, a frozen
dataclass for a station, and a plain function for the Bouguer slab — three
different decisions in one file, each justified where it is made. That is the
lesson's actual content.

## 11. Common mistakes

1. **A class with no invariant.** It is a dict with more typing and a constructor
   that can be bypassed.
2. **Storing a derived quantity.** `duration_s` as an attribute will be stale
   after `decimate`; compute it.
3. **Forgetting `__repr__`.** The single highest-value three lines in the class.
4. **Mutable default attributes.** Same trap as mutable default arguments,
   lesson [04](./04-functions-modules.md) §4.
5. **Inheritance to share code.** Use composition, or a free function.
6. **A god object.** A `Survey` that holds stations, instrument calibration,
   processing parameters, file handles and a plot is five objects.
7. **`isinstance` checks over many classes.** That is a dispatch table in
   disguise; use a dict of functions or polymorphism deliberately.
8. **Validating in every method.** Validate in the constructor; trust the
   invariant thereafter.
9. **Rejecting merely unusual values.** A 10 Hz acquisition rate, a 45° dip, an
   8,100 kg m⁻³ ore density: reject the impossible, warn about the surprising.
10. **Making `__eq__` and then `__hash__` inconsistent**, so instances vanish from
    a set when mutated. If it is mutable, keep it unhashable.

## 12. Real-world applications

- **ObsPy's object model.** A `Trace` is samples plus metadata, a `Stream` is a
  collection of traces, and an `Inventory` holds response information — the same
  design decisions as here, at production scale (module
  [03-10](../10-obspy-and-seismic-data/README.md),
  [docs.obspy.org](https://docs.obspy.org)).
- **Grid models.** An xarray `DataArray` is values plus labelled dimensions plus
  attributes: a class whose invariant is "the coordinates are as long as the
  shape" (module [03-08](../08-gridded-geospatial-data/README.md)).
- **Station and event records** in a database-facing pipeline are dataclasses with
  validation, because the validation is the schema.
- **Frozen records as dictionary keys.** Deduplicating a catalogue by a composite
  key (network, station, channel, start time) requires exactly the hashable,
  immutable, comparable record this lesson builds.

## 13. Further reading

- ObsPy — [docs.obspy.org](https://docs.obspy.org): a large object model in a
  scientific library; read `Trace`, `Stream` and `UTCDateTime` with this lesson's
  questions in mind.
- NumPy — [numpy.org](https://numpy.org): the array as the opposite design choice
  — no per-element metadata, no per-element methods, all the speed.

## 14. Related lessons

- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md)
  — the containers a class replaces.
- [03-01-04 Functions, Scope, Modules and Packages](./04-functions-modules.md) —
  the mutable-default rule, in both arguments and attributes.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](./09-iterators-generators.md)
  — the *other* way to give an object behaviour: make it iterable.
- [03-01-07 Exceptions, Assertions and Systematic Debugging](./07-errors-and-debugging.md)
  — the validation-in-the-constructor pattern.
- [03-10 ObsPy and Seismological Data Handling](../10-obspy-and-seismic-data/README.md)
  — the real trace and stream objects.

## 15. Exercises

[`exercises/08-classes-and-oop-exercises.md`](./exercises/08-classes-and-oop-exercises.md) —
eight problems, ★ to ★★★. Problem ★★4 requires the trace's measured properties;
problem ★★★8 asks you to decide, with reasons, which of five described quantities
should be a class, a dataclass, a namedtuple or a function — and the answers
include at least one of each.

## 16. Self-assessment checklist

- [ ] I can state the four questions that decide whether a class is warranted.
- [ ] I can write a constructor that enforces an invariant and say what it buys.
- [ ] I can explain why `duration_s` is `(n - 1) / rate` and why it is a property.
- [ ] I can write `__repr__` and `__eq__`, and say why one is a debugging tool and
      the other a test tool.
- [ ] I can choose between an instance method, a classmethod and a staticmethod.
- [ ] I can write a frozen dataclass with `__post_init__` validation and use it as
      a dictionary key.
- [ ] I can give one example from my own work where a function is better than a
      class, and say why.
