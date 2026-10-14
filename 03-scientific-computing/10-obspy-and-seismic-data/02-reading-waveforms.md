---
id: 03-10-02
title: "Reading MiniSEED/SAC: Trace and Stream"
level: intermediate
prereqs: ["03-10-01"]
tags: [obspy, miniseed, sac, file-formats, data-quality]
---

# Reading MiniSEED/SAC: Trace and Stream

A waveform file contains an array of samples and the metadata needed to place
those samples in space and time. Two formats account for almost everything in
observational seismology: **MiniSEED**, the archive format of every FDSN data
centre, and **SAC**, the working format of a large fraction of the research
community. They differ in ways that matter — sample type, compression, what
the header can hold — and the differences show up as soon as you try to write
data back out.

This lesson is about what those formats actually store, measured rather than
described. Run the demonstration before reading on.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/reading_waveforms_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a MiniSEED record and a SAC file each contain, and which
   sample type each stores by default.
2. **Measure** the on-disk size of a waveform and explain the ratio to the
   uncompressed integer representation.
3. **Predict** the loss of precision when data are written to SAC as `float32`.
4. **Recognise** the MiniSEED Steim compression levels' effect on file size
   as a function of signal smoothness.
5. **Handle** gaps correctly: read segments, merge with or without a fill, and
   justify the choice.
6. **Explain** how `read()` decides a file's format, and why the file name is
   not the answer.

## Prerequisites

- [03-10-01 ObsPy Architecture and Data Models](./01-obspy-overview.md) —
  `Trace`, `Stream`, `stats`, and what a count is.

## 1. Intuition: three numbers decide everything

For any waveform file, three numbers determine the engineering:

- **How many samples** (the array).
- **How many bits per sample** (4 for `int32`, 4 for `float32`, fewer after
  compression).
- **How many header bytes** per record or per file.

The demonstration writes 3000 `int32` samples — 12000 bytes of raw sample data
— and measures:

```
MSEED   size   8192 bytes  (0.683 x raw int32)  bit-identical=True
SAC     size  12632 bytes  (1.053 x raw int32)  bit-identical=True
```

MiniSEED is *smaller than the raw samples* because it compresses; SAC is
*slightly larger* because of its fixed 632-byte header:
$12000 + 632 = 12632$ bytes exactly. Those two facts generate most of the
practical advice in this lesson.

## 2. Precise definitions

### 2.1 MiniSEED

MiniSEED is a stream of *records*. Each record has:

- a 48-byte **fixed header** (sequence number, quality indicator, station
  identifiers, start time, sample rate factor and multiplier, number of
  samples, flags);
- optional **blockettes** for extended information (1000 = data only, 1001 =
  time, 2000 = opaque, 5000 = timing);
- a **data block** whose encoding is declared in the header.

The common encodings are:

| Code | Encoding | Bits per sample |
|---|---|---|
| 0 | ASCII | variable, ~10 |
| 1 | `int16` | 16 |
| 3 | `int32` | 32 |
| 4 | `float32` | 32 |
| 10 | Steim-1 | 16 (4 nibbles/word) |
| 11 | Steim-2 | 16 (8 diff3 nibbles/word) |

ObsPy writes `int32` data as **Steim-2** by default. Steim is a differencing
scheme: it stores differences between successive samples, in a code that uses
fewer bits for small differences, and it packs the results into 64-byte
frames. Its efficiency therefore depends on the *smoothness* of the signal,
which the demonstration measures directly.

### 2.2 SAC

SAC is a sequence of *files*, one per trace (for the classic single-trace
form). Each file is a 632-byte header followed by the samples. The header
holds 70 floats, 15 integers, 20 strings and more, including:

- `delta` (sampling interval, s), `npts`, `b` (begin time relative to the
  reference), `e`;
- `kstnm`, `kcmpnm`, `knetwk` — the station, component and network strings;
- `stla`, `stlo`, `stle` and `evla`, `evlo`, `evdp` — station and event
  coordinates;
- `dist`, `az`, `baz`, `gcarc` — distance and angle, usually filled by a
  pre-processing step.

The default sample type is `float32`. There is no `location` code analogue;
SAC users encode that information in the component name or in `knetwk`.

### 2.3 What "bit-identical" means here

