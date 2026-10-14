---
id: 03-10-01
title: "ObsPy Architecture and Data Models"
level: intermediate
prereqs: ["03-01-04", "03-02-01"]
tags: [obspy, seismology, data-model, time-series, utc]
---

# ObsPy Architecture and Data Models

A seismogram is an array of numbers plus a dozen pieces of metadata, and almost
every mistake in observational seismology is a mistake about the metadata:
a wrong sample rate, a start time off by an hour, a channel code that promises
a response the instrument does not have, a gap silently filled with zeros.
ObsPy's central design decision is that the array and its metadata travel
together, in an object called a `Trace`, and that a `Stream` is an ordered
collection of them. Everything else in the library is built on those two
types. This lesson is about the types, not the algorithms.

Run the demonstration before reading on; every number quoted below is its
actual output.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_overview_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** ObsPy's layout: one meta-package, many subpackages, and which
   subpackage answers which question.
2. **Construct** a valid `Trace` and `Stream` in memory from NumPy arrays, with
   network, station, location, channel, sampling rate and start time set
   explicitly.
3. **Read** the derived attributes — `delta`, `endtime`, Nyquist frequency —
   and explain which of them are stored and which are computed.
4. **Explain** what a sample value means before and after instrument response
   removal, and why "counts" is not a physical unit.
5. **Use** `UTCDateTime` correctly: absolute instants, epoch seconds, and the
   fact that ObsPy's timestamp field ignores leap seconds.
6. **Predict** what `slice`, `trim` and `merge` do at boundaries and gaps, and
   choose the method that preserves the physical meaning of a gap.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — how a package is imported and how subpackages namespace their functions.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the array model that a `Trace` wraps and that its `.data` attribute returns.

## 1. Intuition: why a data model at all

A MiniSEED file is a sequence of fixed-length records, each with its own
header. A one-hour three-component record from one station can be dozens of
files, split at arbitrary points, with the channel codes and start times in
binary headers. If you read those files as raw bytes you have an array and a
pile of integers, and nothing stops you from adding two segments sampled at
different rates, or from plotting a record against the wrong start time.

ObsPy's answer is to make the metadata part of the object and to make the
operations check it. `Trace.stats` is not a dictionary you may fill with
anything: `sampling_rate`, `starttime`, `npts` and the four channel
identifiers are the minimum needed for the object to mean something, and
`Trace.verify()` will tell you when they are inconsistent.

The trade-off is real. ObsPy is slower than raw NumPy because every operation
re-verifies metadata, and its objects carry more state than a function call
needs. For a 10-station array processing a year of data, that overhead is
negligible; for a 10-million-trace ambient-noise job it is not, and people
drop to `numpy` or `dask` for the inner loop. Knowing where the object model
earns its cost is part of using the library well.

## 2. Precise definitions

### 2.1 The package layout

ObsPy is a namespace package with subpackages that map onto tasks:

| Subpackage | Question it answers |
|---|---|
| `obspy.core` | What are the data types? (`Trace`, `Stream`, `UTCDateTime`, `Catalog`) |
| `obspy.io.*` | How do I read or write format *X*? (MSEED, SAC, SEG-Y, QuakeML, StationXML) |
| `obspy.signal` | How do I process the samples? (filter, detrend, taper, correlate, polarise) |
| `obspy.taup` | What are the travel times and ray paths for a given Earth model? |
| `obspy.geodetics` | How far apart are two points on the Earth? |
| `obspy.clients.fdsn` | How do I download data from a web service? |
| `obspy.imaging` | How do I plot it? |
| `obspy.realtime` | How do I process a live stream? |
| `obspy.db` | How do I index a large local archive? |

The demonstration imports each in turn. On this installation `obspy.db` is
**not importable** — it needs an optional database backend — and the demo
prints exactly that rather than failing. A lesson that claims "ObsPy provides
X" without checking which extras are installed is a lesson that breaks on
someone else's machine.

### 2.2 `UTCDateTime`: an instant, not a string

`UTCDateTime` stores a POSIX timestamp — seconds since 1970-01-01T00:00:00Z —
with microsecond resolution. The demo parses `2024-03-15T08:30:00.123456Z` and
reports

