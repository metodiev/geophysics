# Exercises — 03-01-08 Classes, Objects and When Not to Use OOP

Attempt these **closed-book** before opening the
[solutions](./08-classes-and-oop-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/classes_oop_demo.py`](../code/classes_oop_demo.py) require you to run it
and report its **actual** output.

---

## ★ Foundational

**★1.** For each item, choose `class`, `frozen dataclass`, `namedtuple`, `dict` or
`function`, and justify in one sentence.

(a) A seismic trace: samples plus sampling rate, rate must be positive.
(b) A station: code, latitude, longitude, elevation, latitude within ±90°.
(c) The Bouguer slab correction $2\pi G\rho h$.
(d) A parsed CSV row whose columns are not known until runtime.
(e) A catalogue of stations keyed by code.
(f) A survey whose stations, instrument calibration and processing parameters are
all needed together.

---

**★2.** A trace has $n = 500$ samples at 100 Hz.

(a) Compute its duration under the convention $n/\text{rate}$ and under
$(n-1)/\text{rate}$.
(b) State which is correct for the interval between the first and last sample, and
why.
(c) Repeat for $n = 3$ at 1 Hz, where the difference is largest in relative terms.
(d) State the generic rule for the duration of a uniformly sampled record of $n$
samples.

---

**★3.** Write, for a `SeismicTrace`-like object: a `__repr__` that shows the
station, rate, sample count and peak; an `__eq__` that compares three fields and
returns `NotImplemented` for a foreign type; and a `__len__`. State why `__eq__`
must not return `False` for a foreign type.

---

## ★★ Applied

**★★4.** Run `python3 classes_oop_demo.py` and report:

(a) the `repr` and the five computed properties;
(b) the two rejected sampling rates and their messages;
(c) the three equality results and the repr;
(d) the dataclass's `repr`, the frozen-assignment error and the validation error.

---

**★★5.** Describe what `decimate(factor)` should do to a trace's samples, rate and
duration.

(a) Implement it so that the returned trace's rate is `rate/factor` and its samples
are every `factor`-th sample.
(b) For the demo's trace (500 samples at 100 Hz), compute the new sample count,
rate and duration for `factor = 2` and `factor = 4`.
(c) Explain why the duration shortens slightly, and state whether that is a bug.
(d) State one operation that must *not* be applied to the decimated trace without
regard to its new rate, and why.

---

**★★6.** Run the demo and report the size table.

(a) State each form's `sys.getsizeof` value.
(b) Which two forms are identical in size, and what does that say about the cost of
field names?
(c) Why is the dataclass *smaller* than the tuple, and what does `sys.getsizeof`
omit for a plain class?
(d) State which form you would use for a 10⁷-element array of records and why the
answer is actually "none of them".

---

## ★★★ Research-oriented

**★★★7.** Write a `SeismicTrace` class with:

- a constructor enforcing: non-empty station code, positive rate, non-empty
  samples, and all samples finite (no NaN or infinity);
- `npts`, `duration_s`, `mean`, `rms`, `peak` as properties;
- `detrend()` returning a new trace, not mutating in place;
- `decimate(factor)` preserving the rate-and-duration relationship;
- `__repr__`, `__eq__`, `__len__`;
- a `from_row` classmethod and a `to_dict` method that round-trips.

(a) Show the round trip: build, serialise, rebuild, and assert equality.
(b) Demonstrate each constructor rejection with its message.
(c) Explain why `detrend` returning a new trace is safer than mutating, and what it
costs at $10^{6}$ samples.

---

**★★★8.** Decide, with reasons, for each of these five quantities, whether it
should be a class, a dataclass, a namedtuple or a function — and ensure your answer
includes at least one of each.

1. A velocity model: $n$ layers, each with a depth, $v_p$, $v_s$ and density, with
   the invariants of lesson 07's ★★★7.
2. A single measurement of the gravitational acceleration at one station.
3. A great-circle distance between two points.
4. A catalogue of 10⁵ events with a per-event ID.
5. A processing parameter set (corner frequencies, taper length, gain) that is
   passed around a pipeline.

---

**★★★9.** Refactor a god object.

A `Survey` class has fifteen methods and holds: the station list, the instrument's
calibration table, the processing parameters, the output file handle, the current
plot's axes object, and the reduced anomaly array.

(a) Identify the five responsibilities and name the object or function each should
become.
(b) State which two of the fifteen methods must not be in the same object as the
file handle, and why.
(c) Write the three-line rule you would use to decide whether a new attribute
belongs in an existing class.
