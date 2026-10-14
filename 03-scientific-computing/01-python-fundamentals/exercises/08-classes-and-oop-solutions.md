# Solutions — 03-01-08 Classes, Objects and When Not to Use OOP

> **Read this after attempting the exercises, not before.** Numbers attributed to
> the demo are its actual printed output.

---

## ★1 — Choosing the instrument

| Item | Choice | Reason |
|---|---|---|
| (a) trace with a positive-rate invariant | `class` | Two pieces of data that must stay consistent, one invariant, and several operations needing both |
| (b) station with a latitude range rule | `frozen dataclass` | A record with validation and no behaviour; frozen gives hashability for dictionary keys |
| (c) $2\pi G\rho h$ | `function` | Three multiplications, no state, no invariant |
| (d) a row whose columns are unknown until runtime | `dict` | The schema arrives with the data; a record type cannot be declared in advance |
| (e) a catalogue keyed by code | `dict` | The task is lookup |
| (f) a survey holding stations, calibration and parameters | `class` — or, better, **three** objects | The list is a god-object warning: stations, calibration and parameters are three responsibilities (see ★★★9) |

---

## ★2 — Trace duration

**(a)** $n/\text{rate} = 500/100 = 5.00$ s; $(n-1)/\text{rate} = 499/100 =
4.99$ s. The demo prints `duration_s    = 4.9900 s  (= 499 intervals at 100 Hz)`.

**(b)** $(n-1)/\text{rate}$ is correct for the interval between the first and last
sample: $n$ samples define $n-1$ *intervals*, in the same way that $n$ fence posts
define $n-1$ panels. The $n/\text{rate}$ convention is the "sample count divided by
rate" duration, which is the time the record *occupies* if each sample is treated as
representing a cell of length $1/\text{rate}$; it appears in the literature and in
some file formats, which is why it must be stated rather than assumed.

**(c)** $n = 3$ at 1 Hz: $3/1 = 3.00$ s, and $(3-1)/1 = 2.00$ s. The two differ by
50 per cent — the relative discrepancy is $1/(n-1)$, so it is largest for the
shortest records and vanishes for long ones.

**(d)** The duration between the first and last sample of a uniformly sampled
record is $(n-1)/\text{rate} = (n-1)\,\Delta t$.

---

## ★3 — The three dunder methods

```python
class SeismicTrace:
    def __repr__(self):
        return (f"SeismicTrace({self.station!r}, {self.sampling_rate_hz:g} Hz, "
                f"{len(self.samples)} samples, peak {self.peak:.3e} {self.units})")

    def __eq__(self, other):
        if not isinstance(other, SeismicTrace):
            return NotImplemented
        return (self.station == other.station
                and self.sampling_rate_hz == other.sampling_rate_hz
                and self.samples == other.samples)

    def __len__(self):
        return len(self.samples)
```

`__eq__` must return `NotImplemented` rather than `False` for a foreign type so
that Python can try the *reflected* comparison: if the other object defines
`__eq__` that knows how to compare with this class, returning `NotImplemented`
gives it the chance, and only if that also fails does Python fall back to identity
comparison. Returning `False` would silently declare "not equal" without giving the
other type a say, which breaks interoperating with a foreign trace class — for
example an ObsPy `Trace` wrapper.

---

## ★4 — The demo's trace

**(a)**

```text
  SeismicTrace('STA01', 100 Hz, 500 samples, peak 2.373e+00 V)
  npts          = 500
  duration_s    = 4.9900 s  (= 499 intervals at 100 Hz)
  mean          = 1.946121e-02 V
  rms           = 6.119624e-01 V
  peak          = 2.373381e+00 V
  len(trace)    = 500
```

Note the ordering of the statistics: rms (0.6120 V) is 31 times the mean
(0.01946 V), which is what a zero-mean oscillatory signal looks like; the mean is
nonzero only because the synthetic decaying sinusoid is truncated before a whole
number of cycles.

**(b)**

```text
  rejected zero sampling rate: sampling rate must be positive, got 0.0 Hz
  rejected negative rate: sampling rate must be positive, got -1.0 Hz
```

**(c)**

```text
  a == b (same data)  : True
  a is b              : False
  a == c (other code) : False
  repr(b)             : SeismicTrace('STA01', 100 Hz, 500 samples, peak 2.373e+00 V)
```

`a is b` is `False` because `__eq__` compares values, not identity: two separately
constructed traces with the same data are equal and distinct.

**(d)**

```text
  Station(code='STA02', latitude=47.3769, longitude=8.5417, elevation_m=408.0)
  frozen: assignment is refused -> FrozenInstanceError: cannot assign to field 'elevation_m'
  order=True, sorted : ['STA01', 'STA02']
  validation fires   : latitude out of range: 91.0
```

