# Solutions — 03-10-01 ObsPy Architecture and Data Models

> **Read this after attempting the exercises, not before.** Values attributed
> to the demo are its actual output on this installation (ObsPy 1.5.1,
> NumPy 2.5.4, Python 3.14.4). Values marked *measured* come from running a
> modified copy of the demonstration, with the modification stated.

---

## ★1 — Sample rate, delta, duration, endtime

**(a)** $f_s = 1/\Delta = 1/0.005 = 200$ Hz.

**(b)** $f_{\mathrm{Nyquist}} = f_s/2 = 100\ \mathrm{Hz}$.

**(c)** The record spans $n_{\text{pts}} - 1 = 3599$ intervals, so the duration
as a time span is $3599 \times 0.005 = 17.995$ s. The value $3600 \times 0.005 =
18.000$ s is the *nominal* length and is the number most people quote; the
*measured* span ends at the last sample.

**(d)** The last sample sits $17.995$ s after `starttime`, i.e. at
$t_{\text{end}} = t_{\text{start}} + 17.995$ s.

Units: (a) Hz = s⁻¹, (b) Hz, (c) s, (d) s. The dimensional check on (c) is
$[\text{count}] \times [\text{s}] = \text{s}$.

---

## ★2 — Four representations of one instant

**(a)** As printed by the demo:

```
parsed                : 2024-03-15T08:30:00.123456Z
POSIX/epoch seconds   : 1710491400.123456 s since 1970-01-01T00:00:00Z
matplotlib date       : 19797.354168 days since 1970-01-01
julday                : 75  (day of year, 1..365/366)
```

**(b)** The first is a formatted UTC calendar string, lossless.
The second counts **seconds** from the POSIX epoch 1970-01-01T00:00:00Z.
The third counts **days** from the same 1970 epoch
($1710491400.123456/86400 = 19797.354168$ exactly: $19797 \times 86400 =
1710460800$, and $1710491400 - 1710460800 = 30600$ s $= 8$ h $30$ min).
The fourth counts **days from January 1 of the same year**; 2024 is a leap
year, so 75 is 31 (Jan) + 29 (Feb) + 15.

**(c)** A Julian Day Number for 2024-03-15 is 2460385, and
$2460385 - 75 = 2460310$. The name `julday` in ObsPy (and `nzjday` in SAC)
predates the habit of naming the day of year explicitly, and the two quantities
differ by the accumulated length of the calendar since 4713 BC.

---

## ★3 — Leap seconds

**(a)** `UTCDateTime` stores a POSIX timestamp whose integer part is seconds
since 1970, and it converts to and from `datetime.datetime`, which enforces
`0 <= second <= 59`. There is therefore no representation for an extra second,
and the constructor and both string parsers raise
`ValueError: second must be in 0..59, not 60` — measured for all three forms:

```
constructor UTCDateTime(2016,12,31,23,59,60) -> ValueError: second must be in 0..59, not 60
ISO string '2016-12-31T23:59:60'             -> ValueError: second must be in 0..59, not 60
ISO string '2016-12-31T23:59:60.0'           -> ValueError: second must be in 0..59, not 60
```

**(b)** The demo measures

```
UTC 2016-12-31T23:59:59.000000Z -> 2017-01-01T00:00:00.000000Z: ObsPy reports 1.000000 s
```

Two SI seconds elapsed: the second 23:59:59 and the inserted leap second
23:59:60. ObsPy reports one.

**(c)** Report the SI-second number (2 s) when the question is a duration in
physics — energy release, attenuation, instrumental drift — and state the
convention explicitly: "UTC with leap seconds counted". Report the POSIX
difference (1 s) when the question is "how do I align two files", because that
is what every archive and every clock in the discipline does. The failure mode
is to mix them without saying so; the 2016 boundary is 27 s from a TAI-based
clock, which is a large error in a travel-time residual.

---

## ★4 — What a `Stream` guarantees

**(a)** `len(st)` counts **traces**, i.e. `Trace` objects. Two traces with
different channel codes, different sampling rates or overlapping times still
count as two. The demo's stream holds
`XX.ABCD.00.BHZ` and `XX.EFGH.00.BHZ`, both 6000 samples at 100 Hz, so the
total sample count is 12000 — but nothing in the type forces that.

**(b)** No. The `Stream` in section 7 of the demo contains two traces with a
10.010 s gap between them.

**(c)** `merge` (which must decide what to do about the gap) and `split`
(which exists precisely because a stream may contain discontinuities).