The demonstration verifies `np.array_equal(back.data, tr.data)` for both
formats. For `int32` samples with magnitudes below $2^{24}$ this is exactly
the right test. For `float64` data it is not: SAC stores `float32`, so the
round trip is lossy by construction.

## 3. Derivations and worked reasoning

### 3.1 Where the 8192 bytes come from

MiniSEED records are fixed-length, normally 4096 bytes. Two records are
8192 bytes. Each record holds a 48-byte header plus 4048 bytes of Steim frames
(64 frames per record); after the blockette for the data header, roughly 63
frames of data. Steim-2 stores up to 7 differences per 64-byte frame, so one
record holds about $63 \times 7 = 441$ samples, and two records hold about 882
— far fewer than 3000.

The arithmetic is wrong because Steim-2 uses wider codes only when it must.
For smooth data most differences are small and pack many per frame; the
measured file is 8192 bytes for 3000 samples, i.e. $8192 \times 8 / 3000 = 21.8$
bits per sample, not 4. The useful statement is the measured one:

```
peak amplitude         1: file   4096 bytes for 3000 samples = 1.3653 bytes/sample
peak amplitude      1000: file   8192 bytes for 3000 samples = 2.7307 bytes/sample
peak amplitude  10000000: file  16384 bytes for 3000 samples = 5.4613 bytes/sample
```

The three cases are the *same waveform shape* scaled to three amplitudes. At
peak amplitude 1 almost every sample is 0 or ±1, the differences are tiny, and
the file is 1.37 bytes per sample. At peak amplitude $10^7$ the differences are
large, Steim-2 falls back to 32-bit codes, and the file is 5.46 bytes per
sample — *larger than uncompressed `int32`*, because Steim has per-frame
overhead. Compression is not free and it is not guaranteed.

Note the granularity: 4096, 8192, 16384 — never anything between. MiniSEED file
sizes quantise to record boundaries, so a 3001-sample trace occupies the same
bytes as a 3400-sample one. When you plan storage, plan in records.

### 3.2 The `float32` trap

SAC stores `float32`. Writing 6000 `float64` samples with magnitudes around
$3.6\times10^{-3}$ and reading them back gives

```
largest |value| stored   : 3.556563e-03
max |round-trip error|   : 1.129282e-10
relative error           : 3.175207e-08   (float32 machine epsilon = 1.192093e-07)
```

A relative error of $3.2\times10^{-8}$ is about a quarter of
$\varepsilon_{\text{float32}}$, exactly as expected for round-to-nearest: the
worst case is $\varepsilon/2$ and typical values are smaller. Twenty-four bits
of mantissa give about seven decimal digits, so *anything you write to SAC is
correct to seven significant figures and no more*.

This matters when the numbers are small and the differences are smaller. A
gravity residual or a strain rate stored in `float32` may lose the signal
entirely; a ground velocity in m/s at the $10^{-9}$ level still fits because
the mantissa is relative, but the *difference* between $1.0000000$ and
$1.0000001$ does not.

### 3.3 Gaps, and the file boundary

Waveform archives split records at file boundaries that have nothing to do
with the physics: one file per hour, or per day, or per 4096-byte record. Two
consecutive files read into a `Stream` produce two `Trace` objects whenever
their sample times are not exactly contiguous. The demonstration writes two
segments with a genuine 1 s gap:

```
read two files            : 2 traces
gap between segments      : 1.000 s (100 missing samples)
merge(method=-1)          : 2 traces (gap kept)
merge(method=0)           : 1 traces (gap zero-filled)
```

and then triggers the error that catches almost everyone the first time:

```
merge(fill_value=0.0) on int32 data -> UFuncTypeError: Cannot cast ufunc
'multiply' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
```

Integer data need an integer fill value. That is a real constraint of the
implementation, and it is worth reading as a warning: the library is refusing
to silently introduce floating-point into an integer record.

### 3.4 What the header carries, and what it does not

The demonstration sets `calib = 5.1e8` (counts per m/s), writes MiniSEED and
reads it back:

```
network       : XX
station       : ABCD
location      : 00
channel       : BHZ
sampling_rate : 100.0
starttime     : 2024-03-15T08:30:00.000000Z
calib         : 1.0
```

