# Solutions — 03-10-02 Reading MiniSEED/SAC: Trace and Stream

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output on this installation (ObsPy 1.5.1, NumPy 2.5.4).
> Values marked *measured* come from a modified copy of the demonstration with
> the modification stated.

---

## ★1 — Bits per sample in a MiniSEED file

$8192 / 3000 = 2.7307$ bytes per sample $= 21.85$ bits per sample.

Uncompressed `int32` would be 32 bits. So Steim-2 achieves a factor of
$32/21.85 = 1.46$ on this signal. The exact file sizes are 8192 and 16384 for
the larger amplitude case, so the *achieved* ratio depends on the signal, not
only on the format.

---

## ★2 — Why a SAC file is 12632 bytes

$$632\ \text{bytes (header)} + 3000\ \text{samples} \times 4\ \text{bytes}
= 632 + 12000 = 12632\ \text{bytes}.$$

Checked exactly. There is no padding in the ObsPy writer for this case; a SAC
file's size is completely predictable from `npts`.

---

## ★3 — MiniSEED data-encoding codes

- `int32` → code **3**
- `float32` → code **4**
- Steim-2 → code **11**

ObsPy writes integer data as **Steim-2** by default. For a trace whose data are
`float32` and non-integral, ObsPy writes code 4 instead, because Steim cannot
represent fractional differences without first quantising.

---

## ★4 — The lost `calib`

**MiniSEED** loses it: the demonstration prints `calib : 1.0` after writing
`5.1e8`. There is no fixed-header field for a scalar calibration. The correct
practice is to keep the response in **StationXML**, keyed by
`network.station.location.channel` and valid time, and to call
`Trace.remove_response(inventory=...)`. Nothing in the waveform file tells you
the instrument gain; the file only tells you what the digitizer counted.

---

## ★★5 — `describe(path)` and the one disagreement

```python
from obspy import read

def describe(path: str) -> None:
    for tr in read(path):
        stats = tr.stats
        span_samples = int(round((stats.endtime - stats.starttime)
                                 * stats.sampling_rate)) + 1
        print(f"{tr.id:20s} fs={stats.sampling_rate:7.3f} Hz "
              f"npts={stats.npts:6d} dtype={tr.data.dtype} "
              f"start={stats.starttime} span_implies={span_samples}")
```

Measured output for the same 3000-sample waveform:

| format | `dtype` after read | `npts` | `sampling_rate` |
|---|---|---|---|
| MiniSEED | `int32` | 3000 | 100.0 |
| SAC | `float32` | 3000 | 100.0 |

**The disagreement is the dtype.** The time span check is satisfied in both
cases, the sampling rate survives exactly, and the sample values agree — but
one file returns integers and the other returns floats, so a downstream
`assert tr.data.dtype == np.int32` passes for one and fails for the other.
This is why format-agnostic code should never assert on `dtype`.

---

## ★★6 — Why file size grows with amplitude

Steim stores first differences, then second and third differences, in a
variable-length code: small numbers fit in 4-bit codes, larger ones need 8,
16 or 32 bits, and the encoder falls back to a 32-bit verbatim word when the
differences are large. Scaling a waveform up by a factor of $10^7$ multiplies
every difference by $10^7$, pushing them out of the narrow codes.

Measured, for identical waveform *shape* at three amplitudes:

| peak amplitude | file size | bytes/sample |
|---|---|---|
| 1 | 4096 | 1.3653 |
| 1000 | 8192 | 2.7307 |
| $10^7$ | 16384 | 5.4613 |

The last case is *larger* than uncompressed `int32` (4 bytes/sample) because
fixed-length records plus frame overhead dominate once the codes widen.

---

## ★★7 — `float32` round trip

Predict: relative error at most $\varepsilon_{\text{float32}}/2 = 6\times10^{-8}$
and typically a few times smaller, i.e. $10^{-8}$.

Measured on the demo's data:

```
max |round-trip error|   : 1.129282e-10
relative error           : 3.175207e-08
float32 machine epsilon  : 1.192093e-07
```

$3.18\times10^{-8}$ is $0.27\ \varepsilon_{\text{float32}}$, comfortably inside
the worst case and consistent with round-to-nearest on random mantissas
(mean error about $0.25\varepsilon$). The prediction and the measurement agree,
which is the point: seven significant decimal digits is a *derivable* property
of the format, not folklore.