---

## ★5 — 101 samples in a one-second window

A sampled record is a set of **instants**, not intervals. At 100 Hz the
instants are at $t = 0, 0.01, 0.02, \dots$ s. The closed window
$[1.00, 2.00]$ includes both endpoints, so it contains the instants
$1.00, 1.01, \dots, 2.00$: that is $100$ intervals and $101$ instants.

General rule when both endpoints land on samples:
$n = f_s T + 1$, i.e. $101$ for $f_s T = 100$. When the endpoints do not land
on samples the count is $\lfloor f_s t_1\rfloor - \lceil f_s t_0\rceil + 1$,
which is why the same request on a 250 Hz trace over $[0.000, 0.100]$ s gives
$25 + 1 = 26$ samples.

---

## ★★6 — A consistency checker that reports rather than decides

```python
import numpy as np

def is_consistent(trace) -> list[str]:
    problems = []
    stats = trace.stats
    if stats.sampling_rate <= 0:
        problems.append(f"sampling_rate {stats.sampling_rate} is not positive")
    if stats.npts < 2:
        problems.append(f"npts {stats.npts} is too small for a filter or a taper")
    if not np.isclose(stats.delta, 1.0 / stats.sampling_rate, rtol=1e-9):
        problems.append(f"delta {stats.delta} != 1/{stats.sampling_rate}")
    if not np.isfinite(trace.data).all():
        problems.append("data contain NaN or inf")
    span = (stats.endtime - stats.starttime) * stats.sampling_rate
    if abs(span - (stats.npts - 1)) > 1:
        problems.append(f"starttime/endtime imply {span + 1:.0f} samples, "
                        f"npts is {stats.npts}")
    return problems
```

Corrupting `npts` to 10 while the array still holds 6000 samples fires **two**
checks: `npts == len(trace.data)` is no longer true (the `delta` check
survives, because `delta` is untouched), and the starttime/endtime check
reports that the time span implies 6000 samples while `npts` says 10.

The important design decision is that the function returns a *list of
problems*. A boolean tells the caller that something is wrong and nothing
about what; a list is directly printable in a processing log, which is where
the diagnosis actually happens.

---

## ★★7 — Reconciling 10.010 s with 1001 samples

The first segment ends at `starttime + 999 × 0.01 s` (last *sample* of 1000).
The second segment starts at `endtime_of_first + 1.0 s`; the demo sets
`second.stats.starttime = first.stats.endtime + 1.0`. The gap between the two
*traces* is therefore measured from the last sample of the first to the first
sample of the second:

$$\text{gap} = \underbrace{1.0\ \mathrm{s}}_{\text{requested}} + \underbrace{0.01\ \mathrm{s}}_{\text{one sample interval}} = 1.010\ \mathrm{s}.$$

The demo's other gap is 10.010 s for the same reason: a 10 s requested gap
plus one sample interval. `int(round(gap * 100)) = 1001` samples, and
$1001 \times 0.01 = 10.010$ s. The extra sample is the boundary convention:
a gap of $k$ samples means $k+1$ missing sample *instants*.

---

## ★★8 — Gap preserved versus gap filled

Measured with a 4.5 s gap between two 1000-sample segments at 100 Hz:

| version | `len(st)` | `st[0].stats.npts` | samples that are not measurements |
|---|---|---|---|
| `merge(method=-1)` | 2 | 1000 | 0 |
| `merge(method=0, fill_value=0)` | 1 | 2451 | 451 |

The 451 filled samples are $4.5/0.01 = 450$ intervals plus the boundary sample.
Defensible sentence for using the filled version: "the gap lies in a quiet
interval outside the analysis window, and the fill value affects only the
zero-mean and taper operations because the band-pass removes any DC." The
second sentence must state the test that supports it: "I verified this by
repeating the measurement with the gap deleted rather than filled, and the
two spectra agree to within 0.3 % of their peak, which is below the noise
level." Without that test the fill is an assertion.

---

## ★★9 — A two-hour interval across a leap-second boundary

```python
from obspy import UTCDateTime
a = UTCDateTime("2016-12-31T23:00:00Z")
b = UTCDateTime("2017-01-01T01:00:00Z")
print(b - a)          # 7200.0
```

ObsPy reports **7200.0 s**. The true elapsed SI time is **7201 s**, because a
positive leap second was inserted at 2016-12-31T23:59:60Z. The difference
appears under exactly one assumption, stated in one direction: *you are
comparing an absolute duration in physics against a clock that inserts leap
seconds.* Under the opposite convention — UTC treated as continuous, as every
seismic archive does — 7200 s is the correct and intended answer.