Everything survives except `calib`, which MiniSEED has no field for. The
measured `calib = 1.0` is the default. The transfer function is *not* in the
waveform file: it lives in StationXML, which is why lesson
[03](./03-inventory-and-metadata.md) exists. Thinking of a MiniSEED file as
self-contained is the mistake that produces uncalibrated amplitudes in
published figures.

### 3.5 Format detection

The demonstration writes MiniSEED bytes to a file named `actually_mseed.bin`
and reads it:

```
file named '.bin', read as : XX.ABCD.00.BHZ npts=3000 dt=0.01 s
CHECK identical samples    : True
```

`obspy.read` sniffs the content. The file name is a hint for humans and for
your own file management, never for the parser. The corollary is that a
mislabelled file will be read as whatever it actually is — which is better
than the alternative, but means that a file named `.sac` that is really
MiniSEED will silently change dtype and header fields under you.

## 3b. Worked examples

### 3b.1 Planning storage from the measured bytes per sample

**Problem.** A network of 12 stations runs three-component broadband channels at
100 Hz. How much disk does one year occupy, in MiniSEED and in SAC?

Per station-year, per component:

$$\text{samples} = 100 \times 3.156\times10^{7} = 3.156\times10^{9}.$$

Using the *measured* MiniSEED rates from the demonstration:

| signal character | bytes/sample | per station-year per component | 12 stations, 3 components |
|---|---|---|---|
| very smooth (amplitude ≈ 1) | 1.3653 | 4.31 GB | 155 GB |
| typical band-limited | 2.7307 | 8.62 GB | 310 GB |
| high-dynamic-range | 5.4613 | 17.24 GB | 621 GB |

In SAC, every component is $4 \times 3.156\times10^9 = 12.6$ GB plus a 632-byte
header per file. With files split per hour, that is 8760 files per
station-component-year, adding $8760 \times 632 = 5.5$ MB — negligible compared
with 12.6 GB, but the *file count* is 315 360 for the network, which is the real
operational constraint: metadata operations on a directory of 300 000 files are
slower than the data transfer.

The measured range of 1.37 to 5.46 bytes per sample is a factor of 4, and it is
determined by the *signal*, not by the format. A storage estimate that assumes
4 bytes per sample (uncompressed `int32`) over-estimates a smooth-channel archive
by a factor of 3 and under-estimates a noisy one by 27 %.

### 3b.2 The `float32` decision, quantified

**Problem.** A strain record has values near $1.0\times10^{-9}$ and the science
requires resolving differences of $1.0\times10^{-13}$. Is SAC's `float32`
adequate?

`float32` has a 24-bit mantissa, so the relative resolution at a value $x$ is
$\varepsilon_{32} x$ with $\varepsilon_{32} = 1.19\times10^{-7}$:

$$1.19\times10^{-7} \times 1.0\times10^{-9} = 1.19\times10^{-16}.$$

The resolvable difference is $1.2\times10^{-16}$, *smaller* than the required
$10^{-13}$, so `float32` is adequate — by three orders of magnitude. The
demonstration's measured round-trip relative error of $3.18\times10^{-8}$
(0.27 ε) is comfortably inside that budget.

Now change the example: the record's values are near $1.0$ (a raw count or a
normalised amplitude) and differences of $10^{-9}$ matter. Then
$1.19\times10^{-7} \times 1.0 = 1.19\times10^{-7}$ is the resolution, which is
100 times *larger* than the required $10^{-9}$: `float32` fails. The lesson is
that the answer depends on the *absolute* scale of the values, because
floating-point resolution is relative, and on the *absolute* scale of the
differences, because those are what carry the signal.

### 3b.3 Diagnosing a file that reads but is wrong

**Problem.** A MiniSEED file has the right size, reads without error, and produces
a trace with a plausible waveform — but a colleague reports that its arrival
times are 5 s late. What is the minimum diagnostic sequence?

1. **Check `npts` against the time span.** 3600 samples at 100 Hz span 35.99 s;
   a trace whose start and end times differ by 41 s is inconsistent. This is the
   check that catches a shifted start time, and it is the one nobody writes.
2. **Check the sampling rate against the expectation.** 100.0 vs 99.99 Hz is a
   clock drift, and over an hour it is a 0.4 s shift.
3. **Compare against a second channel of the same station.** A common timing
   error affects every channel equally; a location error does not.