---

## ★★8 — Filling a 4.5 s gap

```python
import numpy as np
from obspy import Stream, Trace, UTCDateTime

def two_segments(gap_seconds: float = 4.5, npts: int = 1000, fs: float = 100.0):
    rng = np.random.default_rng(11)
    first = Trace(np.round(rng.normal(0, 500, npts)).astype(np.int32))
    first.stats.network, first.stats.station = "XX", "ABCD"
    first.stats.location, first.stats.channel = "00", "BHZ"
    first.stats.sampling_rate = fs
    first.stats.starttime = UTCDateTime("2024-03-15T08:00:00Z")
    second = first.copy()
    second.stats.starttime = first.stats.endtime + gap_seconds
    second.data = second.data + 100
    return Stream(traces=[first, second])

gap = two_segments()
kept = gap.copy().merge(method=-1)              # 2 traces, 1000 samples each
filled = gap.copy().merge(method=0, fill_value=0)   # 1 trace, 2451 samples
print(len(kept), [t.stats.npts for t in kept])
print(len(filled), [t.stats.npts for t in filled])
print("invented samples:", filled[0].stats.npts - 2000)
```

Measured: `kept` has 2 traces of 1000 samples; `filled` has 1 trace of 2451
samples, so **451 samples are not measurements**
($4.5/0.01 = 450$ intervals plus the boundary sample).

A test that would justify the fill: repeat the analysis with the 451 samples
*removed* (two separate spectra, then a weighted average) and compare the two
results. If the difference is below the noise floor of the measurement, the
fill is harmless *for that analysis*; that is an empirical statement about one
quantity of interest, not a licence to fill gaps in general.

---

## ★★★9 — Steim-2 compression against `float32` for three signals

Measured on 20 000 samples at 100 Hz, quantised to integers:

| signal | raw `int32` | Steim-2 file | Steim-2 bytes/sample | versus `float32` (4.0) |
|---|---|---|---|---|
| smooth 5 Hz sinusoid, amplitude $10^6$ | 80 000 | 24 576 | 1.2288 | 3.26 x smaller |
| band-limited noise, 1–20 Hz, amplitude $10^6$ | 80 000 | 57 344 | 2.8672 | 1.40 x smaller |
| white noise, amplitude $10^6$ | 80 000 | 81 920 | 4.0960 | 0.98 x, i.e. slightly worse |

The ordering follows the distribution of first differences: a sinusoid's
differences change slowly and stay inside the narrow codes; band-limited noise
needs wider codes; white noise's differences are as large as its samples, so
the differencing buys nothing and Steim's per-word framing costs more than the
4-byte verbatim representation would.

**Which is representative?** The band-limited case. Real seismic data are
band-limited by the sensor (a geophone above its corner frequency is flat to
velocity, but the recording chain high-cuts at Nyquist) and by the Earth's
attenuation. White noise is representative only of a poorly grounded channel
or a broken digitizer, and those channels should be found in quality control
rather than compressed.

---

## ★★★10 — A provenance record for a waveform

```python
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

def provenance(path: Path, *, service: str | None = None,
               query: dict | None = None,
               requested_at: str | None = None) -> dict:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "file": path.name,
        "bytes": path.stat().st_size,
        "sha256": digest,
        "service": service,
        "query": query,
        "requested_at": requested_at,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
```

For a file you wrote yourself, `service`, `query` and `requested_at` are
`None`: offline you cannot populate the fields that say *where the data came
from*. That absence is itself the important part of the exercise. In a real
download you would fill:

- `service`: the base URL, e.g. `https://service.iris.edu/fdsnws/dataselect/1/`
  (a verified endpoint; see the lesson on FDSN clients).
- `query`: network, station, location, channel, start, end.
- `requested_at`: the UTC time of the request, because the archive is not
  immutable — a channel's response can be revised and re-published, and the
  same query a month later can return different metadata.

**Why the checksum is the minimum viable provenance:** every other field can be
reconstructed or guessed later, but the checksum is the only field that lets a
reader prove the bytes they have are the bytes you analysed. Without it, a
provenance record is a description of a file that may no longer exist in that
form. With it, a reader can detect any change — including a silent re-write by
a data centre or a partial download — and stop.