```
POSIX/epoch seconds   : 1710491400.123456 s since 1970-01-01T00:00:00Z
matplotlib date       : 19797.354168 days since 1970-01-01
julday                : 75  (day of year, 1..365/366 -- NOT a Julian Day Number)
```

Three of these deserve comment.

**The epoch field is POSIX time, which does not count leap seconds.** A
difference of two `UTCDateTime` objects is a difference of POSIX timestamps.
The demo shows that the interval from `2016-12-31T23:59:59Z` to
`2017-01-01T00:00:00Z` is reported as exactly

```
UTC 2016-12-31T23:59:59.000000Z -> 2017-01-01T00:00:00.000000Z: ObsPy reports 1.000000 s
```

Two SI seconds elapsed across that boundary, because a positive leap second
was inserted at the end of 2016. ObsPy reports one second. It also refuses to
construct the leap second at all:

```
constructor UTCDateTime(2016,12,31,23,59,60) -> ValueError: second must be in 0..59, not 60
ISO string '2016-12-31T23:59:60'             -> ValueError: second must be in 0..59, not 60
```

This is a measured property of ObsPy 1.5.1, not an inference. The consequences
are concrete: comparisons of epochs with a UTC clock that inserts leap seconds
are off by 27 s in 2024 if you compare against a TAI-based source, and a
travel-time residual computed across a leap-second boundary is off by one
second. Seismological practice is to ignore leap seconds entirely and to treat
UTC as continuous; that is what every archive does, and it is why the
convention is safe as long as you know it is a convention. The fuller
treatment is in [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md).

**`julday` is the day of year.** For 2024-03-15 it is 75, and for 2024-12-31 it
is 366. It is *not* a Julian Day Number, which for the same date would be
2460385. The name is a trap inherited from older seismological software (SAC
calls the same quantity `nzjday`). A Julian Day Number counts days from a fixed
epoch in 4713 BC; a day of year counts days from January 1. They differ by
about 2.46 million.

### 2.3 `Trace`: array plus metadata

A `Trace` has exactly two public attributes of interest:

- `tr.data` — a one-dimensional NumPy array. In memory it is always `float64`;
  on disk it is usually `int32` (MiniSEED) or `float32` (SAC).
- `tr.stats` — an `AttribDict` with the metadata:

| Key | Meaning | Unit |
|---|---|---|
| `network`, `station`, `location`, `channel` | SEED identifiers | — |
| `sampling_rate` | samples per second | Hz |
| `delta` | time between samples, `1/sampling_rate` | s |
| `npts` | number of samples | — |
| `starttime` | time of the first sample | `UTCDateTime` |
| `calib` | scalar calibration to physical units | dimensionless |

Everything else is derived. The demo prints, for a 6000-sample trace at
100 Hz starting at `2024-03-15T08:30:00.000000Z`:

```
Trace.id                 : XX.ABCD.00.BHZ
tr.stats.delta           : 0.01 s  (= 1/sampling_rate)
Nyquist frequency        : 50.0 Hz
tr.stats.endtime         : 2024-03-15T08:30:59.990000Z
duration = npts*delta    : 60.000 s
```

Note the arithmetic of `endtime`. It is not `starttime + 60 s`, because the
record has 6000 *samples*, which span 5999 *intervals*: `starttime + 5999 ×
0.01 s = 08:30:59.990`. A 60-second record at 100 Hz ends at 59.990 s. Mixing
up "number of samples" and "duration in intervals" is the most common
off-by-one in the field, and it is why `delta` rather than `sample rate` is the
quantity that appears in almost every formula.

### 2.4 What a sample value means

Before response removal, a sample is an integer **count** — the output of an
analog-to-digital converter, dimensionless, scaled by whatever gain the
digitizer was set to. The demo's trace of Gaussian noise has

```
trace max |amplitude|    : 4.1680 counts
trace RMS                : 1.0130 counts
```

"Counts" is not a physical unit and cannot be converted to one without the
instrument response. This is the single most important sentence in the module:
a number in a waveform file has no physical meaning until StationXML supplies
the transfer function that produced it. Lesson
[03](./03-inventory-and-metadata.md) does that conversion.

### 2.5 `Stream`: an ordered collection

`Stream` is a list of `Trace` objects with set-like operations: `+`, `select`,
`merge`, `split`, `sort`. It has no constraint that its traces are
contiguous, orthogonal, or even from the same station, which is both its
power and its danger. `len(st)` is a count of traces, not of channels.