---

## ★5 — Decimation

**(a)**

```python
def decimate(self, factor):
    if not isinstance(factor, int) or factor < 1:
        raise ValueError(f"factor must be a positive integer, got {factor!r}")
    return SeismicTrace(self.station, self.sampling_rate_hz / factor,
                        self.samples[::factor], self.units)
```

**(b)** For `factor = 2`: samples $= \lceil 500/2 \rceil = 250$, rate
$= 100/2 = 50$ Hz, duration $= 249/50 = 4.98$ s. For `factor = 4`: samples
$= 125$, rate $= 25$ Hz, duration $= 124/25 = 4.96$ s.

**(c)** The duration shortens because the last sample is dropped when $n$ is not
divisible by the factor, and because the $(n-1)$ term does not scale exactly:
$4.99 \to 4.98 \to 4.96$ s. It is **not a bug** — it is a consequence of the
interval convention — but it must be stated, because a processing pipeline that
checks "does the decimated trace have the same duration?" will fail on every trace
whose sample count is not divisible by the factor.

**(d)** Any operation whose result depends on the sample interval must not be
applied without regard to the new rate. The clearest example is a digital filter
designed for the original rate: the corner frequency in *seconds* is fine, but the
corner frequency in *samples per cycle* changes by the decimation factor, so a
filter applied by sample index silently changes its physical passband. (Decimation
also requires an anti-alias filter *before* the resampling; the demo's version is a
pure subsample and would alias a real signal, which is why module 03-03's SciPy
material exists.)

---

## ★6 — The size table

**(a)**

```text
  form             sys.getsizeof   has names  immutable
  tuple                       80       False       True
  namedtuple                  80        True       True
  dataclass                   48        True       True
  plain class                 48        True      False
```

**(b)** `tuple` and `namedtuple` are identical at 80 bytes, so **the field names
cost nothing at runtime**: a `namedtuple` is a `tuple` subclass whose fields are
properties resolved through a class-level descriptor table.

**(c)** The dataclass's 48 bytes is the instance object itself, and for the plain
class `sys.getsizeof` omits the instance `__dict__` that holds the attributes (a
separate object, at least 104 bytes for four entries, plus a key-sharing table).
The dataclass's fields are stored in slots when `slots=True` and otherwise also live
in a `__dict__`, so the comparison at this size is really "two objects versus two
objects" and the difference is not 32 bytes. **Read `getsizeof` as a measurement of
one object, and never as a measurement of memory used.**

**(d)** For $10^{7}$ records, **none of them**: a list of $10^{7}$ instances costs
of the order of a gigabyte (8 bytes per pointer plus one dict or tuple per record),
and the field values are boxed objects. The right answer is a *structured array* or
a *columnar layout* — parallel `float64` arrays, one per field, or NumPy's record
arrays — which store $10^{7}$ doubles as 80 MB with no per-record object at all.
That is module [03-02](../../02-numpy/README.md), and it is the reason a class is the
right tool for $10^{6}$ traces but the wrong tool for $10^{9}$ samples.

---

## ★★★7 — A trace class with real invariants

```python
import math

class SeismicTrace:
    __slots__ = ("station", "sampling_rate_hz", "samples", "units")

    def __init__(self, station, sampling_rate_hz, samples, units="V"):
        if not isinstance(station, str) or not station:
            raise ValueError(f"station must be a non-empty string, got {station!r}")
        if not isinstance(sampling_rate_hz, (int, float)) or sampling_rate_hz <= 0:
            raise ValueError(f"sampling rate must be positive, got {sampling_rate_hz!r} Hz")
        if not samples:
            raise ValueError("a trace with no samples is not a trace")
        values = [float(s) for s in samples]
        for index, value in enumerate(values):
            if not math.isfinite(value):
                raise ValueError(f"sample {index} is not finite: {value!r}")
        self.station = station
        self.sampling_rate_hz = float(sampling_rate_hz)
        self.samples = values
        self.units = units
    # ... properties and dunders as in lesson 08 ...
    def detrend(self):
        m = self.mean
        return SeismicTrace(self.station, self.sampling_rate_hz,
                            [s - m for s in self.samples], self.units)
    def decimate(self, factor):
        if not isinstance(factor, int) or factor < 1:
            raise ValueError(f"factor must be a positive integer, got {factor!r}")
        return SeismicTrace(self.station, self.sampling_rate_hz / factor,
                            self.samples[::factor], self.units)
    @classmethod
    def from_row(cls, row):
        return cls(row["station"], float(row["sampling_rate_hz"]),
                   [float(x) for x in row["samples"].split("|")])
    def to_dict(self):
        return {"station": self.station,
                "sampling_rate_hz": repr(self.sampling_rate_hz),
                "samples": "|".join(repr(s) for s in self.samples),
                "units": self.units}
```