4. **Check the response epoch.** A station that changed its data logger can have
   a step in its timing; the step is visible as a discontinuity in
   `starttime − expected_grid_time` across the day boundary.

The demonstration's validation function performs steps 1 and 2 and detects both
corruptions it constructs. Steps 3 and 4 need more than one channel and the
StationXML, which is why validation is a *sequence* rather than a line.

### 3b.4 Steim compression is not free

**Problem.** A 3000-sample int32 stream is 12000 bytes of raw samples. How does
the file size depend on the signal's dynamic range, and when does Steim *lose*?

Measured, 3000 samples per file:

| peak amplitude | file size | bytes/sample | vs raw int32 |
|---|---|---|---|
| 1 | 4096 | 1.3653 | 0.341× |
| 1000 | 8192 | 2.7307 | 0.683× |
| $10^{7}$ | 16384 | 5.4613 | **1.365×** |

The trend is the whole lesson: Steim-2 encodes *differences* with variable-length
words, so a signal with small successive differences packs tightly and a
high-amplitude, high-frequency signal does not. At a peak amplitude of $10^{7}$
counts the file is **37 % larger than storing the raw integers**, because Steim
escapes to a literal 32-bit word more often than it finds second differences
that fit in a byte.

Practical consequences:

1. **Compression ratios quoted from one dataset do not transfer.** A ratio of
   0.34 measured on a quiet station is not a prediction for a noisy one.
2. **The comparison to make is against your own data.** If the *measured*
   bytes/sample is above 4, unpacking to float32 and re-encoding with a lossless
   general-purpose compressor may win; below 2, Steim is doing real work.
3. **Never treat the sample rate as a proxy for size.** All three rows have the
   same 3000 samples and the same $dt = 0.01$ s (100 Hz); the sizes differ by a
   factor of 4.

### 3b.5 A read-back checklist

**Problem.** A trace has been read. Which properties must be checked before it is
used, and what are the reference values from the demonstration?

| check | measured reference |
|---|---|
| `len(tr.data) == tr.stats.npts` | 3000 = 3000 |
| `tr.stats.endtime == starttime + (npts−1)·delta` | 59.990 s at 100 Hz, 6000 samples |
| `tr.id` round-trips start time and $dt$ | starttime equal = True, $dt = 0.01$ s |
| samples are bit-identical after a MiniSEED/SAC round trip | True for both formats |
| `calib` survived a MiniSEED write | **No** — 5.1e8 read back as 1.0 |
| `tr.data.dtype` and the physical units are known | int32 counts, not m/s |
| the file's format matches what the name suggests | `read()` sniffs the bytes, not the name |

Three of these deserve comment. The `endtime` formula uses $n - 1$, not $n$:
6000 samples at 100 Hz span 59.990 s, not 60.000 s, and the 0.01 s difference is
the single most common source of a one-sample inconsistency between two codes.
The `calib` loss is silent — the samples are unchanged and still counts, but a
downstream multiplication by `calib` now multiplies by 1 — so the *unit* of the
data must be recorded alongside the file, not inferred from it. And a
`float32` SAC round trip is not exact: measured relative error 3.175207e−08,
against the float32 machine epsilon 1.192093e−07, i.e. about a quarter of an
ulp. The values are recoverable to float32 precision and no further; if a
workflow needs the last bits of a float64 computation, the intermediate file
format must be float64.

### 3b.6 What "bit-identical" is and is not

**Problem.** A pipeline writes MiniSEED, reads it back, and asserts
`np.array_equal(back.data, original.data)`. Is that assertion correct, and is it
sufficient?

**Correct for `int32` data** — the demonstration measures
`bit-identical=True` for both MiniSEED and SAC when the samples are integers,
because Steim is a lossless encoding of integers and the integer→`float32`→
integer path is exact for values below $2^{24}$.

**Not correct for `float64` data.** SAC stores `float32`, so the round trip is
lossy by construction: the measured maximum relative error is
$3.18\times10^{-8}$. An equality assertion fails; the correct assertion is a
tolerance based on `np.finfo(np.float32).eps`.