## 3. Derivations and worked reasoning

### 3.1 Sample rate, delta and Nyquist, with units

A trace sampled at $f_s$ has

$$\Delta = \frac{1}{f_s}\ \mathrm{s}, \qquad
f_{\text{Nyquist}} = \frac{f_s}{2}\ \mathrm{Hz}, \qquad
n_{\text{pts}} = \mathrm{round}\!\left(\frac{t_{\text{end}} - t_{\text{start}}}{\Delta}\right) + 1.$$

The dimensional check is immediate: $[\Delta] = \mathrm{s}$,
$[f_s] = \mathrm{s^{-1}}$, $[\Delta f_s] = 1$ (dimensionless). The Nyquist
frequency is the highest frequency that can be represented without aliasing,
because a sinusoid needs at least two samples per period. For $f_s = 100$ Hz,
$f_{\text{Nyquist}} = 50$ Hz; the demo prints 50.0.

Two consequences that are easy to forget:

- **Decimating by a factor $D$ reduces Nyquist by $D$**, so everything above
  $f_s/2D$ must be removed *before* decimating. Lesson
  [05](./05-filtering-detrending.md) measures what happens when it is not.
- **Resampling is not interpolation of the plot.** It is band-limited
  interpolation, and it fails when the original data contain energy above the
  new Nyquist.

### 3.2 Who owns `delta`?

`delta` is a *derived* attribute: setting `sampling_rate` updates it and vice
versa. This is convenient and occasionally dangerous, because a trace read from
a file with a 0.01 s sampling interval retains `sampling_rate = 100.0` exactly
as a float, and `1.0/100.0 = 0.01` is not exactly representable in binary. The
demo verifies the relation with `np.isclose` rather than `==`:

```
CHECK delta == 1/fs      : True
```

Here it is exactly true because both values round-trip, but a trace at 250 Hz
has $\Delta = 0.004$, and comparing computed `delta` values for exact equality
between two traces is a latent bug of the kind discussed in
[01-01-04 Floating Point](../../01-mathematics/01-arithmetic/04-floating-point.md).

### 3.3 Boundary conventions of `slice`, `trim` and `merge`

The demo asks for the window from 1.0 s to 2.0 s after the start of a
100 Hz trace and reports

```
slice [1 s, 2 s]         : 101 samples, delta 0.01 s
trim  [1 s, 2 s]         : 101 samples
```

One hundred and one samples, not 100. Both boundaries are inclusive, so a
1.0 s window contains 101 sample instants, exactly as a 1.0 m ruler with
millimetre ticks has 1001 marks. The same convention appears in `Stream.trim`,
`Stream.slice` and `Stream.split`.

`merge` is the operation that most needs a decision from the analyst. With a
10.010 s gap between two segments of the same channel, the demo measures
"1001 missing samples" and then:

```
merge(method=-1)         : 2 traces -> the gap is kept
merge(method=0)          : 1 traces, 6000 samples
samples that are not data: 1000 (zeros inserted at the gap by method=0)
```

`method=0` concatenates and *fills* the gap (with zeros by default); that is
why the merged trace has 6000 samples and 1000 of them are invented.
`method=-1` refuses to fill and leaves two traces. The demo also measures the
type error that catches most people the first time:

```
merge(fill_value=0.0) on int32 data -> UFuncTypeError: Cannot cast ufunc
'multiply' output from dtype('float64') to dtype('int32')
```

Integer waveforms need an integer fill value. Use `method=-1` and process the
segments separately unless you can defend the interpolation.

## 4. Physical and computational interpretation

The data model encodes a compromise: **metadata is checked at the object
level, and never inferred**. `Trace` will not guess a sampling rate from a
file name, will not guess that two traces belong to the same channel because
their station codes match, and will not silently resample. Every one of those
prohibitions exists because the alternative has produced published errors.

The cost shows up in three places:

1. **Memory.** A `Stream` of one year of three-component data at 100 Hz is
   $3 \times 100 \times 3.15\times10^7 \times 8$ bytes $\approx 75$ GB in
   `float64`; on disk in `int32` it is half that. This is why serious archives
   never load a year into a `Stream`.