**(a)** Round trip:

```python
t = synthetic_trace()
assert SeismicTrace.from_row(t.to_dict()) == t
```

Note the `repr()` calls in `to_dict`: they make the serialised form round-trip
exactly for arbitrary doubles, which `str` does not guarantee for all values in all
contexts. A decimal-formatted serialisation loses the last digits and the assertion
would fail — an instructive demonstration that **serialisation is a precision
decision**.

**(b)** Rejections: `''` → `station must be a non-empty string, got ''`;
`0.0` → `sampling rate must be positive, got 0.0 Hz`; `[]` → `a trace with no
samples is not a trace`; `[0.0, float('nan')]` → `sample 1 is not finite: nan`.

**(c)** `detrend` returning a new trace is safer because it makes the operation
*pure*: the caller's data is untouched, so an intermediate result can be discarded,
a pipeline stage cannot corrupt an input another stage still needs, and the function
is trivially testable. The cost is a full copy — 8 bytes per sample, so 8 MB for
$10^{6}$ samples — plus the allocation. For a single trace that is irrelevant; for
a processing chain over $10^{4}$ traces it doubles the peak memory unless the
caller drops the input explicitly (`trace = trace.detrend()`), which is what makes
the in-place version attractive and why both designs exist.

---

## ★★★8 — Five quantities, four instruments

| # | Quantity | Instrument | Reason |
|---|---|---|---|
| 1 | Velocity model with cross-layer invariants | **class** (or a validating dataclass plus a module-level `validate_model`) | The invariants are *between* layers — depths strictly increasing, $v_s < v_p$ — so they cannot be enforced by a per-layer record type; something must own the collection |
| 2 | One gravity measurement at one station | **namedtuple** (`Measure(code, g_mgal, sigma_mgal)`) | Two or three immutable scalars, no behaviour, no invariant beyond positivity — and it is small enough to live inside a `float64` array's metadata |
| 3 | Great-circle distance between two points | **function** | Pure computation, no state, no invariant; a named function with units in the name and the docstring is the whole instrument |
| 4 | A catalogue of 10⁵ events with per-event IDs | **class** (or a dict keyed by ID, or a pandas/xarray table) | The invariant is "IDs are unique" and the operations are bulk queries; a class can hold the index, but the honest alternative is a `dict` and the *better* answer at $10^{5}$ rows is a table (module 03-04) |
| 5 | A processing parameter set passed through a pipeline | **frozen dataclass** | It is a record, it must not change mid-pipeline, and freezing gives hashability so that a memoising decorator (lesson 10) can cache on it |

**The distribution matters more than any single answer:** one class, one
namedtuple, one function, one dataclass, plus a table where a container was not
needed at all. A solution that answers "class" five times has not understood the
lesson.

---

## ★★★9 — Refactoring a god object

**(a)** Five responsibilities:

| Responsibility | Becomes |
|---|---|
| Station list and its invariants | `StationCatalogue` (a class) or a plain list plus a keyed `dict` |
| Instrument calibration table | `Calibration` (a frozen dataclass, or a function `apply_calibration`) |
| Processing parameters | `ProcessingParameters` (a frozen dataclass) |
| Reduced anomaly array and its reduction | `reduce_survey(stations, calibration, parameters)` (a function returning the array) |
| Output file handle | A **context manager** inside the writer function (lesson 10) |
| The plot's axes object | A plotting function taking the data and returning the figure |

**(b)** The two methods that must **not** share an object with the file handle:

1. **The reduction.** It computes physics and must be callable, testable and
   re-runnable without touching a file. Holding a handle beside it means a test of
   the reduction either opens a file it does not need or, worse, writes to a real
   one.
2. **The plotting.** It needs an axes object, not a data file, and a method that
   both writes output and draws is a method whose failure modes are entangled: a
   plotting error leaves a truncated file, and a file error leaves a half-drawn
   figure.

The general rule: **resource ownership should be as short-lived and as local as
possible**, so that anything which does not need the resource cannot accidentally
outlive or corrupt it.

**(c)** The three-line rule:

1. Does the new attribute describe the *same thing* as the existing ones — the same
   physical object, at the same level of abstraction?
2. Would every method of the class still be meaningful if this attribute were
   absent?
3. Does the attribute have its own lifecycle (opened and closed, set and reset,
   valid only during one phase)?

If (1) is no, it belongs in another object. If (2) is no, the class has two
responsibilities and should be split. If (3) is yes, the attribute is a resource and
belongs in a context manager, not an attribute.