---

## ★★10 — Counts, RMS, and what the numbers do and do not mean

**(a)** Counts: dimensionless integers produced by the digitizer. Not a
physical unit.

**(b)** The frequency-dependent transfer function from ground motion to
counts, i.e. the poles, zeros, normalisation factor and stage gains of the
sensor and digitizer. That is a `Response` object inside an `Inventory`, and
`Trace.remove_response` is the operation that applies its inverse.

**(c)** For $n$ independent standard normal values, the sample RMS is a random
variable with mean 1 and standard deviation approximately $1/\sqrt{2n}$.
With $n = 6000$, $1/\sqrt{12000} = 0.00913$, so an RMS of 1.0130 is
$(1.0130 - 1)/0.00913 = 1.42$ standard deviations above 1 — entirely
consistent with a standard normal draw. The demo's seed is fixed, so the value
is reproducible, but it is not evidence about the generator: one sample. The
same computation on 100 different seeds would show the expected spread, which
is the point of the exercise.

---

## ★★★11 — Footprint of a 100-trace stream

Measured (100 traces, 1000 samples each):

| quantity | value |
|---|---|
| traces after `select(station="ABCD")` | 100 |
| sample payload as `float64` | 800 000 bytes (0.8 MB) |
| sample payload as `int32` | 400 000 bytes (0.4 MB) |
| payload per trace | 8000 bytes (`float64`) |

For a year at 100 Hz: $100 \times 3.15\times10^7 = 3.15\times10^9$ samples per
component, so $3.15\times10^9 \times 3 \text{ components} \times 8$ bytes
$= 75.6$ GB as `float64` in memory, or 37.8 GB as `int32` on disk. The
conclusion is that a `Stream` is the right tool for hours to days and the wrong
tool for years: use one of (i) `Stream` per day, processed and reduced to
products; (ii) `dask` or `xarray` over chunked files; or (iii) an indexed
database of decimated and derived channels, keeping the raw archive on disk.
ObsPy itself provides `obspy.db` for exactly the third case, which is *not
importable on this installation* — another reason to verify rather than
assume.

---

## ★★★12 — A third test of the leap-second claim

Acceptable answers vary; here is one that is fully offline and conclusive.

**Test.** Compare `UTCDateTime` differences against differences computed with
`datetime` in UTC, on the same two instants.

```python
from datetime import datetime, timezone
from obspy import UTCDateTime

a = UTCDateTime("2016-12-31T23:59:59Z")
b = UTCDateTime("2017-01-01T00:00:00Z")
da = datetime(2016, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
db = datetime(2017, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
print((b - a), (db - da).total_seconds())   # 1.0 1.0
```

**Result.** Both give 1.0 s, which shows that `UTCDateTime` differences inherit
`datetime`'s UTC arithmetic — an implementation inheritance, not an independent
physical check. That is a *negative* result and it should be reported as such.

**What would be conclusive.** A file with a recorded creation time on either
side of the boundary, or a seismic record containing a known event whose
origin time is published in UTC, would test the archive's convention rather
than the library's arithmetic. Neither is available offline.

**Residual uncertainty.** I have verified how ObsPy's arithmetic behaves and
that it cannot represent second 60. I have *not* verified how a particular
archive timestamps a record that spans the boundary; that requires data, and it
is the kind of question whose answer differs between data centres.

---

## ★★★13 — Isolating metadata overhead without quoting milliseconds

The instruction "no wall-clock numbers" forces a ratio-based design. One that
works:

1. Build a fixed-size computation in pure NumPy: `np.diff(a)` on a 1000-sample
   array, repeated enough times to be measurable.
2. Build the same computation as `Trace` operations: create a `Trace`, call
   `tr.copy()` and `tr.slice(...)` the same number of times.
3. Measure both in the same process, on the same data, and report the ratio
   $r = \text{time}(\text{Trace path}) / \text{time}(\text{NumPy path})$.
4. Sweep the number of `Trace` objects from 1 to 1000 and report how $r$ varies
   with the object count.

The ratio is portable in the sense that it is dimensionless and compares two
things measured under identical conditions, which removes most of the machine
dependence. It is not perfectly portable: the two paths may use different
NumPy kernels and therefore scale differently with cache size. State that as a
limitation, and quote the swept counts (1, 10, 100, 1000 traces) with the
array size (1000 samples) so the experiment can be repeated.