2. **Overhead.** Each `Trace` operation re-validates metadata, so a loop over
   10 000 short traces spends measurable time in bookkeeping.
3. **Dtype.** `Trace.data` is `float64` in memory. Reading an `int32` MiniSEED
   file therefore doubles the memory footprint immediately, which is the
   reason `obspy.io.mseed` has low-level functions that return the raw
   integers.

## 5. Python demonstration

The full script is
[`code/obspy_overview_demo.py`](./code/obspy_overview_demo.py). It runs
offline: every trace is synthesised from
`np.random.default_rng(20240315)`, so the printed values are reproducible.
Sections 1–8 cover the package layout, `UTCDateTime` (including the measured
leap-second failure), the `Trace` model, `Stream`, slicing and trimming,
`merge`, and a set of consistency checks.

The checks in section 8 are the ones worth copying into your own code:

```python
print(f"CHECK sampling_rate>0    : {tr.stats.sampling_rate > 0}")
print(f"CHECK delta == 1/fs      : "
      f"{np.isclose(tr.stats.delta, 1.0 / tr.stats.sampling_rate)}")
print(f"CHECK starttime <= endtime: "
      f"{tr.stats.starttime <= tr.stats.endtime}")
```

Four lines, and they catch the three metadata errors that produce silently
wrong plots.

## 6. Exercises

Attempt these closed-book. Full solutions are in
[`exercises/01-obspy-overview-solutions.md`](./exercises/01-obspy-overview-solutions.md).

### ★ Foundational

**★1.** A trace has `npts = 3600` and `delta = 0.005` s. State its sampling
rate in Hz, its Nyquist frequency, its duration in seconds, and the time of its
last sample relative to `starttime`.

**★2.** Convert `UTCDateTime("2024-03-15T08:30:00.123456Z")` to epoch seconds
and back. State how many significant figures the microseconds represent at
that epoch, given that `float64` has 52 bits of mantissa.

**★3.** Explain, in one sentence each, why `julday` is not a Julian Day Number
and why ObsPy's `UTCDateTime` cannot represent `2016-12-31T23:59:60`.

**★4.** A `Stream` contains three traces: `XX.ABCD.00.BHZ`,
`XX.EFGH.00.BHZ` and `XX.ABCD.00.BHN`. How many traces does `select(channel="BHZ")`
return, and what does `len(st)` mean in general?

### ★★ Applied

**★★5.** Write a function that takes a `Trace` and returns `True` only if the
metadata are self-consistent: positive sampling rate, `npts >= 2`, `delta`
equal to `1/sampling_rate` to within $10^{-9}$ relative, and finite samples.
Test it on a deliberately corrupted trace in which `npts` is set to 10 while
`endtime` implies 6000 samples, and explain which check catches the
corruption.

**★★6.** The demo reports that `slice(1 s, 2 s)` returns 101 samples. Compute
the number of samples returned by `slice(t0, t1)` for a 250 Hz trace over
`[0.000 s, 0.100 s]` and verify your answer by running it. Then state the
general formula.

**★★7.** A waveform has a 4.5 s gap between two segments. You need a
continuous 60 s record for a spectral estimate. Write the code for both
options (fill and do not fill), then argue in three sentences which you would
defend in a paper and why the other is indefensible.

**★★8.** Using `UTCDateTime`, compute the number of seconds between
`2016-12-31T23:00:00Z` and `2017-01-01T01:00:00Z` with ObsPy, and state the
number of SI seconds that actually elapsed. Explain the discrepancy.

### ★★★ Research-oriented

**★★★9.** Write a script that builds a `Stream` of 100 synthetic traces, each
1000 samples at 100 Hz, and measures (a) how many traces survive
`st.select(station="ABCD")`, (b) the memory footprint of the `Stream` in
bytes using `numpy.ndarray.nbytes` summed over traces, and (c) the same
footprint if the data were `int32` instead of `float64`. Report the numbers
with units and state the practical implication for reading a year of
three-component data.

**★★★10.** The statement "ObsPy ignores leap seconds" was verified above by
two observations. Design and run a third, independent test: use file
timestamps or a known historical event (a nuclear test or a large earthquake
recorded across a leap-second boundary) and check whether an epoch difference
matches the UTC difference. State clearly what you could and could not verify
without network access, and what the residual uncertainty is.