**Not sufficient even when it passes.** Equality of samples says nothing about
metadata: a file can return the right numbers with a start time off by 5 s, a
sampling rate off by 0.01 %, a lost `calib`, or a different location code. The
demonstration measures exactly that: bit-identical samples, `calib` lost
(5.1e8 → 1.0). **Compare samples *and* metadata, and know which of the two the
format is capable of carrying.**

## 4. Physical and computational interpretation

Reading a waveform is a lossy, format-dependent operation, and the losses are
of three kinds:

- **Precision loss** (`float32` in SAC) — a property of the format.
- **Compression loss** — none for Steim, which is lossless for integer data.
- **Metadata loss** (`calib` in MiniSEED) — a property of the format.

The practical decision tree:

1. **Archival:** MiniSEED. Smaller, streamable, standard, supported by every
   service. Keep StationXML beside it, keyed by channel and time.
2. **Analysis:** read into a `Stream`, keep `float64` in memory, do not write
   back to SAC until the final product.
3. **Exchange with a person who uses SAC:** `trace.write(..., format="SAC")`
   and accept seven digits. State the dtype in the methods section if the
   amplitude precision is within a factor of 100 of `float32` epsilon.
4. **Very large archives:** do not use `Stream`; use a database of headers
   (`obspy.db`, not importable here) plus chunked reads.

## 5. Python demonstration

The full script is
[`code/reading_waveforms_demo.py`](./code/reading_waveforms_demo.py). It
writes its scratch files into `code/_scratch_roundtrip/` and deletes that
directory before exit, so a run leaves the repository clean. The channel-code
conventions printed in section 8 are worth memorising:

| Band code | Sample rate |
|---|---|
| `LH` | 1 Hz (long period) |
| `BH` | 10–80 Hz (broadband) |
| `HH` | 80–250 Hz (high broadband) |
| `EH` | 250–1000 Hz (extremely short period) |

followed by an orientation code: `Z` vertical, `N`/`E` north/east, `1`/`2`
and `3` for other orientations, `T` for a temperature channel.

## 6. Exercises

Full solutions: [`exercises/02-reading-waveforms-solutions.md`](./exercises/02-reading-waveforms-solutions.md).

### ★ Foundational

**★1.** The demo reports a MiniSEED file of 8192 bytes for 3000 samples.
Compute the bytes per sample and the bits per sample, and compare with
uncompressed `int32`.

**★2.** A SAC file is 12632 bytes for a 3000-sample trace. Show that this is
exactly consistent with a 632-byte header and `float32` samples.

**★3.** Name the MiniSEED encoding code for `int32`, for `float32` and for
Steim-2, and state which one ObsPy writes by default for integer data.

**★4.** The demo writes `calib = 5.1e8` and reads back `calib = 1.0`. State
which format lost the field and what a reader should do instead.

### ★★ Applied

**★★5.** Write a function `describe(path)` that reads a waveform file and
prints, for each trace: the trace id, sample rate, number of samples, dtype,
start time and the number of samples implied by the time span. Test it on a
MiniSEED file and on a SAC file written from the same data and report the one
place where they disagree.

**★★6.** The same 3000-sample waveform is written three times, scaled to peak
amplitudes 1, 1000 and $10^7$. Explain why file size increases with amplitude,
in terms of the differencing Steim performs, and state the measured sizes.

**★★7.** Take a 60-second, 100 Hz, `float32` waveform of small amplitudes and
write it to SAC, then read it back and compute the maximum relative error.
Predict the answer before running, then compare with the measured
$3.18\times10^{-8}$.

**★★8.** Construct a `Stream` with a 4.5 s gap, and write code that produces
both a gap-preserving and a gap-filled version. For the filled version, report
how many samples are not measurements and propose a test that would justify the
fill.

### ★★★ Research-oriented

**★★★9.** Measure the *compression ratio* of Steim-2 against `float32` for
three signals of the same length and dynamic range: a smooth sinusoid, a
band-limited random signal and a white-noise signal quantised to integers.
Report bytes per sample for each and explain the ordering in terms of the
distribution of first differences. Then state which of your signals is
representative of real seismic data and why.

**★★★10.** Design a provenance record for a downloaded waveform: a small text
or JSON file written beside the data, containing service URL, query
parameters, query time, the resulting channel list and the file checksums.
Implement it for the offline case (a file you wrote yourself), state which
fields you could not populate without network access, and argue why a checksum
is the minimum viable provenance.