## 7. Common mistakes

1. **Treating `endtime` as `starttime + npts × delta`.** It is
   `starttime + (npts − 1) × delta`. The measured endtime above is
   59.990 s, not 60.000 s, for a 60-second window.
2. **Assuming a sample has physical units.** Counts are not m/s, and the
   conversion needs the response from lesson 03.
3. **Comparing `delta` values with `==`.** Use `np.isclose` with a relative
   tolerance; `1/250` is not exact in binary.
4. **Filling gaps by default.** Measured above: 1000 samples of zeros in a
   6000-sample trace, indistinguishable from data once inside a `Stream`.
5. **Confusing `julday` with a Julian Day Number.** They differ by about
   2.46 million days.
6. **Believing that UTC differences are SI-second differences.** ObsPy reports
   1.000000 s across a boundary where two SI seconds elapsed.
7. **Loading a year of data into a `Stream`.** Estimate the footprint before
   you type the read, not after.

## 8. Real-world applications

- **Routine observatory processing.** A night's data from a 30-station
  network arrives as a few thousand MiniSEED files; the `Stream` model is what
  makes `read` → `select` → `merge` → `detrend` → `filter` a four-line job.
- **Rapid source characterisation.** The USGS National Earthquake Information
  Center locates events within minutes using the same data model; the
  automatic magnitude and the analyst-reviewed magnitude travel through
  `Catalog` objects (lesson 04).
- **Instrument debugging.** Plotting a few hours of raw counts from a station
  whose output looks wrong distinguishes a digitizer problem (counts with the
  wrong scale) from a sensor problem (a step in counts at a known time), which
  is why the raw-count layer is kept accessible.
- **Archival.** Data centres index terabytes by the SEED identifier
  `network.station.location.channel`; nothing else is stable enough over
  decades. The identifier is the primary key of the discipline.

## 9. Further reading

- **ObsPy tutorial, "Getting started" and "Reading seismograms".**
  https://docs.obspy.org/tutorial/ — the canonical walk-through, and the
  fastest way to see the data model in use.
- **ObsPy `Trace` API reference.**
  https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html — the
  authoritative list of `stats` keys and methods.
- **ObsPy `Stream` API reference.**
  https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.html — the
  `merge`, `split`, `select` and `trim` semantics are all here.
- **IRIS/EarthScope data-format descriptions.**
  https://ds.iris.edu/ds/nodes/dmc/data/formats/ — MiniSEED, SAC and StationXML
  described by the archive that maintains them.
- **Beyreuther, M., Barsch, R., Krischer, L., Megies, T., Behr, Y., &
  Wassermann, J. (2010). ObsPy: A Python toolbox for seismology. *Seismological
  Research Letters*, 81(3), 530–533.** Level: intermediate. The design paper;
  read it for the data model rationale, not for API details.

## 10. Related lessons

- [02 Reading MiniSEED and SAC: Trace and Stream on Disk](./02-reading-waveforms.md)
  — what the on-disk formats actually store.
- [03 StationXML, Inventory, Response and Instrument Correction](./03-inventory-and-metadata.md)
  — the step that turns counts into metres per second.
- [05 Preprocessing: Detrend, Taper, Filter, Decimate](./05-filtering-detrending.md)
  — the first operations you will apply to a `Stream`.
- [03-03-05 scipy.signal](../03-scipy/05-signal.md) — the filtering and spectral
  machinery underneath `Trace.filter`.
- [22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md)
  — why channel codes and time stamps have the form they do.

## 11. Self-assessment checklist

- [ ] I can construct a `Trace` from a NumPy array with valid metadata and say
      which fields are required.
- [ ] I can compute `delta`, `endtime` and the Nyquist frequency and state the
      units of each.
- [ ] I can explain why `endtime` is not `starttime + npts × delta`.
- [ ] I can explain what a "count" is and what is needed to convert it.
- [ ] I can state, without looking, whether ObsPy's timestamps count leap
      seconds, and I have seen the measurement that shows it.
- [ ] I can predict how many samples `slice(t0, t1)` returns at a given rate.
- [ ] I can choose between `merge(method=-1)` and `merge(method=0)` for a gap
      and defend the choice.
- [ ] I know which subpackage I would reach for to filter, to locate an event,
      and to compute a distance.
